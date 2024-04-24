from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),

    path('api/v1/user_data/', views.User_data_view),
    path('api/v1/user_data/<str:id_user>/', views.User_data_view, name='user_data_detail'),
    path('api/v1/user_data/<str:id_user>/update/', views.update_user_data),
    path('api/v1/user_data/<str:id_user>/delete/', views.delete_user_data),

    path('api/v1/consommations/', views.create_consommation, name='create_consommation'),
    path('api/v1/consommations/<int:user_id>/', views.get_consommation_by_user, name='get_consommation_by_user'),
    path('api/v1/consommations/<int:user_id>/<int:consommation_id>/', views.get_consommation_by_id, name='get_consommation_by_id'),
    path('api/v1/consommations/<int:user_id>/<int:consommation_id>/update/', views.update_consommation, name='update_consommation'),
    path('api/v1/consommations/<int:user_id>/<int:consommation_id>/delete/', views.delete_consommation, name='delete_consommation'),
]
