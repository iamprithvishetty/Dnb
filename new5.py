from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime
import paho.mqtt.client as mqtt
from threading import Thread
import threading
import time
import os, urlparse
import sys
import re
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/drive.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope)
client = gspread.authorize(credentials)
sheet = client.open('question_dnb').sheet1
#from Quiz_template import Ui_QuizWindow
file_object=open('event_data.txt','r')
Event_Data = file_object.read().split('~')
file_object.close()
Event = Event_Data[0]
Date = Event_Data[1]
Venue = Event_Data[2]
photo =[]
c=0
a=0
b=0	
n=0
s=0
data =[]
text = "Correct !!"
#--> Automatic File Read
FolderPath = r'C:\Prithvi\Notice_Board\img\\' #r-->Raw string & Folder path goes here
filename = os.listdir(FolderPath)
length = len(filename)
n = 0
while n!= length-1:
	filename[n] = FolderPath+filename[n]
	n=n+1
photo = filename
#print(photo)
#-->Photos Filename will be saved in an array named 'photo'
class Ui_MainWindow(object): #--> Main Window
    global b
    global c

	
    def openWindow(self):
		global s
		s=0
		def set():
		 global n
		 n=1
	###	 
		global n
		global s    
		timer = threading.Timer(10.0,set)
		timer.start()
		while s!=1:
			if n==1:
				timer.cancel()
				if __name__ == "__main__":
					global app1
					self.window = QtWidgets.QMainWindow()
					app1 = self.window
					self.ui = Ui_QuizWindow()
					self.ui.setupUi(self.window)
					self.window.show()
					b=1
					print(b)
					print(n)
					print(c)
					n=0
					s=1
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_image = QtWidgets.QLabel(self.centralwidget)
        self.background_image.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.background_image.setAutoFillBackground(False)
        self.background_image.setText("")
        self.background_image.setPixmap(QtGui.QPixmap("C:\Users\TOSHIBA\Downloads\DNB_2.jpg"))
        self.background_image.setScaledContents(True)
        self.background_image.setAlignment(QtCore.Qt.AlignCenter)
        self.background_image.setObjectName("background_image")
        self.image_display = QtWidgets.QLabel(self.centralwidget)
        self.image_display.setGeometry(QtCore.QRect(76, 252, 961, 591))
        self.image_display.setAutoFillBackground(False)
        self.image_display.setPixmap(QtGui.QPixmap(photo[a]))
        self.image_display.setScaledContents(True)
        self.image_display.setAlignment(QtCore.Qt.AlignCenter)
        self.image_display.setObjectName("")
        self.quiz_button = QtWidgets.QPushButton(self.centralwidget)
        self.quiz_button.setGeometry(QtCore.QRect(1160, 690, 381, 141))
        self.quiz_button.clicked.connect(self.openWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        self.quiz_button.setFont(font)
        self.quiz_button.setAutoFillBackground(False)
        self.quiz_button.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(37, 79, 146, 255), stop:0.55 rgba(81, 128, 255, 255), stop:0.98 rgba(142, 126, 196, 255), stop:1 rgba(0, 0, 0, 0));\n"
