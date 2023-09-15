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