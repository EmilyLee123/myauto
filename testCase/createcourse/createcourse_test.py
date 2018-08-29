
from common.logger import Logging
from page_obj.base import Page
from testCase.myunittest import createcourse_t

from testFile.elementAndText import Page_Text

logger = Logging("createCourse").getlog()
class createCoursetest(createcourse_t, Page):
    """创建课程测试用例"""
    def test_texts_course(self):
        """创建课程文本验证"""

        reality_text = self.createCourse.create_course_texts()
        anticipated_text = Page_Text["course_create_string"]
        # print("真实值：", reality_text)
        # print("期望值：", anticipated_text)
        for reality, anticipated in zip(reality_text, anticipated_text):
            try:
                self.assertEqual(reality, anticipated)
                logger.info("实际文本：{}，预期文本：{}".format(reality, anticipated))
            except Exception as e:
                logger.error("********用例执行错误*********%s" % e)
                self.AssertionError.append("实际文本：{}，预期文本：{}".format(reality, anticipated))



    def test_new_course(self):
        """创建课程是否成功验证"""

        check = self.createCourse.input_course_test()
        cid = check[0]
        list = check[1]

        if str(cid) in list:
            logger.info("创建课程成功")
        else:
            logger.error("创建课程失败")
            self.AssertionError.append("创建课程用例执行失败")

