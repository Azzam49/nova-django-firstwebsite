from django.db import models

# Create your models here.

# Task:
    # - Create Student table with the columns (id, name)


# one model = one table in database
class Student(models.Model):
    # 1 - id column
    # id column will be auto created by Django, no need to define it inside the Student model.

    # 2 - name column
    # CharField = varchar
    # CharField is used to store string
    # name column is varchar, with max length of characters as 10
        # if chars count <= 10, no issue
        # if chars count > 10, record will not get created in database (it will error)
    # by default, name is required column
        # if you have a value for name as name="Alice", no issue
        # if name column is left blank as name="", database will error
    # how to make the column optional?
        # by using null=True, blank=True attributes
        # that will not error in case that name is left blank as name=""
    name = models.CharField(max_length=10, null=True, blank=True)
