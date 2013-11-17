from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD
	url(r'^$','principal.views.v_index'),
	url(r'^Factura/$','principal.views.v_Factura'),
    url(r'^Clientes/$', 'principal.views.v_Clientes'),
    url(r'^Pagos/$', 'principal.views.v_Pagos'),
    url(r'^Productos/$', 'principal.views.v_Productos'),
    url(r'^Clientes_Alta/$', 'principal.views.v_Clientes_Alta'),
    url(r'^Clientes_Baja/$', 'principal.views.v_Clientes_Baja'),
    url(r'^Clientes_Cambio/(P<id_Cliente>\d+)$', 'principal.views.v_Clientes_Cambio'),
    url(r'^Seleccionar_Cliente/((P<Nombre_Cliente>\w+)?\+(P<RFC_Cliente>)?)?','principal.views.v_Seleccionar_Cliente'),
    url(r'^Productos_Alta/$', 'principal.views.v_Productos_Alta'),
    url(r'^Productos_Baja/$', 'principal.views.v_Productos_Baja'),
    url(r'^Productos_Cambio/$', 'principal.views.v_Productos_Cambio'),
    url(r'^Seleccionar_Producto/((P<Nombre_Cliente>\w+)?\+(P<RFC_Cliente>)?)?','principal.views.v_Seleccionar_Cliente'),
    url(r'^Pagos_Factura/$', 'principal.views.v_Pagos_Factura'),
    url(r'^Pagos_Clientes/$', 'principal.views.v_Pagos_Clientes'),
=======
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
<<<<<<< HEAD
>>>>>>> d4a64808a65e5145448c73c0cf6537602c1908ff
=======
>>>>>>> d4a64808a65e5145448c73c0cf6537602c1908ff
    # Examples:
    # url(r'^$', 'sfcpc.views.home', name='home'),
    # url(r'^sfcpc/', include('sfcpc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
