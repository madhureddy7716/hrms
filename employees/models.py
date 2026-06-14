from django.db import models


class Employee(models.Model):

    emp_id = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=10
    )

    department = models.CharField(
        max_length=100
    )

    designation = models.CharField(
        max_length=100
    )

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    photo = models.ImageField(
        upload_to='employee_photos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name