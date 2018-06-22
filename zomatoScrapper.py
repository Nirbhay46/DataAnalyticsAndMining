from selenium import webdriver
import time
import xlwt
from JD_PhoneNo import get_phone_no
book = xlwt.Workbook(encoding="utf-8")
sheet1=book.add_sheet("Sheet 1")
browser = webdriver.Firefox()
browser.get("https://www.zomato.com/bhopal/dinner")
z_hotel_list = []
z_address_list = []
z_phone_list = []
z_rating_list = []
z_costoftwo = []
z_votes = []
z_hours = []

def traverse(a,b):
    temp = []
    for i in range(a,b,1):
        a = str(i)
        button = browser.find_element_by_link_text(a)
        button.click()
        name_list = browser.find_elements_by_class_name("result-title.hover_feedback.zred.bold.ln24.fontsize0")
        add_list = browser.find_elements_by_class_name("col-m-16.search-result-address.grey-text.nowrap.ln22")
        phone_list = browser.find_elements_by_class_name("item.res-snippet-ph-info")
        for i in range(1,18):
            if(i==4 or i==10 ):
                continue
            else:
                try:
                    z_costoftwo.append(browser.find_element_by_xpath("/html/body/section/div/div[2]/div[3]/div[2]/div/div[6]/div/div[1]/section/div[1]/div[3]/div["+str(i)+"]/div[1]/div/article/div[3]/div[2]/span[2]").text)
                except Exception as e:
                    z_costoftwo.append("NILL")
                try:
                    z_hours.append(browser.find_element_by_xpath("/html/body/section/div/div[2]/div[3]/div[2]/div/div[6]/div/div[1]/section/div[1]/div[3]/div["+str(i)+"]/div[1]/div/article/div[3]/div[3]/div[1]").text)
                except Exception as e1:
                    z_hours.append("NILL")
                try:
                    z_votes.append(browser.find_element_by_xpath("/html/body/section/div/div[2]/div[3]/div[2]/div/div[6]/div/div[1]/section/div[1]/div[3]/div["+str(i)+"]/div[1]/div/article/div[1]/div/div[2]/div[1]/div[2]/span").text)
                except Exception as e1:
                    z_votes.append("NEW")
                try:
                    z_rating_list.append(browser.find_element_by_xpath("/html/body/section/div/div[2]/div[3]/div[2]/div/div[6]/div/div[1]/section/div[1]/div[3]/div["+str(i)+"]/div[1]/div/article/div[1]/div/div[2]/div[1]/div[2]/div[1]").text)
                except Exception as e:
                    z_rating_list.append("NILL")
        for names in name_list:
            z_hotel_list.append(names.text)
            temp.append(names.text)
        for addname in add_list:
            z_address_list.append(addname.text)
        for phonename in phone_list:
            z_phone_list.append(phonename.get_attribute("data-phone-no-str"))
    if(int(a)<6):
        clk = browser.find_element_by_xpath("/html/body/section/div/div[2]/div[3]/div[2]/div/div[6]/div/div[1]/section/div[2]/div[1]/div[2]/div/div/a[7]")
        clk.click()
    else:
        clk = browser.find_element_by_xpath("/html/body/section/div/div[2]/div[3]/div[2]/div/div[6]/div/div[1]/section/div[2]/div[1]/div[2]/div/div/a[8]")
        clk.click()
traverse(1,6)
traverse(6,11)
traverse(11,16)
traverse(16,21)
traverse(21,26)
# traverse(26,31)
# traverse(31,36)
# traverse(36,41)
# traverse(41,46)
# traverse(46,51)
# traverse(51,56)
# for i in range(1,5,10):
#     traverse(i,i+5)
#     traverse(i+5,i+10)
for i in range(0,len(z_hotel_list),1):
    sheet1.write(i,0,z_hotel_list[i])
for i in range(0, len(z_phone_list), 1):
    sheet1.write(i,1,z_phone_list[i])
for i in range(0, len(z_address_list), 1):
    sheet1.write(i, 2, z_address_list[i])
for i in range(0,len(z_rating_list)):
    sheet1.write(i,3,z_rating_list[i])
for i in range(0, len(z_costoftwo)):
    sheet1.write(i, 4, z_costoftwo[i])
for i in range(0, len(z_hours)):
    sheet1.write(i, 5, z_hours[i])
for i in range(0, len(z_votes)):
    sheet1.write(i, 6, z_votes[i])

print("Writing to excel Finished")
book.save("ZomatoBhopal(data).xls")

