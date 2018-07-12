import unittest
from base.box_driver import BoxDriver
from base.csv_helper import CsvHelper
from pages.sub_business_page.supply_page import SupplyPage


class TestSupply(unittest.TestCase):
    """
    用例 supply_test_01, 对供应商管理中的供应商的测试
    """
    base_driver = None
    base_url = None
    login_dict = None
    company =None
    first_menu =None


    def setUp(self):
        """
        测试前置条件
        :return:
        """
        self.base_driver = BoxDriver("Chrome")
        self.base_url = 'http://t.dj.vding.wang'
        self.supply_page = SupplyPage(self.base_driver, self.base_url)
        self.login_dict = {
            "name": "13889219395",
            "password": "123456"
        }
        self.company = "广州岭南国际旅行社有限公司"
        self.moudle = "business"
        self.first_menu = "supplier_management"


    def tearDown(self):
        """
        测试清理操作
        :return:
        """
        self.base_driver.quit()


    def test_supply01(self):
        """
        测试添加/编辑供应商
        :return:
        """
        self.supply_page.open()
        self.supply_page.login(self.login_dict["name"],self.login_dict["password"])
        self.supply_page.change_company(self.company)
        self.supply_page.select_moudle(self.moudle)
        self.supply_page.select_first_menu(self.first_menu)
        csv_helper = CsvHelper()
        csv_data = csv_helper.read_file("F:\\DiJieTest\\datas\\supply001.csv")
        current_is_header = True
        for row in csv_data:
            if current_is_header:
                current_is_header = False
                continue
            supply_dict = {
                "companyname": row[0],
                "nickname": row[1],
                "city": row[2],
                "detail_address": row[3],
                "responsible": row[4],
                "respon_phone": row[5],
                "contact": row[6],
                "contact_phone": row[7]
            }
            actual_name = self.supply_page.add_supply(supply_dict)
            self.assertEqual(supply_dict["companyname"], actual_name, "添加供应商失败")
        csv_helper.close()
        self.supply_page.logout()




    def test_supply02(self):
        """
        编辑供应商
        :return:
        """
        self.supply_page.open()
        self.supply_page.login(self.login_dict["name"],self.login_dict["password"])
        self.supply_page.change_company(self.company)
        self.supply_page.select_moudle(self.moudle)
        self.supply_page.select_first_menu(self.first_menu)
        csv_helper = CsvHelper()
        csv_data = csv_helper.read_file("F:\\DiJieTest\\datas\\supply002.csv")
        current_is_header = True
        for row in csv_data:
            if current_is_header:
                current_is_header = False
                continue
            Edit_dict = {
                "companyname": row[0],
                "nickname": row[1],
                "city": row[2],
                "detail_address": row[3],
                "responsible": row[4],
                "respon_phone": row[5],
                "contact": row[6],
                "contact_phone": row[7]
            }
            actul_title = self.supply_page.edit_supply(Edit_dict)
            self.assertEqual(actul_title, "供应商管理", "编辑供应商失败")
        csv_helper.close()
        self.supply_page.logout()



    def test_supply03(self):
        """
        测试删除供应商
        :return:
        """
        self.supply_page.open()
        self.supply_page.login(self.login_dict["name"], self.login_dict["password"])
        self.supply_page.change_company(self.company)
        self.supply_page.select_moudle(self.moudle)
        self.supply_page.select_first_menu(self.first_menu)
        list_A = [0,1,2]
        for i in list_A:
            actul_title = self.supply_page.delete_supply()
            self.assertEqual(actul_title, "供应商管理", "编辑供应商失败")
        self.supply_page.logout()


if __name__ == "__main__":
    unittest.main()