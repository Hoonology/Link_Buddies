from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = "community"

urlpatterns = [
    path("", views.community, name="content_list"),
    # path("editor/<int:qna_id>", views.modify, name="content_m_editor"),
    # path("editor/", views.create, name="content_editor"),
    path("detail/<int:content_id>", views.detail, name="qna_detail"),
    # path("delete/<int:qna_id>",views.delete,name="qna_delete"),
]
