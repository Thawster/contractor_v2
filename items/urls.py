from django.urls import path, include
from items.views import PageListView, PageDetailView, PageCreateView


urlpatterns = [
    path('', PageListView.as_view(), name='item-list-page'),path('create/', 
    PageCreateView.as_view(), name='item-create-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='item-details-page'),
    
]
