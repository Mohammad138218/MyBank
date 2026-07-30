from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

from database import get_all_transactions


class HistoryScreen(Screen):

    def __init__(self, bank_name, **kwargs):

        super().__init__(**kwargs)

        self.bank_name = bank_name


        main_layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )


        refresh = Button(
            text="Refresh",
            size_hint_y=None,
            height=50
        )

        refresh.bind(
            on_press=self.load_transactions
        )

        main_layout.add_widget(refresh)


        self.scroll = ScrollView()


        self.list_layout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            spacing=10
        )

        self.list_layout.bind(
            minimum_height=self.list_layout.setter("height")
        )


        self.scroll.add_widget(
            self.list_layout
        )

        main_layout.add_widget(
            self.scroll
        )


        back = Button(
            text="Back",
            size_hint_y=None,
            height=50
        )

        back.bind(
            on_press=self.back_home
        )

        main_layout.add_widget(back)


        self.add_widget(main_layout)



    def on_enter(self):

        self.load_transactions()



    def load_transactions(self, *args):

        self.list_layout.clear_widgets()


        transactions = get_all_transactions(
            self.bank_name
        )


        for row in transactions:

            transaction_id = row[0]

            transaction_type = row[1]

            amount = row[2]

            description = row[3]

            date = row[4]


            text = (
                f"#{transaction_id}\n"
                f"{transaction_type}\n"
                f"{amount}\n"
                f"{description}\n"
                f"{date}"
            )


            button = Button(

                text=text,

                size_hint_y=None,

                height=120

            )


            button.bind(
                on_press=lambda instance,
                transaction_id=transaction_id:
                self.edit_transaction(transaction_id)
            )


            self.list_layout.add_widget(button)



    def edit_transaction(self, transaction_id):

        edit_screen = self.manager.get_screen("edit")


        edit_screen.previous_screen = self.name


        edit_screen.load_transaction(transaction_id)


        self.manager.current = "edit"


    def back_home(self, instance):

        self.manager.current = "home"