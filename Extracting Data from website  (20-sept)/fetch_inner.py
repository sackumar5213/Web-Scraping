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
place="Ghaziabad"
last_record=3  #Enter number of Records
last_page=2    # Enternumber of pages

driver.find_element(By.ID,"location").send_keys(place)
driver.find_element(By.XPATH,"/html/body/section[1]/div/div/div/div/div/div[2]/div[1]/div[3]/button").click()
# time.sleep(5)

# Entering the headers in excel in top of the data
names = ["Sr. No.", "Bank", "Borrower","Type","Address","Area", "Locality", "City","Status", "Auction", "Auth Contact", "Links"]
sheet.append(names)

new_url = driver.current_url
gen_url=new_url+"/all/all/" #for storing next url with all 

empty_row=1
# Going into deeper details of property
for page in range(1,last_page+1):
    driver.get(gen_url+str(page))

    
    for i in range(2,last_record+2):  #each page contains 15 records. Hence 2 to 17
        print("i=  ",i-1)
        try:
            auction_date =driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/ul/li[1]").text
        except NoSuchElementException:
            auction_date="NA"
        try:
            area=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/ul/li[2]").text
        except NoSuchElementException:
            area="NA"
        try:
            status=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/ul/li[3]").text
        except NoSuchElementException:
            status="NA"

        # going inner for storing detailed data of property
        driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[2]/a").click()
        links=driver.current_url
        time.sleep(2)

        #storing data of property
        borrower=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl[1]/dd").text
        bank_name=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl[2]/dd/a").text
        property_type=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl[3]/dd").text
        location=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl[4]/dd").text

        for contact_loop in range(5,20):
            try:
                district=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop)+"]/dt").text
            except NoSuchElementException:
                district="NA"
            if(district=="Locality"):
                district=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop)+"]/dd").text
                break
        
        for contact_loop in range(5,20):
            try:
                town=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop)+"]/dt").text
            except NoSuchElementException:
                city="NA"
            if(town=="City"):
                city=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop)+"]/dd").text
                break

        # city=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop+1)+"]/dd").text


        for contact_loop in range(5,20):
            try:
                contact=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop)+"]/dt").text
            except NoSuchElementException:
                pass
            if(contact=="Contact Details for Support"):
                authorized_details=driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[4]/div[2]/dl["+str(contact_loop)+"]/dd").text
                break

        # data entry into sheet
        empty_row=empty_row+1
        sheet['A'+str(empty_row)]=empty_row-1
        sheet['B'+str(empty_row)]=bank_name
        sheet['C'+str(empty_row)]=borrower
        sheet['D'+str(empty_row)]=property_type
        sheet['E'+str(empty_row)]=location
        sheet['F'+str(empty_row)]=area   
        sheet['G'+str(empty_row)]=city
        sheet['H'+str(empty_row)]=district
        sheet['I'+str(empty_row)]= status
        sheet['J'+str(empty_row)]=auction_date 
        sheet['K'+str(empty_row)]=authorized_details
        sheet['L'+str(empty_row)]=links
        print("Empty row= ", empty_row)

        driver.back()
        ######################################
    # empty_row=empty_row+1


wb.save(place+"2__Sale_entry.xlsx")
time.sleep(2)

