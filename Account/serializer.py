from django_enum_choices.serializers import EnumChoiceModelSerializerMixin
from rest_framework.serializers import ModelSerializer

from .models import Account, Action, Session


class ActionSerializer(EnumChoiceModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Action
        fields = (
            'type',
            'created_at'
        )


class SessionSerializer(ModelSerializer):
    actions = ActionSerializer(many=True, read_only=True)

    class Meta:
        model = Session
        fields = (
            'created_at',
            'session_id',
            'actions',
        )


class AccountSerializer(ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = (
            'number',
            'name',
            'sessions',
        )
