import random
import unittest
from base.box_driver import BoxDriver
from base.csv_helper import CsvHelper
from pages.sub_business_page.scenic_page import ScenicPage


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
        self.base_driver = BoxDriver("Firefox")
        self.base_url = 'http://t.dj.vding.wang'
        self.Scenic_page = ScenicPage(self.base_driver, self.base_url)
        self.login_dict = {
            "name": "13974975623",
            "password": "123456"
        }
        self.company = "南京哪玩国际旅行社有限公司"
        self.moudle = "business"
        self.first_menu = "supplier_management"
        self.list1 = [0, 1, 'piao01', '20', '15', 'hjkhfdsjkhj']
        self.list2 = [1, 0, 'piao02', '40', '28', '这三个会又去']
        self.list3 = [2, 5, 'piao03', '30', '20', '这个不是这样的ty']


    def tearDown(self):
        """
        测试清理操作
        :return:
        """
        # self.base_driver.quit()


    def test_res01(self):
        """
        测试添加供应商
        :return:
        """
        self.Scenic_page.open()
        self.Scenic_page.login(self.login_dict['name'], self.login_dict['password'])
        self.Scenic_page.change_company(self.company)
        self.Scenic_page.select_moudle(self.moudle)
        self.Scenic_page.select_first_menu(self.first_menu)
        csv_helper = CsvHelper()
        csv_data = csv_helper.read_file("../datas/scenic001.csv")
        current_header = True
        for row in csv_data:
            if current_header:
                current_header = False
                continue
            scenic_dict = {
                'name': row[0],
                'detail_city': row[1],
                'introduction': row[2],
                'responsible': row[3],
                'res_phone': row[4],
                'contact': row[5],
                'contact_phone': row[6]
            }
            self.Scenic_page.add_scenic(scenic_dict)
            m = random.randint(1, 3)
            if m == 1:
                self.Scenic_page.choose_supply(self.list1)
            elif m == 2:
                self.Scenic_page.choose_supply(self.list2)
            elif m == 3:
                self.Scenic_page.choose_supply(self.list3)
            else:
                print("没有执行添加供应商")

            res_name = self.Scenic_page.submit_and_yanzheng()
            self.assertEqual(scenic_dict['name'], res_name, '添加酒店失败')

        csv_helper.close()
        self.Scenic_page.logout()


if __name__ == "__main__":
    unittest.main()

