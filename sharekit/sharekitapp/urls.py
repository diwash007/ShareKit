from django.urls import path
from .views import ShareListView, ShareDetailView, ShareAddView, ShareUpdateView, ShareDeleteView
from . import views


urlpatterns = [
    path('home/', ShareListView.as_view(), name="home"),
    path('share/<int:pk>/', ShareDetailView.as_view(), name="share-detail"),
    path('share/add/', ShareAddView.as_view(), name="add-share"),
    path('share/update/<int:pk>', ShareUpdateView.as_view(), name="update-share"),
    path('delete/<int:pk>/', ShareDeleteView.as_view(), name="delete-share")
]