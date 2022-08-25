from enum import Enum

from django.db import models
from django_enum_choices.fields import EnumChoiceField
from phonenumber_field.modelfields import PhoneNumberField


class ActionsType(Enum):
    READ = "read"
    CREATE = "create"
    UPDATE = "update"
    DELETE = 'delete'


class Account(models.Model):
    number = PhoneNumberField(unique=True, null=False, blank=False)
    name = models.CharField(max_length=225, null=False, blank=False)

    def __str__(self):
        return f'ID {self.id}: {self.name}'


class Session(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=225, null=False, blank=False)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, related_name='sessions')

    def __str__(self):
        return f'{self.session_id}: {self.id}'


class Action(models.Model):
    type = EnumChoiceField(ActionsType)
    created_at = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='actions')

    def __str__(self):
        return f'{self.type.value}: {self.session}'
