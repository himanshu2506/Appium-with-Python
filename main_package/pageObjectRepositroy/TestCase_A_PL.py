from main_package.commonLib import Launch, XML_Lib


class TestCase_A_PL:
    loc = XML_Lib.XML_Lib()
    invoke = Launch.Launch()

    def select_animation(self):
        icon1 = self.invoke.driver.find_element_by_xpath(self.loc.reader('Animation', 'Locator'))
        return icon1

    def select_hide_show_animation(self):
        icon2 = self.invoke.driver.find_element_by_xpath(self.loc.reader('Hide-ShowAnimations', 'Locator'))
        return icon2

    def select_hide(self):
        icon3 = self.invoke.driver.find_element_by_xpath(self.loc.reader('Hide', 'Locator'))
        return icon3

    def select_button1(self):
        try:
            icon4 = self.invoke.driver.find_element_by_xpath(self.loc.reader('Button1', 'Locator'))
            return icon4
        except:
            return False

    def select_button2(self):
        icon5 = self.invoke.driver.find_element_by_xpath(self.loc.reader('Button2', 'Locator'))
        return icon5

    def select_show_button(self):
        icon6 = self.invoke.driver.find_element_by_xpath(self.loc.reader('ShowButtons', 'Locator'))
        return icon6

