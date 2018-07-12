#coding:utf-8;
import random
from pages.main_page import MainPage
from time import sleep

class RestaurantPage(MainPage):

    """
    供应商管理下的餐厅管理
    """
    #定位符
    MANAGE_RES = 'x, html/body/div[1]/div[1]/div/ul/li[1]/ul/li[3]/a/span'     #餐厅管理
    ADD_RES = 'x, html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/button[1]'      #添加餐厅
    RES_NAME = 'x, html/body/div[1]/div[2]/div/div[2]/div/form/div/div[1]/div[1]/div/div[1]/input'  #餐厅名称
    DIZHI = 's, .destination-input'    #餐厅地址
    CITI_LIST_ABCD = 'x, html/body/div[3]/div[1]/ul/li[1]'   #城市下拉列表
    CITI_LIST = 'x, .city-item'
    FORM_LIST = 'x, html/body/div[1]/div[2]/div/div[2]/div/form/div/div[1]/div[%d]/div/div/input'
    IS_JINYONG = 'x, html/body/div[1]/div[2]/div/div[2]/div/form/div/div[1]/div[7]/div/div/label'

    TIANJIA  = 'c, add-model'   #添加供应商
    SUPPLY_RES = 's, .brLine-column>p>span'
    QUEREN = 'x, /html/body/div[2]/div[2]/div/div/div[3]/div/button'    #弹窗确认键
    BIAOTOU = 's, .apply-item.position-r'  #点击表头
    BIAOTOU01 = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[1]/div/div[3]'
    JIESUAN_WAY = 's, .ivu-radio-wrapper.ivu-radio-group-item' #结算方式
    QIANDAN  = 'l, 签单'
    XIANFU  = 'l, 现付'
    YUFU = 'l, 预付'
    HOUFAN1 = 'x, html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div[2]/input[1]'   #后返%
    HOUFAN2 = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div[2]/input[2]'   #后返人头
    ADD_LEIXING = 'c, fun-plus-one'
    CANXING = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div/input'
    #房型
    MENSHI = 'x, html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/input'
    #门市价
    CAIGOU = 'x,html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/input'
    #采购价
    BEIZHU = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/table/tbody/tr[2]/td[4]/div/input'
    #备注
    SUBMIT = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[3]/div/button[2]'
    LIST_FIRST = 'x, /html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/table/tbody\
    /tr[1]/td[1]/div/span/a/span'     #列表中第一个名称

    RES_LISTS = "s,.ohellipsis.disib"   #列表中餐厅名称
    DELETE = 's, .mr14.ivu-btn.ivu-btn-danger'   #删除
    COMFIRM = 's, .ivu-btn.ivu-btn-error'   #确认



    def add_res(self, dict_res):
        """
        添加|编辑餐厅
        :return:
        """
        self.base_driver.click(self.MANAGE_RES)
        sleep(3)
        self.base_driver.click(self.ADD_RES)
        sleep(3)
        self.base_driver.type(self.RES_NAME, dict_res['name'])
        # self.base_driver.type(self.DIZHI,)
        # sleep(3)
        # self.base_driver.click(self.CITI_LIST_ABCD)
        # self.base_driver.choose_box(self.CITI_LIST)
        sleep(1)
        self.base_driver.type(self.FORM_LIST % 2, dict_res['detail_dizhi'])
        self.base_driver.type(self.FORM_LIST % 3, dict_res['responsiple'])
        self.base_driver.type(self.FORM_LIST % 4, dict_res['res_phone'])
        self.base_driver.type(self.FORM_LIST % 5, dict_res['contact'])
        self.base_driver.type(self.FORM_LIST % 6, dict_res['cont_phone'])
        sleep(1)
        self.base_driver.choose_box(self.IS_JINYONG)


    def outer():
        """
        装饰器，被装饰的函数放在里面会随机的被执行1/2/3次
        :return:
        """
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


    # @outer()
    def add_res_supply(self):
        """
        添加餐厅供应商
        :return:
        """
        self.base_driver.click(self.TIANJIA)
        sleep(4)
        self.base_driver.choose_box(self.SUPPLY_RES)
        self.base_driver.click(self.QUEREN)
        sleep(3)


    def res_supply(self, list):
        """
        内层嵌套，添加供应商
        :param list:
        :return:
        """
        self.base_driver.choose_box(self.JIESUAN_WAY)
        self.base_driver.type(self.HOUFAN1, list[0])
        self.base_driver.type(self.HOUFAN2, list[1])
        sleep(1)
        self.base_driver.click(self.ADD_LEIXING)
        sleep(1)
        self.base_driver.type(self.CANXING, list[2])
        self.base_driver.type(self.MENSHI, list[3])
        self.base_driver.type(self.CAIGOU, list[4])
        self.base_driver.type(self.BEIZHU, list[5])




    def submit_and_yanzheng(self):
        self.base_driver.click(self.SUBMIT)
        sleep(6)
        ele = self.base_driver.get_text(self.LIST_FIRST)
        return ele


    def delete_res(self):
        """
        删除餐厅
        :return:
        """
        self.base_driver.click(self.MANAGE_RES)
        sleep(3)
        """任选一个"""
        self.base_driver.choose_box(self.RES_LISTS)
        self.base_driver.switch_to_window_by_title("酒店详情")
        sleep(2)
        self.base_driver.click(self.DELETE)
        sleep(3)
        self.base_driver.click(self.COMFIRM)
        sleep(2)
        title = self.base_driver.get_title()
        return title