"border-style:solid;\n"
"border-color:white;\n"
"border-width : 3px;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"border-color:black;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 144, 165, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:solid;\n"
"border-width : 3px;\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.quiz_button.setAutoDefault(False)
        self.quiz_button.setObjectName("quiz_button")
        self.event_display = QtWidgets.QLabel(self.centralwidget)
        self.event_display.setGeometry(QtCore.QRect(1176, 420, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setFamily("Times New Roman")
        self.event_display.setFont(font)
        self.event_display.setTextFormat(QtCore.Qt.RichText)
        self.event_display.setScaledContents(True)
        self.event_display.setAlignment(QtCore.Qt.AlignCenter)
        self.event_display.setWordWrap(True)
        self.event_display.setObjectName("event_display")
        self.date_dispaly = QtWidgets.QLabel(self.centralwidget)
        self.date_dispaly.setGeometry(QtCore.QRect(1280, 500, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.date_dispaly.setFont(font)
        self.date_dispaly.setObjectName("date_dispaly")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1180, 500, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1180, 560, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.venue_display = QtWidgets.QLabel(self.centralwidget)
        self.venue_display.setGeometry(QtCore.QRect(1310, 560, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.venue_display.setFont(font)
        self.venue_display.setObjectName("venue_display")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QTimer()
        self.timer.timeout.connect(self._update)
        self.timer.start(1000)
		
		

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image_display.setText(_translate("MainWindow", "TextLabel"))
        self.quiz_button.setText(_translate("MainWindow", "QUIZ"))
        self.event_display.setText(_translate("MainWindow", Event))
        self.date_dispaly.setText(_translate("MainWindow", Date))
        self.label.setText(_translate("MainWindow", "DATE:"))
        self.label_2.setText(_translate("MainWindow", "VENUE:"))
        self.venue_display.setText(_translate("MainWindow", Venue))
	
		
    def _update(self):
        global c
        global a
        global b
        global photo
        MainWindow = QtWidgets.QMainWindow()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image_display.setText(_translate("MainWindow", "TextLabel"))
        self.quiz_button.setText(_translate("MainWindow", "QUIZ"))
        self.event_display.setText(_translate("MainWindow", Event))
        self.date_dispaly.setText(_translate("MainWindow", Date))
        self.label.setText(_translate("MainWindow", "DATE :"))
        self.label_2.setText(_translate("MainWindow", "VENUE :"))
        self.venue_display.setText(_translate("MainWindow", Venue))
        self.image_display.setPixmap(QtGui.QPixmap(photo[a]))
        self.image_display.setScaledContents(True)
		#--> Timer for 10 seconds
        c=c+1
        if c%5 == 0 :
            a=a+1
            if a == len(photo)-1 :
			    a=0
            if c==100 :
			    c=0
		#-->

#################################################################			
				
class Ui_QuizWindow(object):
    def setupUi(self, QuizWindow):
        global counter
        global data
        counter = 10
        QuizWindow.setObjectName("QuizWindow")
        QuizWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(QuizWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 10, 1600, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 220, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.correct = QtWidgets.QLabel(self.centralwidget)
        self.correct.setGeometry(QtCore.QRect(470, 670, 461, 101))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.correct.setFont(font)
        self.correct.setObjectName("correct")
        self.Question_display = QtWidgets.QLabel(self.centralwidget)
        self.Question_display.setGeometry(QtCore.QRect(150, 230, 1231, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Question_display.setFont(font)
        self.Question_display.setTextFormat(QtCore.Qt.AutoText)
        self.Question_display.setScaledContents(True)
        self.Question_display.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Question_display.setWordWrap(True)
        self.Question_display.setIndent(-1)
        self.Question_display.setObjectName("Question_display")
        self.answer_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.answer_1.setGeometry(QtCore.QRect(130, 320, 450, 100))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.answer_1.setFont(font)
        self.answer_1.setObjectName("answer_1")
        self.answer_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.answer_2.setGeometry(QtCore.QRect(130, 410, 450, 100))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.answer_2.setFont(font)
        self.answer_2.setObjectName("answer_2")
        self.answer_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.answer_3.setGeometry(QtCore.QRect(130, 580, 450, 100))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.answer_3.setFont(font)
        self.answer_3.setObjectName("answer_3")
        self.answer_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.answer_4.setGeometry(QtCore.QRect(130, 490, 450, 100))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.answer_4.setFont(font)
        self.answer_4.setObjectName("answer_4")
        self.count_display = QtWidgets.QLCDNumber(self.centralwidget)
        self.count_display.setGeometry(QtCore.QRect(680, 370, 475, 231))
        self.count_display.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.count_display.setProperty("value",counter)
        self.count_display.setObjectName("count_display")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 410, 500, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n""color:white;\n""}")
        self.label_3.setObjectName("label_3")
        QuizWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QuizWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menubar.setObjectName("menubar")
        QuizWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QuizWindow)
        self.statusbar.setObjectName("statusbar")
        QuizWindow.setStatusBar(self.statusbar)
        data = sheet.row_values(random.randint(1,25))
        
        self.retranslateUi(QuizWindow)
        QtCore.QMetaObject.connectSlotsByName(QuizWindow)
        self.timer = QTimer()
        self.timer.timeout.connect(self._update)
        self.timer.start(1000)

    def retranslateUi(self, QuizWindow):
        global data
        _translate = QtCore.QCoreApplication.translate
        QuizWindow.setWindowTitle(_translate("QuizWindow", "MainWindow"))
        self.label_2.setText(_translate("QuizWindow", "Q."))
        self.Question_display.setText(_translate("QuizWindow", data[1]))
        self.answer_1.setText(_translate("QuizWindow", data[2]))
        self.answer_2.setText(_translate("QuizWindow", data[3]))
        self.answer_3.setText(_translate("QuizWindow", data[5]))
        self.answer_4.setText(_translate("QuizWindow", data[4]))
        self.label_3.setText(_translate("QuizWindow", "Time Remaining !"))
        self.correct.setText(_translate("QuizWindow", ""))
		
    def _update(self):
        global counter
        global app1
        global data
        QuizWindow = QtWidgets.QMainWindow()
        _translate = QtCore.QCoreApplication.translate
        QuizWindow.setWindowTitle(_translate("QuizWindow", "MainWindow"))
        self.label_2.setText(_translate("QuizWindow", "Q."))
        self.Question_display.setText(_translate("QuizWindow", data[1]))
        self.answer_1.setText(_translate("QuizWindow", data[2]))
        self.answer_2.setText(_translate("QuizWindow", data[3]))
        self.answer_3.setText(_translate("QuizWindow", data[5]))
        self.answer_4.setText(_translate("QuizWindow", data[4]))
        self.label_3.setText(_translate("QuizWindow", "Time Remaining !"))
        if counter > 0 :
		 counter=counter - 1
		 self.count_display.setProperty("value", counter)
        if counter <= 0:
         counter = counter-1
         if counter < 0:
          if self.answer_1.isChecked() == True:
           if str(self.answer_1.text()) == str(data[6]):
            self.correct.setText(_translate("QuizWindow", text))
           else :
            self.correct.setText(_translate("QuizWindow", "Wrong !!"))
          if self.answer_2.isChecked() == True:
           if str(self.answer_2.text()) == str(data[6]):
            self.correct.setText(_translate("QuizWindow", text))
           else :
            self.correct.setText(_translate("QuizWindow", "Wrong !!"))
          if self.answer_3.isChecked() == True:
           if str(self.answer_3.text()) == str(data[6]):
            self.correct.setText(_translate("QuizWindow", text))
           else :
            self.correct.setText(_translate("QuizWindow", "Wrong !!"))
          if self.answer_4.isChecked() == True:
           if str(self.answer_4.text()) == str(data[6]):
            self.correct.setText(_translate("QuizWindow", text))
           else :
            self.correct.setText(_translate("QuizWindow", "Wrong !!"))
          #else :
           #self.correct.setText(_translate("QuizWindow", "Wrong !!"))
         if counter == -3:
          print(data[6])
          quit()
		  #app.quit()


def quit():
  global app1
  app1.close()
		 

########################################################################

def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(str(msg.payload) )
    if(str(msg.payload)):
        messageReceived = str(msg.payload)
        result = re.search('%1(.*)%2(.*)%3(.*)%4', messageReceived)

        global Event
        global Date
        global Venue
        Event = result.group(1)
        Date = result.group(2)
        Venue = result.group(3)
        file_object=open('event_data.txt','w')
        file_object.write(Event+'~'+Date+'~'+Venue)
        file_object.close()
		
def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

topic = 'notice'

# Connect
mqttc.username_pw_set("shgibuqt", "Kz_94OIvkHf1")
mqttc.connect("m15.cloudmqtt.com", "17310")

# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)		
#--------
def sqImport(tId):
    if tId == 0:
            while 1:
                rc = 0
                while rc == 0:
                    rc = mqttc.loop()
                print("rc: " + str(rc))

    if tId == 1:
        while 1:
             global app
             global MainWindow
             app = QtWidgets.QApplication(sys.argv)
             MainWindow = QtWidgets.QMainWindow()
             ui = Ui_MainWindow()
             ui.setupUi(MainWindow)
             MainWindow.show() 
             sys.exit(app.exec_())
    '''if tId == 2:
		while 1:
			print('8')'''
            	
 			
threadA = Thread(target = sqImport, args=[0])
threadB = Thread(target = sqImport, args=[1])
threadC = Thread(target = sqImport, args=[2])
threadA.start()
threadB.start()
#threadC.start()
threadA.join()
threadB.join()
#threadC.join()
