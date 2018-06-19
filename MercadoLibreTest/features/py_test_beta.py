from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.google.com.uy")
main_window = driver.current_window_handle
driver.execute_script("window.open('http://www.mercadolibre.com.uy', 'new window')")
tab = driver.current_window_handle
time.sleep(5)
driver.switch_to.window(main_window)
time.sleep(5)
driver.close()
