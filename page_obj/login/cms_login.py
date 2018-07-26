from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig

logger = Logging("cms_Login").getlog()
class \
        cmsLogin(Page):


    def tests(self):
        """登录文本信息"""
        list = []
        list.append(self.text("cms_login", "帮助"))
        list.append(self.text("cms_login", "登录右"))
        list.append(self.text("cms_login", "标题"))
        list.append(self.text("cms_login", "邮箱或手机"))
        list.append(self.element_type_value("cms_login", "账号输入框"))
        print(self.element_type_value("cms_login", "账号输入框"))
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
"""
    #登录功能操作
    def live_login_fun(self, username, password):
        #登录状态操作
        self.send_keys("live_login", "账号输入框", username)
        self.send_keys("live_login", "密码输入框", password)
        self.click("live_login", "登录")
        if self.isElementExist("live_login", "账户错误提示"):
            return self.text("live_login", "账户错误提示")
        elif self.isElementExist("live_login", "密码错误提示"):
            return self.text("live_login", "密码错误提示")
        elif self.isElementExist("live_login","错误提示"):
            logger.info("密码或者账户错误")

       # elif self.isElementExist("live_login", "错误提示"):

"""
class login(Page):
    """登录的通用方法"""
    def cms_login(self):
        config = ReadConfig()
        # 从配置文件获取账户和密码
        username = config.getConfig("username")
        password = config.getConfig("password")
        self.send_keys("cms_login", "账号输入框", username)
        self.send_keys("cms_login", "密码输入框", password)
        self.click("cms_login", "登录")


