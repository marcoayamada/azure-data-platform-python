from data_platform.resource_group.base import BaseAccess
import logging


class Account(BaseAccess):
    def __init__(self, resource_group_name, name, params):
        super().__init__()
        self.resource_group_name = resource_group_name
        self.name = name
        self.params = params

    def create_storage_account(self):
        if self.validate_account_name():
            poller = self.storage_client.storage_accounts.begin_create(self.resource_group_name, self.name, self.params)
            print(f'Creating account {self.name}....')
            logging.info(f'Creating account {self.name}....')
            account_result = poller.result()
            return account_result.name

    def validate_account_name(self):
        availability_result = self.storage_client.storage_accounts.check_name_availability({"name": self.name})
        if not availability_result.name_available:
            logging.info(f"Storage account name {self.name} is already in use")
            print(f"Storage account name {self.name} is already in use")
            return False
        return True

    def get_account(self):
        return self.storage_client.storage_accounts.get_properties(self.resource_group_name, self.name)


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
