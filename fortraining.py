# numbers = [1, 2, 2, 3, 4, 4, 5]
#
# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#      if numbers[i] == numbers[j]:
#          print(numbers[i])
#
# from contextlib import nullcontext
# from xxlimited_35 import Null
#
# word = "hello"
#
# for i in range(len(word)-1, -1, -1):
#     print(word[i])
#
#
#
# numbers = [12, 5, 8, 20, 13, 20, 5]
# maximum = 0
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] > numbers[j] and numbers[i] > maximum:
#             maximum = numbers[i]
#         else:
#             maximum = numbers[j]
# print(maximum)
# j = len(numbers)
# num = []
# for i in range(j):
#     if numbers[i] < maximum:
#         num.append(numbers[i])
# max = 0
# for i in range(len(num)):
#     for j in range(i+1, len(num)):
#         if num[i] > num[j] and num[i] > max:
#             max = num[i]
#         else:
#             max = num[j]
# print(max)
#
#
#
# numbers = [12, 5, 8, 20, 3, 20, 5]
# max = numbers[0]
# second_max = None
#
# for number in numbers:
#     if number > max:
#         second_max = max
#         max = number
#
#     elif number < max and (second_max is None or number > second_max):
#         second_max = number
#
# print(second_max)
#
#
#
# numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
# num=None
# for n in range (len(numbers)):
#     for j in range (n+1, len(numbers)):
#         if numbers[n] == numbers[j] and numbers[n] !=num:
#             print(numbers[n])
#             num=numbers[n]
#             break
#
#
# numbers = [12, 24,10,  32, 45]
#
# result = []
# for number in numbers:
#     if number % 5 == 0:
#         result.append(number)
#         print(number)
#
#
# numbers = [2, 5, 2, 8, 5, 5, 5, 9, 9, 2]
#
# num = []
#
# for n in range(len(numbers)):
#     for j in range(n+1, len(numbers)):
#         if numbers[n]==numbers[j] and numbers[j] not in num:
#             num.append(numbers[n])
#             break
#
# print(num)
#
#
# numbers = [2, 5, 2, 8, 5, 9, 2]
# num = []
# for n in range(len(numbers)):
#     for m in range(n+1, len(numbers)):
#         if numbers[n] == numbers[m] and numbers[n] not in num:
#             num.append(numbers[n])
#             break
#
# for n in range(len(numbers)):
#     if numbers[n] not in num:
#         print(numbers[n])
#
#
#
# numbers = [10, 5, 8, 20, 15]
#
# max_num = numbers[0]
# max_sec_num = None
# for i in range(1,len(numbers)):
#         if numbers[i]>max_num:
#             max_sec_num =max_num
#             max_num = numbers[i]
#         if numbers[i]<max_num and (max_sec_num is None or numbers[i]>max_sec_num):
#             max_sec_num = numbers[i]
#
# print(max_sec_num)
#
#
#
# words = ["cat", "elephant", "dog", "computer"]
#
# max_length = len(words[0])
# index = []
# for w in range(1,len(words)):
#     if len(words[w]) >= max_length:
#         max_length = len(words[w])
#         index.append(words.index(words[w]))
#
# for i in index:
#     print(words[i])
#
#
# words = ["cat", "dog", "house"]
#
# total_length = 0
# total_length1 = 0
# for word in words:
#     total_length += len(word)
#
# print(total_length)
#
#
# words = ["cat", "dog", "house"]
# total_length1 = 0
# for j in range(len(words)):
#     word = words[j]
#     i=0
#     while i < len(word):
#         total_length1+=1
#         i+=1
#
# print(total_length1)
#
#
# numbers = [4, 8, 15, 16, 23, 42]
#
# target = 15
#
# for n in range(len(numbers)):
#     if numbers[n] == target:
#         print(n)
#
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# list3 = []
# for x in list1:
#     for y in list2:
#         if x == y:
#             list3.append(x)
#             break
#
# print(list3)
#
#
# numbers = [1, 1, 2, 3, 3, 4, 5, 5]
# mna = []
# for i in range(len(numbers)):
#     c = 1
#     for j in range(i+1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             c += 1
#             print(c)
#     if c==1 and numbers[i] not in mna:
#         mna.append(numbers[i])
#
#
# print(mna)
#
#
#
# numbers = [4, 8, 15, 16, 23, 42]
# target = 15
#
# for n in range(len(numbers)):
#     if numbers[n] == target:
#         print(n)
#
#
# numbers = [4, 7, 4, 2, 7, 9, 4, 7, 7]
# m = 0
# r = 0
# for i in range(len(numbers)):
#     c = 1
#     for j in range(i+1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             c += 1
#     if c>m:
#         m = c
#         r = i
# print(numbers[r])
#
import multiprocessing
import os
import threading
import time
from abc import ABC, abstractmethod
from asyncio import Protocol
from ctypes.wintypes import CHAR
from logging import Logger
from multiprocessing import Process


