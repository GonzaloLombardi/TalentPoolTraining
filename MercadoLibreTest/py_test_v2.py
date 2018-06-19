from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def wait_for_element_class_name(driver, name):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, name))
        )
    except:
        driver.quit()


def compare_name_price(driver, link, name, price):
    driver2 = webdriver.Firefox()
    driver2.get(link)
    title = driver2.find_element_by_class_name("item-title").text
    wait_for_element_class_name(driver2, "price-tag")
    precios = driver2.find_elements_by_class_name("price-tag")
    if precios.__len__() > 1:
        p = precios.pop(1).text.split("\n")
    else:
        p = precios.pop(0).text.split("\n")
    precio = (p.pop(0) + " " + p.pop(0))

    assert (name == title)
    assert (price == precio)
    print "OK"
    driver2.close()


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.mercadolibre.com.uy")
driver.execute_script("window.scrollTo(0,400)")
wait_for_element_class_name(driver, "recommendations")
slide = driver.find_element_by_class_name("recommendations")


for x in range(0, 4):

    wait_for_element_class_name(driver, "slick-active")
    item_list = slide.find_elements_by_class_name("slick-active")

    for element in item_list:

        webdriver.ActionChains(driver).move_to_element(element).perform()
        time.sleep(0.080)

        txt = element.find_element_by_class_name("ui-item__price").text.split("\n")
        a = txt.pop(0)
        b = txt.pop(0)
        price = (a + " " + b)

        name = element.find_element_by_class_name("ui-item__title").text
        print price + " - " + name
        link = element.find_element_by_class_name("ui-item").get_attribute("href")

        compare_name_price(driver, link, name, price)

    buttons = driver.find_elements_by_class_name("next-button")
    webdriver.ActionChains(driver).move_to_element(buttons.pop(1)).click().perform()
    time.sleep(0.400)

print "Todo OK"
driver.close()
