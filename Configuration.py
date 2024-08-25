class Configuration:
    def __init__(self, name: str):
        """Initializes the configuration with a name and an empty settings map."""
        self.name = name
        self.settings = {}

    def add_setting(self, setting_name: str, enabled: bool):
        """Adds a setting to the configuration with its enabled/disabled status."""
        self.settings[setting_name] = enabled