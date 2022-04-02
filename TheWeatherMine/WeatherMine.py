#importing modules
#importing modules
import sys 
import requests
import ast
import json
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
units=" °C"
counter=0
jumper=10
class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(340, 340)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 135px;\n"
"	background-color: #0B021E ;\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.container)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(63, 54, 150, 150))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.widget)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"border-radius: 135px")
        pixmap=QPixmap("logo250.png")
        self.labelTitle.setPixmap(pixmap)
        self.labelTitle.resize(pixmap.width(),pixmap.height())
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)


        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))

    # retranslateUi



# GLOBALS
counter = 0
jumper = 10


## ==> SPLASHSCREEN WINDOW
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(15)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## DEF TO LOANDING
    ########################################################################
    def progress (self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = main_window()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1.5

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} #FF009C);
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)


#creating class for mainwindow
class main_window(QMainWindow):
    def __init__(self):
        super().__init__()

        #Main Window Dimensions
        self.setGeometry(0,0,1920,1080)
        self.main_ui()

    
    #defines elements on main window
    def main_ui(self):
        self.setStyleSheet("background-color: #0B021E")
        self.setWindowIcon(QIcon('weathermine4.png'))

        #Creating Logo Label
        self.label=QtWidgets.QLabel(self)
        pixmap=QPixmap('weathermine4.png')
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(),pixmap.height())
        self.label.move(850,20)
        self.label.show()


        #Creating slogan label
        self.slogan=QLabel(self)
        self.slogan.setText("Your weather journey begins here.")
        self.slogan.setStyleSheet("color: #FF009C; font: 57 52pt DIN Alternate")
        self.slogan.adjustSize()
        self.slogan.move(270,400)


        #Creating Settings button
        self.settings_button=QtWidgets.QPushButton(self)
        self.settings_button.setIcon(QtGui.QIcon('fin_settings_icon.png'))
        self.settings_button.resize(100,100)
        self.settings_button.setIconSize(QtCore.QSize(self.settings_button.width(),self.settings_button.height()))
        self.settings_button.move(1600,100)
        self.settings_button.clicked.connect(self.load_settings)



        #Creating Start button
        self.start_button=QtWidgets.QPushButton(self)
        self.start_button.setText("Start")
        self.start_button.move(600,700)
        self.start_button.adjustSize()
        self.start_button.setStyleSheet("QPushButton { background-color: #0B021E; color: #FF009C; font: 57 20pt DIN Alternate; border-radius: 15px; border: None} QPushButton:hover { background-color: #45002A; }")
        self.start_button.clicked.connect(self.load_search)

        #Creating exit button
        self.exit_button=QtWidgets.QPushButton(self)
        self.exit_button.setText("Exit")
        self.exit_button.move(1200,700)
        self.exit_button.adjustSize()
        self.exit_button.setStyleSheet("QPushButton { background-color: #0B021E; color: #FF009C; font: 57 20pt DIN Alternate; border-radius: 15px; border: None} QPushButton:hover { background-color: #45002A; }")
        self.exit_button.clicked.connect(lambda:exit())

    #Loads search window
    def load_search(self):
        #Creating object of search window to load on button click
        self.searchw=search_window()
        self.searchw.search_ui()
        self.close()
        self.searchw.showMaximized()

    def load_settings(self):
        self.sw=settings_window()
        self.sw.settings_ui()
        self.close()
        self.sw.show()

