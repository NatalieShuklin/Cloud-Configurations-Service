# GitHub Required Config Provider
class GitHubRequiredConfigProvider:

memebers:
maps of: - most_strict_security_configs
- configs_by_role
- less_strict_security_configs
    
    def get_required_security_configs(self):
        """Returns GitHub's required security configurations."""
        return most_strict_security_configs -> #{"BranchProtection": True, "branch_protection": True}
