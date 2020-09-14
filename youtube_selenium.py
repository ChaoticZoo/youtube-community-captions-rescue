from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import re
import time
import os


def exp_wait(process, by_type, element):
    return WebDriverWait(process, 20).until(EC.presence_of_element_located((by_type, element)))

# Replace with your download foler path
downloads_folder = "C:/Users/zekun/Downloads/"

counter = 0

# Replace with your own selenium installation path
driver = webdriver.Chrome("C:/Python37_64/chromedriver.exe")

# Replace with the txt file name that contains the ids + links.
list = open('hopefully_a_ton_of_links.txt').readlines()


driver.get("https://stackoverflow.com/users/login");

# Have 30 seconds to log in which should be plenty
time.sleep(30)

print(len(list))

for line in list:

    id = line[:11]

    # Really just manually go to the subtitle page for the correct language and put whatever's
    # behind &lang= here.
    lang_id = "zh-Hans"

    driver.get(f"https://www.youtube.com/timedtext_editor?action_mde_edit_form=1&v={id}&lang={lang_id}&bl=vmp&ui=hd&tab=captions&ar=1600018020002&o=U")

    time.sleep(2)

    temp_tag = exp_wait(driver, By.ID, 'edit-track-action-selection')
    button = temp_tag.find_element_by_tag_name('button')

    button.click()

    button = exp_wait(driver, By.XPATH, '//*[@tabindex="0"]/li[2]/a')
    button.click()

    time.sleep(3)

    id_only = id.rstrip("\n")

    try:
        os.rename(downloads_folder + "captions.sbv", downloads_folder + f"{id_only}.sbv")
    except FileExistsError:
        os.remove(downloads_folder + "captions.sbv")
        print("Duplicate for " + id)
        continue

    time.sleep(2)

    counter = counter + 1



print(counter)