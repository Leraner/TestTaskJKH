import pytest
from django.urls import reverse
from rest_framework import status

from Account.models import Action, ActionsType, Account, Session

pytestmark = [
    pytest.mark.django_db,
]


@pytest.mark.parametrize('count', [2])
def test_get_information_read(api_client, create_account, create_session):
    accounts = create_account
    sessions = create_session
    actions = []

    for session in sessions:
        actions.append(Action.objects.create(type=ActionsType.READ, session=session))

    data = {
        'information': [
            {
                'number': f'{accounts[0].number.raw_input[1::]}',
                'actions': [
                    {
                        'type': actions[0].type.value,
                        'last': {
                            'created_at': actions[0].created_at
                        },
                        'count': 1
                    },
                    {
                        'type': 'create',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': 'update',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': 'delete',
                        'last': 'null',
                        'count': 0
                    }
                ]
            },
            {
                'number': f'{accounts[1].number.raw_input[1::]}',
                'actions': [
                    {
                        'type': actions[1].type.value,
                        'last': {
                            'created_at': actions[1].created_at
                        },
                        'count': 1
                    },
                    {
                        'type': 'create',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': 'update',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': 'delete',
                        'last': 'null',
                        'count': 0
                    }
                ]
            }
        ]
    }

    url = reverse('account-get-last-move')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    assert response.data == data


@pytest.mark.parametrize('count', [2])
def test_get_information_create(api_client, create_account, create_session):
    accounts = create_account
    sessions = create_session
    actions = []

    for session in sessions:
        actions.append(Action.objects.create(type=ActionsType.CREATE, session=session))

    data = {
        'information': [
            {
                'number': f'{accounts[0].number.raw_input[1::]}',
                'actions': [
                    {
                        'type': 'read',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': actions[0].type.value,
                        'last': {
                            'created_at': actions[0].created_at
                        },
                        'count': 1
                    },
                    {
                        'type': 'update',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': 'delete',
                        'last': 'null',
                        'count': 0
                    }
                ]
            },
            {
                'number': f'{accounts[1].number.raw_input[1::]}',
                'actions': [
                    {
                        'type': 'read',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': actions[1].type.value,
                        'last': {
                            'created_at': actions[1].created_at
                        },
                        'count': 1
                    },
                    {
                        'type': 'update',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': 'delete',
                        'last': 'null',
                        'count': 0
                    }
                ]
            }
        ]
    }

    url = reverse('account-get-last-move')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    assert response.data == data


@pytest.mark.parametrize('count', [2])
def test_get_information_update(api_client, create_account, create_session):
    accounts = create_account
    sessions = create_session
    actions = []

    for session in sessions:
        actions.append(Action.objects.create(type=ActionsType.UPDATE, session=session))
    data = {
        'information': [
            {
                'number': f'{accounts[0].number.raw_input[1::]}',
                'actions': [
                    {
                        'type': 'read',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': 'create',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': actions[0].type.value,
                        'last': {
                            'created_at': actions[0].created_at
                        },
                        'count': 1
                    },
                    {
                        'type': 'delete',
                        'last': 'null',
                        'count': 0
                    }
                ]
            },
            {
                'number': f'{accounts[1].number.raw_input[1::]}',
                'actions': [
                    {
                        'type': 'read',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': 'create',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': actions[1].type.value,
                        'last': {
                            'created_at': actions[1].created_at
                        },
                        'count': 1
                    },
                    {
                        'type': 'delete',
                        'last': 'null',
                        'count': 0
                    }
                ]
            }
        ]
    }

    url = reverse('account-get-last-move')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    assert response.data == data


@pytest.mark.parametrize('count', [2])
def test_get_information_delete(api_client, create_account, create_session):
    accounts = create_account
    sessions = create_session
    actions = []

    for session in sessions:
        actions.append(Action.objects.create(type=ActionsType.DELETE, session=session))
    data = {
        'information': [
            {
                'number': f'{accounts[0].number.raw_input[1::]}',
                'actions': [
                    {
                        'type': 'read',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': 'create',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': 'update',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': actions[0].type.value,
                        'last': {
                            'created_at': actions[0].created_at
                        },
                        'count': 1
                    },
                ]
            },
            {
                'number': f'{accounts[1].number.raw_input[1::]}',
                'actions': [
                    {
                        'type': 'read',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': 'create',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': 'update',
                        'last': 'null',
                        'count': 0
                    },
                    {
                        'type': actions[1].type.value,
                        'last': {
                            'created_at': actions[1].created_at
                        },
                        'count': 1
                    },
                ]
            }
        ]
    }

    url = reverse('account-get-last-move')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    assert response.data == data
