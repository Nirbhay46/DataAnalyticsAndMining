from selenium import webdriver
import time
import xlwt
from JD_PhoneNo import get_phone_no
book = xlwt.Workbook(encoding="utf-8")
browser2 = webdriver.Chrome("C:/chromedriver.exe")
sheet2=book.add_sheet("Sheet 2")
j_hotelname = []
j_phone = []
j_address = []
j_ratings = []
j_review = []
j_votes = []
j_url = []
j_timmings = []
m = 0
r = 0
for i in range(1,32):
    page = "https://www.justdial.com/Bhopal/Restaurants/page-"+str(i)
    browser2.get(page)
    hotellist = browser2.find_elements_by_class_name("lng_cont_name")
    browser2.implicitly_wait(0.5)
    time.sleep(0.5)
    temp_list = []
    for hotel in hotellist:
        j_hotelname.append(hotel.text)
        temp_list.append((hotel.text))
    for i in range(0,10):
        try:
            j_phone.append(get_phone_no(browser2, m))
        except Exception as e:
            j_phone.append("none")
        m = m + 1
    for i in range(0,len(temp_list),1):
        link = browser2.find_element_by_link_text(temp_list[i])
        link.click()
        browser2.implicitly_wait(1)
        try:
            j_ratings.append(browser2.find_element_by_class_name("value-titles").text)
        except Exception as e1:
            j_ratings.append("none")
        try:
            j_address.append(browser2.find_element_by_class_name("comp-text").text)
        except Exception as e1:
            j_address.append("none")
        try:
            j_votes.append(browser2.find_element_by_class_name("votes").text)
        except Exception as e1:
            j_votes.append("none")
        try:
            j_timmings.append(browser2.find_element_by_class_name("mreinflispn2").text)
        except Exception as e1:
            j_timmings.append("none")
        try:
            j_url.append(browser2.current_url)
        except Exception as e1:
            j_url.append("none")
        try:
            reviews = browser2.find_elements_by_class_name("rwopinion2.thr.lng_commn")
            for review in reviews:
                j_review[r].append(review.text)
        except Exception as e1:
            j_ratings.append("none")
        r = r + 1
        browser2.back()
    temp_list = []
for i in range(0,len(j_hotelname)):
    sheet2.write(i,0,j_hotelname[i])
    sheet2.write(i,1,j_address[i])
    sheet2.write(i,2,j_ratings[i])
    sheet2.write(i,3,j_phone[i])
    sheet2.write(i,4,j_votes[i])
    sheet2.write(i,5,j_url[i])
    sheet2.write(i,6,j_timmings[i])
    sheet2.write(i,7,j_review[i])
book.save("JustdialBhopal.xls")