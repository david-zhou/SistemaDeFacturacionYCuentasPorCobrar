from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','principal.views.v_index'),
	url(r'^Factura/(?P<id_Cliente>\d+)?\+?(?P<RFC_Cliente>\w+)?','principal.views.v_Factura'),
    url(r'^Clientes/$', 'principal.views.v_Clientes'),
    url(r'^Pagos/$', 'principal.views.v_Pagos'),
    url(r'^Productos/$', 'principal.views.v_Productos'),
    url(r'^Clientes_Alta/$', 'principal.views.v_Clientes_Alta'),
    url(r'^Clientes_Baja/(?P<id_Cliente>\d+)$', 'principal.views.v_Clientes_Baja'),
    url(r'^Clientes_Cambio/(?P<id_Cliente>\d+)$', 'principal.views.v_Clientes_Cambio'),
    url(r'^Seleccionar_Cliente/(?P<Nombre_Cliente>\w+)?\+?(?P<RFC_Cliente>\w+)?$','principal.views.v_Seleccionar_Cliente'),
    url(r'^Seleccionar_ClienteBaja/(?P<Nombre_Cliente>\w+)?\+?(?P<RFC_Cliente>\w+)?$','principal.views.v_Seleccionar_ClienteBaja'),
    url(r'^Productos_Alta/$', 'principal.views.v_Productos_Alta'),
    url(r'^Productos_Baja/(?P<id_Producto>\d+)$', 'principal.views.v_Productos_Baja'),
    url(r'^Productos_Cambio/(?P<id_Producto>\d+)$', 'principal.views.v_Productos_Cambio'),
    url(r'^Seleccionar_Producto/(?P<Nombre_Producto>\w+)?\+?(?P<Clave_Producto>\w+)?','principal.views.v_Seleccionar_Producto'),
    url(r'^Seleccionar_ProductoBaja/(?P<Nombre_Producto>\w+)?\+?(?P<Clave_Producto>\w+)?','principal.views.v_Seleccionar_ProductoBaja'),
    url(r'^Pagos_Factura/$', 'principal.views.v_Pagos_Factura'),
    url(r'^Pagos_Clientes/$', 'principal.views.v_Pagos_Clientes'),
    url(r'^Agregar_Estado_Ciudad/$', 'principal.views.v_Agregar_Estado_Ciudad'),
    url(r'^Seleccionar_ClienteFacturacion/(?P<Nombre_Cliente>\w+)?\+?(?P<RFC_Cliente>\w+)?$','principal.views.v_Seleccionar_ClienteFacturacion'),
    url(r'^Reportes/$', 'principal.views.v_Reportes'),
    url(r'^Reporte_Facturas/$', 'principal.views.v_Reporte_Facturas'),
    url(r'^Reporte_Estado/$', 'principal.views.v_Reporte_Estado'),
    url(r'^Generar_Factura/(?P<datos>[\w,]+)$', 'principal.views.v_Generar_Factura'),
    
# Examples:
    # url(r'^$', 'sfcpc.views.home', name='home'),
    # url(r'^sfcpc/', include('sfcpc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
