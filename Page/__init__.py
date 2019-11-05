from selenium.webdriver.common.by import By

search_button = (By.ID,"com.android.settings:id/search")
search_text = (By.ID,"android:id/search_src_text")
search_return_button = (By.CLASS_NAME,"android.widget.ImageButton")
wifi_button = (By.XPATH,"//*[contains(@text,'More')]")