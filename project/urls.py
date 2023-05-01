from django.contrib import admin
from django.urls import path
from revenue import views
from home.views import  home
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
path("", home, name="home"),
path("incoming/", views.incoming, name="incoming"),
path("outgoing/", views.outgoing, name="outgoing"),
path("dashboard/", views.dashboard, name="dashboard"),
path("login/", views.log_in, name="login"),
path("logout/", views.log_out, name="logout"),
    path('admin/', admin.site.urls),
] 

if settings.DEBUG:
  urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

