from django.urls import path
from .views import FourZeroFourPageView, FiveZeroZeroPageView, YandexPageView#, PindexPageView
urlpatterns = [
#path('', PindexPageView.as_view(), name='pindex'),
path('404/', FourZeroFourPageView.as_view(), name='404'),
path('500/', FiveZeroZeroPageView.as_view(), name='500'),
path('yandex/', YandexPageView.as_view(), name='yandex'),
]