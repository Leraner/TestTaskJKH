from django.contrib import admin
from .models import Payment, Accrual, PaidDebt


admin.site.register(Accrual)
admin.site.register(Payment)
admin.site.register(PaidDebt)
