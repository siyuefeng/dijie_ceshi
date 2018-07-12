from time import sleep
from pages.base_page import BasePage


class MainPage(BasePage):

    # 定位符
    LOGIN_ACCOUNT_SELECTOR = "x, html/body/div[1]/div/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input"  # 用户名
    LOGIN_PASSWORD_SELECTOR = "x, //div[@class='formContent']/form/div[2]/div/div/input"  # 密码
    LOGIN_SUBMIT_SELECTOR = "s, .ivu-btn.ivu-btn-primary.ivu-btn-long"
    LOGIN_FAIL_MESSAGE_SELECTOR = "s, body > div.bootbox.modal.fade.bootbox-alert.in > div > div > div.modal-body"
    LOGIN_COMPANY_SELECTOR = "s, .company_name"  # 公司名
    LOGIN_NICKNAME_SELECTOR = "s, .ac-name"  # 用户昵称
    SELECTED_COMPANY = "s, #data-header > div > ul > li > span"

    PERSON_IMG = 'x, //*[@id="data-header"]/div/div[2]/ul/li/img'
    LOGOUT_SELECTOR = "x, html/body/header/div/div[2]/ul/li/ul/li[2]/a/span[2]"  # 登出
    TOP_MOUDLU_SELECTOR = 'x, //*[@id="bigMenu"]/li[%d]/a'  # 顶部模块
    LEFT_MENU_SELECTOR = 'x, //*[@id="navgation"]/ul/li[%d]/a/span[2]'  # 左侧一级菜单
    LEFT_SECOND_MENU_SELECTOR = 'x,//*[@id="navgation"]/li[class="menu-title"]/ul/li[%d]/a/span'  # 左侧二级菜单

    # 方法
    def login(self, account, password):
        """
        登录系统
        :param account:
        :param password:
        :return:
        """
        self.base_driver.type(self.LOGIN_ACCOUNT_SELECTOR, account)
        self.base_driver.type(self.LOGIN_PASSWORD_SELECTOR, password)
        self.base_driver.click(self.LOGIN_SUBMIT_SELECTOR)
        sleep(4)

    def login_by_cookie(self, cookie_dict, url=None):
        """
        使用 cookie 登录地接系统。
        :param cookie_dict: cookie 字典，有两个 key：name 和 value
        :return:
        """
        self.base_driver.add_cookie(cookie_dict)
        self.base_driver.refresh(url)
        sleep(2)

    def get_company_nickname(self):
        """
        获取当前页面的公司名称，个人昵称按钮和登录按钮，以字典类型返回
        :return: 字典
        """
        company_text = self.base_driver.get_text(self.LOGIN_COMPANY_SELECTOR)
        nikename_text = self.base_driver.get_text(self.LOGIN_NICKNAME_SELECTOR)

        text_dict = {
            "companyname": company_text,
            "nickname": nikename_text
        }
        return text_dict

    def change_company(self, company_name):
        """
        如果当前登录的员工有多个公司时
        检查当前公司是不是我们预期的公司，如果不是，切换成我们想要的公司
        这里选择下拉框的所有公司进行循环，如果有我们想要的公司，就选择
        return:选择之后的公司名
        """
        ele = self.base_driver.locate_element(self.LOGIN_COMPANY_SELECTOR)
        if ele.text != company_name:
            self.base_driver.click(self.LOGIN_COMPANY_SELECTOR)
            elements = self.base_driver.locate_elements(self.SELECTED_COMPANY)
            if len(elements) == 1:
                print("给出的登录账号与公司不匹配")
            else:
                for i in elements:
                    if i.text == company_name:
                        i.click()
                        print(i.text)
                        break
        sleep(3)



    def select_moudle(self, moudle):
        """
        选择 顶部模块应用
        :param app: shouye，finance,business,company_set,data_center
        :return:
        """
        if moudle == "shouye":
            self.base_driver.click(self.TOP_MOUDLU_SELECTOR % 1)
        elif moudle == "business":
            self.base_driver.click(self.TOP_MOUDLU_SELECTOR % 2)
        elif moudle == "finance":
            self.base_driver.click(self.TOP_MOUDLU_SELECTOR % 3)
        elif moudle == "company_set":
            self.base_driver.click(self.TOP_MOUDLU_SELECTOR % 4)
        elif moudle == "data_center":
            self.base_driver.click(self.TOP_MOUDLU_SELECTOR % 5)
        else:
            print("没有这个模块")
        sleep(3)

    def get_left_first_menu_selector(self, menu_first):
        """
        获取指定 menu 的 Selector （左侧一级菜单元素的位置）
        :param menu_first: supplier_management(供应商管理), distributor_management（分销商管理）,
        product_management(产品管理),dijie_erp(地接erp),cars_erp(车队erp),enterprise_receive（企业待收款）,
        enterprise_payment（企业待付款）,tour_guide_payment（导游收付款）,account_management（团账管理）,
        signature_management（签单管理）,fapiao_management（发票管理）,shouzhi_management（收支管理）,
        enterprise_information（企业资料）,organization_structure（组织架构）,
        check_set（审批设置）,Currency_set（币种设置）
        :return:menu_first_selector
        """
        if menu_first == "supplier_management" or "enterprise_receive" or "enterprise_information":
            menu_first_selector = self.LEFT_MENU_SELECTOR % 1
        elif menu_first == "distributor_management" or "enterprise_payment" or "organization_structure":
            menu_first_selector = self.LEFT_MENU_SELECTOR % 2
        elif menu_first == "product_management" or "tour_guide_payment" or "check_set":
            menu_first_selector = self.LEFT_MENU_SELECTOR % 3
        elif menu_first == "dijie_erp" or "account_management":
            menu_first_selector = self.LEFT_MENU_SELECTOR % 4
        elif menu_first == "cars_erp" or "signature_management" or "Currency_set":
            menu_first_selector = self.LEFT_MENU_SELECTOR % 5
        elif menu_first == "fapiao_management":
            menu_first_selector = self.LEFT_MENU_SELECTOR % 6
        elif menu_first == "shouzhi_management":
            menu_first_selector = self.LEFT_MENU_SELECTOR % 7
        else:
            menu_first_selector = "error menu"
        return menu_first_selector

    def select_first_menu(self, menu_first):
        """
        选择进入左侧一级菜单
        :param menu_first: todo, task, project, order, contract, review, company, dynamic
        :return:
        """
        menu_selector = self.get_left_first_menu_selector(menu_first)
        self.base_driver.click(menu_selector)
        sleep(3)


    def logout(self):
        """
        鼠标移动到图片位置，显示下拉框后，点击退出
        :return:
        """
        self.base_driver.move_to(self.PERSON_IMG)
        sleep(1)
        self.base_driver.click(self.LOGOUT_SELECTOR)
        sleep(1)
