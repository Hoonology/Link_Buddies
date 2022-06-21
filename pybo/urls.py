from django.urls import path

from . import views
app_name = 'pybo'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name='detail'),
    path('layout/', views.lay, name='layout1'),
    path('layout2/', views.lay2, name='layout2'),
    path('layout3/', views.lay3, name='layout3'),
    path('layout4/', views.lay4, name='layout4'),
]