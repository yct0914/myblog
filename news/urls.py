from django.urls import path
from . import views
urlpatterns = [
    path('weibo',views.WeiBo.as_view())
]
