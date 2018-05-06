def Upper():
    def up(xs):
        result = ""
        for x in xs:
            result=result+x.upper()
        return result
    a = input("Enter string that needs to be in uppercase: ")
    print(up(a))

Upper()
import time
time.sleep(30)
