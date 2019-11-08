from main_package.commonLib import Launch, XML_Lib


class TestCase_B_PL:
    loc = XML_Lib.XML_Lib()
    invoke = Launch.Launch()

    def select_app(self):
        icon7 = self.invoke.driver.find_element_by_xpath(self.loc.reader('App','Locator'))
        return icon7

    def select_action_bar(self):
        icon8 = self.invoke.driver.find_element_by_xpath(self.loc.reader('ActionBar','Locator'))
        return icon8

    def select_display_options(self):
        icon9 = self.invoke.driver.find_element_by_xpath(self.loc.reader('DisplayOptions','Locator'))
        return icon9

    def select_display_show_title(self):
        icon0 = self.invoke.driver.find_element_by_xpath(self.loc.reader('Display_Show_Title','Locator'))
        return icon0

    def select_view(self):
        icon = self.invoke.driver.find_element_by_xpath(self.loc.reader('View','Locator'))
        return icon


