from common.logger import Logging

from testCase.myunittest import cmslogin_test
from testFile.elementAndText import Page_Text

logger = Logging("CMSLoginTest").getlog()

class CMSLoginTest(cmslogin_test):
    """CMS登录测试用例"""
    def test_login_1(self):
        """页面文本验证"""
        reality_text = self.cmsLogin.tests()
        # len(reality_text)

        anticipated_text = Page_Text["cms_login"]
        for reality, anticipated in zip(reality_text, anticipated_text):
            try:
                self.assertEqual(reality, anticipated)
                logger.info("实际文本：{}，预期文本：{}".format(reality, anticipated))
            except Exception as e:
                logger.error("********用例执行错误*********%s" % e)
                self.AssertionError.append("实际文本：{}，预期文本：{}".format(reality, anticipated))

        print("期望的值:", anticipated_text)
        print("获取的值:", reality_text)

    def test_login_2(self):
        """登录错误提示语验证"""
        datas = self.get_excel_data("login/cmslogin", 2)
        # "login/login"是Excel路径
        #u = datas[6]
        #username = u['username']
        #print(username)

        for data in datas:
            logger.info("用例开始》本次用例编号{}".format(data["serial_number"]))

            try:
                error = self.cmsLogin.cms_login_msg(data["username"], data["password"])
                print('期望值', data["description"])
                print('获取值', error)
                self.assertEqual(error, data["description"])
            except Exception as e:
                logger.error("********用例执行错误*********"+'\n'+"错误原因：{}".format(e))
                self.AssertionError.append(str(data["serial_number"]) + data["description"])
            logger.info("用例结束《")


    def test_login_3(self):
        """登录功能验证"""
        res = self.cmsLogin.cms_login_test()
        try:
            self.assertEqual(res, True)
            logger.info("登录成功")
        except Exception as e:
            # self.assertEqual(res, False)
            logger.error("登录失败"+'\n'+"错误原因：{}".format(e))
            self.AssertionError.append("登录失败"+'\n'+"错误原因：{}".format(e))




