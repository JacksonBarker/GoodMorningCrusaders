# Good Morning Crusaders
Good Morning Crusaders simplifies the responsibilities of the St. Mary Catholic Secondary School morning announcements graphics coordinator by allowing for any combination of countdown graphic, background music, national anthem, and land acknowledgment to be played automatically.
## Requirements
 - VLC Media Player installed in the default location.
 - FFmpeg defined in path, or "ffmpeg" binary path set in config.json. (e.g. "/usr/bin/ffmpeg")
## Run instructions
```
# w/ Pipenv (Recommended)
pip install pipenv # If required
pipenv install
pipenv run python GoodMorningCrusaders.py

# w/o Pipenv (Not recommended)
pip install -r requirements.txt
python GoodMorningCrusaders.py
```
## Build instructions
 - *Build output is in "dist/" **not** "build/".*
 - *Files will be written to execution directory **not** executable directory.*
```
# w/ Pipenv (Recommended)
pip install pipenv # If required
pipenv install --dev
pipenv run pyinstaller --onefile --windowed GoodMorningCrusaders.py

# w/o Pipenv (Not recommended)
pip install -r dev-requirements.txt
pyinstaller GoodMorningCrusaders.py
```
## Attribution
Good Morning Crusaders' source code makes use of a modified version of [PyQt5 example for VLC Python bindings](pyqt5vlc.py) from [Python bindings for libvlc](https://git.videolan.org/git/vlc/bindings/python.git) and originally licensed under the terms of the GNU General Public License version 2, as published by the Free Software Foundation. VideoLAN, VLC, and VLC media player are trademarks internationally registered by the [VideoLAN non-profit organization](https://www.videolan.org/videolan/).

Good Morning Crusaders is not endorsed by VideoLAN project.