from turtle import width
from PyQt5.QtWidgets import *
from matplotlib import widgets
import numpy as np
from pylab import*
mpl.rcParams['font.sans-serif']=['SimHei']
import UI.main_ui
import UI.login_ui
import UI.jianjie_ui
import sqlite3
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sys

class jianjie_window(UI.jianjie_ui.Ui_Form,QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

class main_window(UI.main_ui.Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plotother()
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
        self.pushButton_12.clicked.connect(self.plotother)
        
    def display_page1(self):
        self.stackedWidget.setCurrentIndex(1)
        self.pushButton_10.clicked.connect(self.findDate)
    def findDate(self):
        #获取DateEdit的日期
        D = self.dateEdit.date().toString("yyyyMM")
        End_D = self.dateEdit_2.date().toString("yyyyMM")
        #print(D)
        #print(End_D)
        #获取ComboBox的内容
        C = self.comboBox.currentText()
        #print(C)
        #数据库操作
        conn = sqlite3.connect('E:/U盘/Watershed_Query_System/DB/jiangshui2.db')
        cursor = conn.cursor()
        #cursor.execute('select * from jiangshui where name = "%s" and year between %s and %s '%(C, D, End_D))
        cursor.execute('select * from jiangshui t where (t.year * 100 + t.month) between %s and %s and name = "%s"' % (D, End_D, C))
        date = cursor.fetchall()
        self.tableWidget.setRowCount(len(date))
        for i in range(len(date)):
            for j in range(len(date[i])):
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(date[i][j])))
        conn.close()
    def findDate_2(self):
        #获取DateEdit的日期
        D = self.dateEdit_6.date().toString("yyyy")
        #print(D)
        #print(End_D)
        #获取ComboBox的内容
        C = self.comboBox_4.currentText()
        #print(C)
        #数据库操作
        conn = sqlite3.connect('E:/U盘/Watershed_Query_System/DB/jiangshui2.db')
        cursor = conn.cursor()
        #cursor.execute('select * from jiangshui where name = "%s" and year between %s and %s '%(C, D, End_D))
        cursor.execute('select * from jiangshui t where year = %s and name = "%s"' % (D, C))
        date = cursor.fetchall()
        self.tableWidget_2.setRowCount(len(date))
        for i in range(len(date)):
            for j in range(len(date[i])):
                self.tableWidget_2.setItem(i,j,QTableWidgetItem(str(date[i][j])))
        #求water平均值
        cursor.execute('select avg(water) from jiangshui t where year = %s and name = "%s"' % (D, C))
        E = cursor.fetchall()
        E = E[0][0]
        #求water最大值的month
        cursor.execute('select month from jiangshui t where year = %s and name = "%s" and water = (select max(cast(water as int)) from jiangshui t where year = %s and name = "%s")' % (D, C, D, C))
        F = cursor.fetchall()
        try:
            F = int(F[0][0])
        except:
            F = None
        #求water最小值的month
        cursor.execute('select month from jiangshui t where year = %s and name = "%s" and water = (select min(cast(water as int)) from jiangshui t where year = %s and name = "%s")' % (D, C, D, C))
        #cursor.execute('select min(water) from jiangshui t where year = %s and name = "%s"' % (D, C))
        G = cursor.fetchall()
        try:
            G = G[0][0]
        except:
            G = None
        if F == None:
            H = "None"
        elif F >= 1 and F <= 3:
            H = '春'
        elif F >= 3 and F <= 6:
            H = '夏'
        elif F >= 6 and F <= 9:
            H = '秋'
        else:
            H = '冬'
        #显示逻辑文字在textBrowser中
        self.textBrowser.setText("%s年%s平均降水量为%sml,降水量最大为%s月份，最小为%s月份，该年%s季容易涨水应当注意防范"%(D,C,E,F,G,H))
        conn.close()
        
    def plot_Date(self):
        #获取DateEdit的日期
        D = self.dateEdit_7.date().toString("yyyy")
        #获取ComboBox的内容
        C = self.comboBox_5.currentText()
        #print(D)
        #print(C)
        #数据库操作
        conn = sqlite3.connect('E:/U盘/Watershed_Query_System/DB/jiangshui2.db')
        cursor = conn.cursor()
        cursor.execute('select * from jiangshui t where year = %s and name = "%s"' % (D, C))
        date = cursor.fetchall()
        conn.close()
        #print(data)
        #print(type(data))
        # 设置图表标题、轴名称等属性
        #ax.set_title("%s雨水情况折线图%s年" % (C, D))
        #ax.set_xlabel("月份")
        #ax.set_ylabel("降水量")
        # list转换为numpy数组
        #x = np.arange(0.0, 5.0, 0.01)
        #y = np.cos(2 * np.pi * x)
        b = [i[2] for i in date]
        c = [i[3] for i in date]
        b = list(map(float,b))
        c = list(map(float,c))
        x = b
        y = c
        #print(type(x))
        #print(type(y))
        #y = [1,2,3,2,5,3,2,23,9,10,11,13]
        #x = [1,2,3,4,5,6,7,8,9,10,11,12]
        # 绘制折线图
        plt.plot(x, y, 'r-', label='the data')
        #ax.plot(x, y, 'r-')

''' def figure_canvas(self):
        #如果有绘图，先清除绘图
        if self.canvas.figure:
            self.canvas.figure.clear()
        #创建一个新的figure
        self.figure = plt.figure()
        #创建一个新的Axes
        self.axes = self.figure.add_subplot(111)
        #调用plot_figure函数
        self.plot_figure(self.axes)
        #设置绘图窗口的标题
        self.canvas.set_window_title("%s雨水情况折线图" % self.comboBox_5.currentText())
        #将figure绘制到绘图窗口
        self.canvas.draw()
        # 创建一个绘图对象
        #fig = plt.figure()
        # 创建一个子图
        #ax = fig.add_subplot()
        # 调用绘图函数
        #ax = self.plot_figure(ax)
        # 创建一个窗口
        #self.canvas = FigureCanvas(fig)
        #self.canvas.draw()
        #显示在groupBox_2的widget中
        self.graphicsView.setLayout(QVBoxLayout())
        self.graphicsView.layout().addWidget(self.canvas)
        plt.close()'''
class MyFigure(FigureCanvasQTAgg):
    def __init__(self,width=5,height=4,dpi = 100):
        # 1、创建一个绘制窗口Figure对象
        self.fig = Figure(figsize=(width,height),dpi=dpi)
        # 2、在父类中激活Figure窗口,同时继承父类属性
        super(MyFigure, self).__init__(self.fig)
    def plotSin(self,x,y):
        self.axes0 = self.fig.add_subplot(111)
        self.axes0.plot(x,y)
    def plotother(self,x,y):
        F1 = MyFigure(5,4,100)
        F1.axes1 = F1.fig.add_subplot(111)

        x = np.arange(0, 50)
        y = np.random.randn(50)
        F1.axes1.plot(x, y)
        F1.axes1.set_title("%s雨水情况折线图" % self.comboBox_5.currentText())

        width,height = self.graphicsView.size().width(),self.graphicsView.height()
        F1.resize(width,height)

        self.scene = QGraphicsScene()
        self.scene.addWidget(F1)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    sys.exit(app.exec_())


