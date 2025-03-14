import os
import agentql
from playwright.sync_api import sync_playwright
from pyairtable import Api
from dotenv import load_dotenv


# Load-environment variables from .env-file
load_dotenv()

# Get username and password from environment variables
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
os.environ["AGENTQL_API_KEY"] = os.getenv("AGENTQL_API_KEY")

URL = "https://login.k12.com/"

LOGIN_QUERY ="""
{
    login_form {
        username_input
        password_input
        continue_btn
    }
}
"""

def main():
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:

        page = agentql.wrap_page(browser.new_page())

        # Navigate to the URL
        page.goto(URL)

        # Get the username and password fields
        response = page.query_elements(LOGIN_QUERY)

        # Fill the username and password fields
        response.username_field = ("USERNAME")
        response.password_field = ("PASSWORD")

        # Fill the submit button
        response.submit_btn()

        # Used only for demo purposes. It allows you to see the effects of the script
        page.wait_for_timeout(10000)


if __name__ == "__main__":
    main()