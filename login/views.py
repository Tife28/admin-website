from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class LoginPageView(TemplateView):
    template_name = 'login.html'
    # def get(self, request):
    #     form = self.form_class()
    #     message = ''
    #     return render(request, self.template_name, context ={'form': form, 'message': message})
    # def post(self, request):
    #     form = self.form_class(request.get.POST)
    #     if form.is_valid():
    #         user = authenticate(
    #             username=form.cleaned_data['username'],
    #             password=form.cleaned_data['password'],
    #         )
    #         if user is not None:
    #             login(request, user)
    #             return redirect('pindex/')
    #     message = 'Login failed!'
    #     return render(request, self.template_name, context={'form': form, 'message': message})
class PindexPageView(TemplateView):
    template_name = 'pindex.html'