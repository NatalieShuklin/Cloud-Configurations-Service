from github import Github

"""
This script enforces branch protection rules on the main branches of all repositories.
"""


class BranchProtector:
    def __init__(self, token):
        self.github = Github(token)

    def enforce_branch_protections(self):
        for repo in self.github.get_user().get_repos():
            try:
                branch = repo.get_branch("main")
                branch.edit_protection(
                    enforce_admins=True,
                    required_approving_review_count=1,
                    strict=True,
                    contexts=["build-passed"]
                )
                print(f"Branch protection enforced on {repo.name}")
            except Exception as e:
                print(f"Error enforcing branch protection on {repo.name}: {e}")

    def set_repositories_public(self):
        # Get all repositories for the authenticated user
        for repo in self.github.get_user().get_repos():
            if repo.private:  # Check if the repository is private
                print(f"Setting repository {repo.name} to public...")
                repo.edit(private=False)  # Set the repository to public
                print(f"Repository {repo.name} is now public.")
