from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
					# User accounts
					url(r'^$',          'grid_frontend.views.get_main'),
					url(r'^login/$',    'grid_frontend.views.login'),
					url(r'^logout/$',   'grid_frontend.views.logout'),
					url(r'^register/$', 'grid_frontend.views.register'),

					# Projects
					url(r'^jobs/$', 'grid_frontend.views.jobs_list'),
					url(r'^create_job/$', 'grid_frontend.views.create_job'),
					url(r'^ajax/add_loadcase/$', 'grid_frontend.views.create_loadcase'),
					url(r'^ajax/add_model/$', 'grid_frontend.views.create_model'),
					url(r'^search_job/$', 'grid_frontend.views.search_job'),
					url(r'^delete_job/(?P<job_id>\d+)/$', 'grid_frontend.views.delete_job'),
					url(r'^edit_job/(?P<job_id>\d+)/$', 'grid_frontend.views.edit_job'),
					url(r'^calc_job/(?P<job_id>\d+)/$', 'grid_frontend.views.calc_job'),

					# Admin
					url(r'^admin/', include(admin.site.urls)),
					)