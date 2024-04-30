from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),

    path('api/v1/user_data/me/', views.User_data_view, name='user_data_detail'),
    path('api/v1/user_data/update/me/', views.update_user_data),

    path('api/v1/consommations/', views.create_consommation, name='create_consommation'),
    path('api/v1/consommations/consult/me/', views.get_consommation_by_user, name='get_consommation_by_user'),
    path('api/v1/consommations/consult/<int:consommation_id>/', views.get_consommation_by_id, name='get_consommation_by_id'),
    path('api/v1/consommations/update/me/<int:consommation_id>/', views.update_consommation, name='update_consommation'),
    path('api/v1/consommations/delete/me/<int:consommation_id>/', views.delete_consommation, name='delete_consommation'),

    path('api/v1/consommations/search/', views.recherche_de_conso, name='search_consommation'),
    path('api/v1/consommations/calculate/', views.calculateur_de_conso, name='calculateur_de_conso'),

    path('api/v1/consommations/calculate/<str:type_calcul>/<str:choix>/<path:quantite>/', views.calculateur_de_conso),
    path('api/v1/consommations/search/<str:categorie>/', views.recherche_de_conso),
    path('api/v1/consommations/search/<str:categorie>/<str:sous_categorie>/', views.recherche_de_conso),
    path('api/v1/consommations/search/<str:categorie>/<str:sous_categorie>/<str:terme_recherche>/', views.recherche_de_conso),
 
]
