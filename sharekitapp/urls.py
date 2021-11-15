from django.urls import path
from .views import (
    ShareListView, ShareAddView, ShareUpdateView, ShareDeleteView,
    DematListView, DematAddView, DematUpdateView, DematDeleteView)
from . import views


urlpatterns = [
    path('home/', ShareListView.as_view(), name="home"),
    path('share/add/', ShareAddView.as_view(), name="add-share"),
    path('share/update/<int:pk>', ShareUpdateView.as_view(), name="update-share"),
    path('share/delete/<int:pk>/', ShareDeleteView.as_view(), name="delete-share"),
    # path('share/<int:pk>/', ShareDetailView.as_view(), name="share-detail"),

    path('ipo/', DematListView.as_view(), name="ipo"),
    path('demat/add', DematAddView.as_view(), name="add-demat"),
    path('demat/update/<int:pk>', DematUpdateView.as_view(), name="update-demat"),
    path('demat/delete/<int:pk>/', DematDeleteView.as_view(), name="delete-demat"),

    path('ipo-result/', views.ipo_check, name="ipo-result")

]