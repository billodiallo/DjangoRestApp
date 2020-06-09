from django.urls import path
from magazine import views
urlpatterns = [
    path('', views.UserCreateListAPIView.as_view(), name='get-list-users')
]