# def validate_record(record):
#     if type(record[0][1]) is not str and record[0][1].isempty:
#         print("chi kareli")
#     elif (record[1][1].isint() or record[1][1].isfloat()) and record[1][1]>=0:
#         print("karelia")
#     elif record[2][1].isboolean():
#         print("karelia")
#     else:
#         print("chi karelia")
#
#
# record1={"customer_id": "  ", "amount": 100, "active": True}
# record2={"customer_id": "C102", "amount": -5, "active": True}
# record3={"customer_id": "C103", "amount": True, "active": False}
# record4={"customer_id": "C104", "amount": 100, "active": 1}
#
# validate_record(record1)
# validate_record(record2)
# validate_record(record3)
# validate_record(record4)

# transactions = [12000, -500, 8500, 0, 12000, 30000, -1500, 4500, 0, 22000]
# numbers = []
# for i in transactions:
#     if i >=0:
#         numbers.append(i)
#
# print(numbers)
# print(sum(numbers))
# print(transactions)
# print(len(numbers))
# max_n = numbers[0]
# for i in numbers:
#     if i>max_n:
#         max_n = i

# values = [4, 7, 4, 9, 7, 4, 12, 9, 7]
#
# vail =[]
# for i in range (len(values)):
#     for j in range (len(values)):
#         if values[i] == values[j] and values[i] not in vail:
#             vail.append(values[i])
#             break
# print(vail)
# print(values)

# numbers = [2, 4, 6, 8, 10, 12]
#
# for number in numbers:
#     if number % 4 == 0:
#         numbers.remove(number)
#
# print(numbers)

# records = [
#     ["A001", [100, 200]],
#     ["A002", [300, 400]],
#     ["A003", [500, 600]]
# ]
#
# copied = records.copy()
#
# copied[0][1].append(700)
# copied[1] = ["A004", [800, 900]]
# copied.append(["A005", [1000, 1100]])
#
# print(records)
# print(copied)
# def get_unique_ids(ids):
#     idses = []
#     for i in range(len(ids)):
#         if ids[i] not in idses:
#             idses.append(ids[i])
#     return idses
#
# ids = [105, 101, 105, 103, 101, 109, 103, 112, 105]
#
# print(get_unique_ids(ids))


# transactions = (
#     ("T1", 1500, "success"),
#     ("T2", 2500, "failed"),
#     ("T3", 3500, "success"),
#     ("T4", 1000, "success"),
#     ("T5", 2000, "failed")
# )
#
# def get_tup(tuple):
#     tup =()
#     bla = 0
#     blabl = 0
#     for item in tuple:
#         if item[2] =="success":
#             bla += item[1]
#             blabl+=1
#     tup=(bla,blabl)
#     return tup
# print(get_tup(transactions))

#
# transactions = [
#     {"id": "T1", "amount": 1500, "status": "success"},
#     {"id": "T2", "amount": 2500, "status": "failed"},
#     {"id": "T3", "amount": 3500, "status": "success"},
#     {"id": "T4", "amount": 1000, "status": "success"}
# ]
#
# def get_hopar(transactions):
#     bararan = {
#         "total_amount": 0,
#         "success_count": 0,
#         "failure_count": 0
#     }
#     for transaction in transactions:
#
#         bararan["total_amount"] += transaction["amount"]
#         if transaction["status"] == "success":
#             bararan["success_count"] +=1
#         elif transaction["status"] == "failed":
#             bararan["failure_count"] +=1
#
#     return bararan
#
# print(get_hopar(transactions))

