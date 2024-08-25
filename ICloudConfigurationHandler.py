from abc import ABC, abstractmethod

# Interface for Configuration Handlers
class ICloudConfigurationHandler(ABC):
    @abstractmethod
    def check(self):
        """Abstract method to check the configuration."""
        pass

    @abstractmethod
    def fix(self):
        """Abstract method to fix the configuration."""
        pass