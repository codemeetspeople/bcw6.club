from django.urls import path
from shop import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        'category/<int:object_id>/',
        views.CategoryView.as_view(),
        name='category'
    ),
    path(
        'item/<int:object_id>/',
        views.ItemView.as_view(),
        name='item'
    ),
]

app_name = 'shop'
