from common.function import Excel
from common.logger import Logging
from page_obj.base import Page


logger = Logging("AdminLogin").getlog()
class AdminLogin(Page):
    def tests(self):
        """登录文本休息"""
        list = []
        list.append(self.text('admin_login', '中文'))
        list.append(self.text('admin_login', '登录按钮'))
        list.append(self.text('admin_login', '忘记密码'))
        list.append(self.text('admin_login', '验证码登录'))
        return list

    def admin_login_test(self):
        """登录功能验证"""


        excel = Excel('login/login')
        excelr = excel.read_excel(2)
        print(list(range(len(excelr))))
        for number in range(len(excelr)):
            logger.info('用例号码{}正在执行'.format(excelr[number]['serial_number']))
            #print(excelr[number]['username'])
            self.send_keys('admin_login', '账号输入框', excelr[number]['username'])
            #print(excelr[number]['password'])
            self.send_keys('admin_login', '密码输入框', excelr[number]['password'])
            self.click('admin_login', '登录按钮')
            # text = self.text('admin_login', '错误提示')
            # print(text)
            # excel.write_excel_rol(number + 2, 4, text)
            try:

                text = self.text('admin_login', '错误提示')
                print(text)
                rows = number+2
                print('行数为:', rows)
                excel = Excel('login/login')
                excel.write_excel_rol(rows, 4, text)
            except Exception as e:
                logger.info('登录成功')
        excel = Excel('login/login')
        excelr = excel.read_excel(2)
        for number in range(len(excelr)):
            logger.info('对比测试{}正在进行'.format(excelr[number]['serial_number']))

            try:

                assert excelr[number]['description'] == excelr[number]['expected_result']
                logger.error('{} == {}'.format(excelr[number]['description'], excelr[number]['expected_result']))

            except Exception as e:
                #self.AssertionError.append('提示信息与预期不符')
                logger.error('提示信息与预期不符')





