from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.eventhub import EventHubManagementClient
import os


class BaseAccess:

    def __init__(self):
        self.__credential = AzureCliCredential()
        self.__subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

        self.resource_group_client = self.get_resource_client(self.__credential, self.__subscription_id)
        self.storage_client = self.get_storage_client(self.__credential, self.__subscription_id)
        self.eventhub_client = self.get_eventhub_client(self.__credential, self.__subscription_id)

    def get_resource_client(self, credential, subscription_id):
        return ResourceManagementClient(credential, subscription_id)

    def get_storage_client(self, credential, subscription_id):
        return StorageManagementClient(credential, subscription_id)

    def get_eventhub_client(self, credential, subscription_id):
        return EventHubManagementClient(credential, subscription_id)