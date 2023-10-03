import requests, sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow, QVBoxLayout
from PyQt6.QtGui import QPixmap,QDesktopServices
from PyQt6.QtCore import Qt, QUrl

app = QApplication(sys.argv)

# What's for dinner?.... Loading... Slim J, Meal


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Dinner Time by Slim Jesus')
        self.setFixedSize(450,300)
        self.img = QPixmap('dinner-time/images/slim.jpg')
        self.main = QLabel(self, text="what's for dinner?")
        self.fetch_api
        self.button = QPushButton(text="Maybe...?")
        self.food = QLabel()
        self.video = ''
        self.button.pressed.connect(self.fetch_api)
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.main)
        layout.addWidget(self.food)
        layout.addWidget(self.button)
        self.main.setAlignment(Qt.AlignmentFlag.AlignHCenter)        

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)    
    
    
    def fetch_api(self):
        self.main.setPixmap(self.img)
        response = requests.get('https://themealdb.com/api/json/v1/1/random.php')
        if response.status_code == 200:
            json_data = response.json()
            self.search_keys(json_data)
        
    def search_keys(self, json_data):
        meal = json_data['meals'][0]['strMeal']
        video = json_data['meals'][0]['strYoutube']
        self.food.setText(meal)
        self.video = "<a href=" + video + '>' + meal + "!</a>"
        print(self.video)

    
        
window = MainWindow()
window.show()
app.exec()

