# -*- coding : <utf-8> -*-
# main.py

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, id=-1, title="パネル配置", size=(800, 600))
        self.InitializeComponents()

    def InitializeComponents(self):
        top_sp = wx.SplitterWindow(self, -1, style=wx.SP_LIVE_UPDATE | wx.SP_3DSASH)
        top_sp.SetSplitMode(wx.SPLIT_VERTICAL)
        sp = wx.SplitterWindow(top_sp, -1, style=wx.SP_LIVE_UPDATE | wx.SP_3DSASH)
        main_display = wx.Panel(sp, style=wx.SUNKEN_BORDER)
        main_display.SetBackgroundColour('#FF0000')
        sub_display = wx.Panel(sp, style=wx.SUNKEN_BORDER)
        sub_display.SetBackgroundColour('#00FF00')
        sp.SplitVertically(main_display, sub_display)
        sp.SetMinimumPaneSize(100)
        tool_box = wx.Panel(top_sp, wx.ID_ANY, style=wx.BORDER_SIMPLE)
        tool_box.SetBackgroundColour('#0000FF')
        top_sp.SplitHorizontally(sp, tool_box)
        top_sp.SetMinimumPaneSize(100)
        # sp.SetSplitMode(wx.SPLIT_HORIZONTAL)
        # sizer.Add(mainPanel, -1, wx.EXPAND)
        # self.SetSizer(sizer)
        # main_sizer = wx.BoxSizer(wx.VERTICAL)
        # mainPanel = wx.Panel(self, -1, style=wx.BORDER_SIMPLE)
        # main_sizer.Add(mainPanel, -1, wx.EXPAND)
        # sizer = wx.BoxSizer(wx.VERTICAL)
        # upper_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # upper_sizer.Add(main_display, wx.ID_ANY, wx.EXPAND)
        # upper_sizer.Add(tool_box, wx.ID_ANY, wx.EXPAND)
        # sizer.Add(upper_sizer, wx.ID_ANY, wx.EXPAND)
        # sizer.Add(sub_display, wx.ID_ANY, wx.EXPAND)
        # mainPanel.SetSizer(sizer)
        # self.SetSizer(main_sizer)


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
