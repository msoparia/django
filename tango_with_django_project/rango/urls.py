from django.conf.urls import patterns, url
from rango import views



urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
