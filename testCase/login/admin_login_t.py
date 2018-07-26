from common.logger import Logging
from testCase.myunittest import adminlogintest

from testFile.elementAndText import Page_Text

logger =Logging('AdminLoginTest').getlog()
class AdminLoginTest(adminlogintest):
    """登录模块测试用例"""
    def test_logintext_1(self):
        """文本验证"""
        reality_text = self.admin_login.tests()
        anticipated_text = Page_Text["admin_login"]
        for reality, anticipated in zip(reality_text, anticipated_text):
            try:
                self.assertEqual(reality, anticipated)

                logger.info("实际文本：{}，预期文本：{}".format(reality, anticipated))
            except  Exception as e:
                logger.error("********用例执行错误*********%s" % e)
                self.AssertionError.append("实际文本：{}，预期文本：{}".format(reality, anticipated))
    def test_login_2(self):
        """登录功能验证"""
        self.admin_login.admin_login_test()





