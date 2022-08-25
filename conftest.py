import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from Account.models import Account, Session, ActionsType, Action
from Finance.models import Months, Accrual, Payment


@pytest.fixture(scope='function')
def api_client():
    return APIClient()


@pytest.fixture(autouse=True)
def override_settings():
    settings.CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer"
        }
    }


@pytest.fixture(scope='function')
def count():
    return 5


@pytest.fixture(scope='function')
def months():
    return 'September'


@pytest.fixture(scope='function')
def account_data():
    return {
        'name': 'ПользовательTest №',
        'number': '+7922761778'
    }


@pytest.fixture(scope='function')
def session_data():
    return {
        'session_id': 'aBBasdjasjd1'
    }


@pytest.fixture(scope='function')
def create_account(account_data, count):
    accounts_list = []
    for i in range(count):
        new_account_data = account_data.copy()
        new_account_data.update({
            'name': f'{account_data["name"]}{i}',
            'number': f'{account_data["number"]}{i}'

        })
        new_account = Account.objects.create(**new_account_data)
        accounts_list.append(new_account)

    return accounts_list


@pytest.fixture(scope='function')
def create_session(session_data, count):
    sessions_list = []
    for i in range(count):
        new_session_data = session_data.copy()
        new_session_data.update({
            'session_id': f'{session_data["session_id"]}{i}',
            'account': Account.objects.filter(name=f'ПользовательTest №{i}').first()
        })

        new_session = Session.objects.create(**new_session_data)
        sessions_list.append(new_session)

    return sessions_list


@pytest.fixture(scope='function')
def create_accrual(months):
    return Accrual.objects.create(month=Months(value=months))


@pytest.fixture(scope='function')
def create_payment(months):
    return Payment.objects.create(month=Months(value=months))
