import requests
import re
import openpyxl
from time import sleep
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

# cs="100038004359"
list = []
# list = [100038004359,100038004357,100038004355]
wb = openpyxl.Workbook()  # 创建Excel对象
ws = wb.active  # 获取当前正在操作的表对象
# 往表中写入标题行,以列表形式写入！
driver = webdriver.Chrome()
ws.append(['商品名称', '颜色', '配置', '价格'])


def excel_one_line_to_list():
    df = pd.read_excel(r"C:\Users\Administrator\Desktop\新建文件夹 (5)\1.xlsx", usecols=[0], names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()

    for s_li in df_li:
        list.append(s_li[0])
    print(list)


if __name__ == '__main__':
    excel_one_line_to_list()
    for item in list:
        print(item)
        cs = str(item)
        baseurl = "https://item.jd.com/" + (cs) + ".html"
        print(baseurl)

        driver.get(baseurl)
        # sleep(5)
        # 要爬取的网页
        #  创建Excel表并写入数据

        # 请求头
        headers = {
            'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'Upgrade-Insecure-Requests': '1'
        }

        content = requests.get(baseurl, headers=headers).content.decode('utf-8')

        r = requests.get(url=baseurl, headers=headers)
        # 字符串转换成HTML的格式
        _element = etree.HTML(r.content)
        # 通过xpath表达式获取标签中的电影名称的列表
        event_name = _element.xpath('/html/body/div[6]/div/div[2]/div[1]/text()')
        print(event_name[0])

        start_time = _element.xpath('//*[@id="choose-attr-1"]/div[2]/div[contains(@class, "selected")]/a/i/text()')
        print(start_time[0])

        area_name = _element.xpath('//*[@id="choose-attr-2"]/div[2]/div[contains(@class, "selected")]/a/text()')
        print(area_name[0])

        element = driver.find_element(By.CLASS_NAME, "J-p-" + (cs) + "").text
        print(element)
        # introduction = re.findall(r"<span>￥</span><span>(.+?)</span>",content)
        # print(introduction)

        for i in range(len(event_name)):  # 每页25条数据,写入工作表中
            ws.append([event_name[i].strip(), start_time[i].strip(), area_name[i].strip(), element.strip()])
wb.save('数据5.xlsx')  # 存入所有信息后，保存为filename.xlsx