from selenium import webdriver
import time

#using the chrome web driver
driver = webdriver.Chrome("C:/Program Files (x86)/chromedriver.exe")

#opening a new window
driver.get("https://web.whatsapp.com")

#this is so that code wahts for the user to scan thw qr code to link the web whatsapp
print("Scan QR Code, And then Enter")
input()
print("Logged In")

driver.maximize_window()

#Searching for the person/number to send message to
text_area = driver.find_element(
    by="xpath", value="//*[@id='side']/div[1]/div/div/div[2]/div/div[2]")
text_area.clear()
text_area.send_keys("6399149449")

#Clicking on the result of the search that appears
chat_name = driver.find_element(
    by='xpath', value="//*[@id='pane-side']/div[1]/div/div/div[1]/div/div/div")
chat_name.click()


message = "Hi.. I am a simple python script.."

#finding the message bar and writing message to it
driver.find_element(
    by='xpath', value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]').send_keys(message)

#Finding the send button and clicking it
driver.find_element(
    by='xpath', value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

#closing the window
driver.close()
