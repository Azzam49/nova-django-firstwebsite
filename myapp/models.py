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
    address = models.CharField(max_length=200, null=True, blank=True)

    # age uses IntegerField to store full numbers
    # age is required field
    # age will set 0 to existing records (default=0)
    # age will set 0 to new records that didn't set age (default=0)
    age = models.IntegerField(default=0)

    # admission_fee uses DecimalField to store decimal values
    # admission_fee have max number as 999.99 because we max_digits=5,
    #   which includes the decinmal places that set by decimal_places=2
    admission_fee = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    # 1,234,567.89 (max_digits=9, decimal_places=2)
    # 999.99 (max_digits=5, decimal_places=2)

    # DONE - age               = IntegerField
    # DONE - address           = CharField
    # email             = EmailField
    # DONE - admission_fee     = DecimalField


    # This __str__ function, is a function that django expects.
    # It acts as the representation string for the models' record
    def __str__(self):
        return self.name # django will use the `name` column as representation string for each record