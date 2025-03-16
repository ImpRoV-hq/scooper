import dotenv from .env
import agentql
from playwright.sync_api import sync_playwright

# Load-environment variables from .env-file
import.env()

# Initialise the browser
def main()
    with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
    page = agentql.wrap(browser.new_page())
    page.goto("https://login.k12.com/")

    # Find "Username" , "Password" , "Search" button using Smart Locator
    search_button = page.get_by_prompt("username)
    search_button = page.get_by_prompt("password")
    search_button = page.get_by_prompt("LOG IN")

    # Populate fields

    response.username_field = USERNAME
    response.password_field = PASSWORD

    search_button.click()

    # Define a query for modal dialog's search input
    SEARCH_BOX_QUERY = """
    {
        modal {
            search_box
        }
    }
    """

    # Get the modal's search input and fill it with "Quick Start"
    response = page.query_elements(SEARCH_BOX_QUERY)
    response.modal.search_box.type("Quick Start")

    # Define a query for the search results
    SEARCH_RESULTS_QUERY = """
    {
        modal {
            search_box
            search_results {
                items[]
            }
        }
    }
    """

    # Execute the query after the results have returned then click on the first one
    response = page.query_elements(SEARCH_RESULTS_QUERY)
    response.modal.search_results.items[0].click()

    # Used only for demo purposes. It allows you to see the effect of the script.
    page.wait_for_timeout(10000)