
from time import sleep



from common.logger import Logging
from page_obj.base import Page
from testFile.elementAndText import Page_Text

logger = Logging("createlive").getlog()

class createLive(Page):
    def create_live_texts(self):
        """创建直播的文本验证"""
        self.wait_time(3)
        list = []
        list.append(self.text("live_create", "创建直播标题"))
        list.append(self.text("live_create", "直播标题"))
        list.append(self.element_type_value("live_create", "直播标题提示内容"))
        list.append(self.text("live_create", "0/30"))
        list.append(self.element_type_value("live_create", "选择日期提示内容"))
        list.append(self.element_type_value("live_create", "选择时间提示内容"))
        list.append(self.text("live_create", "时区选择"))
        list.append(self.text("live_create", "直播简介"))
        list.append(self.text("live_create", "自动录制"))
        list.append(self.text("live_create", "观看权限"))
        list.append(self.text("live_create", "提示1"))
        list.append(self.text("live_create", "提示2"))
        list.append(self.text("live_create", "提示3"))
        list.append(self.text("live_create", "建议尺寸"))
        list.append(self.text("live_create", "支持"))
        list.append(self.text("live_create", "创建"))
        list.append(self.text("live_create", "取消"))
        return list

    def input_title_test(self):
        """输入标题测试"""
        input = Page_Text["create_string"]
        self.send_keys("live_create", "直播标题提示内容", input[17])
        self.move("live_create", "直播标题提示内容")
        self.click("live_create", "x按钮")
        input_0 = self.text("live_create", "0/30")
        self.send_keys("live_create", "直播标题提示内容", input[17])
        input_18 = self.text("live_create", "0/30")
        self.send_keys("live_create", "直播标题提示内容", input[18])
        input_30 = self.text("live_create", "0/30")
        self.send_keys("live_create", "直播标题提示内容", input[19])
        input_31 = self.text("live_create", "0/30")
        return input_0, input_18, input_30, input_31
    def time_select_test(self):
        """对两个时间选择器进行测试"""
        list = []
        self.click("live_create", "选择日期提示内容")
        self.click("live_create", "选择的时间")
        self.move("live_create", "选择日期提示内容")
        self.click("live_create", "日期x按钮")
        list.append(self.element_type_input("live_create", "选择日期提示内容"))
        self.click("live_create", "选择日期提示内容")
        self.click("live_create", "选择的时间")
        list.append(self.element_type_input("live_create", "选择日期提示内容"))
        self.click("live_create", "选择时间提示内容")
        self.click("live_create", "时选择")
        self.click("live_create", "分选择")
        self.click("live_create", "时间x按钮")
        list.append(self.element_type_input("live_create", "选择时间提示内容"))
        self.click("live_create", "选择时间提示内容")
        self.click("live_create", "时选择")
        self.click("live_create", "分选择")
        list.append(self.element_type_input("live_create", "选择时间提示内容"))
        return list

    def viewlimits_test(self):
        """凭密码进入测试"""
        list = []
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        self.click("live_create", "凭密码进入")
        list.append(self.text("live_create", "密码_1"))
        pw = self.text("live_create", "密码_2").split('：')
        first_cli = pw[-1]
        list.append(pw[-2])
        list.append(self.text("live_create", "密码_3"))
        list.append(self.text("live_create", "密码_4"))
        self.click("live_create", "付费可见")
        list.append(self.text("live_create", "付_1"))
        monkey = self.element_type_input("live_create", "金额输入")
        self.click("live_create", "指定用户可见")
        list.append(self.text("live_create", "指_1"))
        self.click("live_create", "凭密码进入")
        pw = self.text("live_create", "密码_2").split('：')
        second_cli = pw[-1]
        return list, first_cli, second_cli, monkey

    def paymoney(self):
        """付费进入测试"""
        #js滚动到页面地步
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        self.click("live_create", "付费可见")
        default_input = self.element_type_input("live_create", "金额输入")
        if default_input == str(0.1):
            try:
                self.click("live_create", "减金额")
            except Exception as e:

                logger.info("为最低值不能减少")
            self.click("live_create", "加金额")
            if self.element_type_input("live_create", "金额输入") == str(1.1):
                logger.info("增加金额按钮有效")
            else:
                logger.info("增加金额按钮无效")
            self.click("live_create", "减金额")
            if self.element_type_input("live_create", "金额输入") == str(0.1):
                logger.info("减金额按钮有效")
            else:
                logger.info("减加金额按钮无效")
        else:
            logger.info("金额默认值不为0.1")

        self.click("live_create", "试听开关")
        try:
            self.send_keys("live_create", "试听时间", "9")

        except Exception as e:
            logger.info("试听开关正常工作")



    def upload(self):
        """图片上传方法，操作js"""
        try:
            js = "document.getElementById('ossFile').style.display='block'"
            self.driver.execute_script(js)
            self.send_keys("live_create", "upload", '/Users/qfl/eliproject/Elite-live-autotest/function_test/testFile/image/timg.jpeg')

        except Exception as e:
            #logger.info("图片上传失败")
            logger.error(e)



    def all_default(self):
        """完全公开流程测试"""
        input_text = Page_Text["create_all"]
        self.send_keys("live_create", "直播标题提示内容", input_text[0])
        self.click("live_create", "选择日期提示内容")
        self.click("live_create", "选择的时间")
        self.click("live_create", "选择时间提示内容")
        self.click("live_create", "时选择")
        self.click("live_create", "分选择")
        #self.click("live_create", "凭密码进入")
        self.send_keys("live_create", "直播简介输入框", input_text[1])
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        self.upload()
        self.click("live_create", "创建")
        url = self.get_url()
        return url
    def all_pwd(self):
        """凭密码进入测试"""
        input_text = Page_Text["create_all"]
        self.send_keys("live_create", "直播标题提示内容", input_text[0])
        self.click("live_create", "选择日期提示内容")
        self.click("live_create", "选择的时间")
        self.click("live_create", "选择时间提示内容")
        self.click("live_create", "时选择")
        self.click("live_create", "分选择")
        self.click("live_create", "凭密码进入")
        self.send_keys("live_create", "直播简介输入框", input_text[1])
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        self.upload()
        self.click("live_create", "创建")
        url = self.get_url()
        return url

    def all_pay(self, money):
        """付费进入"""
        input_text = Page_Text["create_all"]
        self.send_keys("live_create", "直播标题提示内容", input_text[0])
        self.click("live_create", "选择日期提示内容")
        self.click("live_create", "选择的时间")
        self.click("live_create", "选择时间提示内容")
        self.click("live_create", "时选择")
        self.click("live_create", "分选择")
        self.click("live_create", "付费可见")
        self.send_keys("live_create", "直播简介输入框", input_text[1])
        self.send_keys("live_create", "金额输入", money)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        self.upload()
        self.click("live_create", "创建")
        url = self.get_url()
        return url

    def all_assign(self):
        """验证码进入"""
        input_text = Page_Text["create_all"]
        self.send_keys("live_create", "直播标题提示内容", input_text[0])
        self.click("live_create", "选择日期提示内容")
        self.click("live_create", "选择的时间")
        self.click("live_create", "选择时间提示内容")
        self.click("live_create", "时选择")
        self.click("live_create", "分选择")
        self.click("live_create", "指定用户可见")
        self.send_keys("live_create", "直播简介输入框", input_text[1])

        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        self.upload()
        self.click("live_create", "创建")
        #获取url进行对比
        url = self.get_url()
        return url






