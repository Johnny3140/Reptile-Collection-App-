from django.urls import path
from .views import index, about, reptile_detail, reptile_index

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('reptiles/', reptile_index, name='reptile_index'),

    path('<int:reptile_id>/', reptile_detail, name='reptile_detail'),
]
