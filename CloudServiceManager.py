

from CloudServiceFactory import CloudServiceFactory


# 1. CloudServiceManager - Calls the factory with a service name
class CloudServiceManager:
    def __init__(self):
        # Initialize the registry with predefined services
        self.service_registry = ["github", "aws", "azure"]

    def get_service(self, service_name: str, access_token: str):
        """Delegates service creation to the factory."""
        if service_name in self.service_registry:
            return CloudServiceFactory.create_service(service_name, access_token)
        else:
            raise ValueError(f"Service '{service_name}' is not registered.")


    def register_service(self, service_name: str):
        """Registers a new service by adding it to the registry."""
        service_name = service_name.lower()
        if service_name in self.service_registry:
            raise ValueError(f"Service '{service_name}' is already registered.")

        self.service_registry.append(service_name)


    def get_service_list(self):
        """Returns the list of available services."""
        return self.service_registry

