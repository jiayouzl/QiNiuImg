# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QToolButton,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(426, 429)
        Dialog.setMaximumSize(QSize(426, 429))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        Dialog.setFont(font)
        Dialog.setTabletTracking(False)
        Dialog.setAutoFillBackground(False)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(10, 0, 411, 151))
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 120, 113, 32))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 30, 291, 21))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 101, 21))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 101, 21))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 60, 291, 21))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 101, 21))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(110, 90, 111, 21))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 90, 60, 21))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(290, 90, 113, 21))
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 150, 411, 91))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 30, 111, 21))
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_5 = QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(110, 30, 271, 21))
        self.lineEdit_5.setReadOnly(True)
        self.toolButton = QToolButton(self.groupBox_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(380, 30, 26, 21))
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 60, 113, 32))
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 240, 411, 161))
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 30, 101, 21))
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_6 = QLineEdit(self.groupBox_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(110, 60, 291, 21))
        self.lineEdit_6.setReadOnly(True)
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 60, 101, 21))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_7 = QLineEdit(self.groupBox_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(110, 30, 291, 21))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_8 = QLineEdit(self.groupBox_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(110, 90, 291, 21))
        self.lineEdit_8.setReadOnly(True)
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 90, 101, 21))
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(110, 120, 81, 41))
        self.pushButton_4 = QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(190, 120, 91, 41))
        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(280, 120, 131, 41))
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 400, 101, 31))
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(210, 400, 211, 31))
        self.label_10.setTextFormat(Qt.AutoText)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.baocunanniu1)
        self.toolButton.clicked.connect(Dialog.xuanzetupian)
        self.pushButton_2.clicked.connect(Dialog.shangchuan)
        self.pushButton_3.clicked.connect(Dialog.url)
        self.pushButton_4.clicked.connect(Dialog.html)
        self.pushButton_5.clicked.connect(Dialog.markdown)

        self.pushButton_2.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u4e03\u725b\u56fe\u5e8a v1.0.1", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u53c2\u6570\u914d\u7f6e\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"SecretKey\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"AccessKey\uff1a", None))
        self.lineEdit_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"BucketName\uff1a", None))
        self.lineEdit_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Domain\uff1a", None))
        self.lineEdit_4.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u56fe\u7247\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"image path\uff1a", None))
        self.lineEdit_5.setText("")
        self.toolButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u4f20", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u8fd4\u56de\u7ed3\u679c\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"URL\uff1a", None))
        self.lineEdit_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"HTML\uff1a", None))
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Markdown\uff1a", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u590d\u5236URL", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"\u590d\u5236HTML", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"\u590d\u5236Markdown", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"GitHub\u5f00\u6e90\u5730\u5740", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u5df2\u5f00\u6e90,\u5982\u5bf9\u60a8\u6709\u5e2e\u52a9\u8bf7Star. ", None))
    # retranslateUi

