from common.logger import Logging
from testCase.myunittest import livelogin_test
from testFile.elementAndText import Page_Text

logger = Logging("liveLoginTest").getlog()

class liveLoginTest(livelogin_test):
    """登录模块测试用例"""
    def test_login_1(self):
        """文本验证"""
        reality_text = self.livelogin.tests()
        anticipated_text = Page_Text["live_login"]
        for reality, anticipated in zip(reality_text, anticipated_text):
            try:
                self.assertEqual(reality, anticipated)

                logger.info("实际文本：{}，预期文本：{}".format(reality, anticipated))
            except Exception as e:
                logger.error("********用例执行错误*********%s" % e)
                self.AssertionError.append("实际文本：{}，预期文本：{}".format(reality, anticipated))

    def test_login_2(self):
        #登陆功能验证
        datas = self.get_excel_data("login/login", 2)
        u = datas[6]
        username = u['username']
        print(username)
        """
        for data in datas:
            logger.info("用例开始-----》本次用例编号{}".format(data["serial_number"]))
            try:
                error = self.livelogin.live_login_fun(data["username"], data["password"])
                self.assertEqual(error, data["expected_result"])
            except Exception as e:
                logger.error("********用例执行错误*********%s" % e)
                self.AssertionError.append(str(data["serial_number"])+data["description"])
            logger.info("用例结束《---------------")
    """