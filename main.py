from runners.dijie_runner import DiJieRunner

class Main(object):
    """
    自动化方案的唯一入口
    """
    @staticmethod
    def run_dijie():
        """
        静态执行的方法
        :param self:
        :return:
        """
        print("start-test")
        DiJieRunner().run_test()

if __name__ == '__main__':
    Main.run_dijie()
    print("小小的修改，带我提交git")
