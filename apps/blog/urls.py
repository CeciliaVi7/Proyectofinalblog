from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetConfirmView



urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),

    path('articulo/<slug:articulo_slug>/',
         views.ArticuloDetailView.as_view(), name='articulo'),

    path('categoria/<slug:categoria_slug>/',
         views.ArticulosByCategoriaView.as_view(), name='categoria'),

    path('autor/<str:autor>/', views.ArticulosByAutorView.as_view(), name='autor'),

    path('archivo/<int:year>/<int:month>',
         views.ArticulosByArchivoView.as_view(), name='archivo'),

    path('crear_articulo/', views.ArticuloCreateView.as_view(),
         name='crear_articulo'),

    path('actualizar_articulo/<slug:articulo_slug>',
         views.ArticuloUpdateView.as_view(), name='actualizar_articulo'),

    path('eliminar_articulo/<slug:articulo_slug>',
         views.ArticuloDeleteView.as_view(), name='eliminar_articulo'),

    path('signup/', views.SignUpView.as_view(), name='signup'),
    
    path('comments/', views.comment_section, name='comment_section'),

    #cerrar sesion
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),


]