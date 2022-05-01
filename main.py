import os
import sys
import time

from PyQt5.QtWidgets import QMessageBox, QApplication

inexe = lambda: sys.exec_prefix != os.path.dirname(sys.executable)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def msgquest(title: str, msg: str):
    app = QApplication(sys.argv)
    return QMessageBox.question(None, title, msg) == QMessageBox.Yes

def msgbox(title: str, msg: str):
    app = QApplication(sys.argv)
    QMessageBox.information(None, title, msg) 


def launch():
    msgbox("提示", "右键点击通知栏的图标V即可退出")
    os.startfile(os.path.join(BASE_DIR, "core", "v2rayN.exe"))
    time.sleep(5) # 等待启动
    msgbox("提示", "启动完毕")

def main():
    msgbox("FastHoYoLab", "本工具功能仅有加速一些游戏服务, 并无任何后门, 而且开源")
    msgbox("FastHoYoLab", "项目网址: https://github.com/chenmy1903/FastHoYoLab")
    msgbox("协议", "1. 保证不对加速客户端做任何修改\n2. 不用客户端去盈利(放到拼夕夕/淘宝上面买)\n3. 不要试图卡bug去访问违法内容")
    res = msgquest("问题", "同意协议并启动FastHoYoLab?")
    print(res)
    if res == True:
        launch()

if __name__ == "__main__":
    main()
