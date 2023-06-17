import os

import page
import json

# 设置启动
from config import BASE_PATH

desired_caps = {}
# 必填-且正确
desired_caps['platformName'] = 'Android'
# 必填-且正确
desired_caps['platformVersion'] = '7'
# 必填
desired_caps['deviceName'] = 'emulator-5554'
# APP包名
desired_caps['appPackage'] = page.appPackage
# 启动名
desired_caps['appActivity'] = page.appActivity
# windows注意输入键盘编码
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

def dict_to_json(filename):
    file_path = BASE_PATH + os.altsep + "data" + os.altsep + filename

    with open(file_path, "w", encoding='utf-8')as f:
        json.dump(desired_caps, f)

if __name__ == '__main__':
    dict_to_json("app_data_json.json")

