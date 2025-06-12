from django.urls import path, include, re_path

from app.views import index, confirm_email, send_confirmation_email

app_name = 'app'
urlpatterns = [
    path('', index, name='index'),
    path('confirm_email/<str:token>/', confirm_email, name='confirm_email'),
    path('submit_email/', send_confirmation_email, name='submit_email')
]