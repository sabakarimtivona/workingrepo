from django.db.models import Q
from pricing_api.vm_sku_serializer import VmSkuListSerializer
from rest_framework import generics
from pricing_api.models.vm_sku_models import VmSku, Pricing
from pricing_api.models.vm_benchmark_models import Benchmark

import logging
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend


class VmSkuView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = (IsAuthenticated,) 
    queryset =  VmSku.objects.prefetch_related('Benchmark','pricing').distinct().all()
    serializer_class = VmSkuListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = filterset_fields = {
            "vm_sku_name" : ['exact'],
            "location" : ['exact'],
            "MemoryGB" : ['lte','gte'],
            "vCPUs" : ['lte',"gte"],
            "Benchmark__CPU": ['exact'],
            "pricing__pricePerDay" : ['lte','gte'],
            "CpuArchitectureType":['exact'], 
            "GPUs" : ['lte','gte'],
            "MaxDataDiskCount" : ['lte','gte'],
            "HyperVGenerations" : ['exact'],
            "Benchmark__NUMA_Nodes" : ['exact'],
            "MaxNetworkInterfaces" : ['lte','gte'],
            "RdmaEnabled" : ['exact'],
            "AcceleratedNetworkingEnabled" : ['exact'],
            "CombinedTempDiskAndCachedIOPS": ['lte','gte'],
            "CombinedTempDiskAndCachedReadBytesPerSecond": ['lte','gte'],
            "CombinedTempDiskAndCachedWriteBytesPerSecond":['lte','gte'],
            "UncachedDiskIOPS" : ['lte','gte'],
            "ACUs": ['lte','gte'],
            "Benchmark__Avg_Score" : ['lte','gte'],
            "PremiumIO" : ['exact']

        }
class VmSkuDetailView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = (IsAuthenticated,) 
    serializer_class = VmSkuListSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            VmSku_name = self.kwargs.get('sku')
            location = self.kwargs.get('location')
            if VmSku_name is not None:
                queryset = VmSku.objects.filter(vm_sku_name=VmSku_name, location = location)
            return queryset