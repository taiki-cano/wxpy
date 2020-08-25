# -*- coding : <utf-8> -*-
# main.py

import wx

from pubsub import pub


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='wxpy')
        self.Show()


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)


def main():
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()


if __name__ == '__main__':
    main()
