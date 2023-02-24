from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class Calc(App):
    def build(self):
        self.b_l = BoxLayout(orientation='vertical')
        self.layout = GridLayout(cols=4, row_force_default=False, row_default_height=20)
        self.calc = TextInput(text='', multiline=True, font_size=60)
        self.calc.size_hint = (1, 0.2)
        self.b_l.add_widget(self.calc)
        for i in range(10):
            btn = self.add_btn(str(i))
            btn.bind(on_press=self.txt_insert)
            self.layout.add_widget(btn)
        for i in ['+', '-', '*', '/']:
            btn = self.add_btn(i)
            btn.bind(on_press=self.txt_insert)
            self.layout.add_widget(btn)

        clear = Button(text="AC", size_hint=(1, 0.5))
        clear.bind(on_press=self.clear)
        self.layout.add_widget(clear)
        d = Button(text="DEL", size_hint=(1, 0.5))
        d.bind(on_press=self.delete)
        self.layout.add_widget(d)
        btn_o = self.add_btn("(")
        btn_o.bind(on_press=self.txt_insert)
        self.layout.add_widget(btn_o)
        btn_c = self.add_btn(")")
        btn_c.bind(on_press=self.txt_insert)
        self.layout.add_widget(btn_c)
        btn_t = self.add_btn(".")
        btn_t.bind(on_press=self.txt_insert)
        self.layout.add_widget(btn_t)
        calculate = Button(text="=", size_hint=(1, 0.5))
        calculate.bind(on_press=self.calculate)
        self.layout.add_widget(calculate)
        self.b_l.add_widget(self.layout)
        return self.b_l

    def add_btn(self, text):
        return Button(text=text, size_hint=(1, 0.5))

    def txt_insert(self, text):
        self.calc.text += text.text

    def calculate(self, calc):
        try:
            result = str(eval(self.calc.text))
        except:
            result = ""
        self.calc.text = result

    def clear(self, calc):
        self.calc.text = ""

    def delete(self, calc):
        self.calc.text = self.calc.text[:-1]


if __name__ == "__main__":
    app = Calc()
    app.run()
