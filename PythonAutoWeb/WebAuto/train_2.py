
# 导入selenium 库里面的webdriver 模块
from selenium import webdriver
from selenium.webdriver.support.ui import Select


from winsound import  Beep
import time






# 下面的代码指定是chrome 的驱动，注意这个driver 对象是后面自动化的入口
#  成功后返回一个WebDriver 实例对象，通过它的方法，可以控制浏览器


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")


driver.implicitly_wait(10)

# get 方法 打开指定网址
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')




# 接下来我们要在出发地选输入南京南。

#  driver找到了该元素的话，就会返回一个表示该元素的WebElement对象。
fromEle = driver.find_element_by_id('fromStationText')


# 先点击一下它，这是12306的限制，不点击不行
fromEle.click()

fromEle.clear()
fromEle.send_keys('南京南\n')

# 目的地也是一样的操作
toEle = driver.find_element_by_id('toStationText')
#这里也要点击一下
toEle.click()
toEle.clear()
toEle.send_keys('杭州东\n')

# 选择开始时间，F12 看出来 是Select,
timeSelect =  Select(driver.find_element_by_id('cc_start_time'))
timeSelect.select_by_visible_text('06:00--12:00')

# 第3个tab就是第3天
tomorrow = driver.find_element_by_css_selector('#date_range li:nth-child(3)')

# 要买票的车次
interested = [
    'G1379', 'G1377', 'D3295', 'G7393'
]

# 记录循环次数
i = 0
# 循环不断的搜索
while True:
    i += 1
    isGet = False # 设置为没有找到

    # 点击这个，就会搜索车次了
    tomorrow.click()

    # 选择2等座有票的的车次
    xpath ='//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'


    theTrains = driver.find_elements_by_xpath(xpath)

    for one in theTrains:
        name = one.text
        if name in interested:
            isGet = True
            print('***  有剩余车票 ' + name)



    if isGet:
        print('!!! 有车票了 , 主人，快来')
        Beep(1500,5000) # freqency and duration
        input() # 停在此处


    else:
        print(f'#{i}轮搜索没有找到')

    # 隔5秒钟，进行下一轮搜索，防止服务器认为是攻击
    time.sleep(5)



# 最后，driver.quit让浏览器和驱动进程一起退出
driver.quit()


