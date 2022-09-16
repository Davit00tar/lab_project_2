import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic.properties import QtGui
from validator import isemail, isurl, isdate, isnumber, iscard, isphone


file_name = ''

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100, 100, 500, 250)
    win.setWindowTitle("DATA VALIDATOR")

# TEXT1
    lbl_file = QtWidgets.QLabel(win)
    lbl_file.setText('Enter the data ')
    lbl_file.move(200, 0)

# TEXT2
    lbl_destination = QtWidgets.QLabel(win)
    lbl_destination.setText('Data type')
    lbl_destination.move(220, 80)

# BOX1
    text = QtWidgets.QLineEdit(win)
    text.move(200, 40)




# BUTTON EMAIL
    btn_email = QtWidgets.QPushButton(win)
    btn_email.setText('EMAIL')
    btn_email.move(150, 120)

# BUTTON WEB URL
    btn_web = QtWidgets.QPushButton(win)
    btn_web.setText('WEB URL')
    btn_web.move(270, 120)

    # BUTTON DATE
    btn_date = QtWidgets.QPushButton(win)
    btn_date.setText('DATE')
    btn_date.move(150, 160)

    # BUTTON NUMBER
    btn_number = QtWidgets.QPushButton(win)
    btn_number.setText('NUMBER')
    btn_number.move(270, 160)

    # BUTTON CREDIT CARD
    btn_credit_card = QtWidgets.QPushButton(win)
    btn_credit_card.setText('CREDIT CARD ')
    btn_credit_card.move(150, 200)

    # BUTTON PHONE NUMBER
    btn_phone_num = QtWidgets.QPushButton(win)
    btn_phone_num.setText('PHONE NUM')
    btn_phone_num.move(270, 200)



# CLICKING
    def clicked_email(self):
        print('clicked email')
        print(isemail(text.text()))



    def clicked_web(self):
        print('clicked web')
        print(isurl(text.text()))

    def clicked_date(self):
        print('clicked date')
        print(isdate(text.text()))

    def clicked_number(self):
        print('clicked number')
        print(isnumber(text.text()))

    def clicked_card(self):
        print('clicked credit card')
        print(iscard(text.text()))

    def clicked_phone(self):
        print('clicked credit card')
        print(isphone(text.text()))




    btn_email.clicked.connect(clicked_email)
    btn_web.clicked.connect(clicked_web)
    btn_date.clicked.connect(clicked_date)
    btn_number.clicked.connect(clicked_number)
    btn_credit_card.clicked.connect(clicked_card)
    btn_phone_num.clicked.connect(clicked_phone)
    win.show()
    sys.exit(app.exec())

window()