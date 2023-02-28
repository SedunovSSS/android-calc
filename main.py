from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class Calc(App):
    def build(self):
        self.b_l = BoxLayout(orientation='vertical')
        self.layout = GridLayout(cols=4, row_force_default=False, row_default_height=20)
        self.calc = TextInput(text='', multiline=True, font_size=80)
        self.calc.size_hint = (1, 0.25)
        self.b_l.add_widget(self.calc)
        self.calc.text = "0"
        self.btns = ['1', '2', '3', 'DEL',
                     '4', '5', '6', 'AC',
                     '7', '8', '9', '0',
                     '+', '-', '*', '/',
                     '(', ')', '.', '='
                     ]
        for i in self.btns:
            btn = Button(text=i, size_hint=(1, 0.5), font_size=60)
            if i == "AC":
                btn.bind(on_press=self.clear)
            elif i == "DEL":
                btn.bind(on_press=self.delete)
            elif i == "=":
                btn.bind(on_press=self.calculate)
            else:
                btn.bind(on_press=self.txt_insert)
            self.layout.add_widget(btn)

        self.b_l.add_widget(self.layout)
        return self.b_l

    def txt_insert(self, text):
        if self.calc.text == "0":
            self.calc.text = ""
        self.calc.text += text.text

    def calculate(self, calc):
        try:
            result = str(eval(self.calc.text))
        except:
            result = "0"
        self.calc.text = result

    def clear(self, calc):
        self.calc.text = "0"

    def delete(self, calc):
        if self.calc.text == "":
            self.calc.text = "0"
        self.calc.text = self.calc.text[:-1]


if __name__ == "__main__":
    app = Calc()
    app.run()
