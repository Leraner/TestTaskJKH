from django.core.management.base import BaseCommand
from django.utils import timezone

from datetime import datetime

from Finance.models import Months, Accrual, Payment
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        Accrual.objects.create(date=datetime.now(tz=timezone.utc), month=Months.MAY)
        Accrual.objects.create(date=datetime.now(tz=timezone.utc), month=Months.DECEMBER)
        Accrual.objects.create(date=datetime.now(tz=timezone.utc), month=Months.AUGUST)
        time.sleep(5)
        Payment.objects.create(date=datetime.now(tz=timezone.utc), month=Months.DECEMBER)
        Payment.objects.create(date=datetime.now(tz=timezone.utc), month=Months.OCTOBER)
        Payment.objects.create(date=datetime.now(tz=timezone.utc), month=Months.AUGUST)
        Payment.objects.create(date=datetime.now(tz=timezone.utc), month=Months.APRIL)

        print(f'Created Payment:{Payment.objects.count()} | Accrual: {Accrual.objects.count()} successfully')
