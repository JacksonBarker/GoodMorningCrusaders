import json, os

class Config:
    defaults ={
        "version": "dev",
        "folders": {
            "inputs": {
                "countdowns": "inputs/countdowns/",
                "music": "inputs/music/",
                "anthems": "inputs/anthems/",
                "acknowledgments": "inputs/acknowledgments/"
            },
            "outputs": "outputs/"
        },
        "paths": {
            "ffmpeg": "ffmpeg"
        }
    }

    def __init__(self, path):
        self.path = path
        try:
            with open(self.path) as file:
                self.config = json.loads(file.read())
                file.close()
        except FileNotFoundError:
            self.config = self.defaults
            self.write()
            
        for f in self.config["folders"]["inputs"]:
            if not os.path.exists(self.config["folders"]["inputs"][f]):
                os.makedirs(self.config["folders"]["inputs"][f])
        if not os.path.exists(self.config["folders"]["outputs"]):
            os.makedirs(self.config["folders"]["outputs"])

    def read(self):
        return self.config

    def write(self):
        with open(self.path, "w") as file:
            file.write(json.dumps(self.config, indent=4))
            file.close()
