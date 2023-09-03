# companies/views.py
from rest_framework import viewsets, filters
from .models import Company
from .serializers import CompanySerializer
# companies/views.py
from django.shortcuts import render

def search_company(request):
    return render(request, 'search.html')

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
