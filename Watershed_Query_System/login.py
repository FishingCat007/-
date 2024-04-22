import sys
from PyQt5.QtWidgets import *
import sqlite3
from windows import main_window, Login_window, jianjie_window



def showdata(user):
    #filePath = QFileDialog.getExistingDirectory(None, "选择存储路径","DB File (*.db")
    #conn = sqlite3.connect('C:/Users/m1832/Desktop/Watershed_Query_System/DB/urpd.db')
    conn = sqlite3.connect(filePath[0])
    data = conn.execute("select * from urpd where User= '%s'" % user).fetchall()
    conn.close()
    return data

def log_btn_clicked():
    textuser = ui.user_lineEdit
    textpass = ui.password_lineEdit
    data = showdata(user=textuser.text())
    if data:
        #判断密码是否为6位
        if len(textpass.text()) == 6:
            if textpass.text() == data[0][1]:
                QMessageBox.information(None, '提示', '登录成功')
                open_new_win(ui)
                Login_Window.close()
            else:
                QMessageBox.warning(None, '错误', '密码错误')
            
        else:
            QMessageBox.warning(None, '错误', '请输入6位密码')    
    else:
        QMessageBox.warning(None, '错误', '用户名不存在')
    
        
def exit():
    sys.exit()

def open_new_win(self):
    self.new_win = main_window()
    self.new_win.show()


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login_Window = QWidget()
    ui = main_window()
    ui.setupUi(Login_Window)
    Login_Window.setFixedSize(Login_Window.width(), Login_Window.height())
    filePath = QFileDialog.getOpenFileName(None, "选择文件路径")
    Login_Window.show()
    #filePath = QFileDialog.getOpenFileName(None, "选择文件路径")
    ui.login_Button.clicked.connect(log_btn_clicked)
    ui.exit_Button.clicked.connect(exit)
    ui.user_lineEdit.setFocus()
    ui.password_lineEdit.setFocus()
    sys.exit(app.exec_())
