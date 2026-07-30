from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from database import get_report


class ReportScreen(Screen):

    def __init__(self, bank_name, **kwargs):

        super().__init__(**kwargs)

        self.bank_name = bank_name

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )


        title = Label(
            text=f"{bank_name} Report",
            font_size=28,
            size_hint_y=None,
            height=50
        )

        layout.add_widget(title)


        self.report_label = Label(
            text="",
            halign="left",
            valign="top"
        )

        self.report_label.bind(
            size=self.report_label.setter("text_size")
        )

        layout.add_widget(self.report_label)


        refresh = Button(
            text="Refresh"
        )

        refresh.bind(
            on_press=self.load_report
        )

        layout.add_widget(refresh)


        back = Button(
            text="Back"
        )

        back.bind(
            on_press=self.back_home
        )

        layout.add_widget(back)


        self.add_widget(layout)


    def on_enter(self):

        self.load_report()


    def load_report(self, *args):

        data = get_report(self.bank_name)

        income = 0

        home = 0

        emergency = 0

        free = 0


        for item in data:

            transaction_type = item[0]

            total = item[1] or 0


            if transaction_type == "Income":

                income = total

            elif transaction_type == "Home Expense":

                home = total

            elif transaction_type == "Emergency Expense":

                emergency = total

            elif transaction_type == "Free Expense":

                free = total


        total_expense = home + emergency + free

        balance = income - total_expense


        self.report_label.text = (

            f"Income : {income}\n\n"

            f"Home Expense : {home}\n"

            f"Emergency Expense : {emergency}\n"

            f"Free Expense : {free}\n\n"

            f"----------------------\n\n"

            f"Total Expense : {total_expense}\n\n"

            f"Balance : {balance}"

        )


    def back_home(self, instance):

        self.manager.current = "home"