# words = ["python", "sql", "python", "java", "sql", "python"]
#
# def get_count(words):
#     psch = {"python":0,"sql":0,"java":0}
#     for word in words:
#         if word in psch:
#             psch[word] += 1
#     return psch
#
# print(get_count(words))

#
# employees = [
#     {"id": 1, "department": "IT", "salary": 400000},
#     {"id": 2, "department": "HR", "salary": 250000},
#     {"id": 3, "department": "IT", "salary": 500000},
#     {"id": 4, "department": "HR", "salary": 300000},
#     {"id": 5, "department": "IT", "salary": 450000}
# ]
#
# def get_employees(employees):
#     p = {"IT": 0, "HR": 0}
#     for employee in employees:
#         if employee["department"] == "IT":
#             p["IT"] += employee["salary"]
#         elif employee["department"] == "HR":
#             p["HR"] += employee["salary"]
#     return p
#
# print(get_employees(employees))


# transactions = [
#     ("T1", 1500, "success", "AMD"),
#     ("T2", 2500, "failed", "AMD"),
#     ("T3", 3500, "success", "USD"),
#     ("T4", 1000, "success", "AMD"),
#     ("T5", 2000, "failed", "USD"),
#     ("T6", 4500, "success", "USD"),
#     ("T7", 1500, "success", "AMD"),
#     ("T8", 3000, "pending", "EUR"),
#     ("T9", 2500, "success", "EUR"),
#     ("T10", 1000, "failed", "AMD")
# ]
#
# def analyze_transactions(transactions):
#     di = {
#     "total_transactions": 0,
#     "status_counts": {
#         "success": 0,
#         "failed": 0,
#         "pending": 0
#     },
#     "successful_amount_by_currency": {},
#     "failed_ids":set(),
#     "largest_successful_transaction": None
# }
#     max_amount = 0
#     for transaction in transactions:
#         di["total_transactions"] += 1
#         if transaction[2] == "success":
#             di["status_counts"]["success"] += 1
#             currency = transaction[3]
#             if currency not in di["successful_amount_by_currency"]:
#                 di["successful_amount_by_currency"][currency] = 0
#             di["successful_amount_by_currency"][currency] += transaction[1]
#         if transaction[2] == "pending":
#             di["status_counts"]["pending"] += 1
#         if transaction[2] == "failed":
#             di["status_counts"]["failed"] += 1
#             di["failed_ids"].add(transaction[0])
#         if transaction[1]>max_amount and transaction[2]=="success":
#             max_amount = transaction[1]
#
#     for transaction in transactions:
#         if transaction[2] == "success" and transaction[1]== max_amount:
#             di["largest_successful_transaction"]=transaction
#     return di
#
# print(analyze_transactions(transactions))


# employees = [
#     {"id": 101, "name": "Anna", "department": "IT",
#      "salary": 400000, "skills": ["Python", "SQL"]},
#     {"id": 102, "name": "Aram", "department": "HR",
#      "salary": 250000, "skills": ["Excel", "Communication"]},
#     {"id": 103, "name": "Mariam", "department": "IT",
#      "salary": 500000, "skills": ["Python", "Docker", "SQL"]},
#     {"id": 104, "name": "Karen", "department": "Data",
#      "salary": 450000, "skills": ["Python", "SQL", "Spark"]},
#     {"id": 105, "name": "Ani", "department": "IT",
#      "salary": 450000, "skills": ["SQL", "Docker"]},
#     {"id": 106, "name": "Gor", "department": "Data",
#      "salary": 550000, "skills": ["Python", "Spark", "Airflow"]}
# ]
#
# def analyze_employees(employees):
#     d = {
#         "department_counts": {},
#         "department_average_salary": {},
#         "department_top_employee": {},
#         "unique_skills": set(),
#         "most_common_skill": None,
#         "above_department_average_ids": set()
#     }
#
#     salary_sums = {}
#     skill_counts = {}
#     top_salaries = {}
#
#     # 1. Հաշվում ենք աշխատակիցների քանակը,
#     # աշխատավարձերի գումարը և հմտությունների հաճախականությունը
#     for employee in employees:
#         department = employee["department"]
#         salary = employee["salary"]
#
#         if department not in d["department_counts"]:
#             d["department_counts"][department] = 0
#             salary_sums[department] = 0
#             top_salaries[department] = None
#
#         d["department_counts"][department] += 1
#         salary_sums[department] += salary
#
#         # Ամենաբարձր աշխատավարձ ունեցող աշխատակիցը
#         if (top_salaries[department] is None
#                 or salary > top_salaries[department]):
#             top_salaries[department] = salary
#             d["department_top_employee"][department] = employee["name"]
#
#         # Հմտությունները
#         for skill in employee["skills"]:
#             d["unique_skills"].add(skill)
#
#             if skill not in skill_counts:
#                 skill_counts[skill] = 0
#
#             skill_counts[skill] += 1
#
#     # 2. Հաշվում ենք յուրաքանչյուր բաժնի միջին աշխատավարձը
#     for department in d["department_counts"]:
#         d["department_average_salary"][department] = (
#             salary_sums[department]
#             / d["department_counts"][department]
#         )
#
#     # 3. Գտնում ենք ամենատարածված հմտությունը
#     if skill_counts:
#         d["most_common_skill"] = max(
#             skill_counts, key=skill_counts.get
#         )
#
#     # 4. Գտնում ենք միջինից բարձր աշխատավարձ ունեցող աշխատակիցներին
#     for employee in employees:
#         department = employee["department"]
#
#         if employee["salary"] > d["department_average_salary"][department]:
#             d["above_department_average_ids"].add(employee["id"])
#
#     return d
#
# print(analyze_employees(employees))

