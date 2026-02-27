from django.urls import path

from accounts import views
from common.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]