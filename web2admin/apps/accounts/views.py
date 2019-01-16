from django.urls import reverse
from djang.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.model import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q



User = get_user_model()



class CustomeBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None



class SignInView(View):
    def get(self, request):
        redirect_url = request.GET.get('next', '')
        return render(request, 'signin.html', {'redirect_url': redirect_url})

    def post(self, request):
        forms = SignInForm(request.POST)
        if forms.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                    redirect_url = request.GET.get('next', '')

                    if redirect_url:
                        return HttpResponseRedirect(redirect_url)

                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'signin.html', {'msg': 'user is not
                                                           active'})
            else:
                return render(request, 'signin.html', {'msg': 'user is not
                                                       extist.'})
        return render(request, 'signin.html', {'forms': forms})

