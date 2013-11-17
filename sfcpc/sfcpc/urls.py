from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','principal.views.index'),
	url(r'^Factura/$','principal.views.Factura'),
    url(r'^Clientes/$', 'principal.views.Clientes'),
    url(r'^Pagos/$', 'principal.views.Pagos'),
    url(r'^Productos/$', 'principal.views.Productos'),
    url(r'^Clientes_Alta/$', 'principal.views.Clientes_Alta'),
    url(r'^Clientes_Baja/$', 'principal.views.Clientes_Baja'),
    url(r'^Clientes_Cambio/(P<id_Cliente>\d+)$', 'principal.views.Clientes_Cambio'),
    url(r'^Seleccionar_Cliente/(P<Nombre_Cliente>\w+)?/?(P<RFC_Cliente>)?','principal.views.Seleccionar_Cliente'),
    url(r'^Productos_Alta/$', 'principal.views.Productos_Alta'),
    url(r'^Productos_Baja/$', 'principal.views.Productos_Baja'),
    url(r'^Productos_Cambio/$', 'principal.views.Productos_Cambio'),
    url(r'^Pagos_Factura/$', 'principal.views.Pagos_Factura'),
    url(r'^Pagos_Clientes/$', 'principal.views.Pagos_Clientes'),
    url(r'^Agregar_Estado_Ciudad/$', 'principal.views.Agregar_Estado_Ciudad'),
    # Examples:
    # url(r'^$', 'sfcpc.views.home', name='home'),
    # url(r'^sfcpc/', include('sfcpc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
