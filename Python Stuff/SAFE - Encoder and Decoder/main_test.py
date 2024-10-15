#
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#  Keyword: Test
# ['t', 'e', 's',' a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'u', 'v', 'w', 'x', 'y', 'z']
#


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def __init__(self):

        # List with the alphabet we use to encrypt.
        self.alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']
        
        # Will contain an altered copy of the alphabet list above.
        self.encrypted_alphabet = []

        # The key we use as a basis to encrypt
        self.cipher_key = ""

        # The text to encrypt
        self.input_text = ""

        # The finished product
        self.output_text = ""


    # When a button in the UI is clicked, we go to this function
    def clicked(self, action):
        print(action)

        # If we click encode/decode buttons
        if action == "Encode" or action == "Decode":

            # Get input from text fields in the app
            self.input_text = (self.input.toPlainText())
            self.cipher_key = (self.cipher_2.text())

            # Use that input to make an altered alphabet list.
            self.make_encrypted_alphabet()

            if action == "Encode":
                self.encode_text(self.alphabet, self.encrypted_alphabet)

            if action == "Decode":
                self.encode_text(self.encrypted_alphabet, self.alphabet)

        if action == "save":
            self.save_data()

        if action == "load":
            self.retrive_data()

        if action == "clear":
            self.input.clear()
            self.output.clear()
            self.cipher_2.clear()



    # Encrypt using a Keyword Cipher
    def encode_text(self, list1, list2):
        print("encoding:", self.input_text)
        text = list(self.input_text.lower())
        new_word = ""
        for letter in text:
            found = False
            for index in range(len(list1)):
                if letter == list1[index]:
                    new_word += list2[index]
                    found = True

            # If no match is found, we just add the letter, 
            # which will in this case always be a symbol or weird letter.
            if found == False:
                new_word += letter
                found = False

        # Write the new word into the output textfield
        self.output_text = new_word
        self.output.setPlainText(self.output_text)


    # Make an altered alphabet list based on given keyword.
    def make_encrypted_alphabet(self):
        # Remove spaces
        phrase = self.cipher_key.replace(" ", "")

        # Remove duplicates, while keeping the same order
        phrase = list(dict.fromkeys(phrase))
        
        # Make new list with alpabet, minus the phrase letters
        empty_list = []
        for item in self.alphabet:
            if item not in phrase:
                empty_list.append(item)
        
        # Combine the two lists
        self.encrypted_alphabet = phrase + empty_list


    # Boilerplate PyQt5-setup, mostly from the Designer app.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 482)
        MainWindow.setFixedSize(755, 482)
        MainWindow.setStyleSheet("\n"
            "QPushButton{\n"
            "    background-color:#404249;\n"
            "    color: #FBEAEB;\n"
            "}\n"
            "\n"
            "QMainWindow#MainWindow{\n"
            "    background-color:#313338;\n"
            "}\n"
            "\n"
            "QLabel{\n"
            "    color: White;\n"
            "}\n"
            "\n"
            "QTextEdit{\n"
            "    background-color:#383a40;\n"
            "    color:white;\n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "    background-color:#383a40;\n"
            "    color:white;\n"
            "}")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.title_3 = QtWidgets.QLabel(self.centralwidget)
        self.title_3.setGeometry(QtCore.QRect(430, 60, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title_3.setFont(font)
        self.title_3.setAlignment(QtCore.Qt.AlignCenter)
        self.title_3.setObjectName("title_3")
        self.cipher_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.cipher_2.setGeometry(QtCore.QRect(430, 110, 291, 51))
        self.cipher_2.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cipher_2.setFont(font)
        self.cipher_2.setObjectName("cipher_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 381, 421))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title_1 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title_1.setFont(font)
        self.title_1.setAlignment(QtCore.Qt.AlignCenter)
        self.title_1.setObjectName("title_1")
        self.verticalLayout_3.addWidget(self.title_1)

        self.input = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.input.setObjectName("input")
        self.verticalLayout_3.addWidget(self.input)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.title_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title_2.setFont(font)
        self.title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2.setObjectName("title_2")
        self.verticalLayout.addWidget(self.title_2)

        self.output = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.output.setEnabled(True)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output.setFont(font)
        self.verticalLayout.addWidget(self.output)

        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.encode = QtWidgets.QPushButton(self.centralwidget)
        self.encode.setGeometry(QtCore.QRect(480, 230, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.encode.setFont(font)
        self.encode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.encode.setObjectName("encode")
        self.decode = QtWidgets.QPushButton(self.centralwidget)
        self.decode.setGeometry(QtCore.QRect(480, 320, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.decode.setFont(font)
        self.decode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.decode.setObjectName("decode")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")
        self.menuLoad_text_from_file = QtWidgets.QMenu(self.menubar)
        self.menuLoad_text_from_file.setObjectName("menuLoad_text_from_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.load = QtWidgets.QAction(MainWindow)
        self.load.setObjectName("load")
        self.menuLoad_text_from_file.addAction(self.load)

        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.menuLoad_text_from_file.addAction(self.save)

        self.clear = QtWidgets.QAction(MainWindow)
        self.clear.setObjectName("clear")  
        self.menuLoad_text_from_file.addAction(self.clear)
        
        self.menubar.addAction(self.menuLoad_text_from_file.menuAction())

        self.click_logic()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # More boilerplate PyQt5 stuff
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "A Chuchred Software"))
        self.title_3.setText(_translate("MainWindow", "Write cipher key"))
        self.title_1.setText(_translate("MainWindow", "Input text:"))
        self.title_2.setText(_translate("MainWindow", "Output text:"))
        self.encode.setText(_translate("MainWindow", "Encode"))
        self.decode.setText(_translate("MainWindow", "Decode"))
        self.menuLoad_text_from_file.setTitle(_translate("MainWindow", "File"))
        self.load.setText(_translate("MainWindow", "Load"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.clear.setText(_translate("MainWindow", "Clear"))

    # Assign logic to what fucntion will rund when the buttons are clicked
    def click_logic(self):
        self.decode.clicked.connect(lambda: self.clicked("Decode"))
        self.encode.clicked.connect(lambda: self.clicked("Encode"))
        self.statusbar.addAction(self.load)
        self.statusbar.addAction(self.save)
        self.statusbar.addAction(self.clear)
        self.load.triggered.connect(lambda: self.clicked("load"))
        self.save.triggered.connect(lambda: self.clicked("save"))
        self.clear.triggered.connect(lambda: self.clicked("clear"))


    def retrive_data(self):
        try:
            with open("input.txt", "r") as file: 
                self.input_text = file.read()  
                self.input.setPlainText(self.input_text)
                file.close()
        except Exception as e:
            with open("input.txt", "w") as file: 
                file.close()

    def save_data(self):
        with open("output.txt", "w") as file: 
            file.write(self.output_text)
            file.close()



# PyQt5 setup
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
