import wx
from ui.app import MainFrame
from db.database import init_db

if __name__ == "__main__":
    init_db()
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
