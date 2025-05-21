import wx
from ui.form import UserForm
from ui.listview import UserList

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="CRUD con WxPython y SQLite", size=(500, 500))
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.form = UserForm(panel, self.refresh_list)
        self.list_panel = UserList(panel, self.form)

        vbox.Add(self.form, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(self.list_panel, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(vbox)
        self.Centre()

    def refresh_list(self):
        self.list_panel.refresh()
