from data_platform.resource_group.base import BaseAccess
import logging


class Namespace(BaseAccess):
    def __init__(self, resource_group_name, name, params):
        super().__init__()
        self.resource_group_name = resource_group_name
        self.name = name
        self.params = params

    def create_or_update(self):
        if self.validate_account_name():
            poller = self.eventhub_client.namespaces.begin_create_or_update(self.resource_group_name, self.name, self.params)
            result = poller.result()
            return result.name

    def validate_account_name(self):
        availability_result = self.eventhub_client.namespaces.check_name_availability({"name": self.name})
        if not availability_result.name_available:
            logging.info(f"{self.name} is already in use")
            print(f"{self.name} is already in use")
            return False
        return True


class Blob(BaseAccess):
    def __init__(self, resource_group_name, account_name, blob_name):
        super().__init__()
        self.resource_group_name = resource_group_name
        self.account_name = account_name
        self.blob_name = blob_name

    def create_blob(self):
        container = self.storage_client.blob_containers.create(self.resource_group_name,
                                                               self.account_name,
                                                               self.blob_name,
                                                               {})

        print(f"Provisioned blob container {container.name}")


