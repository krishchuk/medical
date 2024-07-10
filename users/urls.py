from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ConfirmRegisterView, CustomLoginView, ProfileView, PasswordChangeView, \
    UserDeleteView, UsersListView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm/', ConfirmRegisterView.as_view(), name='confirm'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_reset/', PasswordChangeView.as_view(), name='password_reset'),
    path('delete/', UserDeleteView.as_view(), name='delete_user'),

    path('all_users/', UsersListView.as_view(), name='user_list'),
]
