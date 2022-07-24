#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import plistlib
import sys
from datetime import datetime

import qiniu.config
import qtawesome as qta
from PySide6.QtWidgets import (QApplication, QFileDialog, QMessageBox, QPushButton, QWidget)
from qiniu import Auth, etag, put_file

from ui import Ui_Dialog


# print(os.path.join(os.environ.get("HOME", "~"), "Library/Preferences"))#/Users/zhanglei/Library/Preferences


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()

        self.ui.baocunanniu1 = self.baocunanniu1
        self.ui.xuanzetupian = self.xuanzetupian
        self.ui.shangchuan = self.shangchuan
        self.ui.url = self.url
        self.ui.html = self.html
        self.ui.markdown = self.markdown

        self.ui.setupUi(self)

        # 设置按钮的图标
        upload_icon = qta.icon('fa.save')
        self.ui.pushButton.setIcon(upload_icon)

        upload_icon = qta.icon('ei.upload')
        self.ui.pushButton_2.setIcon(upload_icon)

        copy_icon = qta.icon('fa.copy')
        self.ui.pushButton_3.setIcon(copy_icon)
        self.ui.pushButton_4.setIcon(copy_icon)
        self.ui.pushButton_5.setIcon(copy_icon)

        # 将标签变为超级链接框
        self.ui.label_9.setText(chr(0xf0c1) + " " + "<a style='color:#5589C5;text-decoration:none' href=\"https://github.com/jiayouzl/QiNiuImg\">开源地址")
        self.ui.label_9.setOpenExternalLinks(True)  # 使其成为超链接
        # 设置标签图标
        # TODO:这里的fa是图标库的名称
        self.ui.label_9.setFont(qta.font('fa', 13))
        self.ui.label_9.setStyleSheet("color: blue;")  # 设置图标为蓝色

        # 调用Drops方法
        self.setAcceptDrops(True)

        # 读取配置文件
        try:
            result = self.plist_read(self.get_resource_path('Config/com.zhenglei.qiniu.plist'))
            # 取列表数量
            count = len(result['ProgramArguments'])
            print(result['ProgramArguments'])
            self.ui.lineEdit.setText(result['ProgramArguments'][0])
            self.ui.lineEdit_2.setText(result['ProgramArguments'][1])
            self.ui.lineEdit_3.setText(result['ProgramArguments'][2])
            self.ui.lineEdit_4.setText(result['ProgramArguments'][3])
        except Exception as e:
            print('抛出异常:', e)

    def get_resource_path(self, relative_path):
        """
        获取文件绝对路径，MacOS下用PyInstaller打包需要。
        """
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def plist_write(self, data, file_name):
        """
        保存plist文件
        """
        with open(file_name, 'wb') as f:
            plistlib.dump(data, f)

    def plist_read(self, file_name):
        """
        读取plist文件
        """
        with open(file_name, mode='rb') as f:
            return plistlib.loads(f.read())

    def create_plist(self):
        """
        创建plist配置文件
        """
        file_name = 'com.zhenglei.qiniu.plist'
        data = {'Label': file_name, 'ProgramArguments': [self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text()]}
        self.plist_write(data, self.get_resource_path('Config/' + file_name))

    # 鼠标拖入事件
    def dragEnterEvent(self, evn):
        # print('鼠标拖入窗口了')
        # print('文件路径：' + evn.mimeData().text())
        self.ui.lineEdit_5.setText(evn.mimeData().text().replace('file://', ''))
        # 鼠标放开函数事件
        evn.accept()

    # 鼠标放开执行
    def dropEvent(self, evn):
        # print('鼠标放开')
        pass

    def dragMoveEvent(self, evn):
        # print('鼠标移入')
        pass

    def baocunanniu1(self):
        if self.ui.lineEdit.text() == '' or self.ui.lineEdit_2.text() == '' or self.ui.lineEdit_3.text() == '' or self.ui.lineEdit_4.text() == '':
            QMessageBox.warning(self, '提示', '请输入完整的配置信息！')
        else:
            self.create_plist()
            QMessageBox.information(self, "提示", "配置保存成功！")

    def xuanzetupian(self):
        print('选择图片被点击')
        fileName, filetype = QFileDialog.getOpenFileName(self, caption="选取文件", dir=os.path.expanduser('~/Pictures/iShot截屏'),
                                                         filter="All Files (*);;Text Files (*.txt);;Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(fileName, filetype)
        self.ui.lineEdit_5.setText(fileName)

    def shangchuan(self):
        if self.ui.lineEdit.text() == '' or self.ui.lineEdit_2.text() == '' or self.ui.lineEdit_3.text() == '' or self.ui.lineEdit_4.text() == '':
            QMessageBox.warning(self, '提示', '缺失配置信息！')
            return
        if self.ui.lineEdit_5.text() == '':
            QMessageBox.warning(self, "提示", "请选择文件！")
            return
        # print('上传被点击')
        # 代码开始
        # 绑定的域名
        domain = self.ui.lineEdit_4.text()
        # 需要填写你的 Access Key 和 Secret Key
        access_key = self.ui.lineEdit.text()
        print(access_key)
        secret_key = self.ui.lineEdit_2.text()
        print(secret_key)
        # 构建鉴权对象
        q = Auth(access_key, secret_key)
        # 要上传的空间
        bucket_name = self.ui.lineEdit_3.text()
        # 要上传文件的本地路径
        localfile = self.ui.lineEdit_5.text()
        # 生成当前日期
        date = datetime.now().strftime('%Y%m%d')
        # 上传后保存的文件名
        key = date + '/' + os.path.basename(localfile)  # 获取本文件名
        print(key)
        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key, 3600)
        try:
            ret, info = put_file(up_token=token, key=key, file_path=localfile, hostscache_dir=self.get_resource_path('cache/'), version='v2')
            print(ret)
            # print(info)

            # assert ret['key'] == key
            # assert ret['hash'] == etag(localfile)
            # print(ret['key'])
            # print(ret['hash'])

            if ret['key'] == key and ret['hash'] == etag(localfile):
                print('上传成功')
                resultUrl = domain + ret['key']
                print(resultUrl)
                # pyperclip.copy(f'<img src="{resultUrl}" style="zoom:100%;" />')
                self.ui.lineEdit_7.setText(resultUrl)
                self.ui.lineEdit_6.setText(f'<img src="{resultUrl}" style="zoom:100%;" />')
                self.ui.lineEdit_8.setText(f'![]({resultUrl})')
                QMessageBox.information(self, "提示", "上传成功！")
            else:
                QMessageBox.warning(self, "提示", "上传失败，请重试！")
        except Exception as e:
            QMessageBox.critical(self, "提示", '上传失败，请重试！\n' + str(e))
        # 代码结束

    def url(self):
        # 复制URL
        self.ui.lineEdit_7.selectAll()
        self.ui.lineEdit_7.copy()

    def html(self):
        # 复制HTML
        self.ui.lineEdit_6.selectAll()
        self.ui.lineEdit_6.copy()

    def markdown(self):
        # 复制Markdown
        self.ui.lineEdit_8.selectAll()
        self.ui.lineEdit_8.copy()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
