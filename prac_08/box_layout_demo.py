"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Hong K. SOng , IT@JCU
Started 12/11/2025
Estimated 20 mins
Done: 25 mins
"""



from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

BoxLayoutDemo().run()
