from github import Github

class BranchProtectionRiskDemo:
    """Demonstrates the risks of misconfiguring branch protection."""

    def __init__(self, branch):
        self.branch = branch

    def demonstrate_risk(self):
        """Demonstrates the risks if branch protection settings are misconfigured."""
        protection = self.branch.get_protection()

        pr_reviews_required = protection.required_pull_request_reviews is not None
        status_checks_required = protection.required_status_checks is not None
        push_restrictions = protection.restrictions is not None

        print("\nBranch Protection Risk Demonstration:")
        if not pr_reviews_required:
            print("[RISK] Without pull request reviews, unreviewed code can be merged, introducing vulnerabilities.")
        else:
            print("[SAFE] Pull request reviews are required, reducing the risk of unreviewed code being merged.")

        if not status_checks_required:
            print("[RISK] Without status checks, broken or untested code could be merged into the protected branch.")
        else:
            print("[SAFE] Status checks are required, ensuring only tested code is merged.")

        if not push_restrictions:
            print("[RISK] Without push restrictions, any contributor can push directly to the branch, bypassing reviews.")
        else:
            print("[SAFE] Push restrictions are in place, ensuring only authorized users can push directly to the branch.")


class DependabotRiskDemo:
    """Demonstrates the risks of misconfiguring Dependabot alerts and security updates."""

    def __init__(self, repo):
        self.repo = repo

    def demonstrate_risk(self):
        """Demonstrates the risks if Dependabot settings are misconfigured."""
        dependabot_alerts_enabled = self.repo.get_vulnerability_alert()
        dependabot_security_updates_enabled = self.repo.get_dependabot_security_updates_enabled()

        print("\nDependabot Risk Demonstration:")
        if not dependabot_alerts_enabled:
            print("[RISK] Without Dependabot alerts, vulnerabilities in dependencies may go unnoticed.")
        else:
            print("[SAFE] Dependabot alerts are enabled, so you will be notified of vulnerabilities.")

        if not dependabot_security_updates_enabled:
            print("[RISK] Without Dependabot security updates, known vulnerabilities in dependencies may remain unpatched.")
        else:
            print("[SAFE] Dependabot security updates are enabled, ensuring vulnerabilities are automatically patched.")


# Example usage of the script
if __name__ == "__main__":
    # Replace with your GitHub token and repository details
    access_token = "your_github_access_token"
    repository_name = "your_username/your_repository"
    branch_name = "main"

    # Authenticate and get the repository and branch objects
    g = Github(access_token)
    repo = g.get_repo(repository_name)
    branch = repo.get_branch(branch_name)

    # Create risk demonstration objects
    branch_protection_risk_demo = BranchProtectionRiskDemo(branch)
    dependabot_risk_demo = DependabotRiskDemo(repo)

    # Demonstrate risks for branch protection misconfiguration
    branch_protection_risk_demo.demonstrate_risk()

    # Demonstrate risks for Dependabot misconfiguration
    dependabot_risk_demo.demonstrate_risk()
