from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
class FourZeroFourPageView(TemplateView):
    template_name = '404.html'
class FiveZeroZeroPageView(TemplateView):
    template_name = '500.html'
# class PindexPageView(TemplateView):
#     template_name = 'pindex.html'
class YandexPageView(TemplateView):
    template_name = 'yandex.html'