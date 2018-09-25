import random

from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig

logger = Logging("createCourse").getlog()
config = ReadConfig()
class createCourse(Page):

    def create_course_texts(self):
        """创建课程的文本验证"""

        self.wait_time(2)
        list = []
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

    def input_course_test(self):
        """创建课程,获取所有课程编号"""
        #创建课程
        self.send_keys("course_create", "课程名输入框", "自动化测试课程")
        self.send_keys("course_create", "组织机构输入框", "lmyAutoTest")
        cid = random.randint(0, 999999)
        #cid = "001"
        self.send_keys("course_create", "课程编号输入框", cid)
        self.send_keys("course_create", "开课时间输入框", "2018")
        self.click("course_create", "创建")
        while self.is_displayed("course_create", "重复提示") == True:
            self.send_keys("course_create", "课程编号输入框", cid)
            self.click("course_create", "创建")
        # else:
        #     logger.info("成功创建课程")

        #获取所有课程编号
        #后退,默认值为后退
        self.browser_page_handle()
        #刷新页面
        self.browser_page_handle(type="0")
        print("课程编号:lmyAutoTest+" + "%s" % cid + "+2018")
        el = self.find_elements("course_create", "课程编号组")
        list = []
        for n in range(len(el)):
            coursenumbers = el[n].text
            list.append(coursenumbers)
        #print(list)

        return cid, list


