from rest_framework.routers import DefaultRouter
from .views import FonctionnaireViewSet, BulletinPaieViewSet

router = DefaultRouter()
router.register('fonctionnaires', FonctionnaireViewSet)
router.register('bulletins', BulletinPaieViewSet)

urlpatterns = router.urls