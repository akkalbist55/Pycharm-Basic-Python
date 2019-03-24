from random import randint
from time import sleep
from sys import (exit, argv)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QToolTip, QPushButton, QApplication, QWidget, QLabel)
from PyQt5.QtGui import (QIcon, QPixmap, QFont)

#Creates the main widget which will contain everything else
class coinflipsimulator(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #Creates the QLabel 'coin' which will contain the image of the coin
        self.coin = QLabel(self)
        #Uses QPixmap to place a random coin image (head or tail) into the QLabel 'coin'
        self.coin.setPixmap(QPixmap('coin_' + str(randint(1, 2)) + '.png').scaled(162, 302, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.coin.move(0.5, 0.5)

        #Creates the button that will activate the simulated coin flip when clicked and labels it 'Flip' using QPushButton
        self.btn = QPushButton('Flip', self)
        #Selects the font/font size for the label on the QPushButton 'btn' using QFont
        self.btn.setFont(QFont('SansSerif', 20))
        #Creates a tooltip when user hovers over the QPushButton 'btn' using QToolTip
        self.btn.setToolTip('Click to Flip Coin')
        #Selects the font/font size for the QToolTip above on the QPushButton 'btn' using QFont
        QToolTip.setFont(QFont('SansSerif', 10))
        #Connects the QPushButton 'btn' to the function 'flipcoin' to activate when the button is clicked
        self.btn.clicked.connect(self.flipcoin)
        self.btn.resize(166, 43)
        self.btn.move(-2, 161)

        #Sets where on the screen the window will open and the size of the window respectively using x and y coordinates
        self.setGeometry(1427, 30, 162, 201)
        #Locks the size of the window and make it impossible for the user to change it
        self.setFixedSize(self.size())
        self.setWindowTitle('Coin Flip Simulator!')
        #Sets the window icon to the image file 'icon.png' located in the same folder as the source file
        self.setWindowIcon(QIcon('icon.png'))      
        self.show()

    def flipcoin(self):
        #Sets the image inside the Qlabel 'coin' to a coin flipping animation...aspect ratio is ignored to get the animation to fit inside the window correctly 
        self.coin.setPixmap(QPixmap('coin_flipping_animation.png').scaled(162, 302, Qt.KeepAspectRatio, Qt.FastTransformation))
        #Processes any change made to the program/window in this case the change of the image in the Qlabel 'coin'
        QApplication.processEvents()
        #Pauses the execution of any more code for 0.5 seconds
        sleep(0.5)
        #Sets the image inside the QLabel 'coin' to a random coin image (head or tail) into the QLabel 'coin'
        self.coin.setPixmap(QPixmap('coin_' + str(randint(1, 2)) + '.png').scaled(162, 302, Qt.KeepAspectRatio, Qt.FastTransformation))
        #Processes the second change to the QLabel 'dice'
        QApplication.processEvents()



if __name__ == '__main__':

    #Begins the execution of the QApplication

    app = QApplication(argv)
    ex = coinflipsimulator()
    ex.show()
    exit(app.exec_())  