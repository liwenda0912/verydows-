import time
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # suitt = unittest.TestSuite()
    # suitt.addTest(modify_UserMessage('test_modify_User_Message'))
    testfile = r"D:\PycharmProjects\软件测试脚本\自动化项目\test_case"
    runs = unittest.defaultTestLoader.discover(testfile,pattern="*.py")
    filename = "自动化-" + time.strftime("%Y-%m-%d-%H-%M_%S") + r"-report.html"
    file = r"D:\PycharmProjects\软件测试脚本\自动化项目\test_report" + "\\"
    filename = file + filename
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='示例测试报告', description='执行人：liwenda')
        runner.run(runs)