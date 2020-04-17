from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import os
import sys



### Global Variable
driver = Chrome(executable_path='D:\\pythonselenium\\chromedriver.exe')
expectedTitle = "Choose Authentication"
expectedTitle2 = "Infor CloudIdentities - Sign On" #To those non-hybrid #Will use or in the command once implemented to other tenant
delay = 10
csfusername = 'kevinjames.bajao@infor.com'
csfpassword = 'InforAutomation123!'

### CSF URLs
## Password change 4/17
csfd1 = 'https://fin-CSFD1T02-TST.tam.awsdev.infor.com/fsm/web/home'
csfm1 = 'https://fin-CSFM1C07-TST.tam.awsdev.infor.com/fsm/web/home'
csfr2 = 'https://fin-CSFR2T02-TST.tam.awsdev.infor.com/fsm/web/home'
csfe1 = 'https://fin-CSFE1T03-TST.tam.awsdev.infor.com/fsm/web/home'

### Check Time
now = datetime.now()
directoryname = now.strftime("%Y-%m-%d-%H-%M")

### Create Directory
createdir = os.path.join("E:\\MTScreenshots", directoryname)
if not os.path.exists(createdir):
    os.mkdir(createdir)
    os.chdir(createdir)

def validatehealthall():
    print('DO IT ALL')
    csfList = [csfd1, csfm1, csfr2, csfe1]
    for csf in csfList:
        #print(csf)
        driver.get(csf)
        actualTitle = driver.title
        csftenant = csf.replace('//', ' ').replace('-', ' ').replace('.', ' ').split()
        print(csftenant[2])
        print(actualTitle)

        if actualTitle == expectedTitle:
            print('equal')
            driver.find_element_by_link_text("Cloud Identities").click()
            elementPresent_username = EC.presence_of_element_located((By.ID, 'username'))
            WebDriverWait(driver, delay).until(elementPresent_username)
            # WebDriverWait.until(EC.visibility_of_any_elements_located((By.ID, 'username')))
            print('Page ready')
            driver.find_element_by_id('username').click()
            driver.find_element_by_id('username').send_keys(csfusername)
            driver.find_element_by_id('password').click()
            time.sleep(3)
            driver.find_element_by_id('password').send_keys(csfpassword)
            driver.find_element_by_id('password').send_keys(Keys.ENTER)
            time.sleep(10)
            elementPresent_admconsole = EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Administration Console')])[1]"))
            if WebDriverWait(driver, delay).until(elementPresent_admconsole) is not None:
                print('Do this')
                checkAdm = driver.find_element_by_xpath("(//span[contains(text(),'Administration Console')])[1]")
                validatecheckAdm = checkAdm.text
                expectedcheckAdm = 'Administration Console'

                if validatecheckAdm == expectedcheckAdm:
                    print(csftenant[2] + ' is running')
                    driver.save_screenshot('OK_' + csftenant[2] + '.png')
                    print('Screenshot taken')

                else:
                    print(csftenant[2] + ' is not running')
                    driver.save_screenshot('KO_' + csftenant[2] + '.png')
                    print('Screenshot taken')
            else:
                print(csftenant[2] + ' is not running')
                driver.save_screenshot('KO_' + csftenant[2] + '.png')
                print('Screenshot taken')
        else:
            print(csftenant[2] + ' is not accessible')
            driver.save_screenshot('KO_' + csftenant[2] + '.png')

        ### Clear Browsing data
        driver.get('chrome://settings/clearBrowserData')
        driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
        time.sleep(3)

    driver.close()
    print('Done Check')

def checkcsf(csf):
    if csf == 'ALL':
        validatehealthall()


if __name__ == '__main__':
    checkcsf(sys.argv[1])

"""
csfd1url = "https://fin-CSFD1T02-TST.tam.awsdev.infor.com/fsm/web/home"

print(csfd1url)
#driver.get("https://selenium.dev")
#driver.get("https://fin-CSFD1T02-TST.tam.awsdev.infor.com/fsm/web/home")
#driver.save_screenshot("D:\\pythonselenium\\screenshit.png")
def emailcsf(csfemailvar):
    print(csfemailvar + ' send email')

def validatehealth(csf):
    driver = Chrome(executable_path='D:\\pythonselenium\\chromedriver.exe')
    driver.get(csf)
    driver.save_screenshot("D:\\pythonselenium\\screenshit.png")
    csfemailvar = 'CSFD1'
    emailcsf(csfemailvar)
    print('CSFD1 Validate')


def checkcsf(csf):
    if csf == csfd1url:
        selectcsf = validatehealth(csf)
        print('CSFD1 check')
    elif csf == 'ALL':
        print('No')

if __name__ == '__main__':
    checkcsf(sys.argv[1])
"""