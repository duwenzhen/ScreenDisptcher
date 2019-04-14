import math
import json
import os
import pprint

class Config:
    def __init__(self):
        self.HeightNumber = 1
        self.WidthNumber = 1
        self.ScreenByName = {}
        self.DimensionByScreen = {}
        self.DefaultWindow = 1

    def loadConf(self, resolution):
        self.HeightNumber = 2
        self.WidthNumber = 2
        self.Width = int(math.floor(resolution[2] / self.WidthNumber))
        self.Height = int(math.floor(resolution[3] / self.HeightNumber))
        for w in range(self.WidthNumber):
            for h in range(self.HeightNumber):
                self.DimensionByScreen[w + h * self.WidthNumber] = (resolution[0] + w * self.Width, resolution[1] + h * self.Height, self.Width-5, self.Height-5)
        self.ScreenByName["google-chrome.Google-chrome"] = 2
        self.ScreenByName["gnome-terminal-server.Gnome-terminal"] = 0
        self.ScreenByName["jetbrains-pycharm-ce.jetbrains-pycharm-ce"] = 3
        self.ScreenByName["nautilus.Nautilus"] = 1
        self.ScreenByName["emacs25.Emacs"] = 0
        print(self.DimensionByScreen)

    def loadConfFromFile(self, resolution):
        cwd = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(cwd, "config.json")) as f:
            configObject = json.load(f)
            pprint.pprint(configObject)
        self.HeightNumber = configObject["HeightNumber"]
        self.WidthNumber = configObject["WidthNumber"]
        width = int(math.floor(resolution[2] / self.WidthNumber))
        height = int(math.floor(resolution[3] / self.HeightNumber))
        for w in range(self.WidthNumber):
            for h in range(self.HeightNumber):
                self.DimensionByScreen[w + h * self.WidthNumber] = (resolution[0] + w * width, resolution[1] + h * height, width-5, height-5)
        self.ScreenByName = configObject["ScreenByName"]

    def saveConf(self):
        configObject = {}
        configObject["HeightNumber"] = self.HeightNumber
        configObject["WidthNumber"] = self.WidthNumber
        configObject["ScreenByName"] = self.ScreenByName
        configObject["DefaultWindow"] = self.DefaultWindow
        with open('config.json', 'w') as outfile:
            json.dump(configObject, outfile)