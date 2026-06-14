from django.db import models


class Leave(models.Model):

    employee_name = models.CharField(
        max_length=100
    )

    leave_type = models.CharField(
        max_length=100
    )

    from_date = models.DateField(
        null=True,
        blank=True
    )

    to_date = models.DateField(
        null=True,
        blank=True
    )

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    def __str__(self):
        return self.employee_name