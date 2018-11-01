from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def test_home():
    driver = webdriver.Chrome()
    driver.get("http://162.246.156.36:8000/")
    name_elem = driver.find_element_by_id("name")
    assert name_elem != None
    assert name_elem.get_attribute('text') == "Some name"

    about_elem = driver.find_element_by_id("about")
    assert about_elem != None
    assert about_elem.get_attribute('text') == "this is the description"

    education_elem = driver.find_element_by_id("education")
    assert education_elem != None    
    assert education_elem.get_attribute('text') == "i don't go to school"    

    skills_elem = driver.find_element_by_id("skills")
    assert skills_elem != None
    assert skills_elem.get_attribute('text') == "No skills"

    work_elem = driver.find_element_by_id("work")
    assert work_elem != None
    assert work_elem.get_attribute('text') == "I don't work"

    contact_elem = driver.find_element_by_id("contact")
    assert contact_elem != None
    assert contact_elem.get_attribute('text') == "aa@ualberta.ca"
