import time
import requests
import threading
from pricing_api.models.vm_sku_models import VmSku , Pricing
from django.core.management.base import BaseCommand
from pricing_api.data_collection.vm_sku_details import vm_sku_list
import pandas
import datetime , logging
import logging
from requests.adapters import HTTPAdapter, Retry

logger = logging.getLogger('django')


class Command(BaseCommand):
    help = "extracts the vmsku data from api , process it and loads it in the databse"

    def handle(self, *args, **options):
        self.load_vm_size_data(vm_sku_list)
        self.load_vm_price()
        # self.load_best_regional_price()

    def load_vm_size_data(self, vm_sku_list):
        location_sku_objects = []
        vm_sku_creation_objlist = []
        vm_sku_updation_objlist = []
        start = time.time()
        logger.info("object instance creation for vmsku started at " +str(datetime.datetime.now())+' hours!')
       
        queryset = VmSku.objects.all().values("vm_sku_name","location")
        for loaction_sku_pair in queryset:
            location_sku_objects.append((loaction_sku_pair['vm_sku_name'], loaction_sku_pair['location']))
        for vm_sku in vm_sku_list:
            location = vm_sku["location"]
            vm_sku_name = vm_sku["vm_sku_name"]

            if (vm_sku_name, location) in location_sku_objects:
                vm_sku_updation_objlist.append(VmSku(
                            vm_sku_name=vm_sku["vm_sku_name"],
                            vm_sku_details=vm_sku["vm_sku_detail"],
                            family=vm_sku["family"],
                            vCPUs=vm_sku.get("vCPUs"),
                            MemoryGB=vm_sku.get("MemoryGB"),
                            location=vm_sku["location"],
                            MaxResourceVolumeMB =vm_sku.get("MaxResourceVolumeMB"),
                            OSVhdSizeMB=vm_sku.get("OSVhdSizeMB"),
                            MemoryPreservingMaintenanceSupported=vm_sku.get("MemoryPreservingMaintenanceSupported"),
                            HyperVGenerations=vm_sku.get("HyperVGenerations"),
                            MaxDataDiskCount=vm_sku.get("MaxDataDiskCount"),
                            CpuArchitectureType=vm_sku.get("CpuArchitectureType"),
                            LowPriorityCapable=vm_sku.get("LowPriorityCapable"),
                            PremiumIO=vm_sku.get("PremiumIO"),
                            VMDeploymentTypes=vm_sku.get("VMDeploymentTypes"),
                            vCPUsAvailable=vm_sku.get("vCPUsAvailable"),
                            ACUs=vm_sku.get("ACUs"),
                            vCPUsPerCore=vm_sku.get("vCPUsPerCore"),
                            EphemeralOSDiskSupported=vm_sku.get("EphemeralOSDiskSupported"),
                            EncryptionAtHostSupported=vm_sku.get("EncryptionAtHostSupported"),
                            CapacityReservationSupported=vm_sku.get("CapacityReservationSupported"),
                            AcceleratedNetworkingEnabled=vm_sku.get("AcceleratedNetworkingEnabled"),
                            RdmaEnabled=vm_sku.get("RdmaEnabled"),
                            MaxNetworkInterfaces=vm_sku.get("MaxNetworkInterfaces"),
                            CombinedTempDiskAndCachedIOPS=vm_sku.get("CombinedTempDiskAndCachedIOPS"),
                            CombinedTempDiskAndCachedReadBytesPerSecond=vm_sku.get("CombinedTempDiskAndCachedReadBytesPerSecond"),
                            CombinedTempDiskAndCachedWriteBytesPerSecond=vm_sku.get("CombinedTempDiskAndCachedWriteBytesPerSecond"),
                            UncachedDiskIOPS=vm_sku.get("UncachedDiskIOPS"),
                            UncachedDiskBytesPerSecond=vm_sku.get("UncachedDiskBytesPerSecond"),
                            CachedDiskBytes=vm_sku.get("CachedDiskBytes"),
                            UltraSSDAvailable=vm_sku.get("UltraSSDAvailable"),
                            HibernationSupported=vm_sku.get("HibernationSupported"),
                            TrustedLaunchDisabled=vm_sku.get("TrustedLaunchDisabled"),
                            ConfidentialComputingType=vm_sku.get("ConfidentialComputingType"),
                            ParentSize=vm_sku.get("ParentSize"),
                            DiskControllerTypes=vm_sku.get("DiskControllerTypes"),
                            NvmeDiskSizeInMiB=vm_sku.get("NvmeDiskSizeInMiB"),
                            MaxWriteAcceleratorDisksAllowed=vm_sku.get("MaxWriteAcceleratorDisksAllowed"),
                            GPUs=vm_sku.get("GPUs")))
            else:
                vm_sku_creation_objlist.append(VmSku(vm_sku_name=vm_sku["vm_sku_name"],
                                                        vm_sku_details=vm_sku["vm_sku_detail"],
                                                        family=vm_sku["family"],
                                                        vCPUs=vm_sku.get("vCPUs"),
                                                        MemoryGB=vm_sku.get("MemoryGB"),
                                                        location=vm_sku["location"],
                                                        MaxResourceVolumeMB =vm_sku.get("MaxResourceVolumeMB"),
                                                        OSVhdSizeMB=vm_sku.get("OSVhdSizeMB"),
                                                        MemoryPreservingMaintenanceSupported=vm_sku.get("MemoryPreservingMaintenanceSupported"),
                                                        HyperVGenerations=vm_sku.get("HyperVGenerations"),
                                                        MaxDataDiskCount=vm_sku.get("MaxDataDiskCount"),
                                                        CpuArchitectureType=vm_sku.get("CpuArchitectureType"),
                                                        LowPriorityCapable=vm_sku.get("LowPriorityCapable"),
                                                        PremiumIO=vm_sku.get("PremiumIO"),
                                                        VMDeploymentTypes=vm_sku.get("VMDeploymentTypes"),
                                                        vCPUsAvailable=vm_sku.get("vCPUsAvailable"),
                                                        ACUs=vm_sku.get("ACUs"),
                                                        vCPUsPerCore=vm_sku.get("vCPUsPerCore"),
                                                        EphemeralOSDiskSupported=vm_sku.get("EphemeralOSDiskSupported"),
                                                        EncryptionAtHostSupported=vm_sku.get("EncryptionAtHostSupported"),
                                                        CapacityReservationSupported=vm_sku.get("CapacityReservationSupported"),
                                                        AcceleratedNetworkingEnabled=vm_sku.get("AcceleratedNetworkingEnabled"),
                                                        RdmaEnabled=vm_sku.get("RdmaEnabled"),
                                                        MaxNetworkInterfaces=vm_sku.get("MaxNetworkInterfaces"),
                                                        CombinedTempDiskAndCachedIOPS=vm_sku.get("CombinedTempDiskAndCachedIOPS"),
                                                        CombinedTempDiskAndCachedReadBytesPerSecond=vm_sku.get("CombinedTempDiskAndCachedReadBytesPerSecond"),
                                                        CombinedTempDiskAndCachedWriteBytesPerSecond=vm_sku.get("CombinedTempDiskAndCachedWriteBytesPerSecond"),
                                                        UncachedDiskIOPS=vm_sku.get("UncachedDiskIOPS"),
                                                        UncachedDiskBytesPerSecond=vm_sku.get("UncachedDiskBytesPerSecond"),
                                                        CachedDiskBytes=vm_sku.get("CachedDiskBytes"),
                                                        UltraSSDAvailable=vm_sku.get("UltraSSDAvailable"),
                                                        HibernationSupported=vm_sku.get("HibernationSupported"),
                                                        TrustedLaunchDisabled=vm_sku.get("TrustedLaunchDisabled"),
                                                        ConfidentialComputingType=vm_sku.get("ConfidentialComputingType"),
                                                        ParentSize=vm_sku.get("ParentSize"),
                                                        DiskControllerTypes=vm_sku.get("DiskControllerTypes"),
                                                        NvmeDiskSizeInMiB=vm_sku.get("NvmeDiskSizeInMiB"),
                                                        MaxWriteAcceleratorDisksAllowed=vm_sku.get("MaxWriteAcceleratorDisksAllowed"),
                                                        GPUs=vm_sku.get("GPUs")))
        logger.info("object creation done , going to bulk update and create " +
                    str(datetime.datetime.now())+' hours!')
        feilds = ["MaxResourceVolumeMB","OSVhdSizeMB"
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
                    ,"GPUs"]
        VmSku.objects.bulk_update(vm_sku_updation_objlist,feilds,batch_size=100)
        logger.info("bulk updation finished  and creation going to start" +
                    str(datetime.datetime.now())+' hours!')
        VmSku.objects.bulk_create(vm_sku_creation_objlist,batch_size = 100)
        end = time.time()
        elapsed_time = (end-start)
        logger.info("Execution time "+str(elapsed_time)+" seconds") 
        
        
        logger.info("finished loading sku objects with the values at " +
                    str(datetime.datetime.now())+' hours!')

    def load_vm_price(self):
        """
        # Load the vm price data into the Postgres
        """
        start2 = time.time()
        obj_create = []
        obj_update = []
        sku_type_objects = []
        all_data = []
        query_set = Pricing.objects.all().values("skuId","type")

        for sku_type_pair in query_set:
            sku_type_objects.append((sku_type_pair["skuId"],sku_type_pair["type"]))

        def fetch_vm_prices(lower_bound, upper_bound=None):
            url = f"https://prices.azure.com/api/retail/prices?api-version=2023-01-01-preview&$filter=serviceName eq 'Virtual Machines'&$skip={lower_bound}" 
            flag = True
            session = requests.Session()
            logger.info("pricing object data collection create or update started "+str(datetime.datetime.now())+' hours!')
            while(url and flag):
                print(url)
                try:
                    session.timeout = 60
                    retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[ 500, 502, 503, 504 ])
                    adapter = HTTPAdapter(max_retries=retries)
                    session.mount('http://', adapter)
                    session.mount('https://', adapter)
                    response = session.get(url)
                    json_data = response.json()
                except Exception as e:
                    logger.info(f"Error occurs when fetching URL: {e} "+str(datetime.datetime.now())+' hours!')
                for row in json_data['Items']:
                    try:
                        if row["serviceName"] == "Virtual Machines":
                        
                            savings_plan = row["savingsPlan"] if 'savingsPlan' in row else None  
                            skuId = row["skuId"]
                            type = row["type"]
                            priceperday = row["unitPrice"] * 24
                            pricepermonth = priceperday * 30
                            priceperyear = pricepermonth * 12
                            os_type = "Windows" if "Windows" in row.get("productName") else "Linux"

                            if "Spot" in row.get("meterName"):
                                vm_tier = "Spot"
                            elif "Low Priority" in row.get("meterName"):
                                vm_tier = "Low Priority"
                            else:
                                vm_tier = "Standard"

                            if (skuId,type) in sku_type_objects:
                            
                               obj_update.append(Pricing(pricePerDay = priceperday,pricePerMonth = pricepermonth,pricePerYear = priceperyear,VmSku=VmSku.objects.get(location__iexact=row["armRegionName"], vm_sku_name__iexact=row["armSkuName"]),currencyCode=row["currencyCode"],tierMinimumUnits=row["tierMinimumUnits"],reservationTerm=row.get("reservationTerm"),retailPrice=row["retailPrice"],unitPrice=row["unitPrice"],armRegionName=row["armRegionName"],location=row["location"],effectiveStartDate=row["effectiveStartDate"], effectiveEndDate=row.get("effectiveEndDate"), meterId=row["meterId"],meterName=row["meterName"],productId=row["productId"],skuId=row["skuId"],productName=row["productName"],skuName=row["skuName"],serviceName=row["serviceName"], serviceId=row["serviceId"],serviceFamily=row["serviceFamily"],unitOfMeasure=row["unitOfMeasure"],type=row["type"],isPrimaryMeterRegion=row["isPrimaryMeterRegion"],armSkuName=row["armSkuName"],savingsPlan=savings_plan,OperatingSystem=os_type, Meter=vm_tier))

                            else:
                            
                                obj_create.append(Pricing(currencyCode=row["currencyCode"],tierMinimumUnits=row["tierMinimumUnits"],reservationTerm=row.get("reservationTerm"),retailPrice=row["retailPrice"],unitPrice=row["unitPrice"],armRegionName=row["armRegionName"],location=row["location"],effectiveStartDate=row["effectiveStartDate"], effectiveEndDate=row.get("effectiveEndDate"), meterId=row["meterId"],meterName=row["meterName"],productId=row["productId"],skuId=row["skuId"],productName=row["productName"],skuName=row["skuName"],serviceName=row["serviceName"], serviceId=row["serviceId"],serviceFamily=row["serviceFamily"],unitOfMeasure=row["unitOfMeasure"],type=row["type"],isPrimaryMeterRegion=row["isPrimaryMeterRegion"],armSkuName=row["armSkuName"],savingsPlan=savings_plan,pricePerDay = priceperday,pricePerMonth = pricepermonth,pricePerYear = priceperyear,VmSku=VmSku.objects.get(location__iexact=row["armRegionName"],vm_sku_name__iexact=row["armSkuName"]),OperatingSystem=os_type, Meter=vm_tier))
                    except:
                            reason = "mismatched_sku_detail"
                            all_data.append({"armSkuName": row["armSkuName"], "armRegionName": row["armRegionName"], "currencyCode": row["currencyCode"], "tierMinimumUnits": row["tierMinimumUnits"], "retailPrice": row["retailPrice"], "unitPrice": row["unitPrice"], "location": row["location"], "effectiveStartDate": row["effectiveStartDate"], "meterId": row["meterId"], "meterName": row["meterName"], "productId": row[
                                            "productId"], "skuId": row["skuId"],"productName": row["productName"], "skuName": row["skuName"], "serviceName": row["serviceName"], "serviceId": row["serviceId"], "serviceFamily": row["serviceFamily"], "unitOfMeasure": row["unitOfMeasure"], "type": row["type"], "isPrimaryMeterRegion": row["isPrimaryMeterRegion"], "mismatched_reason": reason})
                url = json_data['NextPageLink']
                lower_bound += 100

                if upper_bound:
                    if lower_bound > upper_bound:
                        flag = False
                else: 
                    flag = True
            logger.info("pricing object data collection completed "+str(datetime.datetime.now())+' hours!')

        def execute_thread():
            incremental_value = 8000
            lower_bound = 0
            upper_bound = incremental_value

            thread_count = 40
            thread_objects = []
            for count in range(thread_count):
                if count == thread_count-1:
                    a = threading.Thread(target=fetch_vm_prices, args=(lower_bound,))
                else:    
                    a = threading.Thread(target=fetch_vm_prices, args=(lower_bound, upper_bound,))
                lower_bound, upper_bound = upper_bound+100, upper_bound+incremental_value
                a.start()
                thread_objects.append(a)

            for thread in thread_objects:
                thread.join()
            logger.info("thread finished ")
            if obj_create:
                logger.info("bulk creations started ")
                batch_size = 1000
                count = 0
                total_rows = len(obj_create)  
                for i in range(0, total_rows, batch_size):
                    batch = obj_create[i:i+batch_size]
                    Pricing.objects.bulk_create(batch)
                    count=count+1
                    logger.info("bulk creation batch no "+str(count))
                # Pricing.objects.bulk_create(obj_create)
            

            if obj_update:
                logger.info("bulk updation started ")
                batch_size = 1000
                total_rows = len(obj_update)
                count = 0
                logger.info("updates before feilds  ")
                fields = ["currencyCode","tierMinimumUnits","reservationTerm","retailPrice","unitPrice","armRegionName","location","effectiveStartDate","effectiveEndDate","meterId","meterName","productId","skuId","productName","skuName","serviceName", "serviceId","serviceFamily","unitOfMeasure","type","isPrimaryMeterRegion","armSkuName","savingsPlan"]  
                for i in range(0, total_rows, batch_size):
                    batch = obj_update[i:i+batch_size]
                    Pricing.objects.bulk_update(batch, fields=fields)
                    count=count+1
                    logger.info("bulk update batch no "+str(count))


        execute_thread()
        time_string = time.strftime("%Y %m %d - %H %M ")
        file_name = f"mismatched_dataset_details_{time_string}.csv"
        df = pandas.DataFrame(all_data)
        df.to_csv(path_or_buf=file_name, mode="w")
        end = time.time()

        elapsed_time=(end-start2)
        logger.info("Execution time "+str(elapsed_time)+" seconds")
        print("Data migration completed")
        
    def load_best_regional_price(self):
        best_price_objs = dict()
        logger.info("best regional pricing data collection started " +str(datetime.datetime.now())+' hours!')
        best_price, best_price_region = '', ''
        for row in Pricing.objects.all().values():

            key = row["armSkuName"]
            if key in best_price_objs:
                if best_price_objs[key]['best_price'] > row["unitPrice"]:
                    best_price_objs[key]['best_price'] = row['unitPrice']
                    best_price_objs[key]['best_price_region'] = row['location']
                    
                    best_price_objs[key]['data'].append({'skuId' : row['skuId'],'type':row['type']})
                else:
                    best_price_objs[key]['data'].append({'skuId' : row['skuId'],'type':row['type']})
            else:
                best_price_objs[key] = {'best_price': row['unitPrice'],
                                        'best_price_region': row['location'],
                                        'data': [{'skuId' : row['skuId'],'type':row['type']}]}
            
        for sku in best_price_objs:
            best_price, best_price_region = best_price_objs[sku]['best_price'], best_price_objs[sku]['best_price_region']
            for row in best_price_objs[sku]['data']:
                Pricing.objects.filter(skuId=row['skuId'],type=row['type']).update(best_price=best_price,best_price_region=best_price_region)
        logger.info("best regional pricing data collection completed " +str(datetime.datetime.now())+' hours!')
