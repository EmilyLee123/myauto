import unittest

from common.drive import Driver
from common.function import Excel
from page_obj.createcourse.createcourse import createCourse
from page_obj.createlive.createlive import createLive

from page_obj.livelist.livelist import Livelist
from page_obj.login.admin_login import AdminLogin
from page_obj.login.cms_login import cmsLogin, login_ccreate

from page_obj.login.live_login import liveLogin, login_create, login

from readConfig import ReadConfig


config = ReadConfig()


class myunittest(unittest.TestCase):
    """继承unnittest"""
    url = config.getConfig("url")
    browser = config.getConfig("browser")

    """获取EXCEL表数据"""
    def get_excel_data(self, dataname, row=2):
        data = Excel(dataname)
        return data.read_excel(row)
    """给EXCEL表插入数据"""
    def set_excel_data(self, dataname, datas, row=2):
        excel_data = Excel(dataname)
        excel_data.write_excel(datas, row)

class cmslogin_test(myunittest):
    """cms登录功能"""
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.cmsLogin = cmsLogin(driver)
        self.cmsLogin.open(self.url)
        self.AssertionError = []

    def tearDown(self):
        self.cmsLogin.quit()
        self.assertEqual([], self.AssertionError)

class createcourse_t(myunittest):
    """新建课程"""
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.createCourse = createCourse(driver)
        self.createCourse.open(self.url)
        self.login_ccreate = login_ccreate(driver)
        self.login_ccreate.course_login()
        self.AssertionError = []

    def tearDown(self):
        self.createCourse.quit()
        self.assertEqual([], self.AssertionError)


class livelogin_test(myunittest):
    """live登录功能"""
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.livelogin = liveLogin(driver)
        self.livelogin.open(self.url)
        self.AssertionError = []

    def tearDown(self):
        self.livelogin.quit()
        self.assertEqual([], self.AssertionError)


class livelist(myunittest,):
    #直播列表

    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.login = login(driver)
        self.login.open(self.url)
        self.list_test = Livelist(driver)
        self.login.live_login()
        self.AssertionError = []

    def tearDown(self):
        self.login.quit()
        self.assertEqual([], self.AssertionError)

class livecreate(myunittest):
    #创建直播

    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.login_create = login_create(driver)
        self.login_create.open(self.url)
        self.createLive = createLive(driver)
        self.login_create.live_login()
        self.AssertionError = []

    def tearDown(self):
        self.login_create.quit()
        self.assertEqual([], self.AssertionError)


class adminlogintest(myunittest):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.admin_login = AdminLogin(driver)
        self.admin_login.open(self.url)
        self.AssertionError = []

    def tearDown(self):
        self.admin_login.quit()
        self.assertEqual([], self.AssertionError)






