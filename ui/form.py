import wx
from models.user import insert_user, update_user

class UserForm(wx.Panel):
    def __init__(self, parent, refresh_callback):
        super().__init__(parent)
        self.refresh_callback = refresh_callback
        self.user_id = None

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.name_input = wx.TextCtrl(self)
        self.email_input = wx.TextCtrl(self)

        vbox.Add(wx.StaticText(self, label="Nombre"), 0, wx.ALL, 5)
        vbox.Add(self.name_input, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(wx.StaticText(self, label="Email"), 0, wx.ALL, 5)
        vbox.Add(self.email_input, 0, wx.EXPAND | wx.ALL, 5)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        save_btn = wx.Button(self, label="Guardar")
        save_btn.Bind(wx.EVT_BUTTON, self.on_save)

        hbox.Add(save_btn, 0, wx.ALL, 5)

        vbox.Add(hbox)
        self.SetSizer(vbox)

    def on_save(self, event):
        name = self.name_input.GetValue()
        email = self.email_input.GetValue()

        if self.user_id:
            update_user(self.user_id, name, email)
        else:
            insert_user(name, email)

        self.name_input.SetValue("")
        self.email_input.SetValue("")
        self.user_id = None
        self.refresh_callback()
