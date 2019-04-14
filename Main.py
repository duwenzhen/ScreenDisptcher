import subprocess as s
import socket
import os
import Config



def getCurrentResolution():
    p=s.Popen(["wmctrl","-d"], stdout=s.PIPE)
    out, err = p.communicate()
    outputs = out.decode("utf-8").split("\n")
    resolution = outputs[0].split("WA: ")[1].split(" ")[1].split("x")
    position = outputs[0].split("WA: ")[1].split(" ")[0].split(",")
    print(resolution)
    return (int(position[0]), int(position[1]), int(resolution[0]), int(resolution[1]))

def ActionWindow(windows, config):
    for window in windows:
        if window[1] in config.ScreenByName:
            screen = config.ScreenByName[window[1]]
        else:
            screen = config.DefaultWindow
        dim = config.DimensionByScreen[screen]
        arg = "-ir " + window[0] + " -e 0," + str(dim[0]) + "," + str(dim[1]) + "," + str(dim[2]) + "," + str(dim[3])
        os.system("wmctrl " + arg)



def getWindows():
    p=s.Popen(["wmctrl","-lx"], stdout=s.PIPE)
    out, err = p.communicate()
    outputs = out.decode("utf-8").split("\n")
    computername = socket.gethostname()
    windows = []
    for l in outputs:
        if computername in l:
            id = l[0:10]
            windowName = l.split(" ")[3]
            print(windowName)
            windows.append((id,windowName))
    return windows


def getConfig(resolution):
    config = Config.Config()
    #config.loadConf(resolution)
    config.loadConfFromFile(resolution)
    #config.saveConf()
    return config



if __name__ == '__main__':
    resolution = getCurrentResolution()
    windows = getWindows()
    config = getConfig(resolution)
    ActionWindow(windows,config)
