from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Start a new instance of the Chrome browser
driver = webdriver.Chrome()

# Open the initial URL (the URL where you perform the login)
initial_url = "https://example.com/login"
driver.get(initial_url)

# Perform the login operations here
# ...

# Attempt to click the submit button that opens the new website
submit_button_xpath = "/html/body/section[2]/div/div/div[2]/div[2]/div/div/div/div/ul/li[3]"

try:
    submit_button = driver.find_element_by_xpath(submit_button_xpath)
    submit_button.click()

    # Capture the URL of the newly opened website
    new_url = driver.current_url
    print("Newly opened website URL:", new_url)

except NoSuchElementException:
    # Handle the case where the element is not found
    print("Element not found. Proceeding with an empty URL.")
    new_url = ""

# Continue with the rest of your program
# ...

# Close the browser
driver.quit()
