from kivy.app import App

from kivy.uix.screenmanager import ScreenManager

from database import create_database

from screens.home_screen import HomeScreen
from screens.transaction_screen import TransactionScreen
from screens.report_screen import ReportScreen
from screens.history_screen import HistoryScreen
from screens.edit_screen import EditScreen


class BankApp(App):

    def build(self):

        create_database()

        manager = ScreenManager()

        manager.add_widget(
            HomeScreen(
                name="home"
            )
        )

        manager.add_widget(
            TransactionScreen(
                bank_name="Melli Bank",
                name="melli"
            )
        )

        manager.add_widget(
            TransactionScreen(
                bank_name="Pasargad Bank",
                name="pasargad"
            )
        )

        manager.add_widget(
            ReportScreen(
                bank_name="Melli Bank",
                name="melli_report"
            )
        )

        manager.add_widget(
            ReportScreen(
                bank_name="Pasargad Bank",
                name="pasargad_report"
            )
        )

        manager.add_widget(
            HistoryScreen(
                bank_name="Melli Bank",
                name="melli_history"
            )
        )


        manager.add_widget(
            HistoryScreen(
                bank_name="Pasargad Bank",
                name="pasargad_history"
            )
        )

        manager.add_widget(
            EditScreen(
                name="edit"
            )
        )

        return manager


if __name__ == "__main__":
    BankApp().run()