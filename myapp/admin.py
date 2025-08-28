from django.contrib import admin
from myapp.models import Student

# Register your models here.

@admin.register(Student) # registers the StudentAdmin and link it with the Student model
class StudentAdmin(admin.ModelAdmin):

    # list_display is used to display those columns on the django admin site
    list_display = [
        "name",
        "age",
        "address",
        "admission_fee",
        "email",
    ]