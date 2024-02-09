from django.urls import path
from .views import index, about, reptile_detail, reptile_index, add_reptile , edit_reptile, delete_reptile

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('reptiles/', reptile_index, name='reptile_index'),
    path('<int:reptile_id>/', reptile_detail, name='reptile_detail'),
    path('reptiles/add/', add_reptile, name='add_reptile'),
    path('reptiles/<int:reptile_id>/edit/', edit_reptile, name='edit_reptile'),
    path('reptiles/<int:reptile_id>/delete/', delete_reptile, name='delete_reptile'), 


]

