#
# import pickle
# from bs4 import BeautifulSoup
# import requests
# from csv import writer
# url="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
#
# page=requests.get(url)
# print(page)
# html_code=BeautifulSoup(page.content,'html.parser')
# main_content=html_code.find_all('div',class_="s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border")
# # with open("bag_details.csv",'w',encoding='utf8',newline='')as f:
# #     thewriter=writer(f)
# #     header=['PRODUCT_URL','PRODUCT_NAME','PRODUCT_PRICE','PRODUCT_RATING','NO_OF_REVIEWS_ON_PRODUCT']
# #     thewriter.writerow(header)
# n_list = []
#
# for content in main_content:
#             p_u=content.find('a', {'class': 'a-link-normal s-no-outline'})['href']
#             product_url="https://amazon.in"+p_u
#             product_name=content.find('span',class_="a-size-medium a-color-base a-text-normal").text
#             product_price=content.find('span',class_="a-price-whole").text
#             rating=content.find('span',class_="a-size-base").text
#             no_of_reviews=content.find('span',class_="a-size-base s-underline-text").text
#             # no_of_reviews = reviews.get_text().split()[0]
#             allinfo=[product_url,product_name,product_price,rating,no_of_reviews]
#             print(allinfo)
#             n_list.append(product_url)
# print(n_list)
#
#
# #pikling
#
#
# # l = n_list
# # with open("test", "wb") as fp:
# #     pickle.dump(l, fp)
#
# # >>> with open("test", "rb") as fp:   # Unpickling
# # ...   b = pickle.load(fp)
# # ...
# # >>> b
#
# #
# # for i in n_list:
# #     page2=requests.get(i)
# #     print('page 2 response',page2)
# #     html_code2=BeautifulSoup(page2.content,'html.parser')
# #     main_content2 = html_code2.find('div',class_="a-row a-spacing-top-base")
# #     product_manufacturer = main_content2.find('tr',class_="a-size-base prodDetAttrValue")
# #     print('prdct descrptn',product_manufacturer)
#
#             # page2 = requests.get(url2)
#             # print('page_2 response',page2)
#             # html_code2 = BeautifulSoup(page2.content, 'html.parser')
#             # print('here')
#             # main_content2 = html_code2.find_all('div',id="prodDetails")
#             #
#             # product_manufacturer=main_content2.find_all('tr',class_="a-color-secondary a-size-base prodDetSectionEntry")
#             # print(product_manufacturer)
# "C:\Users\ankit\Downloads\chromedriver_win32\chromedriver.exe"

# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from csv import writer
# driver = webdriver.Chrome(executable_path= r'C:\Users\ankit\Downloads\chromedriver_win32\chromedriver.exe')
url_list=[]
with open("bag_details.csv", 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header=['PRODUCT_URL','PRODUCT_NAME','PRODUCT_PRICE','PRODUCT_RATING','NO_OF_REVIEWS_ON_PRODUCT','ASIN']
    thewriter.writerow(header)
    for i in range(1,21):

        url=f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{i}"
        HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Accept-Language': 'en-US,en;q=0.5'})
        page=requests.get(url,headers=HEADERS)
        print(page)
        html_code=BeautifulSoup(page.content,'html.parser')
        main_content=html_code.find_all('div',class_="s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border")

        for content in main_content:
                    p_u=content.find('a', {'class': 'a-link-normal s-no-outline'})['href']
                    product_url="https://amazon.in"+p_u
                    product_name=content.find('span',class_="a-size-medium a-color-base a-text-normal").text
                    product_price=content.find('span',class_="a-price-whole").text
                    rating=content.find('span',class_="a-size-base").text
                    no_of_reviews=content.find('span',class_="a-size-base s-underline-text").text
                    nor=no_of_reviews.replace('(',' ')
                    nor = nor.replace(')', ' ')
                    no_of_reviews=nor
                    url = product_url
                    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Accept-Language': 'en-US,en;q=0.5'})
                    response = requests.get(url, headers=HEADERS)
                    soup = BeautifulSoup(response.content, "html.parser")
                    asin = soup.find("input", {"name": "ASIN"})
                    p = asin["value"]
                    print(p)
                    allinfo = [product_url, product_name, product_price, rating, no_of_reviews,p]
                    thewriter.writerow(allinfo)
# print(url_list)
# with open("bag_details.csv", 'a', encoding='utf8', newline='') as f:
#     thewriter = writer(f)
#     for i in url_list:
#         url=i
#         HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Accept-Language': 'en-US,en;q=0.5'})
#         response = requests.get(url, headers=HEADERS)
#         print(response)
#         soup = BeautifulSoup(response.content, "html.parser")
#         asin = soup.find("input", {"name": "ASIN"})
#         p = asin["value"]
#         print(p)
#         thewriter.writerow(p)

                    # driver.get(i)
                    # driver.implicitly_wait(0.5)
                    # try:
                    #     element = driver.find_element(By.ID, 'productDetails_db_sections')
                    #
                    #     # p=element.find()
                    #     print('1',element.text)
                    # except NoSuchElementException:
                    #
                    #     text_contents = [el.text for el in driver.find_elements(By.ID, 'detailBullets_feature_div')]
                    #     # Print text
                    #
                    #     for text in text_contents:
                    #         print('2',text)







