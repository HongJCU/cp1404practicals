"""
Name: Hong K. Song
Time Est: 45mins
Time Done: 40 mins 

"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NamesApp(App):
    """Simple app that creates Labels from a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # This is the *model* (your data)
        self.names = ["Henry", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        self.root = Builder.load_file("dynamic_widgets.kv")

        # Create a Label for each name
        for name in self.names:
            label = Label(text=name, font_size=24)
            self.root.ids.main.add_widget(label)

        return self.root


NamesApp().run()
