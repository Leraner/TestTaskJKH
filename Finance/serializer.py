from django_enum_choices.serializers import EnumChoiceModelSerializerMixin
from rest_framework.serializers import ModelSerializer

from Finance.models import Accrual, Payment, PaidDebt


class AccrualSerializer(EnumChoiceModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Accrual
        fields = (
            'date',
            'month'
        )


class PaymentSerializer(EnumChoiceModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'date',
            'month'
        )


class PaidDebtSerializer(ModelSerializer):
    accrual = AccrualSerializer(read_only=True)
    payment = PaymentSerializer(read_only=True)

    class Meta:
        model = PaidDebt
        fields = (
            'accrual',
            'payment'
        )
