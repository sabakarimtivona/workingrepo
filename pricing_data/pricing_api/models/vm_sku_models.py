"""
the model class for vm sku details .
"""
from django.db import models
from .base_models import BaseModel
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class VmSku(BaseModel):
    vm_sku_name = models.CharField(max_length=100 , blank= True,null=True)
    vm_sku_details = models.JSONField(blank= True)
    family = models.CharField(max_length=200,blank= True,null=True)
    vCPUs = models.BigIntegerField(blank= True,null=True)
    MemoryGB = models.DecimalField(max_digits=30, decimal_places=2,blank= True,null=True)
    location = models.CharField(max_length=200,blank= True,null=True)
    MaxResourceVolumeMB = models.BigIntegerField(blank= True,null=True )
    OSVhdSizeMB=models.BigIntegerField(null= True , blank= True)
    MemoryPreservingMaintenanceSupported = models.BooleanField(default=False)
    HyperVGenerations =  models.CharField(max_length=200,blank= True)
    MaxDataDiskCount = models.BigIntegerField(null = True , blank= True, default=0)
    CpuArchitectureType = models.CharField(max_length=200,blank= True,null=True)
    LowPriorityCapable = models.BooleanField(blank= True,null=True)
    PremiumIO = models.BooleanField(blank= True,null=True)
    VMDeploymentTypes = models.CharField(max_length=200,blank= True,null=True)
    vCPUsAvailable = models.BigIntegerField( blank= True,null=True, default=0)
    ACUs =models.BigIntegerField( blank= True,null=True, default=0)
    vCPUsPerCore = models.BigIntegerField( blank= True,null=True, default=0)
    EphemeralOSDiskSupported = models.BooleanField(blank= True,null=True)
    EncryptionAtHostSupported = models.BooleanField(blank= True,null=True)
    CapacityReservationSupported = models.BooleanField(blank= True,null=True)
    AcceleratedNetworkingEnabled = models.BooleanField(blank= True,null=True)
    RdmaEnabled = models.BooleanField(blank= True,null=True)
    MaxNetworkInterfaces = models.BigIntegerField( blank= True,null=True, default=0)
    CombinedTempDiskAndCachedIOPS = models.BigIntegerField(blank= True,null=True, default=0)
    CombinedTempDiskAndCachedReadBytesPerSecond = models.BigIntegerField(blank= True,null=True, default=0)
    CombinedTempDiskAndCachedWriteBytesPerSecond = models.BigIntegerField(blank= True,null=True, default=0)
    UncachedDiskIOPS = models.BigIntegerField(blank= True,null=True, default=0)
    UncachedDiskBytesPerSecond = models.BigIntegerField(blank= True,null=True, default=0)
    CachedDiskBytes = models.BigIntegerField(blank= True,null=True, default=0)
    UltraSSDAvailable = models.BooleanField(blank= True,null=True)
    HibernationSupported = models.BooleanField(blank= True,null=True)
    TrustedLaunchDisabled = models.BooleanField(blank= True,null=True)
    ConfidentialComputingType = models.CharField(max_length=200,blank= True,null=True)
    ParentSize = models.CharField(max_length=200,blank= True,null=True)
    DiskControllerTypes = models.CharField(max_length=25,blank= True,null=True)
    NvmeDiskSizeInMiB = models.BigIntegerField(blank= True,null=True, default=0)
    MaxWriteAcceleratorDisksAllowed = models.BigIntegerField(blank= True,null=True, default=0)
    GPUs = models.BigIntegerField(blank= True,null=True, default=0)

class Pricing(BaseModel):
    currencyCode = models.CharField(max_length=100, blank=True, null=True)
    tierMinimumUnits = models.DecimalField(max_digits=30, decimal_places=2,)
    reservationTerm = models.CharField(max_length=100, blank=True, null=True)
    retailPrice = models.DecimalField(max_digits=30, decimal_places=2,)
    unitPrice = models.DecimalField(max_digits=30, decimal_places=2,)
    armRegionName = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    effectiveStartDate = models.CharField(max_length=100, blank=True, null=True)
    effectiveEndDate = models.CharField(max_length=100, blank=True, null=True)
    meterId = models.CharField(max_length=100, blank=True, null=True)
    meterName = models.CharField(max_length=100, blank=True, null=True)
    productId = models.CharField(max_length=100, blank=True, null=True)
    skuId = models.CharField(max_length=100, blank=True, null=True)
    productName = models.CharField(max_length=100, blank=True, null=True)
    skuName = models.CharField(max_length=100, blank=True, null=True)
    serviceName = models.CharField(max_length=100, blank=True, null=True)
    serviceId = models.CharField(max_length=100, blank=True, null=True)
    serviceFamily = models.CharField(max_length=100, blank=True, null=True)
    unitOfMeasure = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    isPrimaryMeterRegion = models.CharField(max_length=100, blank=True, default='')
    armSkuName = models.CharField(max_length=100, blank=True, null=True)
    savingsPlan = ArrayField(models.CharField(max_length=200, blank=True, null=True), blank=True, null=True)
    VmSku = models.ForeignKey(VmSku, on_delete=models.CASCADE, related_name= "pricing",null=True, blank=True)
    OperatingSystem = models.CharField(max_length=100, blank=True, default='')
    Meter = models.CharField(max_length=100, blank=True, default='')
    pricePerDay = models.DecimalField(max_digits=30, decimal_places=2,blank=True,null=True)
    pricePerMonth = models.DecimalField(max_digits=30, decimal_places=2,blank=True,null=True)
    pricePerYear = models.DecimalField(max_digits=30, decimal_places=2,blank=True,null=True)
    class Meta:
        indexes = [
                models.Index(fields=["skuId","type"]),
            ]

class Best_regional_price_models(BaseModel):
    sku = models.CharField(max_length=100)
    vm_tier = models.CharField(max_length=100)
    price_plan = models.CharField(max_length=100)
    best_price = models.CharField(max_length=100)
    best_price_region = models.CharField(max_length=100)
    effectivestartdate = models.DateTimeField(timezone.now)
