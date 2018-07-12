import time
import unittest
from runners.html_test_runner import HtmlTestRunner
from test.test_supply import TestSupply


class DiJieRunner(object):
    def run_test(self):
        """
        运行测试
        :return:
        """
        suite = unittest.TestSuite()
        suite.addTest(TestSupply("test_supply01"))
        suite.addTest(TestSupply("test_supply02"))
        suite.addTest(TestSupply("test_supply03"))


        # 测试报告的文件
        test_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        report_file = open("./reports/dijie_automate_report_%s.html" % test_time,
                           mode="wb")

        runner = HtmlTestRunner(stream=report_file,
                                title="地接系统自动化测试报告",
                                description="具体测试报告内容如下: ")
        runner.run(suite)
        report_file.close()














