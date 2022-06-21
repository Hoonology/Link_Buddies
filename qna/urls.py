from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = "qna"

urlpatterns = [
    path("", views.qnalist.as_view(), name="qna_view"),
    path("editor/<int:qna_id>", views.modify, name="qna_form_m"),
    path("editor/", views.create, name="qna_form"),
    path("detail/<int:qna_id>", views.detail, name="qna_detail"),
    path("delete/<int:qna_id>", views.delete, name="qna_delete"),
]

