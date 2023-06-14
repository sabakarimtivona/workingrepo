import os
import requests
from pricing_api.models import VmSku

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.run()

    def run(self):
        def get_access_token():
            creds = {
                "grant_type": "client_credentials",
                'client_id': os.environ.get('CLIENT_ID'),
                'client_secret': os.environ.get('CLIENT_SECRET'),
                'scope' : 'https://management.azure.com/.default',
            }
            tenant = os.environ.get('TENANT')
            request_token_url: str = (
                    f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
            )
            print(requests.post(request_token_url, data=creds).json())
            access_token = requests.post(request_token_url, data=creds).json()['access_token']
            return access_token
        access_token = get_access_token()    

        def get_vm_sku_data():
            header={'Authorization': 'Bearer ' + access_token}
            url = "https://management.azure.com/subscriptions/4f33ce2a-258b-4ff1-9caa-f3a2a45baf29/providers/Microsoft.Compute/skus?api-version=2021-07-01"
            response = requests.get(url, headers=header)
            return response

        vm_sku_json = get_vm_sku_data().json()
        vm_sku_list=[]

        def process_collected_data():
            for row in vm_sku_json['value']:
                if row["resourceType"] == "virtualMachines":
                    for location in row["locations"]:
                        processed_json_data = {
                            "vm_sku_name": row["name"],
                            "vm_sku_detail": {k:v  for k,v in row.items()},
                            "family" : row["family"],
                            "location" : location
                            }
                        for capabilities in row["capabilities"]:
                            if capabilities["name"]== "vCPUs":
                                processed_json_data["vCPUs"] = capabilities["value"]
                            if capabilities["name"]== "MemoryGB":
                                processed_json_data["MemoryGB"] = capabilities["value"]
                        vm_sku_list.append(processed_json_data)
            return vm_sku_list

        vm_sku_list = process_collected_data()

        def load_data_to_db():
            for data in vm_sku_list:
                model_object = VmSku(vm_sku_name=data['vm_sku_name'], vm_sku_details = data['vm_sku_detail'],
                                       family = data['family'],vCPUs = data['vCPUs'],MemoryGB = data['MemoryGB'],
                                       location = data['location'])
                model_object.save()
        load_data_to_db()