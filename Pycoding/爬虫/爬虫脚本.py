# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:00:34 2020

@author: Achan
"""

import selenium 
import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup
def myAtoi(str: str) -> int:
    
    op_flag = false
    result = ""
    for c in str:
        if c.isdigit():
            result += c
            
if __name__== '__main__':
    
    driver = webdriver.Chrome()

    #webdriver.PhantomJS()

    driver.get('网址')
    a = driver.find_element_by_xpath("//*[@id='user-profile']/a[1]")
    a.click()
    
    driver.switch_to_window(driver.window_handles[-1])
#switch_to_window方法已过期，使用switch_to.window方法来代替
   
    #print(driver.page_source)
    
    #print(driver.current_url)
    
    
    soup = BeautifulSoup(driver.page_source, "lxml")
    
    p_list = soup.find_all('p', class_='math-captcha-form')
    print(p_list)
    # 获取每个div中的a中的span（第一个），并获取其文本
    src_mul = ''
    for each in p_list:
        src_mul = each.span.text    
        print(src_mul)
    
#    exp = ''.join(src_mul.split())
        
        
        
    #Test Part
  
        
        
    lenth = len(src_mul)
    

        
    #提取num1 num2
    snum1 = ""
    snum2 = ""
    i = 0
    
    for i in  range(0, lenth -1):
        if src_mul[i].isdigit():
            break
    
    while(src_mul[i].isdigit()):
        snum1 += src_mul[i]
        i= i+1
    
 
    
    
    
    #成功提取num1
    for j in  range(i, lenth):
        if src_mul[j].isdigit():
            break
    
    
    while(j < lenth and src_mul[j].isdigit()):
        snum2 += src_mul[j]
        j= j+1
    
        
        
        
    num1 = 0
    num2 = 0
    
    num1 = int(snum1)
    num2 = int(snum2)
        

    
    res = 0
    #代表+操作符
    op_flag = 0
    
    
    
    for i in range(0, lenth-1):
        if(src_mul[i] == '−'): 
            op_flag =  1
            break
    

    
    
    # + x = y
    if(src_mul[0] == ' '):
        if(op_flag == 0):
            res = num2 - num1
        elif(op_flag == 1):
            res = num1 + num2
    
    
    #  x + y =
    elif(src_mul[lenth-1] == ' ' ):
        if(op_flag == 0):
            res = num1 + num2
        elif(op_flag == 1):
            res = num1 - num2
            
    #  x + = y
    else:
        if(op_flag == 0):
            res = num2 - num1
        elif(op_flag == 1):
            res = num1 - num2
        
    
    if(op_flag == 1):
        print("-")
    else:
        print("+")
    
    print(num1)
    print(num2)
    
    
    print(res)
    
    
    
    
    driver.find_element_by_xpath('//*[@id="user_login"]').send_keys("# 登录名") # 登录名
    
    driver.find_element_by_xpath('//*[@id="user_pass"]').send_keys("#密码") #密码
    
    
    driver.find_element_by_xpath('//*[@id="mc-input"]').send_keys(res)
    
    
    driver.find_element_by_xpath('//*[@id="wp-submit"]').click()
    
    
    driver.find_element_by_xpath('//*[@id="menu-item-153"]/a').click()
    time.sleep(1)
    result = driver.page_source
    
    fo = open("res.txt","w",encoding="utf-8")
    for i in range(0,55):
        driver.find_element_by_xpath('//*[@id="pager"]/ul/li[14]').click()    
        time.sleep(3)
        fo.write( driver.page_source.encode("gbk", 'ignore').decode("gbk", "ignore") )
        #result += driver.page_source
   # print(result)
    
   
    #it = re.finditer(r"https://pan.baidu.com[^/<]+",result)
    
    #print(it.group())
   
   
 
    # 关闭打开的文件
    fo.close()
    
#    driver.quit()