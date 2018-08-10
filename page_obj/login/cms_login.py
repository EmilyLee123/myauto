

from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig


logger = Logging("cms_Login").getlog()
class cmsLogin(Page):


    def tests(self):
        """登录文本信息"""
        list = []
        list.append(self.text("cms_login", "帮助"))
        list.append(self.text("cms_login", "登录右"))
        list.append(self.text("cms_login", "标题"))
        list.append(self.text("cms_login", "邮箱或手机"))
        list.append(self.element_type_value("cms_login", "账号输入框"))
        list.append(self.text("cms_login", "密码"))
        list.append(self.text("cms_login", "登录按钮"))
        list.append(self.text("cms_login", "使用验证码登录"))
        list.append(self.text("cms_login", "版权所有"))
        list.append(self.text("cms_login", "商标名称"))

        # list.append(self.text("cms_login", "验证码账号"))
        # list.append(self.element_type_value("cms_login", "验证码账号输入框"))
        # list.append(self.text("cms_login", "验证码"))
        # list.append(self.element_type_value("cms_login", "获取验证码按钮"))
        # list.append(self.element_type_value("cms_login", "验证码登录按钮"))
        # list.append(self.element_type_value("cms_login", "使用账号密码登录"))

        return list

    #登录功能操作
    def cms_login_msg(self, username, password):
        """登录状态操作"""

        self.send_keys("cms_login", "账号输入框", username)
        self.send_keys("cms_login", "密码输入框", password)
        self.click("cms_login", "登录按钮")
        if self.isElementExist("cms_login", "错误提示") == True:
            error = self.text("cms_login", "错误提示")
            return error


    def cms_login_test(self):
        """登录的通用方法"""
        config = ReadConfig()
        # 从配置文件获取账户和密码
        username = config.getConfig("username")
        # print(username)
        password = config.getConfig("password")
        # print(password)
        self.send_keys("cms_login", "账号输入框", username)
        self.send_keys("cms_login", "密码输入框", password)
        self.click("cms_login", "登录按钮")
        self.wait_time(1)

        g_url = self.get_url()
        print("获取的地址:%s" % g_url)

        t_url = 'https://course.beta.e-ducation.cn/home/'
        print("实际的地址:%s" % t_url)

        self.check_url(g_url, t_url, '登录')
        return self.check_url(g_url, t_url, '登录')


class login_ccreate(Page):
    def course_login(self):
        """创建直播的登录方法"""
        config = ReadConfig()
        # 从配置文件获取账户和密码
        username = config.getConfig("username")
        password = config.getConfig("password")
        self.send_keys("cms_login", "账号输入框", username)

        self.send_keys("cms_login", "密码输入框", password)
        self.click("cms_login", "登录按钮")
        self.wait_time(0.8)

        while self.is_displayed('course_create', '创建课程标题') == False:
            self.click("cms_list", "创建课程按钮")
            print(self.is_displayed('course_create', '创建课程标题'))
        # else:
        #     logger.info('点击按钮成功')
