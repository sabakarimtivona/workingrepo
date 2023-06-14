from rest_framework import serializers
from pricing_api.models.vm_sku_models import VmSku , Pricing
from pricing_api.models.vm_benchmark_models import Benchmark
# from rest_framework.response import Response

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = "__all__"
class BenchMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benchmark
        exclude = ['vmbenchRelation']

class VmSkuListSerializer(serializers.ModelSerializer) :
    pricing = PricingSerializer(many=True)
    Benchmark = BenchMarkSerializer(many=True)

    class Meta:
        model = VmSku
        fields = ["vm_sku_name","vm_sku_details","family","location","MaxResourceVolumeMB"
,"OSVhdSizeMB"
,"vCPUs"
,"MemoryPreservingMaintenanceSupported"
,"HyperVGenerations"
,"MemoryGB"
,"MaxDataDiskCount"
,"CpuArchitectureType"
,"LowPriorityCapable"
,"PremiumIO"
,"VMDeploymentTypes"
,"vCPUsAvailable"
,"ACUs"
,"vCPUsPerCore"
,"EphemeralOSDiskSupported"
,"EncryptionAtHostSupported"
,"CapacityReservationSupported"
,"AcceleratedNetworkingEnabled"
,"RdmaEnabled"
,"MaxNetworkInterfaces"
,"CombinedTempDiskAndCachedIOPS"
,"CombinedTempDiskAndCachedReadBytesPerSecond"
,"CombinedTempDiskAndCachedWriteBytesPerSecond"
,"UncachedDiskIOPS"
,"UncachedDiskBytesPerSecond"
,"CachedDiskBytes"
,"UltraSSDAvailable"
,"HibernationSupported"
,"TrustedLaunchDisabled"
,"ConfidentialComputingType"
,"ParentSize"
,"DiskControllerTypes"
,"NvmeDiskSizeInMiB"
,"MaxWriteAcceleratorDisksAllowed"
,"GPUs","pricePerDay","pricePerMonth","pricePerYear","pricing","Benchmark"]     

