from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import pandas as pd
from lxml import etree

list = []
driver = webdriver.Chrome()


def excel_one_line_to_list():
    df = pd.read_excel(r"C:\Users\Administrator\Downloads\spu.xlsx")  # 读取项目名称列,不要列名
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
        # driver.get('https://opendj.jd.com/')

        header = {
            "Cookie": "user_email=jd_bjlcxqd; o2o-stock1.jddj.com=5YTAOP7SIZ7VI26F46QL3H6YFLLHFQUC4VLGOEX46PTMFWWSLBWBT677BN5LWHGMSIL4F7CHMNZPFIYZTP7HPIPCJNB6IO6QLBZMNRJSVRMHRZ6VFXGAD72KNSYEOFKWVAUDAKJVP6VDFYMRJPAWIH3CD6PWNUOQYQSDTWOIDEHF2ZMW3IOV5TIZ3AUHMWEUXTF3CEHZGU75ZXSDBGTVQOQ72GYS6HTWIK64GML7CDSKKFYRDZGNAXJLIZ5L3PUDD455SZZFJHMFGY2U4PLTNS475VLL7M264JS7UB5MEBBIQUVLMD3E5PSJJRJIDVJR4QTTT4GCGPAOIVE753EDC3I24M5KYSLSFL263SQ",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        }

        driver.get(baseurl)
        time.sleep(2)
# time.sleep(10)
