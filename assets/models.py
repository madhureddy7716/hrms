from django.db import models
from employees.models import Employee


class Asset(models.Model):

    asset_id = models.CharField(
        max_length=20
    )

    asset_name = models.CharField(
        max_length=100,
        default='Unknown Asset'
    )

    asset_type = models.CharField(
        max_length=50,
        default='General'
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    issue_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        default='Available'
    )

    def __str__(self):
        return self.asset_name


class AssetHistory(models.Model):

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    action = models.CharField(
        max_length=50
    )

    action_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.asset} - {self.action}"