# -*- coding : <utf-8> -*-
# main.py

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="パネル配置", size=(800, 600))
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        mainPanel = wx.Panel(self, -1, style=wx.BORDER_SIMPLE)
        main_sizer.Add(mainPanel, -1, wx.EXPAND)

        main_display = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_SIMPLE)
        main_display.SetBackgroundColour('#FF0000')
        sub_display = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_SIMPLE)
        sub_display.SetBackgroundColour('#00FF00')
        tool_box = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_SIMPLE)
        tool_box.SetBackgroundColour('#0000FF')

        sizer = wx.BoxSizer(wx.VERTICAL)
        upper_sizer = wx.BoxSizer(wx.HORIZONTAL)
        upper_sizer.Add(main_display, wx.ID_ANY, wx.EXPAND)
        upper_sizer.Add(tool_box, wx.ID_ANY, wx.EXPAND)
        sizer.Add(upper_sizer, wx.ID_ANY, wx.EXPAND)
        sizer.Add(sub_display, wx.ID_ANY, wx.EXPAND)

        mainPanel.SetSizer(sizer)
        self.SetSizer(main_sizer)


class MainDisplay(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        displaypanel = wx.Panel(parent.mainPanel)
        displaypanel.SetBackgroundColour('#FF0000')


class SubDisplay(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        subdisplaypanel = wx.Panel(parent.mainPanel)
        self.SetBackgroundColour('#00FF00')


class ToolBox(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        toolboxpanel = wx.Panel(parent.mainPanel)
        self.SetBackgroundColour('#0000FF')


if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
