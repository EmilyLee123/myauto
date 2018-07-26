from time import sleep

from common.logger import Logging
from page_obj.base import Page
from testCase.myunittest import livecreate
from testFile.elementAndText import Page_Text

logger = Logging("createLive").getlog()
class createLive(livecreate, Page):
    """创建直播测试用例"""
    def test_texts_1(self):
        """文本验证"""
        reality_text = self.createLive.create_live_texts()
        anticipated_text = Page_Text["create_string"]
        for reality, anticipated in zip(reality_text, anticipated_text[0:16]):
            try:
                self.assertEqual(reality, anticipated)
                logger.info("实际文本：{}，预期文本：{}".format(reality, anticipated))
            except  Exception as e:
                logger.error("********用例执行错误*********%s" % e)
                self.AssertionError.append("实际文本：{}，预期文本：{}".format(reality, anticipated))

    def test_title_2(self):
        """测试title输入框"""
        title_texts = self.createLive.input_title_test()
        real_num = ['0/30', '18/30', '30/30', '30/30']
        for title, real in zip(title_texts, real_num):
            try:
                self.assertEqual(title, real)
                logger.info("实际输入:{}个字符,预计输入:{}字符".format(title, real))
            except Exception as e:
                logger.error("********用例执行错误*********%s" % e)
                self.AssertionError.append("实际输入:{}个字符,预计输入:{}字符".format(title, real))

    def test_time_3(self):
        """测试时间选择器"""
        input_text = self.createLive.time_select_test()
        time = Page_Text['time_select']
        if input_text[0] == ""and input_text[2] == "":

            logger.info("清除按钮有效")
        else:
            logger.error("清除按钮无效")
        if input_text[1] == time[0] and input_text[3] == time[1]:
            logger.info("时间选择器正确")
        else:
            logger.error("时间选择器没有正常工作")



    def test_viewlimits_4(self):
        """观看权限测试"""

        reality_text = self.createLive.viewlimits_test()

        anticipated_text = Page_Text["create_string"]
        for reality, anticipated in zip(reality_text[0], anticipated_text[23:-1]):
            try:
                self.assertEqual(reality, anticipated)
                logger.info("实际文本：{}，预期文本：{}".format(reality, anticipated))
            except  Exception as e:
                logger.error("********用例执行错误*********%s" % e)
                self.AssertionError.append("实际文本：{}，预期文本：{}".format(reality, anticipated))
        first_pwd = reality_text[1]
        second_pwd = reality_text[2]
        try:
            self.assertEqual(first_pwd, second_pwd)
            logger.info("生成密码错误，第一和第二次密码一样")
        except Exception as e:
            self.AssertionError.append(e)
            #删除功能出来后修改
            logger.error("生成密码成功")
            self.AssertionError.append("生成密码成功")
    def test_money_5(self):
        """付费输入的测试"""
        self.createLive.paymoney()

    def test_all_6(self):
        """创建直播流程测试未完成，差删除功能"""
        anticipated_url = Page_Text["create_all"]
        reality_url = self.createLive.all_default()
        #print(anticipated_url[2])
        self.check_url(reality_url, anticipated_url[2], "创建直播")
        self.browser_page_handle(-1)
        #print(reality_url)
        reality_url = self.createLive.all_pay(100)
        self.check_url(reality_url, anticipated_url[2], "创建直播_付费")
        self.browser_page_handle(-1)
        reality_url = self.createLive.all_assign()
        self.check_url(reality_url, anticipated_url[2], "创建直播_指定用户")
        self.browser_page_handle(-1)
        reality_url = self.createLive.all_pwd()
        self.check_url(reality_url, anticipated_url[2], "创建直播_密码")









