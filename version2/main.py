# -*- coding : <utf-8> -*-
# main.py

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, id=-1, title="SplitterWindow", size=(800, 600))
        self.InitializeComponents()

    def InitializeComponents(self):
        top_sp = wx.SplitterWindow(
            self, -1, style=wx.SP_LIVE_UPDATE | wx.SP_3DSASH)
        sp = wx.SplitterWindow(
            top_sp, -1, style=wx.SP_LIVE_UPDATE | wx.SP_3DSASH)
        self.main_display = wx.ScrolledWindow(sp, -1)
        self.sub_display = wx.ScrolledWindow(sp, -1)
        self.tool_box = wx.Panel(top_sp, 1)

        self.Create_ToolBox(self, title='Tool_Box', target=self.tool_box)
        self.Create_MainDisplay(self, title='Main_Display', target=self.main_display)
        self.Create_SubDisplay(self, title='Sub_Display', target=self.sub_display)
        self.main_display.SetScrollRate(10, 10)
        self.sub_display.SetScrollRate(10, 10)

        sp.SetSashGravity(0.7)
        top_sp.SetSashGravity(0.8)
        sp.SplitHorizontally(self.main_display, self.sub_display)
        sp.SetMinimumPaneSize(1)
        top_sp.SplitVertically(sp, self.tool_box)
        top_sp.SetMinimumPaneSize(1)

    def Create_ToolBox(self, parent, title, target):
        btn_sizer = wx.StaticBoxSizer(wx.VERTICAL, target, title)
        btn1 = wx.Button(target, -1, 'Button_1')
        btn2 = wx.Button(target, -1, 'Button_2')
        btn_sizer.Add(btn1, flag=wx.ALIGN_CENTER)
        btn_sizer.Add(btn2, flag=wx.ALIGN_CENTER)
        target.SetSizer(btn_sizer)

    def Create_MainDisplay(self, parent, title, target):
        maindisp_sizer = wx.StaticBoxSizer(wx.VERTICAL, target, title)
        maindisp = wx.Panel(target, -1, style=wx.SUNKEN_BORDER, size=(800, 600))
        maindisp.SetBackgroundColour('#009C9E')
        maindisp_sizer.Add(maindisp, 1, wx.EXPAND)
        target.SetSizer(maindisp_sizer)

    def Create_SubDisplay(self, parent, title, target):
        subdisp_sizer = wx.StaticBoxSizer(wx.HORIZONTAL, target, title)
        for _ in range(15):
            subdisp = wx.Panel(
                target, -1, style=wx.SUNKEN_BORDER, size=(200, 100))
            subdisp.SetBackgroundColour('#FF7896')
            subdisp_sizer.Add(subdisp, 0, wx.ALIGN_CENTER)
        target.SetSizer(subdisp_sizer)


if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
