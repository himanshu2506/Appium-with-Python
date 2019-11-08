
class CommonUtils:

    def click(self, go):
        try:
            if go is not None:
                go.click()
                return True
            else:
                print("Null parameter found in click method")
                return False
        except NameError:
            print('An Exception Occurred in click method')
            return False



