from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from database import (
    get_transaction,
    update_transaction,
    delete_transaction
)


class EditScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.transaction_id = None


        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )


        layout.add_widget(
            Label(text="Transaction Type")
        )


        self.type = TextInput()

        layout.add_widget(self.type)


        layout.add_widget(
            Label(text="Amount")
        )


        self.amount = TextInput(
            input_filter="int"
        )

        layout.add_widget(self.amount)


        layout.add_widget(
            Label(text="Description")
        )


        self.description = TextInput()

        layout.add_widget(self.description)


        save = Button(
            text="Save Changes"
        )

        save.bind(
            on_press=self.save_changes
        )

        layout.add_widget(save)


        delete = Button(
            text="Delete"
        )

        delete.bind(
            on_press=self.delete_transaction
        )

        layout.add_widget(delete)


        back = Button(
            text="Back"
        )

        back.bind(
            on_press=self.back_history
        )

        layout.add_widget(back)


        self.add_widget(layout)



    def load_transaction(self, transaction_id):

        self.transaction_id = transaction_id

        row = get_transaction(transaction_id)

        if row:

            self.type.text = row[2]

            self.amount.text = str(row[3])

            self.description.text = row[4]



    def save_changes(self, instance):

        update_transaction(

            self.transaction_id,

            self.type.text,

            int(self.amount.text),

            self.description.text

        )

        print("Updated!")



    def delete_transaction(self, instance):

        delete_transaction(
            self.transaction_id
        )

        print("Deleted!")



    def back_history(self, instance):

        self.manager.current = self.previous_screen