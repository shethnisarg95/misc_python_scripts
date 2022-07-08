''' 
Dependencies to be imported: selenium,  webdriver_manager
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait 

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://bumble.com/app")
assert "Bumble" in driver.title

# Wait time to Log in Manually  
time.sleep(40)

names = []
# num variable to count number of likes you wanna give in a perticular run 
num = 1000
for count in range(num):
    try:
        # Dynamic wait till 20 sec for user profile picture to load
        driverWait = WebDriverWait(driver, 20)
        driverWait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='sidebar-profile__avatar']")))
        
        # Importing profile Name 
        nameElement = driver.find_element(By.XPATH, "//span[@class='encounters-story-profile__name']")
        name = nameElement.text

        # Importing profile age 
        ageElement = driver.find_element(By.XPATH, "//span[@class='encounters-story-profile__age']")
        age = ageElement.text
        
        # Clicking on like button 
        elem = driver.find_element(By.XPATH, "//div[@aria-label='Like']")
        elem.click()
        names.append([name, age])
        
        # Wait for profile to load
        time.sleep(3)
        
    except:
        pass
    
# Exporting name and age of liked profile to txt file
f = open("bumble_names.txt", "a")
f.write(str(names))
f.close()

