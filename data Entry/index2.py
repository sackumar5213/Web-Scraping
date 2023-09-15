from selenium import webdriver

# Start a new instance of the Chrome browser
driver = webdriver.Chrome()

# Open the initial URL (the URL where you perform the login)
initial_url = "https://example.com/login"
driver.get(initial_url)

# Perform the login operations here
# ...

# Click the submit button that opens the new website
submit_button = driver.find_element_by_id("submit_button_id")
submit_button.click()

# Capture the URL of the newly opened website
new_url = driver.current_url

# Print the captured URL
print("Newly opened website URL:", new_url)

# Close the browser
driver.quit()
