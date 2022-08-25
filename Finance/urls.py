from rest_framework.routers import SimpleRouter

from .views import PaidDebtView

router = SimpleRouter()
router.register('', PaidDebtView, basename='finance')

urlpatterns = []

urlpatterns += router.urls
