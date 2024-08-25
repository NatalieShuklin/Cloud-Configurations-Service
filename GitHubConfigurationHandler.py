# GitHub Configuration Handler
from GitHubChecker import GitHubChecker
from GitHubRemediator import GitHubRemediator
from GitHubRequiredConfigProvider import GitHubRequiredConfigProvider
from ICloudConfigurationHandler import ICloudConfigurationHandler


class GitHubConfigurationHandler(ICloudConfigurationHandler):
    def __init__(self, access_token):
        self.access_token = access_token
        self.github = github.connect(access_token)
        self.curr_config_list = self.github.get_curr_configurations_security
        # configuration {"config name" = true\false }

    def check_security_configs(self):
        """Checks GitHub security configurations."""
        print("Checking GitHub security configurations...")
        checker = GitHubChecker()
        expected_config_list = GitHubRequiredConfigProvider().get_required_security_configs()
        if checker.check_security_configs(self.curr_config_list, expected_config_list):
            print("GitHub configurations are correct.")
        else:
            print("GitHub configurations need fixing.")

    def check(self):
        self.check_security_configs()


    def fix_security_configs(self):
        """Fixes GitHub configurations."""
        print("Fixing GitHub configurations...")
        fixer = GitHubRemediator()
        fixer.fix_configs(self.curr_config_list)

    def fix(self):
        self.check_security_configs()