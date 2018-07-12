#coding:utf-8;
import random
from pages.main_page import MainPage
from time import sleep


class HotelPage(MainPage):
    """
    供应商管理下的酒店管理
    """
    #定位符
    MANAGE_HOTEL = 'x, //*[@id="navgation"]/ul/li[1]/ul/li[2]/a/span'   #二级菜单酒店
    ADD_HOTEL = 's, .fr.c-white.mid.ivu-btn.ivu-btn-primary'    #添加酒店
    CHOOSE_XIALA = "x, html/body/div[1]/div[2]/div/div[2]/div/form/div/div[1]/div[2]/div/div[1]/div[1]/span[1]" # 点击下拉
    XINGJI = "x, html/body/div[1]/div[2]/div/div[2]/div/form/div/div[1]/div[2]/div/div[1]/div[2]/ul[2]/li"   #星级
    HOTEL_FORM_01 = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[1]/div[1]/div/div[%d]/input'
    SASBEIZHU = "x, html/body/div[1]/div[2]/div/div[2]/div/form/div/div[1]/div[2]/div/div[2]/input"
    DESTINATION = 's, .destination-input'
    CITY  = 's, .destination-input'
    CITY01 = 's, .search-item'
    HOTEL_FORM_02 = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[1]/div[%d]/div/div/input'
    IS_JINGYONG = 'x ,/html/body/div[1]/div[2]/div/div[2]/div/form/div/div[1]/div[8]/div/div/label'   #是否禁用
    TIANJIA  = 'c, add-model'   #添加供应商
    SUPPLY_HOTEL = 's, .brLine-column>p>span'
    QUEREN = 'x, /html/body/div[2]/div[2]/div/div/div[3]/div/button'    #弹窗确认键
    JIESUAN_WAY = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/label' #结算方式
    HOUFAN1 = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div[2]/input[1]'   #后返%
    HOUFAN2 = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div[2]/input[2]'   #后返人头
    ADD_LEIXING = 'c, fun-plus-one'
    FANGXING = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div/input'
    #房型
    MENSHI = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/input'
    #门市价
    CAIGOU = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/input'
    #采购价
    BEIZHU = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/div[2]/table/tbody/tr[2]/td[4]/div/input'
    #备注
    SUBMIT = 'x, /html/body/div[1]/div[2]/div/div[2]/div/form/div/div[3]/div/button[2]'
    LIST_FIRST = 'x, /html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/table/tbody\
    /tr[1]/td[1]/div/span/a/span'     #列表中第一个名称

    HOTEL_LISTS = 's, .ohellipsis.disib'
    EDIT = "s, .ivu-btn.ivu-btn-primary"
    DELETE = 's, .mr14.ivu-btn.ivu-btn-danger'
    COMFIRM = 's, .ivu-btn.ivu-btn-error'



    def add_hotel(self, dict_hotel):
        """
        添加酒店
        :return:
        """
        self.base_driver.click(self.MANAGE_HOTEL)
        sleep(2)
        self.base_driver.click(self.ADD_HOTEL)
        sleep(2)
        self.base_driver.type(self.HOTEL_FORM_01 % 1, dict_hotel['name'])
        sleep(1)
        self.base_driver.click(self.CHOOSE_XIALA)     #点击下拉框
        sleep(3)
        self.base_driver.choose_box(self.XINGJI)      #选择星级
        sleep(1)

        # self.base_driver.choose_city(self.CITY, dict_hotel['city'], self.CITY01)
        self.base_driver.type(self.HOTEL_FORM_02 % 3, dict_hotel['city_detail'])
        sleep(1)
        self.base_driver.type(self.HOTEL_FORM_02 % 4, dict_hotel['responsible'])
        self.base_driver.type(self.HOTEL_FORM_02 % 5, dict_hotel['res_phone'])
        sleep(1)
        self.base_driver.type(self.HOTEL_FORM_02 % 6, dict_hotel['contact'])
        self.base_driver.type(self.HOTEL_FORM_02 % 7, dict_hotel['con_phone'])
        self.base_driver.choose_box(self.IS_JINGYONG)


    def add_hotel_supply(self, list):
        self.base_driver.click(self.TIANJIA)
        sleep(4)
        self.base_driver.choose_box(self.SUPPLY_HOTEL)
        self.base_driver.click(self.QUEREN)
        sleep(3)
        self.base_driver.choose_box(self.JIESUAN_WAY)
        self.base_driver.type(self.HOUFAN1,  list[0])
        self.base_driver.type(self.HOUFAN2, list[1])
        sleep(1)
        self.base_driver.click(self.ADD_LEIXING)
        sleep(1)
        self.base_driver.type(self.FANGXING, list[2])
        self.base_driver.type(self.MENSHI, list[3])
        self.base_driver.type(self.CAIGOU, list[4])
        self.base_driver.type(self.BEIZHU,list[5])



    def submit_and_yanzheng(self):
        self.base_driver.click(self.SUBMIT)
        sleep(6)
        ele = self.base_driver.get_text(self.LIST_FIRST)
        return ele


    def edit_hotel(self, dict_hotel):
        """
        编辑酒店

        :return:
        """
        self.base_driver.click(self.MANAGE_HOTEL)
        sleep(3)
        """任选一个"""
        self.base_driver.choose_box(self.HOTEL_LISTS)
        self.base_driver.switch_to_window_by_title("酒店详情")
        sleep(2)
        self.base_driver.click(self.EDIT)
        sleep(3)
        self.base_driver.type(self.HOTEL_FORM_01 % 1, dict_hotel['name'])
        sleep(1)
        self.base_driver.click(self.CHOOSE_XIALA)     #点击下拉框
        sleep(3)
        self.base_driver.choose_box(self.XINGJI)      #选择星级
        sleep(1)
        # self.base_driver.choose_city(self.CITY, dict_hotel['city'], self.CITY01)
        self.base_driver.type(self.HOTEL_FORM_02 % 3, dict_hotel['city_detail'])
        sleep(1)
        self.base_driver.type(self.HOTEL_FORM_02 % 4, dict_hotel['responsible'])
        self.base_driver.type(self.HOTEL_FORM_02 % 5, dict_hotel['res_phone'])
        sleep(1)
        self.base_driver.type(self.HOTEL_FORM_02 % 6, dict_hotel['contact'])
        self.base_driver.type(self.HOTEL_FORM_02 % 7, dict_hotel['con_phone'])
        self.base_driver.choose_box(self.IS_JINGYONG)



    def delete_hotel(self):
        """
        删除酒店
        :return:
        """

        self.base_driver.click(self.MANAGE_HOTEL)
        sleep(3)
        """任选一个"""
        self.base_driver.choose_box(self.HOTEL_LISTS)
        self.base_driver.switch_to_window_by_title("酒店详情")
        sleep(2)
        self.base_driver.click(self.DELETE)
        sleep(3)
        self.base_driver.click(self.COMFIRM)
        sleep(2)
        title = self.base_driver.get_title()
        return title


