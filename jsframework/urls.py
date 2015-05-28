from django.conf.urls import include, url
from . import views

    # Examples:
urlpatterns = [
    # Examples:
    # url(r'^$', 'django_drf_starter_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index)
]