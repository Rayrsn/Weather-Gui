# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather_guidqMSwS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import time
from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import images_rc

import os,json,tempfile,sys

global tempdir
# Generate a random file name
tempdir = tempfile.gettempdir()+"/data-weather-gui.json"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 750)
        icon = QIcon()
        icon.addFile(u":/Icon/icon.gif", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #22232a;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.topframe = QFrame(self.centralwidget)
        self.topframe.setObjectName(u"topframe")
        self.topframe.setGeometry(QRect(23, 71, 404, 239))
        self.topframe.setStyleSheet(u"border: 3px solid white;\n"
"border-radius: 25px;\n"
"background-color: rgba(217, 217, 217, 64);")
        self.topframe.setFrameShape(QFrame.StyledPanel)
        self.topframe.setFrameShadow(QFrame.Raised)
        self.line_2 = QFrame(self.topframe)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(1, 141, 117, 1))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.topframe)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(118, 2, 1, 234))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.topframe)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(285, 2, 1, 234))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.weatherconicon = QLabel(self.topframe)
        self.weatherconicon.setObjectName(u"weatherconicon")
        self.weatherconicon.setGeometry(QRect(134, 14, 136, 127))
        self.weatherconicon.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 15px;\n"
"background-color: transparent;")
        hour = time.localtime().tm_hour
        if hour < 6 or hour > 18:
                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/clear-night.png"))
        else:
                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/clear-day.png"))
        self.weatherconicon.setScaledContents(True)
        self.weatherconicon.setFrameShape(QFrame.StyledPanel)
        self.weatherconicon.setFrameShadow(QFrame.Raised)
        self.tempicon = QLabel(self.topframe)
        self.tempicon.setObjectName(u"tempicon")
        self.tempicon.setGeometry(QRect(37, 30, 50, 50))
        self.tempicon.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;")
        self.tempicon.setPixmap(QPixmap(u":/MainGUI/temperature.png"))
        self.tempicon.setScaledContents(True)
        self.tempvalue = QLabel(self.topframe)
        self.tempvalue.setObjectName(u"tempvalue")
        self.tempvalue.setGeometry(QRect(0, 80, 118, 61))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        self.tempvalue.setFont(font1)
        self.tempvalue.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.humidicon = QLabel(self.topframe)
        self.humidicon.setObjectName(u"humidlabelicon")
        self.humidicon.setGeometry(QRect(308, 30, 70, 70))
        self.humidicon.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;")
        self.humidicon.setPixmap(QPixmap(u":/MainGUI/humidity.png"))
        self.humidicon.setScaledContents(True)
        self.humidvalue = QLabel(self.topframe)
        self.humidvalue.setObjectName(u"humidlabel")
        self.humidvalue.setGeometry(QRect(285, 160, 118, 40))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        self.humidvalue.setFont(font1)
        self.humidvalue.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.humidicontext = QLabel(self.topframe)
        self.humidicontext.setObjectName(u"humidlabelicontext")
        self.humidicontext.setGeometry(QRect(360, 162, 30, 30))
        font2 = QFont()
        font2.setPointSize(10)
        self.humidicontext.setFont(font2)
        self.humidicontext.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;")
        self.humidicontext.setPixmap(QPixmap(u":/MainGUI/humidity2.png"))
        self.humidicontext.setScaledContents(True)
        self.weathercondtext = QLabel(self.topframe)
        self.weathercondtext.setObjectName(u"weathercondtext")
        self.weathercondtext.setGeometry(QRect(134, 169, 136, 41))
        font3 = QFont()
        font3.setPointSize(20)
        self.weathercondtext.setFont(font3)
        self.weathercondtext.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.realfeel = QLabel(self.topframe)
        self.realfeel.setObjectName(u"realfeel")
        self.realfeel.setGeometry(QRect(14, 142, 91, 31))
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        font4.setWeight(75)
        self.realfeel.setFont(font4)
        self.realfeel.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.reelfeelvalue = QLabel(self.topframe)
        self.reelfeelvalue.setObjectName(u"reelfeelvalue")
        self.reelfeelvalue.setGeometry(QRect(0, 190, 118, 20))
        self.reelfeelvalue.setFont(font1)
        self.reelfeelvalue.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(15, 331, 420, 1))
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.cityframe = QFrame(self.centralwidget)
        self.cityframe.setObjectName(u"cityframe")
        self.cityframe.setGeometry(QRect(24, 350, 152, 71))
        self.cityframe.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 11px")
        self.cityframe.setFrameShape(QFrame.StyledPanel)
        self.cityframe.setFrameShadow(QFrame.Raised)
        self.cityicon = QLabel(self.cityframe)
        self.cityicon.setObjectName(u"cityicon")
        self.cityicon.setGeometry(QRect(10, 10, 55, 55))
        self.cityicon.setPixmap(QPixmap(u":/MainGUI/city.png"))
        self.cityicon.setScaledContents(True)
        self.cityvalue = QLabel(self.cityframe)
        self.cityvalue.setObjectName(u"cityvalue")
        self.cityvalue.setGeometry(QRect(60, -1, 91, 71))
        self.cityvalue.setFont(font1)
        self.cityvalue.setStyleSheet(u"border: 0px solid white;\n"
"color: rgb(54, 57, 63);\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.countryframe = QFrame(self.centralwidget)
        self.countryframe.setObjectName(u"countryframe")
        self.countryframe.setGeometry(QRect(24, 438, 152, 71))
        self.countryframe.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 11px")
        self.countryframe.setFrameShape(QFrame.StyledPanel)
        self.countryframe.setFrameShadow(QFrame.Raised)
        self.countryicon = QLabel(self.countryframe)
        self.countryicon.setObjectName(u"countryicon")
        self.countryicon.setGeometry(QRect(10, 10, 55, 55))
        self.countryicon.setPixmap(QPixmap(u":/MainGUI/country.png"))
        self.countryicon.setScaledContents(True)
        self.countryvalue = QLabel(self.countryframe)
        self.countryvalue.setObjectName(u"countryvalue")
        self.countryvalue.setGeometry(QRect(60, -1, 91, 71))
        self.countryvalue.setFont(font1)
        self.countryvalue.setWordWrap(True) 
        self.countryvalue.setStyleSheet(u"border: 0px solid white;\n"
"color: rgb(54, 57, 63);\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.populationframe = QFrame(self.centralwidget)
        self.populationframe.setObjectName(u"populationframe")
        self.populationframe.setGeometry(QRect(202, 350, 225, 116))
        self.populationframe.setStyleSheet(u"border: 3px solid white;\n"
"border-radius: 25px;\n"
"background-color: rgba(217, 217, 217, 64);")
        self.populationframe.setFrameShape(QFrame.StyledPanel)
        self.populationframe.setFrameShadow(QFrame.Raised)
        self.populationicon = QLabel(self.populationframe)
        self.populationicon.setObjectName(u"populationicon")
        self.populationicon.setGeometry(QRect(50, 10, 41, 41))
        self.populationicon.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.populationicon.setPixmap(QPixmap(u":/MainGUI/population.png"))
        self.populationicon.setScaledContents(True)
        self.population = QLabel(self.populationframe)
        self.population.setObjectName(u"population")
        self.population.setGeometry(QRect(100, 20, 91, 40))
        self.population.setFont(font1)
        self.population.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.populationvalue = QLabel(self.populationframe)
        self.populationvalue.setObjectName(u"populationvalue")
        self.populationvalue.setGeometry(QRect(70, 60, 91, 40))
        self.populationvalue.setFont(font1)
        self.populationvalue.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.locationinfo = QFrame(self.centralwidget)
        self.locationinfo.setObjectName(u"locationinfo")
        self.locationinfo.setGeometry(QRect(23, 525, 225, 190))
        self.locationinfo.setStyleSheet(u"border: 3px solid white;\n"
"border-radius: 25px;\n"
"background-color: rgba(217, 217, 217, 64);")
        self.locationinfo.setFrameShape(QFrame.StyledPanel)
        self.locationinfo.setFrameShadow(QFrame.Raised)
        self.latitude = QLabel(self.locationinfo)
        self.latitude.setObjectName(u"longitude")
        self.latitude.setGeometry(QRect(30, 20, 121, 40))
        self.latitude.setFont(font1)
        self.latitude.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.longitude = QLabel(self.locationinfo)
        self.longitude.setObjectName(u"longitude2")
        self.longitude.setGeometry(QRect(30, 75, 121, 40))
        self.longitude.setFont(font1)
        self.longitude.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.pressure = QLabel(self.locationinfo)
        self.pressure.setObjectName(u"pressure")
        self.pressure.setGeometry(QRect(30, 130, 121, 40))
        self.pressure.setFont(font1)
        self.pressure.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.latitudevalue = QLabel(self.locationinfo)
        self.latitudevalue.setObjectName(u"longitudevalue")
        self.latitudevalue.setGeometry(QRect(130, 20, 93, 40))
        self.latitudevalue.setFont(font1)
        self.latitudevalue.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.pressurevalue = QLabel(self.locationinfo)
        self.pressurevalue.setObjectName(u"pressurevalue")
        self.pressurevalue.setGeometry(QRect(130, 130, 93, 40))
        self.pressurevalue.setFont(font1)
        self.pressurevalue.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.longitudevalue = QLabel(self.locationinfo)
        self.longitudevalue.setObjectName(u"longitude2value")
        self.longitudevalue.setGeometry(QRect(130, 75, 93, 40))
        self.longitudevalue.setFont(font1)
        self.longitudevalue.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.windframe = QFrame(self.centralwidget)
        self.windframe.setObjectName(u"windframe")
        self.windframe.setGeometry(QRect(260, 476, 159, 239))
        self.windframe.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 11px")
        self.windframe.setFrameShape(QFrame.StyledPanel)
        self.windframe.setFrameShadow(QFrame.Raised)
        self.windicon = QLabel(self.windframe)
        self.windicon.setObjectName(u"windicon")
        self.windicon.setGeometry(QRect(50, 0, 55, 55))
        self.windicon.setPixmap(QPixmap(u":/MainGUI/wind.png"))
        self.windicon.setScaledContents(True)
        self.winddirection = QLabel(self.windframe)
        self.winddirection.setObjectName(u"winddirection")
        self.winddirection.setGeometry(QRect(30, 50, 91, 40))
        self.winddirection.setFont(font1)
        self.winddirection.setStyleSheet(u"border: 0px solid white;\n"
"color: rgb(54, 57, 63);\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"")
        self.winddirectionvalue = QLabel(self.windframe)
        self.winddirectionvalue.setObjectName(u"winddirectionvalue")
        self.winddirectionvalue.setGeometry(QRect(30, 80, 91, 40))
        self.winddirectionvalue.setFont(font1)
        self.winddirectionvalue.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"color: rgb(54, 57, 63);\n"
"")
        self.windspeed = QLabel(self.windframe)
        self.windspeed.setObjectName(u"windspeed")
        self.windspeed.setGeometry(QRect(30, 140, 91, 40))
        self.windspeed.setFont(font1)
        self.windspeed.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"color: rgb(54, 57, 63);\n"
"")
        self.windspeedvalue = QLabel(self.windframe)
        self.windspeedvalue.setObjectName(u"windspeedvalue")
        self.windspeedvalue.setGeometry(QRect(30, 170, 91, 40))
        self.windspeedvalue.setFont(font1)
        self.windspeedvalue.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 0px;\n"
"background-color: transparent;\n"
"color: rgb(54, 57, 63);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(14, 13, 431, 31))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.searchbar = QLineEdit(self.frame)
        self.searchbar.setObjectName(u"searchbar")
        self.searchbar.setGeometry(QRect(0, 0, 416, 31))
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.searchbar.setFont(font5)
        self.searchbar.setStyleSheet(u"QLineEdit {\n"
"border:4px outset white;\n"
"border-radius: 8px;\n"
"background-color: rgb(150, 150, 150);\n"
"padding-left:5px;\n"
"color: #22232a;\n"
"}\n"
"QLineEdit:focus{\n"
"border:4px outset white;\n"
"border-radius: 8px;\n"
"background-color: rgb(112, 112, 112);\n"
"padding-left:5px;\n"
"color: #22232a;\n"
"}")
        self.searchbutton = QPushButton(self.frame)
        self.searchbutton.setObjectName(u"searchbutton")
        self.searchbutton.setGeometry(QRect(365, 0, 51, 31))
        self.searchbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchbutton.setStyleSheet(u"QPushButton{\n"
"border:4px outset;\n"
"background-color: rgb(150, 150, 150);\n"
"border-color: white white white transparent;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:pressed{\n"
"border:4px outset;\n"
"background-color: rgb(121, 121, 121);\n"
"border-color: white white white transparent;\n"
"border-radius: 8px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/MainGUI/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchbutton.setIcon(icon1)
        self.searchbutton.setIconSize(QSize(20, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.searchbutton.clicked.connect(self.getinfo)
        self.searchbar.returnPressed.connect(self.getinfo)
        

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Weather-GUI", None))
        self.tempvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">N/A</span></p></body></html>", None))
        self.humidvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">N/A</p></body></html>", None))
        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Clear</p></body></html>", None))
        self.realfeel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Real Feel</p></body></html>", None))
        self.reelfeelvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">N/A</p></body></html>", None))
        self.cityicon.setText("")
        self.cityvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">city</p></body></html>", None))
        self.countryicon.setText("")
        self.countryvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">country</p></body></html>", None))
        self.populationicon.setText("")
        self.population.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Population</p></body></html>", None))
        self.populationvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">N/A</p></body></html>", None))
        self.latitude.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Latitude</p></body></html>", None))
        self.longitude.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Longitude</p></body></html>", None))
        self.pressure.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.latitudevalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">N/A</p></body></html>", None))
        self.longitudevalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">N/A</p></body></html>", None))
        self.pressurevalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">N/A hPa</p></body></html>", None))
        self.windicon.setText("")
        self.winddirection.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Direction</p></body></html>", None))
        self.winddirectionvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">N/A</p></body></html>", None))
        self.windspeed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Speed</p></body></html>", None))
        self.windspeedvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">N/A km/h</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.searchbar.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.searchbar.setText("")
        self.searchbar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for city...", None))
        self.searchbutton.setText("")
        MainWindow.setFixedSize(MainWindow.size())
    # retranslateUi

    def getinfo(self):
        jsonList = []
        jsonList.clear()
        with open(tempdir,'w') as f:
                if sys.platform == "win32":
                        f.write(os.popen('.\\weather-Cli get '+ self.searchbar.text() + ' --raw').read())
                else:
                        f.write(os.popen('./weather-Cli get '+ self.searchbar.text() + ' --raw').read())
        with open (tempdir, "r") as f:
                for jsonObj in f:
                        jsonDict = json.loads(jsonObj)
                        jsonList.append(jsonDict)
        self.setinfo(jsonList)

    def setinfo(self,jsonList):
        
        self.cityvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">"+jsonList[0]["name"]+"</p></body></html>", None))
        self.countryvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">"+jsonList[0]["country"]+"/"+jsonList[0]["admin1"]+"</p></body></html>", None))
        self.longitudevalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">"+str(jsonList[0]["latitude"])+"</p></body></html>", None))
        self.latitudevalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">"+str(jsonList[0]["longitude"])+"</p></body></html>", None))
        self.populationvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">"+str("{:,}".format(jsonList[0]["population"]))+"</p></body></html>", None))

        self.tempvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">"+str(jsonList[1]["current_weather"]["temperature"])+"°C"+"</span></p></body></html>", None))
        self.humidvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">"+str(round(jsonList[1]["hourly"]["relativehumidity_2m"],2))+"</p></body></html>", None))
        self.reelfeelvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">"+str(round(jsonList[1]["hourly"]["apparent_temperature"],1))+"°C"+"</p></body></html>", None))
        self.pressurevalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">"+str(round(jsonList[1]["hourly"]["surface_pressure"],2))+" hPa"+"</p></body></html>", None))
        self.winddirectionvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">"+str(jsonList[1]["current_weather"]["winddirection"])+"°"+"</p></body></html>", None))
        self.windspeedvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">"+str(jsonList[1]["current_weather"]["windspeed"])+" km/h"+"</p></body></html>", None))
        match jsonList[1]["current_weather"]["windspeed"]:
                case 0:
                        if time.localtime().tm_hour < 6 or time.localtime().tm_hour > 18:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/clear-night.png"))
                        else:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/clear-day.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Clear Sky</p></body></html>", None))
                case 1:
                        if time.localtime().tm_hour < 6 or time.localtime().tm_hour > 18:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/mainlyclear-night.png"))
                        else:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/mainlyclear-day.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Mainly Clear</p></body></html>", None))
                case 2:
                        if time.localtime().tm_hour < 6 or time.localtime().tm_hour > 18:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/partlycloudy-night.png"))
                        else:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/partlycloudy-day.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Partly Cloudy</p></body></html>", None))
                case 3:
                        if time.localtime().tm_hour < 6 or time.localtime().tm_hour > 18:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/overcast-night.png"))
                        else:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/overcast-day.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Overcast</p></body></html>", None))
                case 45:
                        if time.localtime().tm_hour < 6 or time.localtime().tm_hour > 18:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/fog-night.png"))
                        else:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/fog-day.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Fog</p></body></html>", None))

                case 48:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/rime-fog.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Depositing Rime Fog</p></body></html>", None))

                case 51:
                        if time.localtime().tm_hour < 6 or time.localtime().tm_hour > 18:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/drizzle-light-night.png"))
                        else:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/drizzle-light-day.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Light Drizzle</p></body></html>", None))
                case 53:
                        if time.localtime().tm_hour < 6 or time.localtime().tm_hour > 18:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/drizzle-moderate-night.png"))
                        else:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/drizzle-moderate-day.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Moderate Drizzle</p></body></html>", None))
                case 55:
                        if time.localtime().tm_hour < 6 or time.localtime().tm_hour > 18:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/drizzle-dense-night.png"))
                        else:
                                self.weatherconicon.setPixmap(QPixmap(u":/Conditions-Time-Based/conditions/timebased/drizzle-dense-day.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Dense Drizzle</p></body></html>", None))

                case 56:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/freezing-drizzle-light.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Light Freezing Drizzle</p></body></html>", None))
                case 57:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/freezing-drizzle-dense.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Dense Freezing Drizzle</p></body></html>", None))
                case 61:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/rain-slight.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Slight Rain</p></body></html>", None))
                case 63:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/rain-moderate.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Moderate Rain</p></body></html>", None))
                case 65:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/rain-heavy.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Heavy Rain</p></body></html>", None))
                case 66:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/freezing-rain-light.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Light Freezing Rain</p></body></html>", None))
                case 67:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/freezing-rain-heavy.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Heavy Freezing Rain</p></body></html>", None))
                case 71:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/snow-slight.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Slight Snow Fall</p></body></html>", None))
                case 73:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/snow-moderate.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Moderate Snow Fall</p></body></html>", None))
                case 75:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/snow-heavy.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Heavy Snow Fall</p></body></html>", None))
                case 77:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/snow-grains.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Snow Grains</p></body></html>", None))
                case 80:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/showers-slight.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Slight Rain Showers</p></body></html>", None))
                case 81:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/showers-moderate.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Moderate Rain Showers</p></body></html>", None))
                case 82:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/showers-violent.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Violent Rain Showers</p></body></html>", None))
                case 85:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/snow-showers-slight.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Slight Snow Showers</p></body></html>", None))
                case 86:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/snow-showers-heavy.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Heavy Snow Showers</p></body></html>", None))
                case 95:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/thunderstorm.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Thunderstorm</p></body></html>", None))
                case 96:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/thunderstorm-hail-light.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Thunderstorm With Light Hail</p></body></html>", None))
                case 99:
                        self.weatherconicon.setPixmap(QPixmap(u":/Conditions/conditions/thunderstorm-hail-heavy.png"))
                        self.weathercondtext.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Thunderstorm With Heavy Hail</p></body></html>", None))

