# first install python    https://www.python.org/
# 2nd install selenium    pip install selenium
# 3rd install openpyxl    pip install openpyxl  

# and then run it

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook 
from selenium.common.exceptions import NoSuchElementException  # for if element not found


wb = Workbook()  
sheet = wb.active  

driver=webdriver.Chrome()

def Login():
    driver.find_element(By.XPATH,"/html/body/header/nav/div[2]/ul/li[2]/a").click()
    driver.find_element(By.XPATH,"/html/body/section[2]/div/div[1]/div[2]/form/div[1]/input").send_keys("ofc.prudent@gmail.com")
    driver.find_element(By.XPATH,"/html/body/section[2]/div/div[1]/div[2]/form/div[2]/input").send_keys("Rahul@100")
    driver.find_element(By.XPATH,"/html/body/section[2]/div/div[1]/div[2]/form/div[3]/button").click()
    # time.sleep(3)




url="https://findauction.in/"
driver.get(url)


# Log In
Login()
time.sleep(1)


# # Enter place
# driver.current_url
place="Ghaziabad"
driver.find_element(By.ID,"location").send_keys(place)
driver.find_element(By.XPATH,"/html/body/section[1]/div/div/div/div/div/div[2]/div[1]/div[3]/button").click()
# time.sleep(5)


# Going into deeper details of property
i=1
try:
    auction_date =driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/ul/li[1]").text
except NoSuchElementException:
    auction_date=""
try:
    area=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/ul/li[2]").text
except NoSuchElementException:
    area=""
try:
    status=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/ul/li[3]").text
except NoSuchElementException:
    status=""

driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/a").click()

#storing data of property
borrower=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl[1]/dd").text
bank_name=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl[2]/dd/a").text
property_type=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl[3]/dd").text
location=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl[4]/dd").text

for contact_loop in range(5,20):
    try:
        locality=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop)+"]/dt").text
    except NoSuchElementException:
        pass
    if(locality=="Locality"):
        district=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop)+"]/dd").text
        break

city=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop+1)+"]/dd").text


for contact_loop in range(5,20):
    try:
        contact=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop)+"]/dt").text
    except NoSuchElementException:
        pass
    if(contact=="Contact Details for Support"):
        authorized_details=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop)+"]/dd").text
        break

# driver.back()

# data entry into sheetsheet['A1']=borrower
sheet['A1']=borrower
sheet['B1']=bank_name
sheet['C1']=property_type
sheet['D1']=location
# sheet['E1']=status d  (ispe kaam karna hai status nhi enter ho raha hai excel mai)
# sheet['F1']=district
# sheet['G1']=city
# sheet['H1']=area d
# sheet['I1']=auction_date d
sheet['J1']=authorized_details

wb.save("Sale_entry.xlsx")


# driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div[3]/div/div/div/div/div[2]/a").click()
time.sleep(4)

