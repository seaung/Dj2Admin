from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.db.models import Q
# Create your views here.


User = get_user_model()


class UserModelBackends(ModelBackend):
    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password=password):
                return user
        except Exception as e:
            return None


class HomeView(View):
    def get(self, request):
        return render(request, "home.html", locals())


class SignInView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class SignUpView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
