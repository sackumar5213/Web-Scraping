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

place_name="Gautam budh nagar"
bank_name="Punjab National Bank"
url="https://findauction.in/"
driver.get(url)
place=driver.find_element(By.XPATH,"/html/body/section[1]/div/div/div/div/div/div[2]/div[1]/div[1]/input").send_keys(place_name)
main_search=driver.find_element(By.XPATH,"/html/body/section[1]/div/div/div/div/div/div[2]/div[1]/div[3]/button").click()

# bank=driver.find_element(By.XPATH,"/html/body/section[1]/div/div/ul/li[3]/input").send_keys(bank_name)

# time.sleep(20)
# search=driver.find_element(By.XPATH,"/html/body/section[1]/div/div/ul/li[4]/button").click()


new_url = driver.current_url
gen_url=new_url+"/all/all/" #for storing next url with all 

print(new_url)
print(gen_url)



z=0
for y in range(1,3): # from page 1 to 5
    driver.get(gen_url+str(y))
    next_url=driver.current_url
    sheet['H'+str(z+1)]=next_url
    # time.sleep(3)
    
    for i in range(2,17):   #extracting data
        sachin="ehloodsakfasj"
        location_name=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[1]/h5/a").text
        price=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[1]/h6").text
        bank=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[1]/h5/small").text
        if(bank=="Punjab National Bank"):
            print("if wala  ",bank)
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
        else:
            print("Else wala= ", bank)
            bank=""
            location_name=""
            area=""
            status=""
            price=""
            auction_date=""    
        z=z+1
        # Entering the record of the property in row of the excel
        sheet['A'+str(z)]=bank
        print("edataa entry")
        sheet['B'+str(z)]=location_name
        sheet['C'+str(z)]=area
        sheet['D'+str(z)]=status
        if(price==""):
            sheet['E'+str(z)]=price
        else:
            sheet['E'+str(z)]=text_to_number(price)
        sheet['F'+str(z)]=auction_date    
        sheet['I1']=sachin
    z=z+1   # to create empty row for differentiate the data of each pages
        
wb.save(place_name+"cvzc_Sale_enteries.xlsx")  


