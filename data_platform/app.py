from data_platform.resource_group.base import ResourceGroup
from data_platform.storage.base import Account, Blob
from data_platform.event_hub.base import Namespace

RESOURCE_GROUP_NAME = 'development-mark-test-rg'
rg_params = {
        "location": "eastus",
        "tags": { "environment":"test", "department":"tech"}
    }

ACCOUNT_NAME = 'developmentacc'
acc_params = {
  "location": 'eastus',
  "kind": "StorageV2",
  "sku": {"name": "Standard_LRS"}
}

BLOB_NAME = 'development-mark-blob'

rg = ResourceGroup(RESOURCE_GROUP_NAME, rg_params)
print(rg.create_or_update())


# a = Account(RESOURCE_GROUP_NAME, ACCOUNT_NAME, acc_params)
# print(a.create_storage_account())
#
# b = Blob(RESOURCE_GROUP_NAME, ACCOUNT_NAME, BLOB_NAME)
# print(b.create_blob())

n = Namespace(
        RESOURCE_GROUP_NAME,
        'developmentehmarktestppp',
        {
            'location': 'eastus',
            'sku': {'name': 'basic'},
            'maximum-throughput-units': '1'
        })
print(n.create_or_update())