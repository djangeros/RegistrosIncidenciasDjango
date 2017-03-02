from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.forms import AdminPasswordChangeForm
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','principal.views.ingresar'),
	url(r'^inicio/$','principal.views.inicio'),
    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^sobre/$','principal.views.sobre'),
    url(r'^incidencias/$','principal.views.lista_incidencias'),
    url(r'^asignaciones/$','principal.views.lista_incidencias_asignaciones'),
    url(r'^cierrei/$','principal.views.lista_incidencias_cierre'),
    url(r'^incidencia/(?P<id_incidencia>\d+)$','principal.views.detalle_incidencia'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
    url(r'^contacto/$','principal.views.contacto'),
    url(r'^incidencia/nueva/$','principal.views.nueva_incidencia'),
    url(r'^solucion/(?P<id>\d+)$','principal.views.nuevo_solucion'),
    url(r'^solucions/$','principal.views.ver_solucion'),
    url(r'^cierres/$','principal.views.nuevo_cierre'),
    url(r'^cierre/(?P<id>\d+)$','principal.views.nuevo_cierre'),
    url(r'^usuario/nuevo$','principal.views.nuevo_usuario'),
    url(r'^ingresar/$','principal.views.ingresar'),
    url(r'^reportes/$','principal.views.reportes'),
    url(r'^reportes1/$','principal.views.reportes1'),
    url(r'^reportes2/$','principal.views.reportes2'),
    url(r'^reportes3/$','principal.views.reportes3'),
    url(r'^cerrar/$', 'principal.views.cerrar'),
    url(r'^consultas/$','principal.views.privado'),
    url(r'^editar_contrasena/$', 'principal.views.editar_contrasena'),
    url(r'^search/$', 'principal.views.search'),
)
