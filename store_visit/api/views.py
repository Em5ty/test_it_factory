from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Store, Employee, Visit
from .serializers import StoreSerializer, VisitSerializer


class StoreList(generics.ListCreateAPIView):
    serializer_class = StoreSerializer

    def get_queryset(self):
        phone = self.request.query_params.get('phone')
        employee = get_object_or_404(Employee, phone_number=phone)
        return Store.objects.filter(employee=employee)


class VisitCreate(generics.CreateAPIView):
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()

    def perform_create(self, serializer):
        phone = self.request.data.get('phone')
        employee = Employee.objects.get(phone_number=phone).first()
        store_id = self.request.data.get('store')
        store = get_object_or_404(Store, id=store_id, employee=employee).first()
        serializer.save(employee=employee, store=store)
