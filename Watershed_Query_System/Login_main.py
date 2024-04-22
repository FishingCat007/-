import sys
from PyQt5.QtWidgets import *
import sqlite3
import UI.login_ui
import UI.main_ui
from windows import main_window


class Login_window(UI.login_ui.Ui_Form,QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.setFixedSize(self.width(), self.height())
        self.login_Button.clicked.connect(self.log_btn_clicked)
        self.exit_Button.clicked.connect(exit)

    #数据库链接
    def showdata(self):
        #filePath = QFileDialog.getExistingDirectory(None, "选择存储路径","DB File (*.db")
        #conn = sqlite3.connect('C:/Users/m1832/Desktop/Watershed_Query_System/DB/urpd.db')
        #filePath = QFileDialog.getOpenFileName(None, "选择文件路径")
        user = self.user_lineEdit.text()
        conn = sqlite3.connect(filePath[0])
        data = conn.execute("select * from urpd where User= '%s'" % user).fetchall()
        conn.close()
        return data

    def log_btn_clicked(self):
        textpass = self.password_lineEdit
        data = self.showdata()
        if data:
            #判断密码是否为6位
            if len(textpass.text()) == 6:
                if textpass.text() == data[0][1]:
                    QMessageBox.information(self, '提示', '登录成功')
                    self.open_new_win()
                    window.close()
                else:
                    QMessageBox.warning(self, '错误', '密码错误')
                
            else:
                QMessageBox.warning(self, '错误', '请输入6位密码')    
        else:
            QMessageBox.warning(self, '错误', '用户名不存在')

    def open_new_win(self):
        self.new_win = main_window()
        self.new_win.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    filePath = QFileDialog.getOpenFileName(None, "选择文件路径")
    window = Login_window()
    sys.exit(app.exec_())