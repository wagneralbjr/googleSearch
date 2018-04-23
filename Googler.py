from selenium import webdriver

from selenium.webdriver.common.keys import Keys

URL = 'http://www.google.com.br'

class Googler():
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(URL) 
    
    def busca_img(self, termo):
        self.driver.get(URL+ "/search?q=" + termo)
        xPath = """/html/body/div[5]/div[3]/div[5]/div/div/div[1]/div/div/div/div[1]/div/div[3]/a"""
        img_search = self.driver.find_element_by_xpath(xPath)

        img_search.click()
    
    def baixa_imgs(self, qtd = 10):
        
        test = self.driver.find_element_by_tag_name('img') 
        print(test.size) 

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    obj = Googler()
    obj.busca_img('teste')
    obj.baixa_imgs() 
    obj.close()    
