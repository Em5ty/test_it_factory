from django.urls import path
from . import views

urlpatterns = [
    path('stores/', views.StoreList.as_view(), name='store-list'),
    path('visit/', views.VisitCreate.as_view(), name='visit-create')
]
