from azure.storage.blob import BlobServiceClient
import datetime
import os
from pathlib import Path
import glob

BASE_DIR = Path(__file__).resolve().parent.parent

connection_string   = "DefaultEndpointsProtocol=https;AccountName=pricingapilogs;AccountKey=Puh72OLmKhFEt/P/XWWf5/vIPkCMt/TC9aa8cVwtVyG7fs0tDoCcz3ossb4PugCqWzhWr2T9iMUg+AStLg9tEw==;EndpointSuffix=core.windows.net"

container_name      = "pricinglogs"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

log_files = glob.glob(os.path.join(BASE_DIR, "*.log"))

for log_file_path in log_files:
    blob_name = str(datetime.datetime.now())+" "+os.path.basename(log_file_path)
    with open(log_file_path, "rb") as data:
        blob_client = blob_service_client.get_blob_client(container_name, blob_name)
        blob_client.upload_blob(data)
