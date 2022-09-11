from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<id>/', views.index, name='index'),
    path('config/', views.stripe_config),
    path('buy/<id>/', views.buy),
]
