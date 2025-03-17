import agentql
from playwright.sync_api import sync_playwright

# Set the URL to the desired website
URL = "https://login.k12.com/"

LOGIN_QUERY = """
{
    username_field
    password_field
    submit_btn
}
"""

Gio_Weekly_View_Query = """
{
     week 
}   
"""

Scrape_Query = """
{
    monday[]{
        day
        class
        required
        time
    }
    mondayassignment[]{
        date
        class
        icon
    }
    tuesday[]{
        day
        class
        required
        time
    }
    tuesdayassignment[]{
        day(Tuesday)
        class
        icon
    }
    wednesday[]{
        class
        required
        time
    }
    wednesdayassignment[]{
        day
        class
        icon
    }
    thursday[]{
        class
        required
        time
    }
    thursdayassignment[]{
        day
        class
        icon
    }
    friday[]{
        class
        required
        time
    }
    fridayassignment[]{
        day
        class
        icon
    }
}


def main():
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:

        # Step 1 - Log in and access dashboard
        # Wrapped to access AgentQL's query API
        page = agentql.wrap(browser.new_page())

        # Navigate to the URL AND waitForPageReadyState
        page.goto("https://login.k12.com/")

        # Get the username and password fields
        response = page.query_elements(LOGIN_QUERY)

        # Fill the username and password fields
        response.username_field.fill("quinterodell")
        response.password_field.fill("jemwi6-covxur-Mukfiq")

        # Click the submit button
        response.submit_btn.click()

        # Used only for demo purposes. It allows you to see the effect of the script.
        page.wait_for_timeout(50000)

        # Step 2 - Change dashboard to weekly view, and identify scraping data on page load
        #


if __name__ == "__main__":
    main()