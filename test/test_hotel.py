import random
import unittest
from base.box_driver import BoxDriver
from base.csv_helper import CsvHelper
from pages.sub_business_page.hotel_page import HotelPage



class TestHotel(unittest.TestCase):
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
        self.hotel_page = HotelPage(self.base_driver, self.base_url)
        self.login_dict = {
            "name": "18641198447",
            "password": "123456"
        }
        self.company = "南京哪玩国际旅行社有限公司"
        self.moudle = "business"
        self.first_menu = "supplier_management"
        self.list1 = [0, 1, '大房', '120', '100', 'hjkhfdsjkhj']
        self.list2 = [1, 0, '双人间', '150', '120', '这三个会又去']
        self.list3 = [2, 5, '单人间', '80', '75', '这个不是这样的ty']


    def tearDown(self):
        """
        测试清理操作
        :return:
        """
        self.base_driver.quit()


    def test_hotel01(self):
        """
        测试添加供应商
        :return:
        """
        self.hotel_page.open()
        self.hotel_page.login(self.login_dict['name'], self.login_dict['password'])
        self.hotel_page.change_company(self.company)
        self.hotel_page.select_moudle(self.moudle)
        self.hotel_page.select_first_menu(self.first_menu)
        csv_helper = CsvHelper()
        csv_data = csv_helper.read_file("../datas/hotel001.csv")
        current_is_header = True
        for row in csv_data:
            if current_is_header:
                current_is_header = False
                continue
            dict_hotel = {
                'name': row[0],
                'bei_zhu': row[1],
                'city': row[2],
                'city_detail': row[3],
                'responsible': row[4],
                'res_phone': row[5],
                'contact': row[6],
                'con_phone': row[7]
            }
            self.hotel_page.add_hotel(dict_hotel)
            m = random.randint(1, 3)
            if m == 1:
                self.hotel_page.add_hotel_supply(self.list1)
            elif m == 2:
                self.hotel_page.add_hotel_supply(self.list2)
            elif m == 3:
                self.hotel_page.add_hotel_supply(self.list3)
            else:
                print("没有执行添加供应商")

            hotel_name = self.hotel_page.submit_and_yanzheng()
            self.assertEqual(dict_hotel['name'], hotel_name, '添加酒店失败')

        csv_helper.close()
        self.hotel_page.logout()


    def test_hotel02(self):
        """
        删除酒店
        :return:
        """
        self.hotel_page.open()
        self.hotel_page.login(self.login_dict['name'], self.login_dict['password'])
        self.hotel_page.change_company(self.company)
        self.hotel_page.select_moudle(self.moudle)
        self.hotel_page.select_first_menu(self.first_menu)
        list_A = [0, 1, 2]
        for i in list_A:
            title = self.hotel_page.delete_hotel()
            self.assertEqual(title, "酒店管理", "删除酒店失败")
        self.hotel_page.logout()



if __name__ == "__main__":
    unittest.main()












