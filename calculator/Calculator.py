from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class CalcGridLayout(GridLayout):

    def equal(self, text):
        if text:
            try:
                self.display.text = str(eval(text))
            except Exception:
                self.display.text = "Error"

    def clear_value(self, text):
        self.display.text = text[:-1]

    def percent(self, text):
        if text:
            try:
                self.display.text = str(eval(text)/100)
            except Exception:
                self.display.text = "Error"


class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()


if __name__ == '__main__':
    calcApp = CalculatorApp()
    calcApp.run()




