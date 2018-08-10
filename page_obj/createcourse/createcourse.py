from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig

logger = Logging("createlive").getlog()

class createCourse(Page):

    def create_course_texts(self):
        """创建课程的文本验证"""

        #self.wait_time(2)
        list = []
        #self.click("cms_list", "创建课程按钮")
        list.append(self.text("course_create", "创建课程标题"))
        list.append(self.text("course_create", "课程名称"))
        list.append(self.element_type_value("course_create", "课程名输入框"))
        list.append(self.text("course_create", "课程名备注"))
        list.append(self.text("course_create", "组织机构"))
        list.append(self.element_type_value("course_create", "组织机构输入框"))
        list.append(self.text("course_create", "组织机构备注"))
        list.append(self.text("course_create", "课程编号"))
        list.append(self.element_type_value("course_create", "课程编号输入框"))
        list.append(self.text("course_create", "课程编号备注"))
        list.append(self.text("course_create", "开课时间"))
        list.append(self.element_type_value("course_create", "开课时间输入框"))
        list.append(self.text("course_create", "开课时间备注"))
        list.append(self.text("course_create", "课程分类"))
        list.append(self.text("course_create", "新增分类"))
        list.append(self.element_type_value("course_create", "创建", 'value'))
        list.append(self.element_type_value("course_create", "取消", 'value'))

        return list

        #self.wait_time(2)