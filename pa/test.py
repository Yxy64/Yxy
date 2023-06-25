from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import pandas as pd
from lxml import etree

list = []
driver = webdriver.Chrome()

# driver.set_page_load_timeout(10)

def excel_one_line_to_list():
    df = pd.read_excel(r"C:\Users\Administrator\Downloads\新建 XLS 工作表.xlsx")  # 读取项目名称列,不要列名
    df_li = df.values.tolist()

    for s_li in df_li:
        list.append(s_li[0])
    print(list)


if __name__ == '__main__':
    excel_one_line_to_list()
    for item in list:
        print(item)
        cs = str(item)
        baseurl = cs
        print(baseurl)

        driver.get('https://store.jddj.com/')

        driver.delete_all_cookies()
        cookies = [
            {'domain': '.jddj.com', 'expiry': 1687932944, 'httpOnly': True, 'name': 'o2o-stock1.jddj.com', 'path': '/',
             'sameSite': 'None', 'secure': True,
             'value': 'GURC6Q6L7EC3C2BZSL3X7L6VWBFH65MWTGCUEJBZHMDIVCO3VWZDHKPZS2WBTXF2VBZFB22NEIGLKUTB5744THAW7ZAIXLXJGA77AEHFUQAIMDQDOARGJKSLXIO7MWNSA3Z7XDFIHHJOEQZADNRNG26652GAOP6GZTYLEHDAMST42ORGBZJHJ7XJD2CDWUCSFUP2ODMYGZGU6ODDDHCWNECJVQK3673TWQEKQQ7WNSXKJ6KISHBE2XVMXXW7K6NNSUABZGFKZJGHTPANQUVCFCX7HTYFATVNFZ52IT63RVSAZGVT2SRNTXHINDKABRMWMRF4P6DXRCVWCK5ZH47FYJNYNDLHSE75RQ534V3L425VXWU5KHBJ5GL7IKJCKF3X'},
            {'domain': '.jddj.com', 'expiry': 1687932944, 'httpOnly': True, 'name': 'josl-privilege1.jddj.com',
             'path': '/', 'sameSite': 'Lax', 'secure': False,
             'value': 'GURC6Q6L7EC3C2BZSL3X7L6VWBFH65MWTGCUEJBZHMDIVCO3VWZDHKPZS2WBTXF2VBZFB22NEIGLKUTB5744THAW7ZAIXLXJGA77AEHFUQAIMDQDOARGJKSLXIO7MWNSA3Z7XDFIHHJOEQZADNRNG26652GAOP6GZTYLEHDAMST42ORGBZJKS7N2GNUU35OOLZGALA5H2LOGSPZJVQGR2V6TTOC4CJ7ZW2XAVDT6YCU4FDAS243OTXBOYHDTOLYEHCLP7VMBUG3PUZT2QZRUSRDKWMC4EE35K6SM4KFKCOHUZ4WZ5KI5L4VW7OFKI7YSJZR25PPVDUT7EVTSQCJRD63Q7SVSX6NWW6HIKTRHOTI75ICV7KJMGRPD5TKWOLLZ3OIXVOYCBOVPV2KKX3YBIOJ4QQDSHMPF3R5MQMGYD7QQP7PKN35A'},
            {'domain': '.jddj.com', 'expiry': 1695104143, 'httpOnly': False, 'name': 'store_deviceid', 'path': '/',
             'sameSite': 'Lax', 'secure': False, 'value': 'e3231e56d3e5ed550bc681058747c739'},
            {'domain': '.jddj.com', 'httpOnly': False, 'name': 'store_session', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '%231687328143914'},
            {'domain': '.jddj.com', 'expiry': 1687932943, 'httpOnly': True, 'name': 'lsp-store1.jddj.com', 'path': '/',
             'sameSite': 'Lax', 'secure': False,
             'value': 'GURC6Q6L7EC3C2BZSL3X7L6VWBFH65MWTGCUEJBZHMDIVCO3VWZDHKPZS2WBTXF2VBZFB22NEIGLKUTB5744THAW7ZAIXLXJGA77AEHFUQAIMDQDOARGJKSLXIO7MWNSA3Z7XDFIHHJOEQZADNRNG26652GAOP6GZTYLEHDAMST42ORGBZJLNZSQ7UJILZ6T23MI7JRUNW2OEKMIXIYG775L6WMXHVDYKXSEAMPHMPK3OTIFET2LKPA4QC76JMTI43Q5DE2U5RVXTTDB37HD74HXWOPT6MXBCVCJ6IFEIDYUBRGK3VKG3W4XNYWRPVO2NM7AW4U5LLFPPKYAQU5N52QDEYRYOKFIE2FPBWLPJWRXV4N5FWRMZXFH7GOKSKRSJOVTWFTLHEVLOS7UXRB3EVOIJY'},
            {'domain': 'store.jddj.com', 'expiry': 1695104132, 'httpOnly': False, 'name': 'deviceid_pdj_jd',
             'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'H5_DEV_7595A1CE-E928-4858-9AE4-2ACE11B6477C'},
            {'domain': 'store.jddj.com', 'httpOnly': True, 'name': 'vender_id', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '376719'},
            {'domain': '.jddj.com', 'expiry': 1687932944, 'httpOnly': False, 'name': 'user_email', 'path': '/',
             'sameSite': 'None', 'secure': True, 'value': 'jd_sxgmtsm'},
            {'domain': 'store.jddj.com', 'expiry': 1687932943, 'httpOnly': True, 'name': 'client_id', 'path': '/',
             'sameSite': 'Lax', 'secure': False, 'value': '4e66cbba-e61b-458a-9d21-a0bfc5b88de7'},
            {'domain': 'store.jddj.com', 'httpOnly': True, 'name': 'vender_name', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '\\u7EFC\\u5408-\\u5C71\\u897F\\u5149\\u7F8E\\u6CF0'},
            {'domain': '.jddj.com', 'expiry': 1687932945, 'httpOnly': True, 'name': 'o2o-pms1.jddj.com', 'path': '/',
             'sameSite': 'Lax', 'secure': False,
             'value': 'GURC6Q6L7EC3C2BZSL3X7L6VWBFH65MWTGCUEJBZHMDIVCO3VWZDHKPZS2WBTXF2VBZFB22NEIGLKUTB5744THAW7ZAIXLXJGA77AEHFUQAIMDQDOARGJKSLXIO7MWNSA3Z7XDFIHHJOEQZADNRNG26652GAOP6GZTYLEHDAMST42ORGBZJKKGHTMHG25AFMHVUZMPRIZJHREODDDHCWNECJVQK3673TWQEKQQ7QT5EHXF3TLCPR74FUZ3I277ZZSUABZGFKZJGHTPANQUVCFCX7HSTAUPAUQU67FWJF6ZQUIAMBGOSA'},
            {'domain': 'store.jddj.com', 'httpOnly': True, 'name': 'user_key', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '712846'},
            {'domain': '.jddj.com', 'expiry': 1713248143, 'httpOnly': False, 'name': '3AB9D23F7A4B3C9B', 'path': '/',
             'sameSite': 'Lax', 'secure': False,
             'value': 'YXA5NUZ6LMZWEB7OL6WC23HXPHPT6CTOYXDRDMTZTRJ4A5MJ4RAOLY25LA3SAM4BFELQIOAZIFWXHS3DJ342MJ2JCI'}]
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            driver.add_cookie(cookie)
        # driver.refresh()
        driver.get('https://store.jddj.com/')
        driver.get(baseurl)
        time.sleep(2)
        driver.find_element(By.XPATH, '//div[@class="dj-tab-inner"]/ul/li[5]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="goods-detail"]/form/div[1]/div/div/div/label[1]/span[2]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[2]/button[1]/div[2]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button/div[2]').click()
        time.sleep(2)

    # driver.quit()


# driver.get('https://store.jddj.com/')
# driver.implicitly_wait(10)
# time.sleep(10)
# coo = driver.get_cookies()
# print(coo)
# driver.quit()
