import subprocess

class Encoding():
    def __init__(self, config):
        self.path = config["paths"]["ffmpeg"]
        self.outputs = config["folders"]["outputs"]

    def merge(self, video_path, audio_path):
        output = self.outputs + "merge.mp4"
        return subprocess.run([self.path, "-y", "-i", video_path, "-i", audio_path, "-c:v", "copy", "-c:a", "copy", output]).returncode

    def concat(self, files):
        output_list = self.outputs + "concat.txt"
        output = self.outputs + "concat.mp4"

        with open(output_list, "w") as list:
            for file in files:
                list.write("file '" + file + "'\n")
            list.close()
        return subprocess.run([self.path, "-y", "-f", "concat", "-safe", "0", "-i", output_list, "-c", "copy", output]).returncode