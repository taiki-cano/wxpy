# -*- coding : <utf-8> -*-
# main.py

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="パネル配置", size=(800, 600))
        self.SetBackgroundColour('#000000')
        self.InitializeComponents()
        self.Show()

    def InitializeComponents(self):
        self.mainPanel = wx.Panel(self, -1, size=(600, 400), style=wx.BORDER_SIMPLE)
        self.mainPanel.SetBackgroundColour('#FFFFFF')
        maindisplay = MainDisplay(self)
        subdisplay = SubDisplay(self)
        toolbox = ToolBox(self)

        sizer = wx.GridBagSizer()
        sizer.Add(maindisplay, (0, 0), (1, 2), flag=wx.EXPAND)
        sizer.Add(subdisplay, (0, 2), (1, 1), flag=wx.EXPAND)
        sizer.Add(toolbox, (1, 0), (1, 2), flag=wx.EXPAND)

        self.mainPanel.SetSizer(sizer)


class MainDisplay(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        displaypanel = wx.Panel(parent.mainPanel, -1, pos=(0, 0), size=(250, 250))
        displaypanel.SetBackgroundColour('#FF0000')


class SubDisplay(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent.mainPanel, -1, pos=(250, 0), size=(150, 150))
        self.SetBackgroundColour('#00FF00')


class ToolBox(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent.mainPanel, -1, pos=(0, 250), size=(50, 50))
        self.SetBackgroundColour('#0000FF')


if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()
