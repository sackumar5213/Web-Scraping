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

# Price is in text, so make it in number
def text_to_number(text_with_commas):
    # Remove commas from the text
    text_without_commas = text_with_commas.replace(',', '')
    numeric_value = float(text_without_commas)
    return numeric_value

url="https://findauction.in/"
driver.get(url)
place=driver.find_element(By.XPATH,"/html/body/section[1]/div/div/div/div/div/div[2]/div[1]/div[1]/input").send_keys("Ghaziabad")
search=driver.find_element(By.XPATH,"/html/body/section[1]/div/div/div/div/div/div[2]/div[1]/div[3]/button").click()
new_url = driver.current_url
gen_url=new_url+"/all/all/"

print(new_url)
print(gen_url)
sachin="hello"
z=0
for y in range(1,10): 
    if(sachin==""):
        pass
    else:
        driver.get(gen_url+str(y))
        next_url=driver.current_url
        sheet['H'+str(z+1)]=next_url
        # time.sleep(3)
        
        for i in range(2,15):
            location_name=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[1]/h5/a").text
            bank_name  =driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[1]/h5/small").text
            price=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[1]/h6").text

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
                



            
            # print(bank_name)
            # print(auction_date)
            # print(area)
            # print(status)
            # print(price)

            z=z+1
            sheet['A'+str(z)]=bank_name
            sheet['B'+str(z)]=location_name
            sheet['C'+str(z)]=area
            sheet['D'+str(z)]=status
            if(price==""):
                sheet['E'+str(z)]=price
            else:
                sheet['E'+str(z)]=text_to_number(price)
            sheet['F'+str(z)]=auction_date
            
        
        print("__")
        print("################################################")

        print("y=",y,"   i=",i)
        print("z=",z)
        z=z+1
    
    
        

wb.save("Sale_enteries_15sept.xlsx")  


