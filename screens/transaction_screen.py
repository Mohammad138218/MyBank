from datetime import datetime

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox

from database import add_transaction


class TransactionScreen(Screen):

    def __init__(self, bank_name, **kwargs):

        super().__init__(**kwargs)

        self.bank_name = bank_name


        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )


        title = Label(
            text=f"{bank_name}",
            font_size=28
        )

        layout.add_widget(title)


        # --------------------
        # Transaction Type
        # --------------------

        self.income = CheckBox(group="type")
        self.home = CheckBox(group="type")
        self.emergency = CheckBox(group="type")
        self.free = CheckBox(group="type")


        options = [

            ("Income", self.income),

            ("Home Expense", self.home),

            ("Emergency Expense", self.emergency),

            ("Free Expense", self.free)

        ]


        for text, checkbox in options:

            row = BoxLayout(size_hint_y=None, height=40)

            row.add_widget(
                Label(text=text)
            )

            row.add_widget(
                checkbox
            )

            layout.add_widget(row)


        # --------------------
        # Amount
        # --------------------

        self.amount = TextInput(
            hint_text="Amount",
            multiline=False,
            input_filter="int"
        )

        layout.add_widget(self.amount)


        # --------------------
        # Description
        # --------------------

        self.description = TextInput(
            hint_text="Description",
            multiline=False
        )

        layout.add_widget(self.description)


        # --------------------
        # Message Label
        # --------------------

        self.message = Label(
            text=""
        )

        layout.add_widget(self.message)


        # --------------------
        # Save Button
        # --------------------

        save = Button(
            text="Save"
        )

        save.bind(
            on_press=self.save_transaction
        )

        layout.add_widget(save)


        # --------------------
        # Back Button
        # --------------------

        back = Button(
            text="Back"
        )

        back.bind(
            on_press=self.back_home
        )

        layout.add_widget(back)


        self.add_widget(layout)


    # =====================================

    def save_transaction(self, instance):

        if self.amount.text == "":

            self.message.text = "Enter amount"

            return


        if self.income.active:

            transaction_type = "Income"

        elif self.home.active:

            transaction_type = "Home Expense"

        elif self.emergency.active:

            transaction_type = "Emergency Expense"

        elif self.free.active:

            transaction_type = "Free Expense"

        else:

            self.message.text = "Select transaction type"

            return


        date = datetime.now().strftime("%Y-%m-%d %H:%M")


        add_transaction(

            self.bank_name,

            transaction_type,

            int(self.amount.text),

            self.description.text,

            date

        )


        self.message.text = "Transaction Saved"


        # پاک کردن فرم

        self.amount.text = ""

        self.description.text = ""

        self.income.active = False
        self.home.active = False
        self.emergency.active = False
        self.free.active = False


    # =====================================

    def back_home(self, instance):

        self.manager.current = "home"