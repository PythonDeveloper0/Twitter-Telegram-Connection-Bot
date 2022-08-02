from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pyperclip
    

gChromeOptions = webdriver.ChromeOptions()
gChromeOptions.add_argument("window-size=1920x1480")
gChromeOptions.add_argument("disable-dev-shm-usage")
driver = webdriver.Chrome(
    chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
)

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://twitter.com/CemalTheMM")
time.sleep(5)


#Maximize windows and scroll
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 1000);") 
time.sleep(2)

    #Telegram         
Chat_ID = "-1001666208772"
def telegram(tweet):
    requests.post(url="https://api.telegram.org/bot5222039809:AAFoeqBn2PwlJZdJVA0TB4fNFmSPA_L_SjE/sendMessage",data={"chat_id":Chat_ID,"text":tweet}).json
           
beforetweet = ''
#Tweet selection
while True:
    articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    #print("ARTICLES: ",articles)
    for i in range(20):

        article = articles[i]
        #time.sleep()
        #PINNED
        try:
            pinned = article.find_element(By.XPATH,"./div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/span").text
        except:
            print("Not pinned.")
            if article.find_element(By.XPATH,"./div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/a/div/span").text == "@CemalTheMM":
                
                break

    
    #Tweet link copy
    article.find_element(By.XPATH,".//div[@aria-label='Share Tweet']/div").click()
    time.sleep(2)
    article.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[1]").click()
    time.sleep(2)        

    url = pyperclip.paste()
    #url = pd.read_clipboard()
    #win32clipboard.CloseClipboard()
    if url != beforetweet:
        beforetweet = url
        telegram(beforetweet) 
    
         
    time.sleep(10)
