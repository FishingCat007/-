from PyQt5.QtWidgets import *
import UI.main_ui
import UI.jianjie_ui
import sqlite3
class jianjie_window(UI.jianjie_ui.Ui_Form,QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
class main_window(UI.main_ui.Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.display_page)
        self.pushButton_4.clicked.connect(self.display_page2)
        self.pushButton_3.clicked.connect(self.display_page3)
        self.pushButton_2.clicked.connect(self.display_page1)
        self.pushButton_9.clicked.connect(self.new_display_page)
        self.pushButton_8.clicked.connect(self.new_display_page1)
        self.pushButton_7.clicked.connect(self.new_display_page2)
        self.pushButton_6.clicked.connect(self.new_display_page3)
        self.pushButton_5.clicked.connect(self.new_display_page4)
    
    def new_display_page(self):
        self.new_win = jianjie_window()
        self.new_win.show()
        self.stackedWidget.setCurrentIndex(0)
    def new_display_page1(self):
        self.new_win = jianjie_window()
        self.new_win.show()
        self.new_win.stackedWidget.setCurrentIndex(1)
    def new_display_page2(self):
        self.new_win = jianjie_window()
        self.new_win.show()
        self.new_win.stackedWidget.setCurrentIndex(2)
    def new_display_page3(self):
        self.new_win = jianjie_window()
        self.new_win.show()
        self.new_win.stackedWidget.setCurrentIndex(3)
    def new_display_page4(self):
        self.new_win = jianjie_window()
        self.new_win.show()
        self.new_win.stackedWidget.setCurrentIndex(4)
    def display_page(self):
        self.stackedWidget.setCurrentIndex(0)
    def display_page2(self):
        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_11.clicked.connect(self.findDate_2)
    def display_page3(self):
        self.stackedWidget.setCurrentIndex(3)
    def display_page1(self):
        self.stackedWidget.setCurrentIndex(1)
        self.pushButton_10.clicked.connect(self.findDate)
    def findDate(self):
        #获取DateEdit的日期
        D = self.dateEdit.date().toString("yyyyMM")
        End_D = self.dateEdit_2.date().toString("yyyyMM")
        print(D)
        print(End_D)
        #获取ComboBox的内容
        C = self.comboBox.currentText()
        print(C)
        #数据库操�?
        conn = sqlite3.connect('C:/Users/m1832/Desktop/test_2/jiangshui.db')
        cursor = conn.cursor()
        #cursor.execute('select * from jiangshui where name = "%s" and year between %s and %s '%(C, D, End_D))
        cursor.execute('select * from jiangshui t where (t.year * 100 + t.month) between %s and %s and name = "%s"' % (D, End_D, C))
        data = cursor.fetchall()
        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(data[i][j])))
        conn.close()
    def findDate_2(self):
        #获取DateEdit的日期
        D = self.dateEdit_3.date().toString("yyyyMM")
        End_D = self.dateEdit_4.date().toString("yyyyMM")
        print(D)
        print(End_D)
        #获取ComboBox的内容
        C = self.comboBox_2.currentText()
        print(C)
        #数据库操作
        conn = sqlite3.connect('C:/Users/m1832/Desktop/test_2/jiangshui.db')
        cursor = conn.cursor()
        #cursor.execute('select * from jiangshui where name = "%s" and year between %s and %s '%(C, D, End_D))
        cursor.execute('select * from jiangshui t where (t.year * 100 + t.month) between %s and %s and name = "%s"' % (D, End_D, C))
        data = cursor.fetchall()
        self.tableWidget_2.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.tableWidget_2.setItem(i,j,QTableWidgetItem(str(data[i][j])))
        conn.close()