import random
import re
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select



class BoxDriver(object):
    """
    a simple demo of selenium framework tool
    """

    base_driver = None

    def __init__(self,browser):
        if browser == 'Chrome':
            driver = webdriver.Chrome()
            try:
                self.base_driver = driver
            except Exception:
                print("Chrome is not found")
        elif browser == 'Firefox':
            driver = webdriver.Firefox()
            try:
                self.base_driver = driver
            except Exception:
                print("Firefox is not found")
        else:
            print("没有可用的浏览器")

    def clear_cookies(self):
        """
        clear all cookies after driver init
        """
        self.base_driver.delete_all_cookies()


    def add_cookies(self, cookies):
        """
        Add cookie by dict
        :param cookies:
        :return:
        """
        self.base_driver.add_cookie(cookie_dict=cookies)

    def add_cookie(self, cookie_dict):
        """
        Add single cookie by dict
        添加 单个 cookie
        如果该 cookie 已经存在，就先删除后，再添加
        :param cookie_dict: 字典类型，有两个key：name 和 value
        :return:
        """
        cookie_name = cookie_dict["name"]
        cookie_value = self.base_driver.get_cookie(cookie_name)
        if cookie_value is not None:
            self.base_driver.delete_cookie(cookie_name)

        self.base_driver.add_cookie(cookie_dict)

    def refresh(self, url=None):
        """
        刷新页面
        如果 url 是空值，就刷新当前页面，否则就刷新指定页面
        :param url: 默认值是空的
        :return:
        """
        if url is None:
            self.base_driver.refresh()
        else:
            self.base_driver.get(url)

    def maximize_window(self):
        """
        最大化当前浏览器的窗口
        :return:
        """
        self.base_driver.maximize_window()

    def navigate(self, url):
        """
        打开 URL
        :param url:
        :return:
        """
        self.base_driver.get(url)

    def quit(self):
        self.base_driver.quit()

    def close_browser(self):
        self.base_driver.close()

    def locate_element(self, selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        if "," not in selector:
            return self.base_driver.find_element_by_id(selector)

        selector_by = selector.split(",")[0].strip()
        selector_value = selector.split(",")[1].strip()
        if selector_by == "i" or selector_by == 'id':
            element = self.base_driver.find_element_by_id(selector_value)
        elif selector_by == "n" or selector_by == 'name':
            element = self.base_driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.base_driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.base_driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.base_driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.base_driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            element = self.base_driver.find_element_by_xpath(selector_value)
        elif selector_by == "s" or selector_by == 'css_selector':
            element = self.base_driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def type(self, selector, text):
        """
        Operation input box.

        Usage:
        driver.type("i,el","selenium")
        """
        el = self.locate_element(selector)
        el.clear()
        el.send_keys(text)

    def click(self, selector):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("i,el")
        """
        el = self.locate_element(selector)
        el.click()

    def click_by_enter(self, selector):
        """
        It can type any text / image can be located  with ENTER key

        Usage:
        driver.click_by_enter("i,el")
        """
        el = self.locate_element(selector)
        el.send_keys(Keys.ENTER)

    def select_by_index(self, selector, index):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self.locate_element(selector)
        Select(el).select_by_index(index)

    def select_by_visible_text(self, selector, text):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self.locate_element(selector)
        Select(el).select_by_visible_text(text)

    def select_by_value(self, selector, value):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self.locate_element(selector)
        Select(el).select_by_value(value)

    def click_by_text(self, text):
        """
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        """
        self.locate_element('p,' + text).click()

    def submit(self, selector):
        """
        Submit the specified form.

        Usage:
        driver.submit("i,el")
        """
        el = self.locate_element(selector)
        el.submit()

    def execute_js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.base_driver.execute_script(script)

    def get_attribute(self, selector, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("i,el","type")
        """
        el = self.locate_element(selector)
        return el.get_attribute(attribute)

    def get_text(self, selector):
        """
        Get element text information.

        Usage:
        driver.get_text("i,el")
        """
        el = self.locate_element(selector)
        return el.text

    def get_display(self, selector):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("i,el")
        """
        el = self.locate_element(selector)
        return el.is_displayed()

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self.base_driver.title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        return self.base_driver.current_url

    def accept_alert(self):
        '''
            Accept warning box.
            Usage:
            driver.accept_alert()
            '''
        ele = self.base_driver.switch_to.alert()
        ele.accept()

    def get_alert_text(self):
        ele = self.base_driver.switch_to.alert()
        return ele.text

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismissAlert()
        '''
        self.base_driver.switch_to.alert.dismiss()



    def implicitly_wait(self, secs):
        """
        Implicitly wait. All elements on the page.

        Usage:
        driver.implicitly_wait(10)
        """
        self.base_driver.implicitly_wait(secs)

    def switch_to_frame(self, selector):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("i,el")
        """
        el = self.locate_element(selector)
        self.base_driver.switch_to.frame(el)

    def switch_to_default(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        self.base_driver.switch_to.default_content()

    def switch_to_window_by_title(self, title):
        """
        通过标题来切换窗口
        :param title:
        :return:
        """
        for handle in self.base_driver.window_handles:
            self.base_driver.switch_to.window(handle)
            if self.base_driver.title == title:
                break
            self.base_driver.switch_to.window(handle)



    def open_new_window(self, selector):
        '''
        Open the new window and switch the handle to the newly opened window.
        Usage:
        driver.open_new_window()
        '''
        original_windows = self.base_driver.current_window_handle
        el = self.locate_element(selector)
        el.click()
        all_handles = self.base_driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.base_driver._switch_to.window(handle)


    def wait(self, seconds):
        time.sleep(seconds)

    def move_to(self, selector):
        """
        to move mouse pointer to selector
        :param selector:
        :return:
        """
        el = self.locate_element(selector)
        ActionChains(self.base_driver).move_to_element(el).perform()

    def right_click(self, selector):
        """
        to click the selector by the right button of mouse
        :param selector:
        :return:
        """
        el = self.locate_element(selector)
        ActionChains(self.base_driver).context_click(el).perform()

    def locate_elements(self, selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        if ',' not in selector:
            return self.base_driver.find_elements_by_id(selector)

        selector_by = selector.split(',')[0].strip()
        selector_value = selector.split(',')[1].strip()

        if selector_by == "i" or selector_by == 'id':
            elements = self.base_driver.find_elements_by_id(selector_value)
        elif selector_by == "n" or selector_by == 'name':
            elements = self.base_driver.find_elements_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            elements = self.base_driver.find_elements_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            elements = self.base_driver.find_elements_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            elements = self.base_driver.find_elements_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            elements = self.base_driver.find_elements_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            elements = self.base_driver.find_elements_by_xpath(selector_value)
        elif selector_by == "s" or selector_by == 'css_selector':
            elements = self.base_driver.find_elements_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return elements

    def count_elements(self, selector):
        els = self.locate_elements(selector)
        return len(els)

    def save_snapshot(self, file_name):
        """
        save screen snapshot
        :param file_name: the image file name and path
        :return:
        """
        driver = self.base_driver
        driver.save_screenshot(file_name)

    def is_selected(self, selector):
        """
        to return the selected status of an WebElement
        :param selector: selector to locate
        :return: True False
        """
        el = self.locate_element(selector)
        return el.is_selected()


    def choose_boxes(self,selector):
        """
        获取一组元素，并且依次选择其中的选项（全选）
        :return:
        """
        boxes = self.locate_elements(selector)
        for i in boxes:
            i.click()


    def choose_box(self,selectors):
        """
        单选框，获取这一组单选框的地址，从中随意选择一个
        :return:
        """
        eles = self.locate_elements(selectors)
        m = len(eles)
        n = random.randint(0, m-1)   #产生随机整数
        eles[n].click()
        sleep(3)
        return eles[n].text


    def choose_list(self,selectors,n):
        """
        获取列表中的一组元素，随机选择其中的一部分元素
        :return:
        """
        choose_elements = []
        eles = self.locate_elements(selectors)
        m = len(eles)
        ran = [random.randint(0, m) for _ in range(n)]
        for i in ran:
            element = eles[i]
            choose_elements.append(element)
        return choose_elements


    def jiequ_int(self,st,m,n):
        """
        str:字符串
        m,n:截取的开始位和结束位，最小为0
        从字符串中截取出数字，并变成数值型
        :return:返回截取得到的数字
        """
        BB = str(st)
        jiequ = BB[m:n]
        print(jiequ)
        cc = int(jiequ)
        return cc

    def choose_city(self, selector, city, selectors):
        """
        针对系统的城市插件，包装函数来选择城市
        输入城市名，在产生别的下拉城市名选择第一个
        :return:
        """
        el = self.locate_element(selector)
        el.clear()
        el.send_keys(city)
        sleep(4)
        ele = self.locate_elements(selectors)
        if len(ele) > 1:
            ele[1].click()
        else:
            print("没有这个城市")


    def outer():
        def decro(func):
            def inner(*args, **kwargs):
                ran = random.randint(0, 2)
                i = 0
                if ran == 2:
                    for m in (0, 5):
                        func(*args, **kwargs)
                        i = i + 1
                        if i > 3:
                            break
                elif ran == 1:
                    func(*args, **kwargs)
                elif ran == 0:
                    pass
                return func(*args, **kwargs)
            return inner
        return decro
