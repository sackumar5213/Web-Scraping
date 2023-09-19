import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  # for if element not found



driver=webdriver.Chrome()

sachin=""
print("Sachin",sachin)


def find_contact_details(contact_url):
    for contact_loop in range(5,20):
        print("loop=",contact_loop)
        try:
            contact=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop)+"]/dt").text
        except NoSuchElementException:
            contact=""
            pass
        print("contact=",contact)
        if(contact=="Contact Details for Support"):
            contact_details=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop)+"]/dd").text
            return contact_details

            
