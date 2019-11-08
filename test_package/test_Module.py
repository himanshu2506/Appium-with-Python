from main_package.businessLogic import TestCase_A_BL, TestCase_B_BL
from main_package.commonLib import Launch


class Test():
    A_obj = TestCase_A_BL.TestCase_A_BL()
    B_obj = TestCase_B_BL.TestCase_B_BL()
    invoke = Launch.Launch()

    def test_1(self):
        self.A_obj.go_to_page()
        self.A_obj.check_hide()
        self.A_obj.check_number()
        assert self.A_obj.path_of_clicked_buttons() == False, "test1 failed"

    def test_2(self):
        self.A_obj.check_show()
        assert self.A_obj.path_of_clicked_buttons() == True, "test2 failed"

    def test_3(self):
        self.invoke.driver.back()
        self.invoke.driver.back()
        b = self.B_obj.app()
        assert b == True, "test3 failed"


#Command that is being runned in Terminal in order to generate Report.html file
#pytest -v -s --html=Report.html --self-contained-html test_package/test_Module.py














