import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook 

wb = Workbook()  
sheet = wb.active  

driver=webdriver.Chrome()

url="https://findauction.in/"
driver.get(url)

        

place=driver.find_element(By.XPATH,"/html/body/section[1]/div/div/div/div/div/div[2]/div[1]/div[1]/input").send_keys("Delhi")
search=driver.find_element(By.XPATH,"/html/body/section[1]/div/div/div/div/div/div[2]/div[1]/div[3]/button").click()

new_url = driver.current_url
time.sleep(5)

print(new_url)
sheet['A1']=new_url
        

wb.save("Sample.xlsx")  



