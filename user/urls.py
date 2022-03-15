from django.urls import *
from . import views

urlpatterns = [
    path('get_info', views.get_info),
    path('login', views.UserViewSet.as_view({'post':'login'})),
    path('logon', views.UserViewSet.as_view({'post':'logon'})),
    
]

