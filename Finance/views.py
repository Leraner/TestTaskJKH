from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Accrual, Payment, PaidDebt
from .serializer import AccrualSerializer, PaymentSerializer, PaidDebtSerializer
from .services import get_same_months, search_for_payments_by_month, searching_for_single_payments


class PaidDebtView(ModelViewSet):
    serializer_class = PaidDebtSerializer
    queryset = PaidDebt.objects.all()

    def list(self, request, *args, **kwargs):
        accruals = Accrual.objects.all().order_by('-date')
        payments = Payment.objects.all().order_by('-date')

        if not (payments and accruals):
            return Response({"information": "Nothing"})

        same_months = get_same_months(payments, accruals)
        payments, accruals = search_for_payments_by_month(payments, accruals, same_months)
        searching_for_single_payments(payments, accruals)

        return super(PaidDebtView, self).list(request, *args, **kwargs)

    @action(detail=False, methods=["GET"])
    def get_remaining_payments(self, request):
        remaining_payments = []
        serialized_data = []

        for payment in Payment.objects.all():
            if not PaidDebt.objects.filter(payment=payment).exists():
                remaining_payments.append(payment)

        if remaining_payments:
            for payment in remaining_payments:
                serialized_data.append(PaymentSerializer(instance=payment).data)
            return Response({"information": serialized_data})
        return Response({"information": "Nothing"})

    @action(detail=False, methods=["GET"])
    def get_remaining_accruals(self, request):
        remaining_accruals = []
        serialized_data = []

        for accrual in Accrual.objects.all():
            print(PaidDebt.objects.filter(accrual=accrual))
            if not PaidDebt.objects.filter(accrual=accrual).exists():
                remaining_accruals.append(accrual)

        if remaining_accruals:
            for accrual in remaining_accruals:
                serialized_data.append(AccrualSerializer(instance=accrual).data)
            return Response({"information": serialized_data})
        return Response({"information": "Nothing"})
