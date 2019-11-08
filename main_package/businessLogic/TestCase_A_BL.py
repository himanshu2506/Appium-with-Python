from main_package.commonLib import CommonUtil
from main_package.pageObjectRepositroy import TestCase_A_PL


class TestCase_A_BL:
    cu_obj = CommonUtil.CommonUtils()
    call_A = TestCase_A_PL.TestCase_A_PL()

    def go_to_page(self):
        try:
            self.cu_obj.click(self.call_A.select_animation())
            self.cu_obj.click(self.call_A.select_hide_show_animation())
            return True
        except NameError:
            print('An Exception occurred in go_to_page method ')
            return False

    def check_hide(self):
        try:
            self.cu_obj.click(self.call_A.select_hide())
            return True
        except NameError:
            print('An Exception occurred in check_hide method ')
            return False

    def check_number(self):
        self.cu_obj.click(self.call_A.select_button1())
        self.cu_obj.click(self.call_A.select_button2())

    def path_of_clicked_buttons(self):              #Mobile eleement could not be located at this point
        try:                                      #as the number are being hide
            hide_b1 = self.call_A.select_button1()
            hide_b2 = self.call_A.select_button2()
            return True
        except:
            return False

    def check_show(self):
        try:
            self.cu_obj.click(self.call_A.select_show_button())
            return True
        except NameError:
            print('An Exception occurred in check_show method ')
            return False





