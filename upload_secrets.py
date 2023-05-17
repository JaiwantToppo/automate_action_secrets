import os
from dotenv import load_dotenv
from github import Github
from config import repository_url, secrets

# Load environment variables from .env file
load_dotenv()

def upload_secrets(repository_url, secrets):
    # Create a PyGithub instance using the developer token
    g = Github(os.environ.get("GITHUB_TOKEN"))

    # Get the repository using the URL
    repo = g.get_repo(repository_url)

    # Get the existing secrets in the repository
    existing_secrets = repo.get_secrets()

    # Upload or update each secret
    for secret_name, secret_value in secrets.items():
        if secret_name in existing_secrets:
            # Update the existing secret
            secret = repo.get_secret(secret_name)
            secret.update(secret_value)
            print(f"Updated secret: {secret_name}")
        else:
            # Create a new secret
            repo.create_secret(secret_name, secret_value)
            print(f"Uploaded secret: {secret_name}")

    print("Secrets uploaded and updated successfully.")



upload_secrets(repository_url, secrets)
