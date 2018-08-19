from django.urls import path
from accounts.views import SignInView, SignUpView

urlpatterns = [
    path('/sigin/', SignInView.as_view(), name='login'),
    path('/sigup/', SignUpView.as_view(). name='signup'),
]
