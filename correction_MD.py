# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_example(self):

        driver = self.driver

        # Connexion
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME,"username").click()
        driver.find_element(By.NAME,"username").clear()
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").clear()
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()

        # Navigation sur la page viewEmployeeList
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.LINK_TEXT,"PIM").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

        # Ajout d'un employé
        # driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()
        
        # for index in range(5):
        #     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
        #     driver.find_element(By.NAME,"firstName").click()
        #     driver.find_element(By.NAME,"firstName").clear()
        #     driver.find_element(By.NAME,"firstName").send_keys(f"John{index}")
        #     driver.find_element(By.NAME,"middleName").click()
        #     driver.find_element(By.NAME,"middleName").clear()
        #     driver.find_element(By.NAME,"middleName").send_keys(f"John{index}")
        #     driver.find_element(By.NAME,"lastName").click()
        #     driver.find_element(By.NAME,"lastName").clear()
        #     driver.find_element(By.NAME,"lastName").send_keys(f"Wick{index}")
        #     driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/div/div/div[2]/input").click()
        #     driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/div/div/div[2]/input").clear()
        #     driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/div/div/div[2]/input").send_keys("03134")
        #     driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

        # Compte le nombre d'elements selon la pagination (numeros de pages)
        total_count = 0
        while True:

            # Enregistrez le contenu de la liste avant l'ajout de l'élément
            employes_list = driver.find_elements(By.CLASS_NAME, "oxd-table-card")

            count_on_page = len(employes_list)

            # Accumuler le total
            total_count += count_on_page

            print(f'Page actuelle: {count_on_page} éléments sur la premiere page | Total jusqu à présent: {total_count} éléments')
           
            if count_on_page < 50 :
                # Pas de page suivante, sortie de la boucle
                break

            next_page_button = self.driver.find_element(By.XPATH, "//button[@class='oxd-pagination-page-item oxd-pagination-page-item--previous-next']")
            # next_page_button.click()
            elements = driver.find_elements(By.XPATH, "//button[@class='oxd-pagination-page-item oxd-pagination-page-item--previous-next']/i[@class='oxd-icon bi-chevron-right']")
            
            # //ul[@class='oxd-pagination__ul']/li
            elementsCount = driver.find_elements(By.XPATH, "//ul[@class='oxd-pagination__ul']/li")
            print("COUNT li", len(elementsCount))

            if len(elements) == 1:
                next_page_button.click()
            else :
                # Pas de page suivante, sortie de la boucle
                break
            
        # self.assertEqual(total_count, 105)

    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
