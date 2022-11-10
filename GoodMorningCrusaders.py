import os, sys
from PyQt5 import QtWidgets
from config import Config
from main_dialog import MainDialog

CONFIG_PATH = "config.json"

def main():
    global config
    config = Config(CONFIG_PATH).read()
    os.environ["FFMPEG_PATH"] = config["paths"]["ffmpeg"]

    app = QtWidgets.QApplication(sys.argv)
    main_dialog = MainDialog(config)
    main_dialog.resize(700, 350)
    main_dialog.show()
    app.exec_()
    if sys.platform.startswith('linux'):
        os.environ.setdefault('PYTHON_VLC_MODULE_PATH', "/usr/lib64/vlc/plugins")
    from pyqt5vlc import Player
    player = Player()
    player.showFullScreen()
    player.open_file(config["folders"]["outputs"] + "concat.mp4")
    app.exec_()

if __name__ == "__main__":
    main()