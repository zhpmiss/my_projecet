# coding:utf-8

"""
author:*成相
filename:selenium_qqGroupSpider.py
time:2017-01-27
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.select import Select
import re
#使用进程池
from multiprocessing import Pool

# 登录操作
def log_in(username, password):
    driver = webdriver.Chrome()
    url = 'http://qun.qq.com/manage.html'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    sleep(2)
    driver.find_element_by_link_text('登录').click()
    sleep(1)
    driver.switch_to.frame('login_frame')
    driver.find_element_by_id('switcher_plogin').click()
    driver.find_element_by_id('u').clear()
    driver.find_element_by_id('u').send_keys(username)
    sleep(2)
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys(password)
    sleep(3)
    driver.find_element_by_id('login_button').click()
    driver.switch_to.default_content()
    sleep(1)
    try:
        # 定位群管理
        driver.find_element_by_xpath('/html/body/div[3]/ul/li[2]/a').click()

    except:
        print('验证码错误')
        driver.quit()
    handle = driver.window_handles
    driver.switch_to.window(handle[1])
    # 群总数定位
    try:
        find_group_number = driver.find_elements_by_css_selector('div.my-all-group>h4')
    except:
        print('无信息')
        driver.quit()

    #群分类（我创建的群/我加入的群）
    if len(find_group_number) == 2:
        my_group = driver.find_elements_by_css_selector('div.my-all-group>h4')[0].text
        my_group_1 = re.search('\d+', my_group).group(0)
        no_group = driver.find_elements_by_css_selector('div.my-all-group>h4')[1].text
        no_group_1 = re.search('\d+', no_group).group(0)
        all_group = int(my_group_1) + int(no_group_1)
    else:
        group_u = driver.find_elements_by_css_selector('div.my-all-group>h4')[0].text
        all_group = re.search('\d+', group_u).group(0)
    for x in range(int(all_group)):
        group_list = driver.find_elements_by_css_selector('ul.my-group-list>li')
        switch_group(driver,group_list[x])
    driver.quit()


# 切换群
def switch_group(driver,group):
    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div[1]/input').clear()
    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div[1]/input').send_keys(group.text)
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div[2]/ul/li').click()
    memeber_information(driver)
    driver.find_element_by_link_text('[切换QQ群]').click()


# 成员信息
def memeber_information(driver):
    memebers_dic = {}
    # 成员定位
    sleep(2)
    all_memeber = driver.find_element_by_id('groupMemberNum').text
    while True:
        memeber = driver.find_elements_by_class_name('mb')
        sleep(1)
        js = "window.scrollBy(0,9999999)"
        # js = "var q=document.documentElement.scrollTop=9999999"
        driver.execute_script(js)
        if len(memeber) == int(all_memeber):
            break
    for i in range(len(memeber)):
        name = driver.find_elements_by_css_selector('td.td-user-nick>span')
        card = driver.find_elements_by_css_selector('td.td-card>span')
        qq = driver.find_elements_by_css_selector('#groupMember tr.mb>td:nth-child(5)')
        memebers_dic['name'] = name[i].text
        memebers_dic['card'] = card[i].text
        memebers_dic['qq'] = qq[i].text
        print(memebers_dic)



# 文件读取
def file_read(filename):
    #创建进程池，进程数4个
    pool=Pool(4)
    with open(filename, 'r+', encoding='utf-8') as f:
        qq_1 = f.readlines()
        for x in qq_1:
            if x != '\n':
                qq_2 = re.match('(\d+)----(.*?)----', x)
                #添加子进程，args代入是进程函数的参数
                pool.apply_async(log_in,args=(qq_2.group(1),qq_2.group(2))) 
        print ('等待所有子进程执行……')
        pool.close()
        pool.join()
        print("子进程执行完毕")
# 多线程实现


if __name__ == "__main__":
    #chromeOptions = webdriver.ChromeOptions()
    # 设置代理
    #chromeOptions.add_argument("--proxy-server=http://127.0.0.1:1080")
    #driver = webdriver.Chrome(chrome_options=chromeOptions)
    file_read('30.txt')  # ‘x’参数指的是qq群组名和密码文件

