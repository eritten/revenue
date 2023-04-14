from django.contrib import admin
from django.urls import path
from revenue import views

urlpatterns = [
path("incoming/", views.incoming, name="incoming"),
path("outgoing/", views.outgoing, name="outgoing"),
path("dashboard/", views.dashboard, name="dashboard"),
path("login/", views.log_in, name="login"),
path("logout/", views.log_out, name="logout"),
    path('admin/', admin.site.urls),
]
