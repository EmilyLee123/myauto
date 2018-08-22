from common.logger import Logging
from page_obj.base import Page
from testCase.myunittest import createcourse_t

from testFile.elementAndText import Page_Text

logger = Logging("createCourse").getlog()
class createCoursetest(createcourse_t, Page):
    """创建课程测试用例"""
    # def test_texts_course(self):
    #     """文本验证"""
    #
    #     reality_text = self.createCourse.create_course_texts()
    #     anticipated_text = Page_Text["course_create_string"]
    #     print("111", reality_text)
    #     print("222", anticipated_text)
    #     for reality, anticipated in zip(reality_text, anticipated_text):
    #         try:
    #             self.assertEqual(reality, anticipated)
    #             logger.info("实际文本：{}，预期文本：{}".format(reality, anticipated))
    #         except Exception as e:
    #             logger.error("********用例执行错误*********%s" % e)
    #             self.AssertionError.append("实际文本：{}，预期文本：{}".format(reality, anticipated))



    def test_new_course(self):
        self.createCourse.input_course_test()