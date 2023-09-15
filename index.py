import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook 

wb = Workbook()  
sheet = wb.active  

driver=webdriver.Chrome()

# Price is in text, so make it in number
def text_to_number(text_with_commas):
    # Remove commas from the text
    text_without_commas = text_with_commas.replace(',', '')
    numeric_value = float(text_without_commas)
    return numeric_value

z=0
for y in range(1,20): 
    if(y==9):
        pass
    else:
        driver.get("https://findauction.in/bank-property/ghaziabad/pnbindia/all/"+str(y))
        # time.sleep(3)
        
        for i in range(2,17):
            location_name=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[1]/h5/a").text
            bank_name  =driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[1]/h5/small").text
            auction_date =driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/ul/li[1]").text
            area=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/ul/li[2]").text
            status=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/ul/li[3]").text
            price=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[1]/h6").text


            
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
            sheet['E'+str(z)]=text_to_number(price)
            sheet['F'+str(z)]=auction_date
        
        print("__")
        print("################################################")

        print("y=",y,"   i=",i)
        print("z=",z)
        z=z+1
    
    
        

wb.save("Sale_enteries_15sept.xlsx")  


