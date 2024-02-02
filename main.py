from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class RainbowApp(App):
    color_dict = {
        "Красный": "#ff0000",
        "Оранжевый": "#ff8800",
        "Желтый": "#ffff00",
        "Зеленый": "#00ff00",
        "Голубой": "#00ffff",
        "Синий": "#0000ff",
        "Фиолетовый": "#ff00ff"
    }

    def build(self):
        layout = BoxLayout(orientation='vertical')

        for color_name, color_code in self.color_dict.items():
            button = Button(
                text=color_name,
                font_size=20,
                on_press=self.btn_press,
                background_color=hex_to_rgb(color_code),
                background_normal='',
                size_hint=(1, 0.1),
                height=100
            )
            layout.add_widget(button)

        self.text_field = Label(
            text='',
            font_size=20,
            size_hint=(1, 0.1),
            height=50
        )
        layout.add_widget(self.text_field)

        self.color_label = Label(
            text='',
            font_size=20,
            size_hint=(1, 0.1),
            height=50
        )
        layout.add_widget(self.color_label)

        return layout

    def btn_press(self, instance):
        color_name = instance.text
        color_code = self.color_dict[color_name]
        self.text_field.text = color_code
        self.color_label.text = color_name


def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    r = int(hex_code[0:2], 16) / 255.0
    g = int(hex_code[2:4], 16) / 255.0
    b = int(hex_code[4:6], 16) / 255.0
    return (r, g, b)


if __name__ == "__main__":
    RainbowApp().run()