# system_a = [
#     {"id": 1, "email": "anna@example.com", "status": "active"},
#     {"id": 2, "email": "aram@example.com", "status": "active"},
#     {"id": 3, "email": "mariam@example.com", "status": "inactive"},
#     {"id": 4, "email": "karen@example.com", "status": "active"},
#     {"id": 5, "email": "ani@example.com", "status": "active"}
# ]
#
# system_b = [
#     {"id": 2, "email": "aram@example.com", "status": "active"},
#     {"id": 3, "email": "mariam_new@example.com", "status": "inactive"},
#     {"id": 4, "email": "karen@example.com", "status": "inactive"},
#     {"id": 6, "email": "gor@example.com", "status": "active"},
#     {"id": 5, "email": "ani@example.com", "status": "active"}
# ]
#
# def compare_systems(a,b):
#     bla = {"missing_ids":set(),
#            "unexpected_ids":set(),
#            "email_mismatches":set(),
#            "status_mismatches" : (),
#            "duplicate_ids_a":{},
#            "duplicate_ids_b":{}
#            }
#     for i in a:
#         for j in b:
#             if i["id"] == j["id"]:
#                 break
#             else:
#                 bla["missing_ids"].add(i["id"])
#
#     for j in b:
#         for k in a:
#             if j["id"] == k["id"]:
#                 break
#             else:
#                 bla["unexpected_ids"].add(j["id"])
#     for k in a:
#         for l in b:
#             if k["id"] == l["id"] and k["email"] != l["email"]:
#                 bla["email_mismatches"].add(k["email"])
#                 bla["email_mismatches"].add(l["email"])
#     for k in a:
#         for l in b:
#             if k["id"] == l["id"] and k["status"] != l["status"]:
#                 bla["email_mismatches"].add(k["status"])
#                 bla["email_mismatches"].add(l["status"])
#
#     for k in a:
#         for l in a:
#             if k["id"] == l["id"]:
#                 bla["duplicate_ids_a"]=k["id"]
#     for k in b:
#         for l in b:
#             if k["id"] == l["id"]:
#                 bla["duplicate_ids_b"]=k["id"]
#
#
#     return bla
#
# print(compare_systems(system_a,system_b))
#


# class Student:
#     def __init__(self, name, grade):
#         self.__name = name
#         self.__grade = grade
#     def get_grade(self):
#         return self.__grade
#     def set_grade(self,new_grade):
#         if new_grade < 0 or new_grade >= 100:
#             print("Invalid Grade")
#         else:
#             self.__grade = new_grade
#
# student = Student("John", 100)
# print(student.get_grade())
# bla =100
# student.set_grade(bla)
# print(student.get_grade())
#

