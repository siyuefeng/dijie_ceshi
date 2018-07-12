import random
import unittest
from base.box_driver import BoxDriver
from base.csv_helper import CsvHelper
from pages.sub_business_page.restaurant_page import RestaurantPage


class TestRes(unittest.TestCase):
    """
    用例 supply_test_01, 对供应商管理中的供应商的测试
    """
    base_driver = None
    base_url = None
    login_dict = None
    company =None
    first_menu =None
    list1 = None
    list2 = None
    list3 = None

    def setUp(self):
        """
        测试前置条件
        :return:
        """
        self.base_driver = BoxDriver("Chrome")
        self.base_url = 'http://t.dj.vding.wang'
        self.restaurant_page = RestaurantPage(self.base_driver, self.base_url)
        self.login_dict = {
            "name": "13974975623",
            "password": "123456"
        }
        self.company = "南京哪玩国际旅行社有限公司"
        self.moudle = "business"
        self.first_menu = "supplier_management"
        self.list1 = [0, 1, '早餐', '20', '15', 'hjkhfdsjkhj']
        self.list2 = [1, 0, '午餐', '40', '28', '这三个会又去']
        self.list3 = [2, 5, '晚餐', '30', '20', '这个不是这样的ty']


    def tearDown(self):
        """
        测试清理操作
        :return:
        """
        self.base_driver.quit()


    def test_res01(self):
        """
        测试添加供应商
        :return:
        """
        self.restaurant_page.open()
        self.restaurant_page.login(self.login_dict['name'], self.login_dict['password'])
        self.restaurant_page.change_company(self.company)
        self.restaurant_page.select_moudle(self.moudle)
        self.restaurant_page.select_first_menu(self.first_menu)
        csv_helper = CsvHelper()
        csv_data = csv_helper.read_file("../datas/res001.csv")
        current_header = True
        for row in csv_data:
            if current_header:
                current_header = False
                continue
            dict_res = {
                'name': row[0],
                'detail_dizhi': row[1],
                'responsiple': row[2],
                'res_phone': row[3],
                'contact': row[4],
                'cont_phone': row[5]
            }
            self.restaurant_page.add_res(dict_res)
            self.restaurant_page.add_res_supply()
            m = random.randint(1, 3)
            if m == 1:
                self.restaurant_page.res_supply(self.list1)
            elif m == 2:
                self.restaurant_page.res_supply(self.list2)
            elif m == 3:
                self.restaurant_page.res_supply(self.list3)
            else:
                print("没有执行添加供应商")

            res_name = self.restaurant_page.submit_and_yanzheng()
            self.assertEqual(dict_res['name'], res_name, '添加酒店失败')

        csv_helper.close()
        self.restaurant_page.logout()


    def test_res002(self):
        """
        删除餐厅
        :return:
        """
        self.restaurant_page.open()
        self.restaurant_page.login(self.login_dict['name'], self.login_dict['password'])
        self.restaurant_page.change_company(self.company)
        self.restaurant_page.select_moudle(self.moudle)
        self.restaurant_page.select_first_menu(self.first_menu)
        list_A = [0, 1, 2]
        for i in list_A:
            title = self.restaurant_page.delete_res()
            self.assertEqual(title, "餐厅管理", "删除餐厅失败")
        self.restaurant_page.logout()


if __name__ == "__main__":
    unittest.main()


