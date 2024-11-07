from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home2, name='home2'),
    path('add_product/',views.add_product,name="add_product"),
    path('edit_product/<int:product_id>/',views.edit_product,name="edit_product"),
    path('delete_product/<int:product_id>/',views.delete_product,name="delete_product"),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('signout/', views.signout, name='signout'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
