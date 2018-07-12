#coding:utf-8;
from pages.main_page import MainPage
from time import sleep


class SupplyPage(MainPage):
    """
    左侧菜单供应商管理下的供应商
    """
    #定位符
    MANAGE_SUPPLY = 'x,//*[@id="navgation"]/ul/li[1]/ul/li[1]/a/span'
    ADD_SUPPLY = "x, /html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/button/span"  #添加供应商
    SUPPLY_FORM = "x, /html/body/div[1]/div[2]/div/div[2]/div/div/form/div[%d]/div/div/input"   #表单
    HANGYE = "x, /html/body/div[1]/div[2]/div/div[2]/div/div/form/div[3]/div/div/label"    #行业
    CITY_DIZHI = "x, /html/body/div[1]/div[2]/div/div[2]/div/div/form/div[4]/div/span/input"   #城市地址
    CITY_XIALA ="s, body > div.mod-district-box > div.search-wrap > ul > li:nth-child(1)"   #下拉选择第一个选项

    IS_JINYONG = "x, /html/body/div[1]/div[2]/div/div[2]/div/div/form/div[9]/div/div/label"   #是否禁用
    SUBMIT = "x, /html/body/div[1]/div[2]/div/div[2]/div/div/form/div[10]/div/button[2]"  #登录按钮
    LIST_FIRST = "x, /html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/\
    table/tbody/tr[1]/td[1]/div/span/a/span"  #列表中第一个元素


    SUPPLY_LISTS = 'x, /html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/table/tbody\
    /tr/td[1]/div/span/a/span'               #列表中供应商名称
    EDIT = "x,  /html/body/div[1]/div[2]/div/div[2]/div[1]/div/button[2]"    #编辑按钮
    DELETE = "x, /html/body/div[1]/div[2]/div/div[2]/div[1]/div/button[1]"   #删除按钮
    COMFIRM = "x, /html/body/div[2]/div[2]/div/div/div[3]/div/button[2]"     #确认框
    TEXT = "x, html/body/div[2]/div[2]/div/div/div[2]/div/p"





    #方法
    def add_supply(self, supply_dict):
        """
        添加供应商
        :return:
        """
        self.base_driver.click(self.MANAGE_SUPPLY)
        sleep(3)
        self.base_driver.click(self.ADD_SUPPLY)
        sleep(3)
        self.base_driver.type(self.SUPPLY_FORM % 1, supply_dict["companyname"])
        self.base_driver.type(self.SUPPLY_FORM % 2, supply_dict["nickname"])
        self.base_driver.choose_boxes(self.HANGYE)
        self.base_driver.click(self.CITY_DIZHI)
        sleep(1)
        self.base_driver.type(self.CITY_DIZHI, supply_dict["city"])   #输入城市
        sleep(1)
        self.base_driver.click(self.CITY_XIALA)
        self.base_driver.type(self.SUPPLY_FORM % 4, supply_dict["detail_address"])   #详细地址
        sleep(2)
        self.base_driver.type(self.SUPPLY_FORM % 5, supply_dict["responsible"])   #负责人
        self.base_driver.type(self.SUPPLY_FORM % 6, supply_dict["respon_phone"])   #负责人电话
        sleep(1)
        self.base_driver.type(self.SUPPLY_FORM % 7, supply_dict["contact"])   #联系人
        self.base_driver.type(self.SUPPLY_FORM % 8, supply_dict["contact_phone"])  # 联系人电话
        sleep(2)
        self.base_driver.choose_box(self.IS_JINYONG)   #随机选择禁用和启用
        self.base_driver.click(self.SUBMIT)     #提交
        sleep(3)
        element = self.base_driver.get_text(self.LIST_FIRST)    #获取列表中第一个供应商名称
        print(element)
        return element


    def edit_supply(self, Edit_dict):
        """
        获取一组供应商名称
        :return:
        """
        """进入到供应商页面"""
        self.base_driver.click(self.MANAGE_SUPPLY)
        sleep(3)
        """任选一个"""
        self.base_driver.choose_box(self.SUPPLY_LISTS)
        self.base_driver.switch_to_window_by_title("供应商详情")
        sleep(2)
        self.base_driver.click(self.EDIT)
        sleep(3)
        """输入编辑数据"""
        self.base_driver.type(self.SUPPLY_FORM % 1, Edit_dict["companyname"])
        self.base_driver.type(self.SUPPLY_FORM % 2, Edit_dict["nickname"])
        self.base_driver.type(self.SUPPLY_FORM % 4, Edit_dict["detail_address"])  # 详细地址
        self.base_driver.type(self.SUPPLY_FORM % 5, Edit_dict["responsible"])  # 负责人
        self.base_driver.type(self.SUPPLY_FORM % 6, Edit_dict["respon_phone"])  # 负责人电话
        self.base_driver.type(self.SUPPLY_FORM % 7, Edit_dict["contact"])  # 联系人
        self.base_driver.type(self.SUPPLY_FORM % 8, Edit_dict["contact_phone"])  # 联系人电话
        self.base_driver.click(self.SUBMIT)  # 提交
        sleep(3)
        title = self.base_driver.get_title()
        print(title)
        return title



    def delete_supply(self):
        """
        删除供应商,不包含供应商已提供某一类资源，不能删除的情况
        为了避免这种情框，保证supply001.csv的数据大于20条即可
        :return:
        """

        """进入到供应商页面"""
        self.base_driver.click(self.MANAGE_SUPPLY)
        sleep(3)
        """随意选择一项"""

        self.base_driver.choose_box(self.SUPPLY_LISTS)
        self.base_driver.switch_to_window_by_title("供应商详情")
        sleep(2)
        self.base_driver.click(self.DELETE)
        sleep(2)

        self.base_driver.click(self.COMFIRM)
        sleep(2)
        title = self.base_driver.get_title()
        return title



