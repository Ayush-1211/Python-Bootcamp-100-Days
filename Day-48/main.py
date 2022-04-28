from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.in/Test-TST_Exclusive1003-Exclusive-1003/dp/B0844592FT?ref_=Oct_DLandingS_D_f12f6055_60&smid=A14CZOWI0VEHLG&th=1")
# price = driver.find_element("a-offscreen")
# print(price.text)

driver.get("https://www.python.org/")
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "event": event_names[n].text
    }

print(events)

driver.quit()