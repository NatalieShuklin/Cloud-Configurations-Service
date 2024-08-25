#  ServiceFactory - Decides which service to create based on the input string
from GitHubConfigurationHandler import GitHubConfigurationHandler


class CloudServiceFactory:
    def create_service(self, service_name: str, access_token: str):
        """Creates and returns the appropriate service configuration handler based on the service name."""
        service_name = service_name.lower()

        if service_name == "github":
            return GitHubConfigurationHandler(access_token)
        elif service_name == "aws":
            return AWSConfigurationHandler(access_token)
        elif service_name == "azure":
            return AzureConfigurationHandler(access_token)
        else:
            raise ValueError(f"Service '{service_name}' is not supported.")