#
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.__owner = owner
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
#     def deposit(self,amount):
#         if amount <= 0:
#             raise ValueError('amount must be positive')
#         self.__balance += amount
#     def withdraw(self,amount):
#         if amount <= 0 or amount > self.__balance:
#             raise ValueError('amount must be positive')
#         self.__balance -= amount
#
# account = BankAccount("Anna", 20000)
#
# account.deposit(5000)
# account.withdraw(3000)
# account.withdraw(5000)
#
# print(account.get_balance())

# class Student(object):
#     def __init__(self, name, grade):
#         self.name = name
#         self.__grade = grade
#     def get_grade(self):
#         return self.__grade
#     def set_grade(self, grade):
#         if grade < 0 or grade > 100:
#             raise ValueError("Grade must be between 0 and 100")
#         self.__grade = grade
#
#     def is_passed(self):
#         if self.__grade >=60:
#             return True
#         else:
#             return False
#
# student = Student("John", 50)
# student1 = Student("Babo", 70)
# print(student.is_passed())
# print(student1.is_passed())
# print(student.get_grade())

# class Product(object):
#     def __init__(self, name, price,quantity):
#         self.name = name
#         self.__price = price
#         self.__quantity = quantity
#     def get_price(self):
#         return self.__price
#     def get_quantity(self):
#         return self.__quantity
#
#     def restock(self, amount):
#         self.__quantity += amount
#         return self
#
#     def sell(self, amount):
#         self.__quantity -= amount
#         return self
#
# st =  Product("Milk",100,5)
# print(st.get_price())
# print(st.get_quantity())
# st.restock(10)
# print(st.get_price())
# print(st.get_quantity())
# st.sell(1)
# print(st.get_price())

# class Employee:
#     def __init__(self, name, salary, bonus):
#         self.name = name
#         self.__salary = salary
#         self.__bonus = bonus
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self,new_salary):
#         if new_salary > 0:
#             self.__salary = new_salary
#     def get_bonus(self, bonus):
#         if bonus >= 0:
#             self.__bonus = bonus
#
#     def get_total_salary(self):
#         return self.__salary + self.__bonus
#
#     def give_raise(self,amount):
#         if amount > 0:
#             self.__salary += amount
#
#     def display_info(self):
#         print("Name:", self.name)
#         print("Salary:", self.get_total_salary())
#
# employee1 = Employee("", 100000, 4000)
# employee2 = Employee("", 13000, 4000)
# employee1.display_info()
# employee = Employee("Anna", 300000, 20000)
#
# print(employee.get_salary())       # 300000
# print(employee.get_total_salary()) # 320000
#
# employee.give_raise(50000)
#
# print(employee.get_salary())       # 350000
# print(employee.get_total_salary()) # 370000
#
# employee.set_salary(-1000)          # Անվավեր
# print(employee.get_salary())       # 350000


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def make_sound(self):
#         print("Animal makes a sound")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
#
#
# dog = Dog("mila", 18)
# dog.make_sound()
# dog.bark()

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#     def get_age(self):
#         return self.__age
#     def set_age(self, new_age):
#         if new_age >0:
#             self.__age = new_age
#
# class Dog(Animal):
#     def bark(self):
#         print("bark")
#
# dog = Dog("Mila", 1)
# dog.bark()
# print(dog.get_age())
# dog.set_age(2)
# dog.bark()
# print(dog.get_age())
# dog.set_age(-3)
# print(dog.get_age())
# dog.bark()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Employee(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary
#     def set_salary(self, salary):
#         if salary > 0:
#             self.__salary = salary
#     def display_info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Salary:", self.get_salary())
#
# employee = Employee("WSF", 20, 10000)
# employee.display_info()
# print(employee.get_salary())
# employee.set_salary(3432)
# employee.display_info()
# print(employee.get_salary())

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             raise Exception('You cannot withdraw more than you have')
#         self.__balance -= amount
#
# class SavingsAccount(BankAccount):
#     def __init__(self, owner, balance,interest_rate):
#         super().__init__(owner, balance)
#         self.__interest_rate = interest_rate
#     def apply_interest(self):
#         self.deposit(self.get_balance() * self.__interest_rate/100)
#
# blbl = BankAccount("ezo", 10000)
#
# print(blbl.get_balance())
# blbl.withdraw(100)
# print(blbl.get_balance())
# blbl.deposit(500)
# print(blbl.get_balance())
#
# abab=SavingsAccount("abab",10000,20)
# print(abab.get_balance())
# abab.apply_interest()
# print(abab.get_balance())

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.__price = price
#         self.__quantity = quantity
#
#
# class DigitalProduct(Product):
#     def __init__(self, name, price, quantity):
#         Product.__init__(self, name, price, quantity)
#         self.__price = price
#         self.__quantity = quantity
#
# #     def show_price(self):
# #         print(self.__price)
#
#
# class Animal:
#     def make_sound(self):
#         return "My favorite animal"
#     def make_animal(self):
#         return "My favorite "
#
# class Dog(Animal):
#     def make_sound(self):
#         return "My favorite dog"
#
# class Cat(Animal):
#     def make_sound(self):
#         return "My favorite cat"
#
#
# animal = Animal()
# dog = Dog()
# cat = Cat()
# print(animal.make_sound())
# print(dog.make_sound())
# print(cat.make_animal())
# print(cat.make_sound())
#


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
#
# rec = Rectangle(100, 200)
# print(rec.area())

