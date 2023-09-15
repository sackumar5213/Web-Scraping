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
y=1
url="https://findauction.in/login"
driver.get(url)

        
# for i in range(2,17):
#     location_name=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[1]/h5/a").text
#     bank_name  =driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[1]/h5/small").text
#     auction_date =driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/ul/li[1]").text
#     area=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/ul/li[2]").text
#     status=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/ul/li[3]").text
#     price=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div["+str(i)+"]/div/div/div/div/div[1]/h6").text


#     sheet['A'+str(i)]=bank_name
#     sheet['B'+str(i)]=location_name
#     sheet['C'+str(i)]=area
#     sheet['D'+str(i)]=status
#     sheet['E'+str(i)]=text_to_number(price)
#     sheet['F'+str(i)]=auction_date
        
#     print("__")
#     print("################################################")

#     print("y=",y,"   i=",i)
email=driver.find_element(By.XPATH,"/html/body/section[2]/div/div[1]/div[2]/form/div[1]/input").send_keys("ofc.prudent@gmail.com")
password=driver.find_element(By.XPATH,"/html/body/section[2]/div/div[1]/div[2]/form/div[2]/input").send_keys("Rahul@100")
login=driver.find_element(By.XPATH,"/html/body/section[2]/div/div[1]/div[2]/form/div[3]/button").click()

new_url = driver.current_url
time.sleep(5)

print(new_url)
sheet['A1']=new_url
        

wb.save("Sample.xlsx")  



