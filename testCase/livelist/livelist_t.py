from time import sleep

from common.logger import Logging
from page_obj.base import Page

from testCase.myunittest import livelist

from testFile.elementAndText import Page_Text

logger = Logging("liveList").getlog()
class liveList(livelist, Page):
    """直播列表测试用例"""
    def test_txt_1(self):
        """文本验证"""
        reality_text = self.list_test.list_tests()
        anticipated_text = Page_Text["live_list"]
        for reality, anticipated in zip(reality_text, anticipated_text):
            try:
                self.assertEqual(reality, anticipated)

                logger.info("实际文本：{}，预期文本：{}".format(reality, anticipated))
            except  Exception as e:
                logger.error("********用#例执行错误*********%s" % e)
                self.AssertionError.append("实际文本：{}，预期文本：{}".format(reality, anticipated))

    def test_cretelive_2(self):
        """创建直播按钮&开始直播测试"""
        self.list_test.list_check_url()
        anticipated_url = Page_Text["list_string"]
        reality_url = self.list_test.list_check_url()

        self.check_url(reality_url, anticipated_url[3], "直播")
        self.list_test.list_check_click()

    def test_moreOperation_3(self):
        """更多操作测试"""
        self.list_test.list_move_to()

    def test_delete_4(self):
        after = self.list_test.list_delete()
        if after[0] == after[1]:
            logger.info("删除直播失败")
        else:
            logger.info("删除成功")
        """删除框文本验证"""
        reality_text = self.list_test.list_delete_texts()
        anticipated_text = Page_Text["list_string"]
        anticipated_text1 = anticipated_text[1:4]
        #print(anticipated_text1)
        #print(reality_text)
        for reality, anticipated in zip(reality_text, anticipated_text):
            try:
                self.assertEqual(reality, anticipated)

                logger.info("实际文本：{}，预期文本：{}".format(reality, anticipated))
            except  Exception as e:
                logger.error("********用例执行错误*********%s" % e)
                self.AssertionError.append("实际文本：{}，预期文本：{}".format(reality, anticipated))

























