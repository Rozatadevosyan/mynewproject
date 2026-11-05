import csv

import psycopg2


class EmployeeDataSource():
    def extract(self, connection):
        with open('orders.csv', "r") as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            with connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS employee_raw (
                        order_id BIGINT PRIMARY KEY,
                        customer_id BIGINT NOT NULL,
                        product VARCHAR(100) NOT NULL,
                        quantity INTEGER NOT NULL,
                        unit_price NUMERIC(10, 2) NOT NULL,
                        status VARCHAR(50) NOT NULL,
                        order_date DATE NOT NULL,
                        imported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                for row in rows:
                    cursor.execute("INSERT INTO employee_raw values(%s, %s, %s,%s,%s, %s,%s)",
                                   (row["order_id"],
                                   row["customer_id"],
                                   row["product"],
                                   row["quantity"],
                                   row["unit_price"],
                                   row["status"],
                                   row["order_date"]))
            return len(rows)

    def validate(self, connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employee_raw")
        columns =  [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        total = [dict(zip(columns, row)) for row in rows]

        invalid_rows = []
        valid_rows = []
        error_rows = []
        seen_ids = set()
        for row in total:
            errors =[]
            if row["id"] in seen_ids:
                errors.append("ID xndir")
            else:
                seen_ids.add(row["id"])
            if row["name"] == " ":
                errors.append("xndir")
            if row["status"] == " ":
                errors.append("xndir")
            if row["order_date"] != " ":
                errors.append("xndir")

            if errors:
                invalid_rows.append(row)
                error_rows.append({"row":invalid_rows,"xndir":errors })
            else:
                valid_rows.append(row)

        return invalid_rows, valid_rows, error_rows

    def transform(self, valid_rows):
        transformed_rows = []

        for row in valid_rows:
            transformed_row = {
                "order_id": int(row["order_id"]),
                "customer_id": int(row["customer_id"]),
                "product": row["product"].strip().title(),
                "quantity": int(row["quantity"]),
                "unit_price": float(row["unit_price"]),
                "status": row["status"].strip().lower(),
                "order_date": row["order_date"],
                "total_price": int(row["quantity"]) * float(row["unit_price"])
            }
            transformed_rows.append(transformed_row)

        return transformed_rows

    def load(self,connection, valid_rows):
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employee_clean (
                order_id BIGINT PRIMARY KEY,
                customer_id BIGINT NOT NULL,
                product VARCHAR(100) NOT NULL,
                quantity INTEGER NOT NULL,
                unit_price NUMERIC(10, 2) NOT NULL,
                status VARCHAR(50) NOT NULL,
                order_date DATE NOT NULL,
                imported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        for row in valid_rows:
            cursor.execute("INSERT INTO employee_clean values(%s, %s, %s, %s, %s, %s, %s) on conflict (order_id) do NOTHING",
                           (row["order_id"],
                            row["customer_id"],
                            row["product"],
                            row["quantity"],
                            row["unit_price"],
                            row["status"],
                            row["order_date"]))


        connection.commit()
        return len(valid_rows)

    def run(self, connection):
        con = self.extract(connection)
        invalid_rows, valid_rows, error_rows = self.validate(connection)
        bl = self.transform(valid_rows)
        blbl = self.load(connection, bl)
        print("ectracted:", con)
        print("validated:", valid_rows)
        print("val:", invalid_rows)
        print("transf:", bl)
        print("load:", blbl)
        return valid_rows, invalid_rows, error_rows



class EmployeeDSource():
    def extract(self):
        with open('orders.csv', "r") as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

            return rows
    def load(self, connection, rows):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee_raw (
                    order_id BIGINT PRIMARY KEY,
                    customer_id BIGINT NOT NULL,
                    product VARCHAR(100) NOT NULL,
                    quantity INTEGER NOT NULL,
                    unit_price NUMERIC(10, 2) NOT NULL,
                    status VARCHAR(50) NOT NULL,
                    order_date DATE NOT NULL,
                    imported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            for row in rows:
                cursor.execute("""
                    INSERT INTO employee_raw (
                        order_id, customer_id, product,
                        quantity, unit_price, status, order_date
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (order_id) DO NOTHING
                """, (
                    row["order_id"],
                    row["customer_id"],
                    row["product"],
                    row["quantity"],
                    row["unit_price"],
                    row["status"],
                    row["order_date"]
                ))
        connection.commit()
        return len(rows)

    def transform(self, connection):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee_clean (
                    order_id BIGINT PRIMARY KEY,
                    customer_id BIGINT NOT NULL,
                    product VARCHAR(100) NOT NULL,
                    quantity INTEGER NOT NULL,
                    unit_price NUMERIC(10, 2) NOT NULL,
                    status VARCHAR(50) NOT NULL,
                    order_date DATE NOT NULL,
                    total_price NUMERIC(12, 2) NOT NULL,
                    imported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            cursor.execute("""
                INSERT INTO employee_clean (
                    order_id, customer_id, product,
                    quantity, unit_price, status,
                    order_date, total_price
                )
                SELECT
                    CAST(order_id AS BIGINT),
                    CAST(customer_id AS BIGINT),
                    TRIM(product),
                    CAST(quantity AS INTEGER),
                    CAST(unit_price AS NUMERIC(10, 2)),
                    LOWER(TRIM(status)),
                    CAST(order_date AS DATE),
                    CAST(quantity AS INTEGER) *
                        CAST(unit_price AS NUMERIC(10, 2))
                FROM employee_raw
                WHERE
                    TRIM(product) <> ''
                    AND TRIM(status) <> ''
                    AND quantity > 0
                    AND unit_price >= 0
                    AND order_date IS NOT NULL
                    AND CAST(quantity AS INTEGER) > 0
                    AND CAST(unit_price AS NUMERIC(10, 2)) >= 0
                ON CONFLICT (order_id) DO NOTHING
            """)

        connection.commit()

    def run(self, connection):
        c = self.extract()
        d = self.load(connection, c)
        a = self.transform(connection)



connection = psycopg2.connect(
    user = 'postgres',
    password = 'postgres1234',
    host = 'localhost',
    port = 5441,
    database = 'new_db')

if __name__ == "__main__":
    try:
        emp = EmployeeDSource()
        emp.run(connection)

        e = EmployeeDSource()
        e.run(connection)
    except Exception as e:
        print(e)
    finally:
        connection.close()
