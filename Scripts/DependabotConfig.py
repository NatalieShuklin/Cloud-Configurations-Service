from github import Github

class DependabotConfiguration(Configuration):
    """Manages Dependabot alerts and security updates."""

    def __init__(self, repo):
        """Initializes with the repository object."""
        self.repo = repo

    def check(self):
        """Checks the current Dependabot settings and returns their status."""
        dependabot_alerts_enabled = self.repo.get_vulnerability_alert()
        dependabot_security_updates_enabled = self.repo.get_dependabot_security_updates_enabled()

        print("Dependabot Settings:")
        print(f"  - Alerts Enabled: {dependabot_alerts_enabled}")
        print(f"  - Security Updates Enabled: {dependabot_security_updates_enabled}")

        # Return the current status of both settings
        return dependabot_alerts_enabled, dependabot_security_updates_enabled

    def fix(self):
        """Fixes the Dependabot settings if necessary by calling check()."""
        dependabot_alerts_enabled, dependabot_security_updates_enabled = self.check()

        if not dependabot_alerts_enabled:
            self.repo.enable_vulnerability_alert()
            print("  - Dependabot alerts have been enabled.")

        if not dependabot_security_updates_enabled:
            self.repo.enable_dependabot_security_updates()
            print("  - Dependabot security updates have been enabled.")


# Example usage of the script
if __name__ == "__main__":
    # Replace with your GitHub token and repository details
    access_token = "your_github_access_token"
    repository_name = "your_username/your_repository"

    # Authenticate and get the repository object
    g = Github(access_token)
    repo = g.get_repo(repository_name)

    # Create a DependabotConfiguration object and run the checks/fixes
    dependabot_config = DependabotConfiguration(repo)

    # Explicitly call check() to see the current status of Dependabot settings
    dependabot_config.check()

    # Call fix() to apply any necessary fixes
    dependabot_config.fix()
