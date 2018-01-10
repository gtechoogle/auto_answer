import os
import time
import webbrowser

class Translate(object):
    def __init__(self):
        print (time.time())

        self.screenshot();
        print (time.time())

        self.translate()
        print (time.time())
        self.search()
        print (time.time())
    def search(self):
        command = "http://www.baidu.com.cn/s?wd=" + "晒太阳能够合成以下哪种物质?"
        webbrowser.open(command)

    def translate(self):
        command = "tesseract screen.png output -l chi_sim"
        os.system(command)
    def screenshot(self):
        command = "adb shell screencap -p /sdcard/screen.png"
        os.system(command)
        cwd = os.getcwd()
        command = "adb pull /sdcard/screen.png " + cwd;
        os.system(command)

        

def main():
    translate = Translate()

if __name__ == '__main__':
    main()