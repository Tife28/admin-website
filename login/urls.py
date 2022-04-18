from django.urls import path
from .views import LoginPageView, PindexPageView
urlpatterns = [
path('', LoginPageView.as_view(), name='login'),
path('pindex/', PindexPageView.as_view(), name='pindex'),
]