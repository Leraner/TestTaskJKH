from datetime import datetime
from enum import Enum

from django.db import models
from django_enum_choices.fields import EnumChoiceField


class Months(Enum):
    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUNE = 'June'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER = 'October'
    NOVEMBER = 'November'
    DECEMBER = 'December'


class Accrual(models.Model):
    date = models.DateTimeField(default=datetime.now)
    month = EnumChoiceField(Months)

    def __str__(self):
        return f'ACCRUAL {self.pk}: {self.date}'


class Payment(models.Model):
    date = models.DateTimeField(default=datetime.now)
    month = EnumChoiceField(Months)

    def __str__(self):
        return f'PAYMENT {self.pk}: {self.date}'


class PaidDebt(models.Model):
    accrual = models.OneToOneField(Accrual, on_delete=models.CASCADE)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return f'REPAID DEBTS {self.pk}: {self.accrual, self.payment}'
