import sys
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_lable =QLabel("Enter city name", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)
        self.termperature_lable = QLabel(self)
        self.description_lable = QLabel(self)
        self.emoji_lable = QLabel(self) 
        self.intUi()

   
   
   
   
    def intUi(self):
        self.setWindowTitle("Weather app")


        vbox =QVBoxLayout()

        vbox.addWidget(self.city_lable)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.termperature_lable)
        vbox.addWidget(self.emoji_lable)
        vbox.addWidget(self.description_lable)

        self.setLayout(vbox)
        
        self.city_lable.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.termperature_lable.setAlignment(Qt.AlignCenter)
        self.description_lable.setAlignment(Qt.AlignCenter)

        self.city_lable.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.termperature_lable.setObjectName("termperature_lable")
        self.description_lable.setObjectName("description_lable")
        

        self.setStyleSheet("""
            Qlabel, QPushButton{
                 font-family: calibri         
                            }  
                           Qlabel#city_label{
                                font-size: 75px;
                                font-style: italic;
                           }
                           QLineEdit#city_input{
                               font-size: 75px;
                        
                           }
                           QPushButton#get_weather_button{
                              font-size: 75px;
                              font-weight: Bold;
                           }
                           QLabel#temperature_lable{
                                 font-size: 75px;
                           
                           } 
        
                           QLabel#description_lable{
                                 font-size: 69px;
                           }        
                           """)
        
        self.get_weather_button.clicked.connect(self.get_weather)
    def get_weather(self):
        
        api_key="2efee20996af6481e25a6e859fe21034"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try: 

            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        
        
        except requests.exceptions.HTTPError as http_error:
          match response.status_code:
                case 400:
                    self.display_error("Bad request:\nplease check your input")
                case 401:
                    self.display_error("unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not Found:\nCity Not Found")
                case 500:
                    self.display_error("Internel Server Error:\nplease Try Again Later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid Response From Server")
                case 503:
                    self.display_error("Service Unavailable:\nServer Is Down")
                case 504:
                    self.display_error("Gateway Time Out:\nNO response from server")


                case _:
                  self.display_error(f"HTTP error occured\n{http_error} ")

        except requests.exceptions.ConnectionError:
          self.display_error("Connection Error\nCheck Your Internet Connection")
        
        except requests.exceptions.Timeout:
         self.display_error("CTimeout Error/nThe Request Timed Out")
        except requests.exceptions.TooManyRedirects:
          self.display_error("TooManyRedirects\nCheck Your Url")

                  
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")


                                



    def display_error(self, message):
        self.termperature_lable.setStyleSheet("font-size 75px;")
        self.termperature_lable.setText(message)
    def display_weather(self, data):
        
        self.termperature_lable.setStyleSheet("font-size 75px;")
        
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        self.termperature_lable.setText(f"{temperature_c:.0f}℃")
       # self.emoji_lable.setText(self.get_weather_emoji(weather_id))

        self.description_lable.setText(weather_description)

        @staticmethod



        def get_weather_emoji(weather_id):
            if 200 <= weather_id <= 232:
                return "⛈"
            elif 300 <= weather_id <= 321:
                return "🌦️"
            elif 500 <= weather_id <= 531:
                return "🌧️"
            elif 600 <= weather_id <=622:
                return "❄️"
            elif 701 <= weather_id <= 741:
                return "🌁"
            elif weather_id == 762:
                return "🌋"
            elif weather_id == 771:
                return "🌬️"
            elif weather_id == 781:
                return "🌪"
            elif weather_id == 800:
                return "☀️"
            elif 801 <= weather_id <= 804:
                return "☁️"
            else:
                return ""

    
        
            
        
 




        
        

if __name__ =="__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())



































