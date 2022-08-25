from rest_framework.routers import SimpleRouter

from .views import AccountView

router = SimpleRouter()
router.register('', AccountView, basename='account')

urlpatterns = []

urlpatterns += router.urls