class settings_window(QMainWindow):
    global units
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,1920,1080)
        self.settings_ui()

    def settings_ui(self):
        self.setWindowIcon(QIcon('weathermine4.png'))
        global units
        self.setStyleSheet("background-color: #0B021E")
        #Settings Title Label
        self.settings_label=QtWidgets.QLabel(self)
        self.settings_label.setText("Settings")
        self.settings_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")
        self.settings_label.adjustSize()
        self.settings_label.move(900,100)

        #Units Label
        self.units_label=QtWidgets.QLabel(self)
        self.units_label.setText("Units")
        self.units_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")
        self.units_label.adjustSize()
        self.units_label.move(200,200)

        #Radio Button for Celsius
        self.celsius_button=QtWidgets.QRadioButton("Celsius", self)
        self.celsius_button.move(400,200)
        self.celsius_button.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")
        self.celsius_button.adjustSize()
        self.celsius_button.toggled.connect(self.cel)

        #Radio Button for Fahrenheit
        self.fahrenheit_button=QtWidgets.QRadioButton("Fahrenheit",self)
        self.fahrenheit_button.move(600,200)
        self.fahrenheit_button.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")
        self.fahrenheit_button.adjustSize()
        self.fahrenheit_button.toggled.connect(self.fah)

        #Home button
        self.home_button=QtWidgets.QPushButton(self)
        self.home_button.move(1650,100)
        self.home_button.setIcon(QtGui.QIcon('home_icon.png'))
        self.home_button.resize(100,100)
        self.home_button.setIconSize(QtCore.QSize(self.home_button.width(),self.home_button.height()))
        self.home_button.clicked.connect(self.load_home)

        #about us page
        self.about_us=QLabel(self)
        about="""We are a student duo committed to learn, innovate, create and develop software applications. 
This is our first attempt to make something that could make use of our current knowledge, along with new learning. 
We are open to suggestions, feedback, and recommendations.
Our passion for the software development and the weather inspired us to create our own simple yet practical app. 
You can contact us at: theweathermine@gmail.com. Cheers!"""
        self.about_us.setText("About Us")
        self.about_us.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")
        self.about_us.adjustSize()
        self.about_us.move(200,400)
        
        self.about_us_info=QLabel(self)
        self.about_us_info.setText(about)
        self.about_us_info.setStyleSheet("color: #FF009C; font: 57 15pt DIN Alternate")
        self.about_us_info.setAlignment(QtCore.Qt.AlignJustify)
        self.about_us_info.move(200,500)
        self.about_us_info.adjustSize()

        #Powered by label
        self.pb=QLabel(self)
        self.pb.setText("Powered by")
        self.pb.setStyleSheet("color: #FF009C; font: 57 16pt DIN Alternate")
        self.pb.move(1450, 740)
        self.pb.adjustSize()
        

        #Accuweather logo
        self.accu=QLabel(self)
        pixmap=QPixmap("accu_logo.png")
        self.accu.setPixmap(pixmap)
        self.accu.resize(300,150)
        self.accu.move(1450, 780)


        #donations
        self.donations=QLabel(self)
        self.donations.setText("Support us at theweathermine@gmail.com !\n\nYour support motivates us to create more!\nDonations are welcome and appreciated!")
        self.donations.setStyleSheet("color: #FF009C; font: 57 15pt DIN Alternate")
        self.donations.move(200,750)
        self.donations.adjustSize()
        
        #Info section
        self.info=QLabel(self)
        self.info.setText("Created by: Dhruv Khanna and Ritvik Prakash")
        self.info.setStyleSheet("color: #FF009C; font: 57 15pt DIN Alternate")
        self.info.adjustSize()
        self.info.move(200,700)


        


    #Redirects to main window/home screen
    def load_home(self):
        self.mw=main_window()
        self.close()
        self.mw.showMaximized()

    def cel(self):
        global units
        units=" °C"
    
    def fah(self):
        global units
        units=" °F"

    #Redirects to main window/home screen
    def load_home(self):
        self.mw=main_window()
        self.close()
        self.mw.showMaximized()

