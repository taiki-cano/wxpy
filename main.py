import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='wxpy')
        self.Show()


def main():
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()


if __name__ == '__main__':
    main()
