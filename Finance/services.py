from typing import Any

from .models import PaidDebt


def is_exist(accruals, payment) -> bool:
    if PaidDebt.objects.filter(accrual=accruals, payment=payment).exists() or \
            PaidDebt.objects.filter(payment=payment).exists() or \
            PaidDebt.objects.filter(accrual=accruals).exists():
        return True
    return False


def get_same_months(payments, accruals) -> list:
    """ Search same payments and accrual months """
    payments_with_months = []

    for payment in payments:
        filtered_accruals = accruals.filter(month=payment.month, date__lte=payment.date)
        if filtered_accruals:
            payments_with_months.append(payment.month.value)

    return payments_with_months


def search_for_payments_by_month(payments, accruals, payments_with_months: list) -> tuple[Any, Any]:
    """ Search and conjugation payments with accrual by same months """
    for payment in payments[::-1]:
        if payment.month.value in payments_with_months:
            accrual = accruals.filter(month=payment.month, date__lte=payment.date).last()
            if accrual and not is_exist(accrual, payment):
                PaidDebt.objects.create(accrual=accrual, payment=payment)
                accruals = accruals.exclude(pk=accrual.pk)
                payments = payments.exclude(pk=payment.pk)

    return payments, accruals


def searching_for_single_payments(payments, accruals) -> None:
    """ Conjugation remaining payments and accruals """
    for payment in payments[::-1]:
        accrual = accruals.filter(date__lte=payment.date).order_by('date').first()
        if accrual:
            accruals = accruals.exclude(pk=accrual.pk)
            if not PaidDebt.objects.filter(accrual=accrual, payment=payment).exists():
                PaidDebt.objects.create(accrual=accrual, payment=payment)

