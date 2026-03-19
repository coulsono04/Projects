
# This project creates a real time digital alarm clock using widgets.



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


#Contructing entites for the clock
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        #time label
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

# Layout of digital clock
    def initUI(self):
        # Sets a title for the window
        self.setWindowTitle("Digital Clock")
        # Sets the size of the window
        self.setGeometry(600, 400, 300, 100)

        #arranges widets vertically
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        #sets the lael to be centrally aligned horizntally
        self.time_label.setAlignment(Qt.AlignCenter)

        #Formats the time label
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "font-family: Ariel;"
                                      "color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color: black;")

        #gets it to updatetime every 1s (1000ms)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    #To add current time, finds it, converts it to string, formats it and adds AM or PM
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    #argv = arguments
    app = QApplication(sys.argv)
    clock = DigitalClock()
    #shows clock but for a second
    clock.show()
    #access module of sys.  does execture methods
    sys.exit(app.exec_())