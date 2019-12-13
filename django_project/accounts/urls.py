from django.urls import path
from . import views
from django.contrib.auth import views as account_view


urlpatterns = [
    path('register/', views.register, name='account-register'),
    path('login/', account_view.LoginView.as_view(template_name='accounts/login.html'),
         name='account-login'),
    path('logout/', account_view.LogoutView.as_view(template_name='accounts/logout.html'),
         name='account-logout'),
    path('password-reset/', account_view.PasswordResetView.as_view(template_name='accounts/password-reset.html'),
         name='password-reset'),
    path('password-reset/done/', account_view.PasswordResetDoneView.as_view(template_name='accounts/password-reset-done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', account_view.PasswordResetConfirmView.as_view(template_name='accounts/password-reset-confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete', account_view.PasswordResetCompleteView.as_view(template_name='accounts/password-reset-complete.html'),
         name='password_reset_complete'),
    path('profile/', views.profile, name='account-profile'),
]
