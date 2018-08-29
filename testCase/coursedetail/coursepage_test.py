from common.logger import Logging
from page_obj.base import Page
from testCase.myunittest import coursedetail_login
from testFile.elementAndText import Page_Text

logger = Logging("courseDetail").getlog()
class pageTest(coursedetail_login, Page):
    """内容页面测试用例"""

    def test_texts_page(self):
        """内容页面文本验证"""

        reality_text = self.coursePage.course_page_texts()
        anticipated_text = Page_Text["course_page_string"]
        print("真实值：", reality_text)
        print("期望值：", anticipated_text)
        for reality, anticipated in zip(reality_text, anticipated_text):
            try:
                self.assertEqual(reality, anticipated)
                logger.info("实际文本：{}，预期文本：{}".format(reality, anticipated))
            except Exception as e:
                logger.error("********用例执行错误*********%s" % e)
                self.AssertionError.append("实际文本：{}，预期文本：{}".format(reality, anticipated))