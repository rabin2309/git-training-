import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# Initialize WebDriver
profile_directory = r'C:/Users/HP/AppData/Local/Google/Chrome/User Data'

# driver = webdriver.Chrome() 
# driver.set_capability("goog:loggingPrefs", {"performance": "ALL"})  # Enable performance logging

# driver.add_argument('--user-data-dir=C://Users//HP//AppData//Local//Google//Chrome//User Data') 
# driver.add_argument('--profile-directory=Default')

driver = webdriver.Chrome()  # Replace with your WebDriver setup
driver.get("https://reqres.in")  # Replace with your frontend URL

# # Fetch cookies from the browser
# cookies = driver.get_cookies()
session = requests.Session()

try:
#     time.sleep(10)
#     driver.find_element(By.XPATH, '//*[@id="root"]/section/section[1]/section[3]/div/div[4]/div/button').click()
#     time.sleep(3)
#     driver.find_element(By.XPATH, "//input[@placeholder='Search']").click()
#     time.sleep(2)

#     figcaptions = driver.find_elements(By.TAG_NAME, 'figcaption')

    # target_name = ""
   
    api_url = "https://reqres.in/api/users?page=2" 
    # params = {
    # "name": "morpheus",
    # "job": "leader"


    response = session.get(api_url)  

    if response.status_code == 200:
        try:
            backend_data = response.json()  
            print("Backend Data:", backend_data)
        except requests.JSONDecodeError:
            print("Failed to parse JSON from the backend response.")
            print("Response Text (Full):", response.text)  
    else:
        print(f"Failed to fetch backend data: HTTP {response.status_code}")
        print("Response Text:", response.text)

    # Check if ID 7 exists in the response
    # found = any(user.get("id") == 7 for user in backend_data.get("data", []))
    # print(found)
    # # Print user details if found
    # for user in backend_data.get("data", []):
        
    #     if user.get("id") == 7:
    #         print("User Found:", user)
        

    # Validation message
    # if found:
    #     print("Validation Success: 'id : 7' exists in the response.") 
    # else:
    #     print("Validation Failed: 'id : 7' not found in the response.")
    
    
    #First Name
    
    # found = any(user.get("first_name") == "Michael" for user in backend_data.get("data", []))
      
    # if found:
    #     print("Validation Success: 'first_name : Michael' exists in the response.")
    # else:
    #     print("Validation Failed: 'first_name : Michael' not found in the response.")


    #Support
    

    



finally:
    driver.quit()


hello tester
