from django.conf.urls import include, url
from django.contrib import admin
from jsframework import urls as js_urls


urlpatterns = [
    # Examples:
    # url(r'^$', 'django_drf_starter_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^exercise/', include(exercise_customization_database.urls))
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(js_urls)),
]
