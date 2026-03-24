from django.urls import include, path
from rest_framework.routers import DefaultRouter

from garage import views

router = DefaultRouter()
router.register('parts', views.PartModelViewSet, basename='parts')

urlpatterns = [
    path('cars/', include([
        path('', views.ListCreateCar.as_view(), name='car-list'),
        path('<int:pk>/', views.RetrieveUpdateDestroyCarAPIView.as_view(), name='car-detail'),
        path('stats/', views.CarStatsView.as_view(), name='car-stats'),
    ])),

    path('manufacturers/', views.ListCreateManufacturerAPIView.as_view(), name='manufacturer-list'),
    path('admin-dashboard/', views.AdminDashboardView.as_view(), name='admin-dashboard'),

] + router.urls
