from selenium import webdriver
from selenium.webdriver.common.keys import Keys
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('./chromedriver',options=option)

driver.get("http://192.168.25.1/")
print(driver.title)
test = driver.find_element_by_tag_name('td')

if driver.title == "internet hotspot > login":
    print("got")
    login = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/form/table/tbody/tr[1]/td[2]/input").send_keys('25ramesh63')
    password = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/form/table/tbody/tr[2]/td[2]/input").send_keys('ramesh')
    submit = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/form/table/tbody/tr[3]/td[2]/input").click()
    
elif driver.title == "mikrotik hotspot > status":
    data = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]").text
    time = data.split("/")
    print(time[1])
    
    
    
    letters = ['d', 'h', 'm', 's']
    final_date = time[1].replace('d',",").replace('h',",").replace('m',",").replace('s',"")
    print(final_date)
        
    