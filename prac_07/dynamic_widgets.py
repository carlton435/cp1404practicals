
from kivy.app import App
from kivy.lang import Builder


class DynamicWidgets(App):
    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        return self.root

    def add_widget(self):
        temp_button = Button(text=name)
        self.root.ids.entries_box.add_widget(temp_button)
        temp_button.bind(on_release=self.press_entry)

DynamicWidgets().run()