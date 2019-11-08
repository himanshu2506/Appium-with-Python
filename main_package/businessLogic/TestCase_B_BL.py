from main_package.commonLib import CommonUtil
from main_package.pageObjectRepositroy import TestCase_B_PL


class TestCase_B_BL:
    cu_obj = CommonUtil.CommonUtils()
    call_B = TestCase_B_PL.TestCase_B_PL()

    def app(self):
        try:
            self.cu_obj.click(self.call_B.select_app())
            self.cu_obj.click(self.call_B.select_action_bar())
            self.cu_obj.click(self.call_B.select_display_options())
            self.cu_obj.click(self.call_B.select_display_show_title())
            self.cu_obj.click(self.call_B.select_display_show_title())
            title_element = self.call_B.select_view()
            title = title_element.is_displayed()
            return title
        except NameError:
            print('An Exception occurred in app method ')
            return False






