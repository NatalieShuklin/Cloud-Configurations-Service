# GitHub Required Config Provider
class GitHubRequiredConfigProvider:
    def get_required_security_configs(self):
        """Returns GitHub's required security configurations."""
        return {"BranchProtection": True, "branch_protection": True}