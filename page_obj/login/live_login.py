from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig

logger = Logging("live_Login").getlog()
class \
        liveLogin(Page):


    def tests(self):
        """登录文本信息"""
        list = []
        list.append(self.text("live_login", "账号文本"))
        list.append(self.element_type_value("live_login", "账号输入框"))
        list.append(self.element_type_value("live_login", "密码输入框"))
        list.append(self.text("live_login", "自动登录"))
        list.append(self.text("live_login", "忘记密码"))
        list.append(self.text("live_login", "登录"))
        list.append(self.text("live_login", "注册账户"))
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
    def live_login(self):
        config = ReadConfig()
        # 从配置文件获取账户和密码
        username = config.getConfig("username")
        password = config.getConfig("password")
        self.send_keys("live_login", "账号输入框", username)
        self.send_keys("live_login", "密码输入框", password)
        self.click("live_login", "登录")

class login_create(Page):
    """创建直播的登录方法"""
    def live_login(self):
        config = ReadConfig()
        # 从配置文件获取账户和密码
        username = config.getConfig("username")
        password = config.getConfig("password")
        self.send_keys("live_login", "账号输入框", username)
        self.send_keys("live_login", "密码输入框", password)
        self.click("live_login", "登录")
        self.wait_time(0.8)
        self.click("live_list", "创建直播按钮")
