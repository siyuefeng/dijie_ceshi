#coding:utf-8;
import random
from pages.main_page import MainPage
from time import sleep



class ScenicPage(MainPage):
    """
    供应商管理下的景区管理
    """
    #定位符
    MANAGE_SCENIC = 'x, html/body/div[1]/div[1]/div/ul/li[1]/ul/li[4]/a'   #景区管理
    ADD_SCENIC = 'x, html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/button[1]' #添加景区
    ADD_BENDI = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[1]/div/div/div/label[1]'   #景区类型


    SCENIC_NAME = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[1]/div/div[1]/input'
    SCENIC_FORM = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[%d]/div/div/input'  #表单
    XIALA = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[2]/div/div/div[1]/span[1]'   #下拉框
    JIBIE = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[2]/div/div/div[2]/ul[2]/li'      #景区级别
    SCENIC_INTRODUCTION = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[4]/div/div/div[2]'   #景区介绍
    IS_JINYONG = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[9]/div/div/label[1]'   #是否禁用

    ADD_SUPPLY = 'l, 添加'
    SUPPLY_LIST = 's, .ivu-table-cell>div>span'
    QUEREN = 'x, html/body/div[3]/div[2]/div/div/div[3]/p/button'

    JIESUAN_WAY = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[10]/div/div[%d]/div/div[1]/div[1]/label' #结算方式
    HOUFAN01 = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[10]/div/div[%d]/div/div[2]/input[1]'
    HOUFAN02 = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[10]/div/div[%d]/div/div[2]/input[2]'
    PIAOXING = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[10]/div/div[%d]/table/tbody/tr[2]/td[1]/div/input'
    MENSHIJIA = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[10]/div/div[%d]/table/tbody/tr[2]/td[2]/div/input'
    CAIGOUJIA = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[10]/div/div[%d]/table/tbody/tr[2]/td[3]/div/input'
    BEIZHU = 'x, html/body/div[1]/div[2]/div/div[2]/div/form[2]/div[10]/div/div[%d]/table/tbody/tr[2]/td[4]/div/input'

    SUBMIT = 's, .btn.btn-confirm.ivu-btn.ivu-btn-primary'
    LIST_FIRST = 'x, html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/div/a'



    def add_scenic(self, scenic_dict):
        """
        添加/编辑景区
        :return:
        """
        self.base_driver.click(self.MANAGE_SCENIC)
        sleep(2)
        self.base_driver.click(self.ADD_SCENIC)
        sleep(3)
        ran = random.randint(0, 0)
        if ran == 0:
            self.base_driver.choose_box(self.ADD_BENDI)
            self.base_driver.type(self.SCENIC_NAME, scenic_dict["name"])
            self.base_driver.click(self.XIALA)
            sleep(2)
            self.base_driver.choose_box(self.JIBIE)
            sleep(3)
            self.base_driver.type(self.SCENIC_FORM % 3, scenic_dict['detail_city'])
            self.base_driver.type(self.SCENIC_INTRODUCTION, scenic_dict["introduction"])
            self.base_driver.type(self.SCENIC_FORM % 5, scenic_dict['responsible'])
            self.base_driver.type(self.SCENIC_FORM % 6, scenic_dict['res_phone'])
            self.base_driver.type(self.SCENIC_FORM % 7, scenic_dict['contact'])
            self.base_driver.type(self.SCENIC_FORM % 8, scenic_dict['contact_phone'])
            self.base_driver.choose_box(self.IS_JINYONG)

    def choose_supply(self,list):
        """
        选择供应商
        :return:
        """
        choose_text = []
        for i in (1, 3):
            self.base_driver.click(self.ADD_SUPPLY)
            sleep(3)
            text = self.base_driver.choose_box(self.SUPPLY_LIST)
            choose_text.append(text)
            self.base_driver.click(self.QUEREN)
            sleep(3)
            self.base_driver.click('l,' + choose_text[i-1])
            sleep(1)
            self.base_driver.choose_box(self.JIESUAN_WAY)
            self.base_driver.type(self.HOUFAN01 % (i+1), list[0])
            self.base_driver.type(self.HOUFAN02 % (i+1), list[1])
            sleep(1)
            self.base_driver.type(self.PIAOXING % (i+1), list[2])
            self.base_driver.type(self.MENSHIJIA % (i+1), list[3])
            self.base_driver.type(self.CAIGOUJIA % (i+1), list[4])
            self.base_driver.type(self.BEIZHU % (i+1), list[5])
        return choose_text



    def submit_and_yanzheng(self):
        self.base_driver.click(self.SUBMIT)
        sleep(6)
        ele = self.base_driver.get_text(self.LIST_FIRST)
        return ele