class search_window(QMainWindow):
    global units
    def __init__(self):
        super().__init__()

        #Main Window Dimensions
        
        self.setGeometry(0,0,1920,1080)
        self.search_ui()

    def search_ui(self):
        self.setWindowIcon(QIcon('weathermine4.png'))
        self.setStyleSheet("background-color: #0B021E")

        #Creating Logo Label
        #Creating Logo Label
        self.label=QtWidgets.QLabel(self)
        pixmap=QPixmap('weathermine4.png')
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(),pixmap.height())

        self.label.move(825,20)
        self.label.show()

        #Creating Home button
        self.home_button=QtWidgets.QPushButton(self)
        self.home_button.setIcon(QtGui.QIcon('home_icon.png'))
        self.home_button.resize(100,100)
        self.home_button.setIconSize(QtCore.QSize(self.home_button.width(),self.home_button.height()))
        self.home_button.adjustSize()
        self.home_button.move(150,100)
        self.home_button.clicked.connect(self.load_home)

        #Creating Settings button
        self.settings_button=QtWidgets.QPushButton(self)
        self.settings_button.setIcon(QtGui.QIcon('fin_settings_icon.png'))
        self.settings_button.resize(100,100)
        self.settings_button.setIconSize(QtCore.QSize(self.settings_button.width(),self.settings_button.height()))

        self.settings_button.move(1650,100)
        self.settings_button.clicked.connect(self.load_settings)

        #Creating location label
        
        
        self.location_label=QtWidgets.QLabel(self)
        self.location_label.setText("Enter a location:")
        self.location_label.adjustSize()
        self.location_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")
        self.location_label.move(150,300)
        self.location_label.resize(400,30)


        #creating the search box and the search button
        self.location_input=QtWidgets.QLineEdit(self)
        self.location_input.setGeometry(150,400,1400,40)
        self.location_input.setStyleSheet("background-color: #412A73 ; color: #FF009C; font: 57 21pt DIN Alternate; border-radius: 12px;")
        self.search_button=QtWidgets.QPushButton(self)
        self.search_button.setIcon(QtGui.QIcon('search_icon.png'))
        self.search_button.resize(100,100)
        self.search_button.setIconSize(QtCore.QSize(self.search_button.width(),self.search_button.height()))
        self.search_button.move(1650,360)
        self.search_button.clicked.connect(self.load_list)
        

    #Searches for location from api and returns a list of place suggestions for user to choose from
    def load_list(self):
        global items, location, td
        location=self.location_input.text() #Input locatiob by user
        self.location_list=QtWidgets.QListWidget(self) #List widget that lists all the suggested locations(autocomplete)
        self.location_list.setGeometry(150,600,1400,300)
        self.location_list.setStyleSheet("QListWidget { background-color: #412A73 ;color: #FF009C; font: 57 21pt DIN Alternate; border-radius: 12px; } QListWidget::item:hover { background: #2A1B4A; }")
        try:
            #Send request to api to get autocomplete list
            sample=requests.get("http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=9fgIF8kaccBIj9DSsxRVldRn2gOWgWh8&q={}".format(location)).content
            r=sample.decode("utf-8")
            res=r.strip('][').split(', ')
            dic=res[0]
            td=ast.literal_eval(dic) #convert api output to readable format
        
            #Traverse through list to add each element of autocomplete list to list widget
            for i in range(len(td)):
                city=td[i]["LocalizedName"] #name of city
                state=td[i]["AdministrativeArea"]["LocalizedName"] #name of state
                country=td[i]["Country"]["LocalizedName"] #name of country
                place='{}, {}, {}'.format(city,state,country) #string of location dets
                QListWidgetItem(place,self.location_list) #Adding location to list
            
            #Content of Qlistwidget in iterable normal list
            items=[]
            for index in range(self.location_list.count()): #count() gives the number of iterables in list widget
                items.append(self.location_list.item(index).text())
            
            
            self.location_list.show()
            self.location_list.itemClicked.connect(self.click)

        except:
            info_box=QMessageBox()
            info_box.setIcon(QMessageBox.Warning)
            info_box.setText("No such location found!")
            info_box.setStyleSheet("background-color: #0B021E; color: #FF009C; font: 57 20pt DIN Alternate")
            info_box.setStandardButtons(QMessageBox.Ok)
            info_box.exec_() 
    
    #function to get weather data of selected location from api
    def click(self):
        global items, td, units
        Index=self.location_list.currentRow()
        loc=items[Index] #finds what location/element is selected by user
        m=loc.split(', ')
        City=m[0]
        State=m[1]
        Country=m[2]
        #find the key of location
        for i in range(len(td)):
            if td[i]["LocalizedName"]==City and td[i]["AdministrativeArea"]["LocalizedName"]==State and td[i]["Country"]["LocalizedName"]==Country:
                key=td[i]["Key"]


        #finding weather data by using location key
        sample3=requests.get('http://dataservice.accuweather.com/currentconditions/v1/{}?apikey=9fgIF8kaccBIj9DSsxRVldRn2gOWgWh8&details=True'.format(key)).content
        r=sample3.decode("utf-8")
        res=r.strip('][').split(', ')
        d=res[0]
        R=json.loads(d)
        #converting the output of api request to readable format
        global current_temp,real_feel,humidity,windspeed,pressure,ppt,minimum,maximum,weather_status,units
        if units==" °C":
            current_temp=str(R["Temperature"]["Metric"]["Value"])+units
            real_feel=str(R["RealFeelTemperature"]["Metric"]["Value"])+units
            humidity=str(R["RelativeHumidity"])+" %"
            windspeed=str(R["Wind"]["Speed"]["Metric"]["Value"])+" kph"
            pressure=str(R["Pressure"]["Metric"]["Value"])+" mb"
            ppt=str(R["PrecipitationSummary"]["Precipitation"]["Metric"]["Value"])+" mm"
            minimum=str(R["TemperatureSummary"]["Past24HourRange"]["Minimum"]["Metric"]["Value"])+units
            maximum=str(R["TemperatureSummary"]["Past24HourRange"]["Maximum"]["Metric"]["Value"])+units
        
        #Conversion to fahrenheit if units is °F
        else:
            current_temp=str(round((R["Temperature"]["Metric"]["Value"]*9/5)+32,2))+units
            real_feel=str(round((R["RealFeelTemperature"]["Metric"]["Value"]*9/5)+32,2))+units
            humidity=str(R["RelativeHumidity"])+" %"
            windspeed=str(R["Wind"]["Speed"]["Metric"]["Value"])+" kph"
            pressure=str(R["Pressure"]["Metric"]["Value"])+" mb"
            ppt=str(R["PrecipitationSummary"]["Precipitation"]["Metric"]["Value"])+" mm"
            minimum=str(round((R["TemperatureSummary"]["Past24HourRange"]["Minimum"]["Metric"]["Value"]*9/5)+32,2))+units
            maximum=str(round((R["TemperatureSummary"]["Past24HourRange"]["Maximum"]["Metric"]["Value"]*9/5)+32,2))+units
        weather_status=str(R["WeatherText"])
        
        self.info_window=weather_window()
        self.info_window.weather_ui()
        self.close()
        self.info_window.showMaximized()
       
        
    
    #Redirects to main window/home screen
    def load_home(self):
        self.mw=main_window()
        self.mw.main_ui()
        self.close()
        self.mw.showMaximized()

    #Loads settings window
    def load_settings(self):
        #Creating object of settings window to load on button click
        self.sw=settings_window()
        self.sw.settings_ui()
        self.close()
        self.sw.showMaximized()

