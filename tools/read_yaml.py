import yaml
from config import BASE_PATH
import os

# 定义函数
def read_yaml(filename):
    file_path = BASE_PATH + os.altsep + "data" + os.altsep + filename
    # 定义空列表，组装测试数据
    arr = []
    # 获取文件流
    with open(file_path, "r", encoding="utf-8")as f:
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))
    # 返回结果
    return arr

if __name__ == '__main__':
    print(read_yaml("tp_login.yaml"))