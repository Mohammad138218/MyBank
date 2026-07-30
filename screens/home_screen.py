from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class HomeScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = GridLayout(
            cols=2,
            padding=40,
            spacing=20
        )

        # Buttons
        melli_btn = Button(text="Melli Bank")

        pasargad_btn = Button(text="Pasargad Bank")

        melli_report_btn = Button(text="Melli Report")

        pasargad_report_btn = Button(text="Pasargad Report")

        melli_history_btn = Button(
            text="Melli History"
        )

        pasargad_history_btn = Button(
            text="Pasargad History"
        )


        # Events
        melli_btn.bind(on_press=self.open_melli)

        pasargad_btn.bind(on_press=self.open_pasargad)

        melli_report_btn.bind(on_press=self.open_melli_report)

        pasargad_report_btn.bind(on_press=self.open_pasargad_report)

        melli_history_btn.bind(
            on_press=self.open_melli_history
        )

        pasargad_history_btn.bind(
            on_press=self.open_pasargad_history
        )


        # Add Buttons
        layout.add_widget(melli_btn)

        layout.add_widget(pasargad_btn)

        layout.add_widget(melli_report_btn)

        layout.add_widget(pasargad_report_btn)

        layout.add_widget(melli_history_btn)

        layout.add_widget(pasargad_history_btn)

        self.add_widget(layout)



    def open_melli(self, instance):

        self.manager.current = "melli"



    def open_pasargad(self, instance):

        self.manager.current = "pasargad"



    def open_melli_report(self, instance):

        self.manager.current = "melli_report"



    def open_pasargad_report(self, instance):

        self.manager.current = "pasargad_report"



    def open_melli_history(self, instance):

        self.manager.current = "melli_history"



    def open_pasargad_history(self, instance):

        self.manager.current = "pasargad_history"