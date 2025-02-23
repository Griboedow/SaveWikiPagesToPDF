import time
from  selenium import webdriver
import os
import json

download_dir = r"C:\your-target-dir"

settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
            
        }],
       "selectedDestinationId": "Save as PDF",
       "version": 2,
       "isHeaderFooterEnabled": False,
       "isLandscapeEnabled": True
    }

options = webdriver.ChromeOptions()
#options.add_argument("--start-maximized")
#options.add_argument('--window-size=1280,1080')
options.add_argument(f"user-data-dir={download_dir}")
options.add_argument('--enable-print-browser')
options.add_experimental_option("prefs", {
    "printing.print_preview_sticky_settings.appState": json.dumps(settings),
    "savefile.default_directory": download_dir,  
    "download.default_directory": download_dir,  
    "download.prompt_for_download": False,  
    "download.directory_upgrade": True,
    "profile.default_content_setting_values.automatic_downloads": 1,
    "safebrowsing.enabled": True
})
options.add_argument("--kiosk-printing")
#service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)



#main part
login_url = 'my-mediaiwki-site/index.php/'
driver.get(login_url)


#manual login if needed. Make breakpoint here. When reach breakpoint, login in the Selenium browser
pass

urls = []
with open('urls_to_save.txt', 'r', encoding="utf8") as file:
    pages = file.read().splitlines()

for i, page in enumerate(pages):
    driver.get('https://my-mediaiwki-site/index.php/' + page)
    driver.execute_script('window.print();')
