from django.urls import path
from .views import home, SignUpView, LoginView, logout_user

app_name = 'account'
urlpatterns = [
    path('home/', home, name='home'),
    path('sing_up/', SignUpView.as_view(), name='sing_up'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

]