class weather_window(QMainWindow):
    global current_temp, real_feel, humidity, windspeed, pressure, ppt, minimum, maximum, weather_status, location, desc
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1920,1080)
        self.weather_ui()
        self.showMaximized()
    
    def weather_ui(self):
        self.setWindowIcon(QIcon('weathermine4.png'))
        self.setStyleSheet("background-color: #0B021E")

        desc=''

        if weather_status=='Sunny':
            desc+="It's a bright, sunny day outside."
            pixmap=QPixmap('sunny_icon.png')

        elif weather_status=='Mostly sunny':
            desc+="It's a bright, sunny day with some cloud cover outside."
            pixmap=QPixmap('final_mostly_sunny_icon.png')

        elif weather_status=="Partly sunny":
            desc+="It's a partly sunny day outside."
            pixmap=QPixmap('partly_sunny_icon.png')

        elif weather_status=="Intermittent clouds":
            desc+="It's a partly bright day with some cloud cover outside."
            pixmap=QPixmap('int_clouds_icon.png')

        elif weather_status=="Hazy sunshine":
            desc+="It's a sunny day with some mist outside."
            pixmap=QPixmap("hazy_sun_icon.png")
        
        elif weather_status=="Mostly cloudy":
            desc+="It's a cloudy day with some sunshine outside."
            pixmap=QPixmap("fin_mostly_cloudy_icon.png")

        elif weather_status=="Cloudy":
            desc+="It's a cloudy day outside."
            pixmap=QPixmap("cloudy_icon.png")
        
        elif weather_status=="Dreary (Overcast)":
            desc+="It's an overcast, dreary day outside."
            pixmap=QPixmap("cloudy_icon.png")

        elif weather_status=="Fog":
            desc+="It's a foggy day outside."
            pixmap=QPixmap("fog_icon.png")
        
        elif weather_status=="Showers":
            desc+="There's some light rain outside."
            pixmap=QPixmap("light_rain_icon.png")
        
        elif weather_status=="Mostly cloudy w/ showers":
            desc+="It's a cloudy day with some light rain outside."
            pixmap=QPixmap("light_rain_icon.png")
        
        elif weather_status=="Partly cloudy w/ showers":
            desc+="It's a partly cloudy day with some light rain outside."
            pixmap=QPixmap('pc_w_light_rain_icon.png')

        elif weather_status=="Partly sunny w/ showers":
            desc+="It's a partly bright day with some light rain outside."
            pixmap=QPixmap('pc_w_light_rain_icon.png')

        elif weather_status=="T-Storms":
            desc+="Thunderstorms outside."
            pixmap=QPixmap('tstorms_icon.png')

        elif weather_status=="Mostly cloudy w/ t-Storms":
            desc+="It's a mostly cloudy day with thunderstorms outside."
            pixmap=QPixmap('tstorms_icon.png')
        
        elif weather_status=="Partly cloudy w/ t-Storms":
            desc+="It's a partly cloudy day with thunderstorms outside."
            pixmap=QPixmap('tstorms_icon.png')

        elif weather_status=="Partly sunny w/ t-Storms":
            desc+="It's a partly sunny day with thunderstorms outside."
            pixmap=QPixmap('tstorms_icon.png')
        
        elif weather_status=="Rain":
            desc+="It's a rainy day outside."
            pixmap=QPixmap("light_rain_icon.png")
        
        elif weather_status=="Flurries":
            desc+="There's some light snowfall outside."
            pixmap=QPixmap("snow_icon.png")
        
        elif weather_status=="Mostly cloudy w/ flurries":
            desc+="It's a mostly cloudy day with some light snowfall outside."
            pixmap=QPixmap("snow_icon.png")
        
        elif weather_status=="Partly sunny w/ flurries":
            desc+="It's a partly sunny day with some light snowfall outside."
            pixmap=QPixmap("snow_icon.png")
        
        elif weather_status=="Snow":
            desc+="It's a snowy day outside."
            pixmap=QPixmap("snow_icon.png")

        elif weather_status=="Mostly cloudy w/ snow":
            desc+="It's a mostly cloudy, snowy day outside."
            pixmap=QPixmap("snow_icon.png")
        
        elif weather_status=="Ice":
            desc+="It's an icy day with slippery ground outside."
            pixmap=QPixmap("snow_icon.png")

        elif weather_status=="Sleet":
            desc+="It's an icy day with thin ice outside."
            pixmap=QPixmap("snow_icon.png")
        
        elif weather_status=="Freezing rain":
            desc+="Freezing rain outside."
            pixmap=QPixmap("freezing_rain_icon.png")
        
        elif weather_status=="Rain and snow":
            desc+="It's a rainy and snowy day outside."
            pixmap=QPixmap("freezing_rain_icon.png")
        
        elif weather_status=="Hot":
            desc+="It's a very hot day outside"
            pixmap=QPixmap("fin_hot_icon.png")
        
        elif weather_status=="Cold":
            desc+="It's a very cold day  outside"
            pixmap=QPixmap("cold_icon.png")
        
        elif weather_status=="Windy":
            desc+="It's a very windy day outside"
            pixmap=QPixmap("windy_icon.png")
        
        elif weather_status=="Clear":
            desc+="It's a clear night"
            pixmap=QPixmap("clear_icon.png")
        
        elif weather_status=="Mostly clear":
            desc+="It's mostly clear outside"
            pixmap=QPixmap("mostly_clear_icon.png")
        
        elif weather_status=="Partly cloudy":
            desc+="It's partly cloudy outside"
            pixmap=QPixmap("pc_night_icon.png")
        
        elif weather_status=="Hazy moonlight":
            desc+="It's a misty night"
            pixmap=QPixmap("hazy_moon_icon.png")


        #Creating label with name of place
        self.location_label=QLabel(self)
        self.location_label.setText(location)
        self.location_label.setStyleSheet("color: #FF009C; font: 57 28pt DIN Alternate")
        self.location_label.resize(700,60)
        self.location_label.move(800,50)

        #Creating label "Current Weather"
        self.cw=QLabel(self)
        self.cw.setText("Current Weather")
        self.cw.setStyleSheet("color: #FF009C; font: 57 28pt DIN Alternate")
        self.cw.setGeometry(100,150,500,100)

        #Creating icon for weather icon
        self.icon=QLabel(self)
        self.icon.setGeometry(100,300,200,200)
        self.icon.setPixmap(pixmap)
        self.icon.resize(pixmap.width(),pixmap.height())

        #Creating temperature label
        self.temperature_label = QLabel(self)
        self.temperature_label.setGeometry(550, 300, 350, 40)
        self.temperature_label.setText("Temperature")
        self.temperature_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")


        #Creating real feel label
        self.real_feel_label = QLabel(self)
        self.real_feel_label.setGeometry(550, 400, 350 ,40)
        self.real_feel_label.setText("Real Feel")
        self.real_feel_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")

        #Creating high label
        self.high_label = QLabel(self)
        self.high_label.setGeometry(550, 500, 350,50)
        self.high_label.setText("High")
        self.high_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")

        
        #Creating low label
        self.low_label = QLabel(self)
        self.low_label.setGeometry(550, 600, 350,40)
        self.low_label.setText("Low")
        self.low_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")

        #Creating humidity label
        self.humidity_label=QLabel(self)
        self.humidity_label.setGeometry(1000, 300, 350,50)
        self.humidity_label.setText("Humidity")
        self.humidity_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")


        #Creating wind speed label
        self.wind_speed_label = QLabel(self)
        self.wind_speed_label.setGeometry(1000, 400, 350,40)
        self.wind_speed_label.setText("Wind Speed")
        self.wind_speed_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")


        #Creating precipitation label
        self.ppt_label = QLabel(self)
        self.ppt_label.setGeometry(1000, 500, 350,40)
        self.ppt_label.setText("Precipitation")
        self.ppt_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")

        #Creating pressure label
        self.pressure_label = QLabel(self)
        self.pressure_label.setGeometry(1000, 600, 350,40)
        self.pressure_label.setText("Pressure")
        self.pressure_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")


        #Creating description label
        self.description_label = QLabel(self)
        self.description_label.setGeometry(100, 800, 1111, 91)
        self.description_label.setText(desc)
        self.description_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")



        #Displaying labels with values of data

        #Creating temperature value label
        self.temp_value_label = QLabel(self)
        self.temp_value_label.setGeometry(800, 300, 150, 40)
        self.temp_value_label.setText(current_temp)
        self.temp_value_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")

        #Creating real feel value label
        self.rf_value_label = QLabel(self)
        self.rf_value_label.setGeometry(800, 400, 150,40)
        self.rf_value_label.setText(real_feel)
        self.rf_value_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")

        #Creating high value label
        self.high_value_label = QLabel(self)
        self.high_value_label.setGeometry(800, 500, 150,40)
        self.high_value_label.setText(maximum)
        self.high_value_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")

        #Creating low value label
        self.low_value_label = QLabel(self)
        self.low_value_label.setGeometry(800, 600, 150,40)
        self.low_value_label.setText(minimum)
        self.low_value_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")

        #Creating humidity value label
        self.humidity_value_label = QLabel(self)
        self.humidity_value_label.setGeometry(1300, 310, 150,40)
        self.humidity_value_label.setText(humidity)
        self.humidity_value_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")

        #Creating wind speed value label
        self.wind_speed_value_label = QLabel(self)
        self.wind_speed_value_label.setGeometry(1300, 400, 150,40)
        self.wind_speed_value_label.setText(windspeed)
        self.wind_speed_value_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")

        #Creating precipitaion value label
        self.ppt_value_label = QLabel(self)
        self.ppt_value_label.setGeometry(1300, 503, 150,40)
        self.ppt_value_label.setText(ppt)
        self.ppt_value_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")

        #Creating pressure value label
        self.pressure_value_label = QLabel(self)
        self.pressure_value_label.setGeometry(1300, 600, 150,40)
        self.pressure_value_label.setText(pressure)
        self.pressure_value_label.setStyleSheet("color: #FF009C; font: 57 20pt DIN Alternate")

        #Creating button to go to search window
        self.search_button=QtWidgets.QPushButton(self)
        self.search_button.setIcon(QtGui.QIcon('search_icon.png'))
        self.search_button.resize(100,100)
        self.search_button.setIconSize(QtCore.QSize(self.search_button.width(),self.search_button.height()))
        self.search_button.move(1500,50)
        self.search_button.clicked.connect(self.load_search)

        #Creating Settings button
        self.settings_button=QtWidgets.QPushButton(self)
        self.settings_button.setIcon(QtGui.QIcon('fin_settings_icon.png'))
        self.settings_button.resize(100,100)
        self.settings_button.setIconSize(QtCore.QSize(self.settings_button.width(),self.settings_button.height()))
        self.settings_button.move(1750,50)
        self.settings_button.clicked.connect(self.load_settings)

        

    def load_search(self):
        #Creating object of search window to load on button click
        self.searchw=search_window()
        self.searchw.search_ui()
        self.close()
        self.searchw.showMaximized()

    def load_settings(self):
        #Creating object of settings window to load on button click
        self.sw=settings_window()
        self.sw.settings_ui()
        self.close()
        self.sw.showMaximized()
def main():

    #creating main app
    app=QApplication([])
    app.setQuitOnLastWindowClosed(False)
    app.setWindowIcon(QIcon('weathermine4.png'))
    #creating main window object
    #mw=main_window()
    #mw.showMaximized()
    win=SplashScreen()
    sys.exit(app.exec_()) #Event loop

main()