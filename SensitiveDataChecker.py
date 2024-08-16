from github import Github
import re

""" This script checks each repository to determine if it is public and contains sensitive information.
"""


class SensitiveDataChecker:
    def __init__(self, token):
        self.github = Github(token)

    def check_public_repositories(self):
        for repo in self.github.get_user().get_repos():
            if not repo.private:
                print(f"Checking repository: {repo.name}")
                self.check_for_sensitive_data(repo)

    def check_for_sensitive_data(self, repo):
        try:
            contents = repo.get_contents("")
            for content in contents:
                if content.type == "file":
                    data = repo.get_contents(content.path).decoded_content.decode('utf-8')
                    if re.search('password|secret|apikey', data, re.IGNORECASE):
                        print(f"Sensitive data found in {repo.name}, setting to private.")
                        repo.edit(private=True)
        except Exception as e:
            print(f"Error checking repository {repo.name}: {e}")