#
# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
#

# class BankAccount():
#     def __init__(self,owner, balance):
#         self.owner = owner
#         self.__balance = balance
#
#     def deposit(self,amount):
#         try:
#             self.__balance += amount
#         except ValueError:
#             raise ValueError("Cannot deposit amount to bank account")
#
#     def withdraw(self,amount):
#         try:
#             self.__balance -= amount
#         except ValueError:
#             raise ValueError("Cannot withdraw amount to bank account")
#
#     def get_balance(self):
#         return self.__balance

# class Account(ABC):
#     @abstractmethod
#     def account_info(self):
#         pass
#
#
#
# class BankAccount(Account):
#     def __init__(self,owner, balance):
#         self.owner = owner
#         self.__balance = balance
#
#     def deposit(self,amount):
#         if amount <= 0:
#             raise ValueError("Cannot deposit amount to bank account")
#
#         self.__balance += amount
#
#     def withdraw(self,amount):
#         if amount <= 0 or amount >= self.__balance:
#             raise ValueError("Cannot withdraw amount to bank account")
#         self.__balance -= amount
#
#     def get_balance(self):
#         return self.__balance
#     def account_info(self):
#         return {"owner":self.owner,"balance":self.__balance}
#
# class SavingsAccount(BankAccount):
#     def __init__(self,owner,balance,interest_rate):
#         super(SavingsAccount,self).__init__(owner,balance)
#         self.interest_rate = interest_rate
#
#     def add_interest(self):
#         self.deposit(self.interest_rate*self.get_balance()/100)
#
#     def account_info(self):
#         return {"owner":self.owner,"balance":self.get_balance(),"interest_rate":self.interest_rate}
#
# rec = BankAccount("john",100)
# print(rec.get_balance())
# try:
#     rec.withdraw(100)
# except ValueError as e:
#     print(e)
# dec = SavingsAccount("Mila",400,20)
# print(dec.account_info())
#
# animals = [dec,rec]
# for animal in animals:
#     animal.account_info()
# ss = BankAccount("john",100)
# ss.account_info()


# class PaymentProcessor(Protocol):
#     def process_payment(self, amount: float) -> bool:
#         ...
#
# class BankPayment:
#     def process_payment(self, amount: float) -> bool:
#         return amount>100
#
# def make_payment(processor: PaymentProcessor, amount: float):
#     print(processor.process_payment(amount))
#
#
# s = BankPayment()
# make_payment(s, 70)





# class Account(ABC):
#     def __init__(self, owner):
#         self.owner = owner
#     @abstractmethod
#     def account_info(self):
#         pass
#

