# -*- coding : <utf-8> -*-
# main.py

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, id=-1, title="パネル配置", size=(800, 600))
        self.InitializeComponents()

    def InitializeComponents(self):
        top_sp = wx.SplitterWindow(self, -1, style=wx.SP_LIVE_UPDATE | wx.SP_3DSASH)
        sp = wx.SplitterWindow(top_sp, -1, style=wx.SP_LIVE_UPDATE | wx.SP_3DSASH)
        main_display = wx.Panel(sp, style=wx.SUNKEN_BORDER)
        main_display.SetBackgroundColour('#FF0000')
        sub_display = wx.Panel(sp, style=wx.SUNKEN_BORDER)
        sub_display.SetBackgroundColour('#00FF00')
        sp.SetSashGravity(0.8)
        sp.SplitVertically(main_display, sub_display)
        tool_box = wx.Panel(top_sp, wx.ID_ANY, style=wx.BORDER_SIMPLE)
        tool_box.SetBackgroundColour('#0000FF')
        top_sp.SetSashGravity(0.7)
        top_sp.SplitHorizontally(sp, tool_box)


if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
