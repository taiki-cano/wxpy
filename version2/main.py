# -*- coding : <utf-8> -*-
# main.py

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, id=-1, title="SplitterWindow", size=(800, 600))
        self.InitializeComponents()

    def InitializeComponents(self):
        top_sp = wx.SplitterWindow(self, -1, style=wx.SP_LIVE_UPDATE | wx.SP_3DSASH)
        sp = wx.SplitterWindow(top_sp, -1, style=wx.SP_LIVE_UPDATE | wx.SP_3DSASH)
        self.main_display = wx.Panel(sp, wx.ID_ANY, style=wx.SUNKEN_BORDER)
        self.tool_box = wx.Panel(sp, wx.ID_ANY, style=wx.SUNKEN_BORDER | wx.ALIGN_CENTER)
        self.sub_display = wx.Panel(top_sp, wx.ID_ANY, style=wx.SUNKEN_BORDER)

        self.Create_SBS(self, title='Tool_Box', target=self.tool_box)
        self.Create_SBS(self, title='Main_Display', target=self.main_display)
        self.Create_SBS(self, title='Sub_Display', target=self.sub_display)

        sp.SetSashGravity(0.8)
        top_sp.SetSashGravity(0.7)
        sp.SplitVertically(self.main_display, self.tool_box)
        sp.SetMinimumPaneSize(1)
        top_sp.SplitHorizontally(sp, self.sub_display)
        top_sp.SetMinimumPaneSize(1)

    def Create_SBS(self, parent, title, target):
        btn_sizer = wx.StaticBoxSizer(wx.VERTICAL, target, title)
        btn1 = wx.Button(target, -1, 'Button_1')
        btn2 = wx.Button(target, -1, 'Button_2')
        btn_sizer.Add(btn1)
        btn_sizer.Add(btn2)
        target.SetSizer(btn_sizer)


if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
