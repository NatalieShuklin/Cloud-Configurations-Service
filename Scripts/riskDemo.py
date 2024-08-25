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
