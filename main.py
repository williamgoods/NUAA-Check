import time

import requests
import logging
import os
import datetime
import json
from encrypt import AES_decrypt

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

sckey = os.getenv("SCKEY")
key = os.getenv("KEY")


def send(message):
    url = 'https://sctapi.ftqq.com/{}.send'.format(sckey)
    params = dict()
    params['text'] = 'i南航打卡'
    time_now = datetime.datetime.now() + datetime.timedelta(hours=8)  # 转换成中国时间
    message = time_now.strftime("%Y-%m-%d %H:%M:%S\n\n   ") + message
    params['desp'] = message
    response = requests.post(url, params)
    response.encoding = 'utf-8'

    if response.status_code != 200:
        logger.warning("请求错误，错误信息:{}".format(response.status_code))
        raise AssertionError("无法发送消息")

    if response.json()['code'] != 0:
        logger.warning("API调用错误，错误信息:{}".format(response.json()))
        raise AssertionError("无法发送消息")
    else:
        logger.info("发送消息成功")


def generte_sh():
    path = os.getcwd()
    encrypt_file = os.path.join(path, "encrypt.txt")
    if not os.path.exists(encrypt_file):
        AssertionError("数据文件不存在")
    with open(encrypt_file, "r") as f:
        content = f.read()
    content = AES_decrypt(key, content)
    with open(os.path.join(path, "main.sh"),"w") as f:
        index = content.find("date=")
        if index == -1:
            AssertionError("数据文件错误，请重新复制浏览器请求")
        content = content[0:index+5] + datetime.datetime.now().strftime("%Y%m%d") + content[index+13:]
        index = content.find("created=")
        if index == -1:
            AssertionError("数据文件错误，请重新复制浏览器请求")
        content = content[0:index + 8] + str(int(time.time())) + content[index + 18:]
        f.write(content)

def check():
    generte_sh()
    # path = os.getcwd()
    # bash = "bash "+os.path.join(path,"main.sh")
    # result = os.popen(bash).read()
    # logger.info(result)
    # result = json.loads(result)
    # if result['e'] == 0:
    #     send("打卡成功")
    # else:
    #     send("打卡失败:"+result['m'])


if __name__ == "__main__":

    try:
        check()
    except Exception as err:
        send("打卡失败，程序错误，" + repr(err))
        logger.critical("打卡失败，程序错误，" + repr(err))
