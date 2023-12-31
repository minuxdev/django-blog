from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("article/create/", views.article_create, name="article_create"),
    path(
        "article/update/<slug>/", views.article_update, name="article_update"
    ),
    path(
        "article/details/<slug>/",
        views.article_details,
        name="article_details",
    ),
    path(
        "article/delete/<slug>/",
        views.article_delete,
        name="article_delete",
    ),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
