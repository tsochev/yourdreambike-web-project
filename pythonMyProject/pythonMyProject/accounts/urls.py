from django.urls import path

from pythonMyProject.accounts.views import UserRegistrationView, UserLoginView, logout_view, DetailsProfileView, \
    EditProfileView, ChangePasswordProfileView, DeleteProfileView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', logout_view, name='logout user'),

    path('profile/<int:pk>/', DetailsProfileView.as_view(), name='profile details'),
    path('edit/<int:pk>/', EditProfileView.as_view(), name='profile edit'),
    path('change_password/<int:pk>/', ChangePasswordProfileView.as_view(), name='profile change password'),
    path('delete/<int:pk>/', DeleteProfileView.as_view(), name='profile delete'),

)
