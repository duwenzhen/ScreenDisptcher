# screenDispatcher
If yon use a large tv screen as a pc monito, this script maybe useful for you.

Below is the config file.
here I divide my 55" tv screen to 4 small screens.

-------------------
|Screen0 | Screen1|
-------------------
|Screen2 | Screen3|
-------------------
width = 2 and height = 2
Default screen is Screen1

And I affect emacs to Screen0
Pycharm to Screen3
ect...

please use "wmctrl -lx" if you need to now the name of your window. The third column is the window id.


{'DefaultWindow': 1,
 'HeightNumber': 2,
 'ScreenByName': {'emacs25.Emacs': 0,
                  'gnome-terminal-server.Gnome-terminal': 0,
                  'google-chrome.Google-chrome': 2,
                  'jetbrains-pycharm-ce.jetbrains-pycharm-ce': 3,
                  'nautilus.Nautilus': 1},
 'WidthNumber': 2}
