from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('Agregar_Producto_Proteccion/', views.Agregar_Producto_Proteccion, name='Agregar_Producto_Proteccion'),
    path('Agregar_Producto_Almacen/', views.Agregar_Producto_Almacen, name='Agregar_Producto_Almacen'),
    
    
    path('', views.productos_Almacen, name='productos_Almacen'),
    path('productos_Proteccion/', views.productos_Proteccion, name='productos_Proteccion'),
    
    path('buscar-producto-p/', views.buscar_producto_proteccion, name='buscar_producto_proteccion'),
    path('buscar-producto-a/', views.buscar_producto_almacen, name='buscar_producto_almacen'),

    path('editar-producto-p/<int:producto_id>/editar/', views.editar_producto_Proteccion, name='editar_producto_Proteccion'),
    path('editar-producto-a/<int:producto_id>/editar/', views.editar_producto_almacen, name='editar_producto_almacen'),

    path('retirar_producto_proteccion/<int:producto_id>/', views.retirar_producto_proteccion, name='retirar_producto_proteccion'),
    path('retirar_producto_almacen/<int:producto_id>/', views.retirar_producto_almacen, name='retirar_producto_almacen'),
    
    path('retiros/', views.retiros, name='retiros'),

    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('eliminar_Producto_almacen/<int:producto_id>/', views.eliminar_Producto_almacen, name='eliminar_Producto_almacen'),

]
    


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
