from data_platform.base.base import BaseAccess


class ResourceGroup(BaseAccess):
    def __init__(self, name, params):
        self.name = name
        self.params = params
        super().__init__()

    def create_or_update(self):
        return self.resource_group_client.resource_groups.create_or_update(self.name, self.params)

    def get_rg(self):
        return self.resource_group_client.resource_groups.get(self.name)
