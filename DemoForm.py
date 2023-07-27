#DemoForm.py
import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget

#디자인된 문서 로딩
form_lass = uic.loadUiType("DemoForm.ui")[0]
#폼 클래스 정의
class DemoForm(QDialog, form_class):
    #초기화메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")
#직접 모듈을 실행했는지 체크(진입점)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()