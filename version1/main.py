# -*- coding : <utf-8> -*-
# main.py (MVC Viewer)

import os
import wx

import controller
import dialogs
import model

from pubsub import pub
from ObjectListView import ObjectListView, ColumnDefn


class BookPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        if not os.path.exists("books.db"):
            controller.setup_database()

        self.session = controller.connect_to_database()
        try:
            self.book_results = controller.get_all_records(self.session)
        except Exception:
            self.book_results = []

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        search_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)

        # Create the search related widgets
        categories = ["Author", "Title", "ISBN", "Publisher"]
        search_label = wx.StaticText(self, label="Search By:")
        search_label.SetFont(font)
        search_sizer.Add(search_label, 0, wx.ALL, 5)

        self.categories = wx.ComboBox(self, value="Author", choices=categories)
        search_sizer.Add(self.categories, 0, wx.ALL, 5)

        self.search_ctrl = wx.SearchCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.search_ctrl.Bind(wx.EVT_TEXT_ENTER, self.search)
        search_sizer.Add(self.search_ctrl, 0, wx.ALL, 5)

        self.book_results_olv = ObjectListView(self, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.book_results_olv.SetEmptyListMsg("データーがありません")
        self.update_book_results()

        # create the button row
        add_record_btn = wx.Button(self, label="追加")
        add_record_btn.Bind(wx.EVT_BUTTON, self.add_record)
        btn_sizer.Add(add_record_btn, 0, wx.ALL, 5)

        edit_record_btn = wx.Button(self, label="編集")
        edit_record_btn.Bind(wx.EVT_BUTTON, self.edit_record)
        btn_sizer.Add(edit_record_btn, 0, wx.ALL, 5)

        delete_record_btn = wx.Button(self, label="削除")
        delete_record_btn.Bind(wx.EVT_BUTTON, self.delete_record)
        btn_sizer.Add(delete_record_btn, 0, wx.ALL, 5)

        show_all_btn = wx.Button(self, label="全て表示")
        show_all_btn.Bind(wx.EVT_BUTTON, self.on_show_all)
        btn_sizer.Add(show_all_btn, 0, wx.ALL, 5)

        main_sizer.Add(search_sizer)
        main_sizer.Add(self.book_results_olv, 1, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(btn_sizer, 0, wx.CENTER)
        self.SetSizer(main_sizer)

    def add_record(self, event):
        with dialogs.RecordDialog(self.session) as dlg:
            dlg.ShowModal()

        self.show_all_records()

    def edit_record(self, event):
        selected_row = self.book_results_olv.GetSelectedObject()
        if selected_row is None:
            dialogs.show_message('No row selected!', 'Error')
            return

        with dialogs.RecordDialog(self.session, selected_row, title="Modify", addRecord=False) as dlg:
            dlg.ShowModal()

        self.show_all_records()

    def delete_record(self, event):
        selected_row = self.book_results_olv.GetSelectedObject()
        if selected_row is None:
            dialogs.show_message('No row selected!', 'Error')
            return
        controller.delete_record(self.session, selected_row.id)
        self.show_all_records()

    def show_all_records(self):
        self.book_results = controller.get_all_records(self.session)
        self.update_book_results()

    def search(self, event):
        print("AAA = ")
        filter_choice = self.categories.GetValue()
        print("filter_choice : %s" % filter_choice)
        keyword = self.search_ctrl.GetValue()
        self.book_results = controller.search_records(self.session, filter_choice, keyword)
        self.update_book_results()

    def on_show_all(self, event):
        self.show_all_records()

    def update_book_results(self):
        self.book_results_olv.SetColumns([
            ColumnDefn("Title", "left", 350, "title"),
            ColumnDefn("Author", "left", 150, "author"),
            ColumnDefn("ISBN", "right", 150, "isbn"),
            ColumnDefn("Publisher", "left", 150, "publisher")
        ])
        self.book_results_olv.SetObjects(self.book_results)


class BookFrame(wx.Frame):
    def __init__(self):
        """ Constructor """
        super().__init__(
            None, title='Media Organizer', size=(800, 600))
        panel = BookPanel(self)
        self.Show()


if __name__ == '__main__':
    app = wx.App(False)
    frame = BookFrame()
    app.MainLoop()
