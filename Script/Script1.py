from selenium import webdriver
import time
import pushbullet

# connecting pushbullet account to send notification
# api_key = 'YOUR_ACCESS_TOKEN'
# pb = pushbullet.Pushbullet(api_key)
# pushes = pb.delete_pushes()

# print(pb.channels) -----> Run this command by un commenting it after entering your ACCESS TOKEN of your pushbullet account to check that your created channel is listed here
# select channel in which you want notification by index

# my_channel = pb.channels[0]


url = "https://anichart.net/airing"

driver = webdriver.Chrome()


# extract data
driver.get(url)

# wait
time.sleep(5)

# results
results = driver.find_elements_by_class_name("day")

#source = driver.page_source  ---> after this line I can use beautiful soup


for items in results:
    itemArr = items.text 
    print (itemArr)
    print("\n")
    # push = my_channel.push_note("EP Info", itemArr)

driver.close()


