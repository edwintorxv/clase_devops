import wx
from models.user import get_users, delete_user

class UserList(wx.Panel):
    def __init__(self, parent, form):
        super().__init__(parent)
        self.form = form
        self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.list_ctrl.InsertColumn(0, 'ID', width=50)
        self.list_ctrl.InsertColumn(1, 'Nombre', width=140)
        self.list_ctrl.InsertColumn(2, 'Email', width=200)

        btn_delete = wx.Button(self, label="Eliminar Seleccionado")
        btn_delete.Bind(wx.EVT_BUTTON, self.on_delete)

        btn_edit = wx.Button(self, label="Editar Seleccionado")
        btn_edit.Bind(wx.EVT_BUTTON, self.on_edit)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.list_ctrl, 1, wx.EXPAND | wx.ALL, 5)
        vbox.Add(btn_edit, 0, wx.ALL, 5)
        vbox.Add(btn_delete, 0, wx.ALL, 5)

        self.SetSizer(vbox)
        self.refresh()

    def refresh(self):
        self.list_ctrl.DeleteAllItems()
        for row in get_users():
            index = self.list_ctrl.InsertItem(self.list_ctrl.GetItemCount(), str(row[0]))
            self.list_ctrl.SetItem(index, 1, row[1])
            self.list_ctrl.SetItem(index, 2, row[2])

    def on_delete(self, event):
        index = self.list_ctrl.GetFirstSelected()
        if index != -1:
            user_id = int(self.list_ctrl.GetItemText(index))
            delete_user(user_id)
            self.refresh()

    def on_edit(self, event):
        index = self.list_ctrl.GetFirstSelected()
        if index != -1:
            user_id = int(self.list_ctrl.GetItemText(index))
            name = self.list_ctrl.GetItem(index, 1).GetText()
            email = self.list_ctrl.GetItem(index, 2).GetText()
            self.form.user_id = user_id
            self.form.name_input.SetValue(name)
            self.form.email_input.SetValue(email)
