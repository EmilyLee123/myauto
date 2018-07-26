from common.logger import Logging
from testCase.myunittest import cmslogin_test
from testFile.elementAndText import Page_Text

logger = Logging("CMSLoginTest").getlog()

class CMSLoginTest(cmslogin_test):
    """CMS登录测试用例"""
    def test_login_1(self):
        """文本验证"""
        reality_text = self.cmslogin.tests()

        anticipated_text = Page_Text["cms_login"]
        for reality, anticipated in zip(reality_text, anticipated_text):
            try:
                self.assertEqual(reality, anticipated)

                logger.info("实际文本：{}，预期文本：{}".format(reality, anticipated))
            except Exception as e:
                logger.error("********用例执行错误*********%s" % e)
                self.AssertionError.append("实际文本：{}，预期文本：{}".format(reality, anticipated))

    def test_login_2(self):
        #登录功能验证
        datas = self.get_excel_data("login/login", 2)
        u = datas[6]
        username = u['username']
        print(username)