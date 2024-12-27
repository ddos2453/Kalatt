
import time
import requests
import base64

TOKEN = "7757765173:AAG-a07XG_iWY0Ee_R_zXTRyFBk6wMRBI8o"  # Ensure to keep your token secure
REPO_OWNER = "Adil Khan"
REPO_SLUG = "armam"
FILE_PATH = ".travis.yml"
BRANCH = "main"

BASE_URL = f"https://api.bitbucket.org/2.0/repositories/{REPO_OWNER}/{REPO_SLUG}"

HEADERS = {
    "Authorization": f"Basic {base64.b64encode((TOKEN + ':').encode()).decode()}"
}

def get_file_sha():
    """Get the SHA of the file to modify."""
    url = f"{BASE_URL}/src/{BRANCH}/{FILE_PATH}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()["commit"]

def get_file_content():
    """Fetch the content of the file."""
    url = f"{BASE_URL}/src/{BRANCH}/{FILE_PATH}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()["data"]

def update_file(new_content, sha):
    """Update the content of the file."""
    url = f"{BASE_URL}/src/{BRANCH}/{FILE_PATH}"  # Correct update URL
    data = {
        "message": "Add space to the end of file",
        "content": new_content,
        "branch": BRANCH,
        "sha": sha
    }
    response = requests.put(url, json=data, headers=HEADERS)
    response.raise_for_status()

def main():
    while True:
        try:
            sha = get_file_sha()
            current_content = get_file_content()

            # Trim and update the file
            updated_content = current_content.rstrip() + " "  # Add a single space

            # Update the file
            update_file(updated_content, sha)
            print("Successfully added a space to the file.")

        except requests.RequestException as e:
            print(f"Request error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        time.sleep(300)  # Sleep for 5 minutes (300 seconds), adjust as necessary

if __name__ == "__main__":  # Correct statement
    main()