# class DataSource(Protocol):
#     def  read_data(self) -> list :
#         ...
#
# class CSVDataSource:
#     def read_data(self,ab):
#         for i in ab:
#             print(i)
#
# class DatabaseDataSource:
#     def read_data(self, bla):
#         for i in bla:
#             print(i)
# class Logger:
#     def log(self,message):
#         print(message)
#
# class Validator:
#     def validate(self,data):
#         print(data)
#
# class DataPipeline(Logger,Validator,CSVDataSource, DatabaseDataSource):
#     def __init__(self,logger):
#         self.logger = logger
#     def read_data(self,data):
#         read_tx = self.log(data)
#         validate_tx = self.validate(read_tx)
#         self.logger=validate_tx
#     def get_data(self):
#         return self.logger
# A =[121,343,12125,5343,32323]
# B =[121,343,12125,5323]
# b = CSVDataSource()
# print(b.read_data(A))
# print(b.read_data(B))
# C =[121,343,12125,5343,32323]
# D =[121,343,12125,5323]
# c = DatabaseDataSource()
# print(c.read_data(C))
# print(c.read_data(D))
#
# # g = Logger()
# # g.log("hvgvhj")
# #
# # t = Validator()
# # t.validate("rde5768g")
#
# p = DataPipeline("barevik arevik")
# p.read_data("hgfcfyij")
# p.get_data()

# employees = [
#     {"id": 1, "name": "Anna", "department": "IT", "salary": "350000"},
#     {"id": 2, "name": "Karen", "department": "HR", "salary": 280000},
#     {"id": 3, "name": "Aram", "department": "IT", "salary": 420000},
#     {"id": 4, "name": "Mariam", "department": "Finance", "salary": 390000},
# ]
#
# class EmployeeDataSource:
#     def get_data(self):
#         return employees
#
# class EmployeeProcessor:
#     def __init__(self, data: EmployeeDataSource):
#             self.__data_source = data
#
#     def get_data(self):
#         return self.__data_source.get_data()
#
#     def get_it_employees(self):
#         emp = self.get_data()
#         ret = []
#         for employee in emp:
#             if employee["department"] == "IT":
#                 ret.append(employee)
#         return ret
#
#     def get_average_salary(self):
#         emp = self.get_data()
#         avg_salary = 0
#         for employee in emp:
#             if employee["salary"] is not None:
#                 avg_salary += employee["salary"]
#         return avg_salary/len(emp)
#
#
# source = EmployeeDataSource()
# processor = EmployeeProcessor(source)
# print(processor.get_it_employees())
# try:
#     print(processor.get_average_salary())
# except TypeError:
#     raise ("TypeError")
# finally:
#     print("meka anelu ei ")





# array = [1475,412856, 50850, 74152, 145236, 10523697, 10, 82586]
# def blabla(tiv):
#     count = 0
#     while tiv!=0:
#         count += 1
#         tiv//=10
#     return count
#
# for j in range(len(array)):
#     for i in range(j+1,len(array)):
#         if blabla(array[j])<blabla(array[i]):
#             k = array[i]
#             array[i]= array[j]
#             array[j] = k
#         elif blabla(array[j])==blabla(array[i]):
#             if array[i]>array[j]:
#                 k = array[i]
#                 array[i] = array[j]
#                 array[j] = k
# print(array)

# def is_valid_username(username: str):
#     l = str.strip(username)
#     if l[0].isalpha() and (len(l)>=5 and len(l)<=15):
#         for i in range(1,len(l)):
#             if l[i] == "_" or l[i] is CHAR:
#                 return True
#
#     return False
#
# print(is_valid_username("YOUR_USERNAME"))
#

#
# def process_file(filename: str):
#     print("Started processing:" + filename)
#     time.sleep(2)
#     print("Finished processing:" + filename)
#
# filenames = ["orders.csv","orders.csv", "orders.csv",
#              "orders.csv", "orders.csv", "orders.csv",
#              "orders.csv", "orders.csv", "orders.csv", "orders.csv" ]
# threads = []
# for filename in filenames:
#     t = threading.Thread(target=process_file, args=(filename,))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#


# def calculate_square(number):
#         n1 = number ** 2
#         print(f"{number} squared = {n1}")
#
#
# # p2 = Process(target=calculate_square, args=(5))
# # p3 = Process(target=calculate_square, args=(5))
# # p4 = Process(target=calculate_square, args=(5))
# # p5 = Process(target=calculate_square, args=(5))
# #
# #
# # p1.start()
# # p2.start()
# # p3.start()
# # p4.start()
#
# # p2.join()
# # p3.join()
# # p4.join()
# # p5.join()
#
# if __name__ == "__main__":
#     numbers = [10, 20, 30, 40]
#     processes = []
#     for number in numbers:
#         process = multiprocessing.Process(target=calculate_square, args=(number,))
#
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()
#
#     print("prc")


