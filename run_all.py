import unittest

import os
import readConfig
from common import logger
from common.HTMLTestRunner import HTMLTestRunner

log = logger.Logging("run").getlog()


def get_case_list():
    """获取case_list.txt文件中要执行的用例文件的名称"""
    list = open(os.path.join(readConfig.ProjectPath, "case_list.txt"))
    cases = []
    for value in list.readlines():
        data = str(value)
        if data != "" and not data.startswith("#"):
            cases.append(data.replace("\n", ""))
    print(cases, "cases")
    return cases


def get_list():
    """获取case_list.txt文件中要执行的用例文件，返回以文件为单位的list集合"""
    suite_module = []
    list = get_case_list()
    for value in list:
        case_path = os.path.join(logger.projectPath, "testCase")
        discover = unittest.defaultTestLoader.discover(case_path,   pattern=value.split("/")[-1]+'.py', top_level_dir=None)
        suite_module.append(discover)
    print(suite_module, "suite_module")
    return suite_module


if __name__ == '__main__':
    result_html = logger.Logging("Run").get_logPath()
    config = readConfig.ReadConfig()
    title = config.getConfig("title") + "测试报告"
    browser = config.getConfig("browser")
    description = "浏览器：" + browser
    testunit = unittest.TestSuite()
    list = get_list()
    if len(list) > 0:
        for suite in get_list():
            testunit.addTest(suite)
    filename = os.path.join(result_html, "result.html")
    fp = open(filename, "wb")
    renner = HTMLTestRunner(stream=fp, title=title, description=description)
    renner.run(testunit)
    fp.close()

