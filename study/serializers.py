from rest_framework import serializers
from rest_framework.fields import CharField, EmailField, IntegerField

from study.models import Department, Employee, Project


class DepartmentSerializer(serializers.ModelSerializer):
    name = CharField(max_length=50)
    description = CharField(max_length=50)
    class Meta:
        model = Department
        fields = ('id', 'name', 'description')

    def create(self, validated_data):
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class EmployeeSerializer(serializers.ModelSerializer):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = EmailField()
    salary = IntegerField(min_value=0)
    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department_id'
    )
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'email', 'salary', 'department', 'hire_date')

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.department = validated_data.get('department', instance.department)
        instance.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):
    name = CharField(max_length=50)
    description = CharField(max_length=100)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description')
    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance