from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime
import paho.mqtt.client as mqtt
from threading import Thread
import time
import os, urlparse
import sys
import re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 571)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.event = QtWidgets.QLabel(self.centralwidget)
        self.event.setGeometry(QtCore.QRect(36, 22, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.event.setFont(font)
        self.event.setAlignment(QtCore.Qt.AlignCenter)
        self.event.setObjectName("event")
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(40, 140, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.date.setFont(font)
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setObjectName("date")
        self.venue = QtWidgets.QLabel(self.centralwidget)
        self.venue.setGeometry(QtCore.QRect(40, 250, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.venue.setFont(font)
        self.venue.setAlignment(QtCore.Qt.AlignCenter)
        self.venue.setObjectName("venue")
        self.publish1 = QtWidgets.QPushButton(self.centralwidget)
        self.publish1.setGeometry(QtCore.QRect(274, 372, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.publish1.setFont(font)
        self.publish1.setObjectName("publish1")
        self.event_display = QtWidgets.QTextEdit(self.centralwidget)
        self.event_display.setGeometry(QtCore.QRect(263, 10, 491, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.event_display.setFont(font)
        self.event_display.setObjectName("event_display")
        self.date_display = QtWidgets.QTextEdit(self.centralwidget)
        self.date_display.setGeometry(QtCore.QRect(260, 130, 491, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.date_display.setFont(font)
        self.date_display.setObjectName("date_display")
        self.venue_display = QtWidgets.QTextEdit(self.centralwidget)
        self.venue_display.setGeometry(QtCore.QRect(260, 250, 491, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.venue_display.setFont(font)
        self.venue_display.setObjectName("venue_display")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.event.setText(_translate("MainWindow", "EVENT NAME :"))
        self.date.setText(_translate("MainWindow", "DATE :"))
        self.venue.setText(_translate("MainWindow", "VENUE :"))
        self.publish1.setText(_translate("MainWindow", "PUBLISH"))
        self.publish1.clicked.connect(self.publish)

    def publish(self) :
        Event = self.event_display.toPlainText()
        Venue = self.venue_display.toPlainText()
        Date = self.date_display.toPlainText()
        textsend = "%1"+Event+"%2"+Date+"%3"+Venue+"%4"
        mqttc.publish(topic, textsend)


def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

topic = 'notice'

# Connect
mqttc.username_pw_set("shgibuqt", "Kz_94OIvkHf1")
mqttc.connect("m15.cloudmqtt.com", "17310")
# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)

#-------------------------------------------------
#Threading
def sqImport(tId):
    if tId == 0:
        while 1:
            rc = 0
            while rc == 0:
                rc = mqttc.loop()
            print("rc: " + str(rc))

    if tId == 1:
        while 1:
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
                
threadA = Thread(target = sqImport, args=[0])
threadB = Thread(target = sqImport, args=[1])
threadA.start()
threadB.start()
# Do work indepedent of loopA and loopB 
threadA.join()
threadB.join()



