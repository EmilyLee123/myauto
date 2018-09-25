from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig

logger = Logging("courseOutline").getlog()
config = ReadConfig()
class courseOutline(Page):
    def course_outline_texts(self):
        """内容课程大纲的文本验证"""
        self.click("course_outline", "顶内容")
        self.click("course_outline", "顶大纲")
        self.wait_time(2)
        outlinelist = []
        outlinelist.append(self.text("course_outline", "课程大纲"))
        outlinelist.append(self.text("course_outline", "课程开始日期"))
        outlinelist.append(self.text("course_outline", "新增章固定"))
        outlinelist.append(self.text("course_outline", "在线查看"))
        outlinelist.append(self.text("course_outline", "说明标题1"))
        outlinelist.append(self.text("course_outline", "说明内容1.1"))
        outlinelist.append(self.text("course_outline", "说明内容1.2"))
        outlinelist.append(self.text("course_outline", "说明标题2"))
        outlinelist.append(self.text("course_outline", "说明内容2"))
        outlinelist.append(self.text("course_outline", "了解更多2"))
        outlinelist.append(self.text("course_outline", "说明标题3"))
        outlinelist.append(self.text("course_outline", "说明内容3"))
        outlinelist.append(self.text("course_outline", "了解更多3"))
        outlinelist.append(self.text("course_outline", "说明标题4"))
        outlinelist.append(self.text("course_outline", "说明内容4.1"))
        outlinelist.append(self.text("course_outline", "说明内容4.2"))
        outlinelist.append(self.text("course_outline", "说明内容4.3"))
        outlinelist.append(self.text("course_outline", "了解更多4"))

        return outlinelist
