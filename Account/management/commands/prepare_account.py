from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from Account.models import Account, Session, Action, ActionsType

User = get_user_model()


class Command(BaseCommand):
    ACCOUNTS = {"Пользователь №1": "+79213615564", "Пользователь №2": "+79213615532"}

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
            if admin:
                print('Administrator created successfully - credits - admin/admin')

        for account_info in self.ACCOUNTS:

            if not Account.objects.filter(name=account_info, number=self.ACCOUNTS[account_info]).exists():
                account = Account.objects.create(name=account_info, number=self.ACCOUNTS[account_info])
                print(f'Account {account_info} created successfully')
            else:
                account = Account.objects.filter(name=account_info, number=self.ACCOUNTS[account_info]).first()

            session = Session.objects.create(session_id='jjADgg231HHjdjasdjg2g23', account=account)

            if session:
                for _ in range(0, 12):
                    action = Action.objects.create(type=ActionsType.READ, session=session)

                    if action:
                        print(f'Action [type: {action.type.value}] created successfully')

                for _ in range(0, 12):
                    action = Action.objects.create(type=ActionsType.CREATE, session=session)

                    if action:
                        print(f'Action [type: {action.type.value}] created successfully')
