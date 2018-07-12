from time import sleep
from base.box_driver import BoxDriver


class BasePage(object):
    """
    测试系统的最基础的页面类，是所有其他页面的基类
    """
    # 变量
    base_driver = None
    # 方法
    def __init__(self, driver: BoxDriver,base_url):
        """
        构造方法
        :param driver: ":BoxDriver" 规定了 driver 参数类型
        """
        self.base_driver = driver
        self.base_url = base_url

    def open(self):
        """
        打开页面
        :param url:
        :return:
        """
        self.base_driver.navigate(self.base_url)
        self.base_driver.maximize_window()
        sleep(2)


