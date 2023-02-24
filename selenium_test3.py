from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import threading


def watch_link(url):
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("-inprivate")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    driver = Edge(executable_path = r"C:\edgedriver\msedgedriver.exe", options = options) # Modify the path here...

    print("Watching:"+"https://www.youtube.com/watch?v="+url)
    driver.get("https://youtube.com/watch?v="+url)

    #yt_short
    #driver.get("https://www.youtube.com/shorts/"+url)

    time.sleep(3)
    try:
        #driver.find_element_by_xpath('//*[@id="movie_player"]').click()

        #yt_short
        driver.find_element_by_xpath('//*[@id="shorts-inner-container"]').click()
    except Exception as e:
        ActionChains(driver).send_keys("k").perform()
    time.sleep(60)
    #ActionChains(driver).send_keys("Esc").perform()


#https://www.youtube.com/watch?v=2sx0BSFrS-c
#https://www.youtube.com/shorts/vGDv-IHi1tA


link_to_watch = ["OESq2h5kSWg"]
#link_to_watch = ["2sx0BSFrS-c"]
#link_to_watch = ["MCg5z210x24"] 

#yt_short
#link_to_watch = ["vGDv-IHi1tA"]

time_to_watch = 10
threads = []
i = 1
for link in link_to_watch:
    for ttw in range(time_to_watch):
        threads.append(threading.Thread(target=watch_link, args=(link, ) ,name=str(i)))
        i+=1

for thread in threads:
  thread.start()

for thread in threads:
  thread.join()

print("done")