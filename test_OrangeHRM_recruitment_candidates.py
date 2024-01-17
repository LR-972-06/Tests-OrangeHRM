# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


"""
But : Afin de tester le site https://opensource-demo.orangehrmlive.com/web/index.php/auth/login, 
écrire 3 ou 4 stratégies de tests

ONGLET CHOISI : RECRUITMENT >
"""


class RecruitmentTab_Tests (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_OrangeHRM_recruitment_candidates (self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Test login 
        """
        Le test Login permet de vérifier si l'utilisateur peut se connecter à son espace et accéder au dashboard. 
        La capture d'écran doit montrer le dashboard si le login a été fait avec succès.
         >> screenshot associé : "login_OK.png"
        """
        driver.find_element(By.NAME,"username").click()
        driver.find_element(By.NAME,"username").clear()
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").click()
        driver.find_element(By.NAME,"password").clear()
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, ".oxd-form").submit()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

        driver.save_screenshot("screenshots/login_OK.png")

# Test de la fonction ajout
        """
        Le test de la fonction ajout permet de vérifier si l'utilisateur peut ajouter un candidat à 
        sa liste ; cas de test : ajout du candidat suivant
        First name : IN TEST
        Middle name : DON'T TOUCH
        Last name : PLEASE !
        Mail : aaaa@gmail.com
        
        Le test passe s'il y a moins de candidats à cette liste avant qu'après.
         >> screenshot associé : "add_OK.png"
        """

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")

        candidat_ajoute = driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")
        taille_liste_before=len(candidat_ajoute)

        driver.find_element(By.NAME,"firstName").click()
        driver.find_element(By.NAME,"firstName").clear()
        driver.find_element(By.NAME,"firstName").send_keys("IN TEST")
        driver.find_element(By.NAME,"middleName").click()
        driver.find_element(By.NAME,"middleName").clear()
        driver.find_element(By.NAME,"middleName").send_keys("DON'T TOUCH")
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("PLEASE")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").send_keys("aaaa@gmail.com")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div").click()
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div[2]/div/div/div/label/span").click()

        time.sleep(10)

        driver.save_screenshot("screenshots/add_OK.png")
        
        candidat_ajoute = driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")
        taille_liste_after=len(candidat_ajoute)
        
        assert taille_liste_before < taille_liste_after

        
# Test de la fonction editer
        """
        Le test de la fonction editer permet de vérifier simodifier les informations 
        du candidat "IN TEST DON'T TOUCH".
        Nouveau last name : PLEASE !
        
         >> screenshot associé : "updated_OK.png"
        """

        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("PLEASE !")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[5]/a/span").click()

        time.sleep(5)
        driver.save_screenshot("screenshots/updated_OK.png")

# Test de la fonction supprimer
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        candidat_supprime = driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")
        taille_liste_before=len(candidat_supprime)

        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[5]/div/div[7]/div/button[2]/i").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()

        time.sleep(5)
        driver.save_screenshot("screenshots/delete_OK.png")

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        candidat_supprime = driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")
        taille_liste_after=len(candidat_supprime)
        
        assert taille_liste_before==(taille_liste_after+1)
        
        

# Test logout
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        time.sleep(5)
        driver.save_screenshot("screenshots/logout_OK.png")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
