from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def test_home():
    driver = webdriver.Chrome()
    driver.get("http://162.246.156.36:8000/")
    name_elem = driver.find_element_by_id("name")
    assert name_elem != None
    about_elem = driver.find_element_by_id("about")
    assert about_elem != None
    education_elem = driver.find_element_by_id("education")
    assert education_elem != None    
    skills_elem = driver.find_element_by_id("skills")
    assert skills_elem != None
    work_elem = driver.find_element_by_id("work")
    assert work_elem != None
    contact_elem = driver.find_element_by_id("contact")
    assert contact_elem != None
