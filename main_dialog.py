import os, sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from encoding import Encoding

class MainDialog(QtWidgets.QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.inputs = self.config["folders"]["inputs"]
        self.version = self.config["version"]

        self.setWindowTitle("Good Morning Crusaders [" + self.version + "]")

        layout = QtWidgets.QVBoxLayout()
        check_stretch = QtWidgets.QSizePolicy()

        self.countdown_index = 0
        self.music_index = 0
        self.anthem_index = 0
        self.acknowledgment_index = 0

        countdown_label = QtWidgets.QLabel()
        countdown_label.setFont(QFont("Consolas"))
        countdown_label.setText("Countdown Theme")
        layout.addWidget(countdown_label)
        countdown_selector = QtWidgets.QComboBox()
        countdown_selector.setFont(QFont("Consolas"))
        countdown_selector.addItems(os.listdir(self.inputs["countdowns"]))
        countdown_selector.activated.connect(self.countdown_activated)
        layout.addWidget(countdown_selector)

        music_label = QtWidgets.QLabel()
        music_label.setFont(QFont("Consolas"))
        music_label.setText("Countdown Music")
        layout.addWidget(music_label)
        music_selector = QtWidgets.QComboBox()
        music_selector.setFont(QFont("Consolas"))
        music_selector.addItems(os.listdir(self.inputs["music"]))
        music_selector.activated.connect(self.music_activated)
        layout.addWidget(music_selector)

        anthem_label = QtWidgets.QLabel()
        anthem_label.setFont(QFont("Consolas"))
        anthem_label.setText("Anthem Video")
        layout.addWidget(anthem_label)
        anthem_layout = QtWidgets.QHBoxLayout()
        anthem_check = QtWidgets.QCheckBox()
        anthem_check.setSizePolicy(check_stretch)
        anthem_check.setCheckState(2)  # type: ignore
        anthem_check.stateChanged.connect(self.is_anthem)
        anthem_layout.addWidget(anthem_check)
        self.anthem_selector = QtWidgets.QComboBox()
        self.anthem_selector.setFont(QFont("Consolas"))
        self.anthem_selector.addItems(os.listdir(self.inputs["anthems"]))
        self.anthem_selector.activated.connect(self.anthem_activated)
        anthem_layout.addWidget(self.anthem_selector)
        anthem_widget = QtWidgets.QWidget()
        anthem_widget.setLayout(anthem_layout)
        layout.addWidget(anthem_widget)

        acknowledgment_label = QtWidgets.QLabel()
        acknowledgment_label.setFont(QFont("Consolas"))
        acknowledgment_label.setText("Land acknowledgment")
        layout.addWidget(acknowledgment_label)
        acknowledgment_layout = QtWidgets.QHBoxLayout()
        acknowledgment_check = QtWidgets.QCheckBox()
        acknowledgment_check.setSizePolicy(check_stretch)
        acknowledgment_check.setCheckState(2)  # type: ignore
        acknowledgment_check.stateChanged.connect(self.is_acknowledgment)
        acknowledgment_layout.addWidget(acknowledgment_check)
        self.acknowledgment_selector = QtWidgets.QComboBox()
        self.acknowledgment_selector.setFont(QFont("Consolas"))
        self.acknowledgment_selector.addItems(os.listdir(self.inputs["acknowledgments"]))
        self.acknowledgment_selector.activated.connect(self.acknowledgment_activated)
        acknowledgment_layout.addWidget(self.acknowledgment_selector)
        acknowledgment_widget = QtWidgets.QWidget()
        acknowledgment_widget.setLayout(acknowledgment_layout)
        layout.addWidget(acknowledgment_widget)

        self.play_button = QtWidgets.QPushButton()
        self.play_button.setCheckable(True)
        self.play_button.setText("Play")
        self.play_button.clicked.connect(self.play)
        layout.addWidget(self.play_button)

        self.progress = QtWidgets.QProgressBar()
        self.progress.setTextVisible(False)
        layout.addWidget(self.progress)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def countdown_activated(self, index):
        self.countdown_index = index

    def music_activated(self, index):
        self.music_index = index

    def is_anthem(self, state):
        if state == 2:
            self.anthem_selector.setEnabled(True)
        else:
            self.anthem_selector.setEnabled(False)

    def anthem_activated(self, index):
        self.anthem_index = index

    def is_acknowledgment(self, state):
        if state == 2:
            self.acknowledgment_selector.setEnabled(True)
        else:
            self.acknowledgment_selector.setEnabled(False)

    def acknowledgment_activated(self, index):
        self.acknowledgment_index = index

    def closeEvent(self, event):
        if not self.play_button.isChecked():
            sys.exit(0)

    def play(self):
        try:
            encoding = Encoding(self.config)
            concat = [os.path.abspath(self.config["folders"]["outputs"] + "merge.mp4")]
            if self.anthem_selector.isEnabled() and os.listdir(self.inputs["anthems"]).__len__() > 0:
                concat.append(os.path.abspath(self.inputs["anthems"] + os.listdir(self.inputs["anthems"])[self.anthem_index]))
            if self.acknowledgment_selector.isEnabled() and os.listdir(self.inputs["acknowledgments"]).__len__() > 0:
                concat.append(os.path.abspath(self.inputs["acknowledgments"] + os.listdir(self.inputs["acknowledgments"])[self.acknowledgment_index]))
            self.progress.setValue(int(100 / (concat.__len__() + 1)))
            if encoding.merge(self.inputs["countdowns"] + os.listdir(self.inputs["countdowns"])[self.countdown_index], self.inputs["music"] + os.listdir(self.inputs["music"])[self.music_index]):
                raise Exception()
            self.progress.setValue(int(100 / (concat.__len__())))
            if encoding.concat(concat):
                raise Exception()
            self.progress.setValue(100)
        except:
            QtWidgets.QMessageBox.about(self, "Error", "An encoding error has occured!")
            sys.exit(1)
        self.close()