from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dev01.views.home', name='home'),
    # url(r'^dev01/', include('dev01.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^projects/$', 'dev01.gerenciadorprojetos.views.project_index'),    
    url(r'^projects/create', 'dev01.gerenciadorprojetos.views.project_create'),
    url(r'^projects/new', 'dev01.gerenciadorprojetos.views.project_new'),
    url(r'^/project/(?P\d+)/edit$', 'dev01.gerenciadorprojetos.views.project_edit'),
)
