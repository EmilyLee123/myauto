from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig

logger = Logging("courseDetail").getlog()
config = ReadConfig()
class coursePage(Page):
    def course_page_texts(self):
        """内容页面文本验证"""
        #缺笔记文本获取，“页面”和“右答3”有换行符可能会出问题

        self.click("course_page", "顶内容")
        self.click("course_page", "顶页面")
        self.wait_time(2)

        pagelist = []
        pagelist.append(self.text("course_page", "内容"))
        pagelist.append(self.text("course_page", "页面"))
        pagelist.append(self.text("course_page", "在线查看"))
        pagelist.append(self.text("course_page", "注意"))
        pagelist.append(self.text("course_page", "主页"))
        pagelist.append(self.text("course_page", "课程"))
        pagelist.append(self.text("course_page", "讨论"))
        pagelist.append(self.text("course_page", "Wiki"))
        pagelist.append(self.text("course_page", "进度"))
        # pagelist.append(self.text("course_page", "笔记"))
        pagelist.append(self.text("course_page", "右问1"))
        pagelist.append(self.text("course_page", "右答1"))
        pagelist.append(self.text("course_page", "右问2"))
        pagelist.append(self.text("course_page", "右答2"))
        pagelist.append(self.text("course_page", "右问3"))
        pagelist.append(self.text("course_page", "右答3"))

        return pagelist
