from time import sleep

from common.logger import Logging
from page_obj.base import Page
from testFile.elementAndText import Page_Text

logger = Logging("livelist").getlog()
class Livelist(Page):
    """文本信息"""
    def list_tests(self):
        """文本信息对比测试"""
        list = []
        #text方法，把元素文本值取出来，append到list中
        list.append(self.text("live_list", "title"))
        list.append(self.text("live_list", "直播列表"))
        list.append(self.text("live_list", "开始直播"))
        list.append(self.text("live_list", "更多操作"))
        list.append(self.text("live_list", "创建直播"))
        list.append(self.text("live_list", "页数"))
        return list

    def list_check_url(self):

        self.click("live_list", "创建直播按钮")
        reality_url = self.get_url()
        self.browser_page_handle("-1")
        return reality_url
    def list_check_click(self):
        """开始直播测试，断言是否开启新窗口"""
        self.click("live_list", "开始直播")
        self.new_window()

    def list_move_to(self):
        """更多菜单测试"""
        self.move("live_list", "更多操作")
        self.click("live_list", "编辑直播")
        reality_url = self.get_url()
        self.browser_page_handle("-1")
        self.move("live_list", "更多操作")
        self.click("live_list", "观看直播")
        self.new_window()
        self.window_to_old('old_page')

        return reality_url

    def list_delete(self):
        """删除操作，删除后返回页面判断直播是否存在"""
        self.move("live_list", "更多操作")
        self.click("live_list", "删除直播")
        self.click("live_list", "取消")
        after_cancl = self.text("live_list", "直播标题")
        self.move("live_list", "更多操作")
        self.click("live_list", "删除直播")
        self.click("live_list", "确认")
        afetr_confirm = self.text("live_list", "直播标题")
        return after_cancl, afetr_confirm

    def list_delete_texts(self):
        """删除提示框测试"""
        self.move("live_list", "更多操作")
        self.click("live_list", "删除直播")

        list = []
        list.append(self.text("live_list", "删除提示框标题"))
        list.append(self.text("live_list", "取消"))
        list.append(self.text("live_list", "确认"))
        self.click("live_list", "取消")
        return list
