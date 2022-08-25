import json

import pytest
from django.urls import reverse
from rest_framework import status

from Finance.models import Accrual, Months, Payment, PaidDebt

pytestmark = [
    pytest.mark.django_db,
]


@pytest.mark.parametrize('months', ['September'])
def test_accrual_and_payments_same_months(api_client, create_accrual, create_payment):
    accrual = create_accrual
    payment = create_payment

    data = [
        {
            "accrual": {
                "date": str(accrual.date.isoformat()) + 'Z',
                "month": accrual.month.value
            },
            "payment": {
                "date": str(payment.date.isoformat()) + 'Z',
                "month": payment.month.value
            }
        }
    ]

    url = reverse('finance-list')

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(json.dumps(response.data[0], indent=4)) == data[0]


def test_accrual_and_payments_different_months(api_client, create_accrual):
    accrual = create_accrual
    payment = Payment.objects.create(month=Months.SEPTEMBER)

    data = [
        {
            "accrual": {
                "date": str(accrual.date.isoformat()) + 'Z',
                "month": accrual.month.value
            },
            "payment": {
                "date": str(payment.date.isoformat()) + 'Z',
                "month": payment.month.value
            }
        }
    ]

    url = reverse('finance-list')

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(json.dumps(response.data[0], indent=4)) == data[0]


def test_get_remaining_payments(api_client, create_accrual):
    accrual = create_accrual
    payment1 = Payment.objects.create(month=Months.SEPTEMBER)
    payment2 = Payment.objects.create(month=Months.OCTOBER)

    data = [
        {
            "date": str(payment2.date.isoformat()) + 'Z',
            "month": "October"
        }
    ]

    url_remaining = reverse('finance-get-remaining-payments')
    url = reverse('finance-list')

    api_client.get(url)
    response = api_client.get(url_remaining)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(json.dumps(response.data['information'][0], indent=4)) == data[0]


def test_get_remaining_accruals(api_client):
    accrual1 = Accrual.objects.create(month=Months.SEPTEMBER)
    accrual2 = Accrual.objects.create(month=Months.JANUARY)
    payment1 = Payment.objects.create(month=Months.APRIL)

    data = [
        {
            "date": str(accrual2.date.isoformat()) + 'Z',
            "month": "January"
        }
    ]

    url_remaining = reverse('finance-get-remaining-accruals')
    url = reverse('finance-list')

    api_client.get(url)

    response = api_client.get(url_remaining)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(json.dumps(response.data['information'][0], indent=4)) == data[0]
