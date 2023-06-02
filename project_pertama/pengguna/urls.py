from django.urls import path
from pengguna import views

urlpatterns = [path("pengguna/", views.pengguna, name="pengguna")]
