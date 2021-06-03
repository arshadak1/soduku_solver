from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
import sudoku_solve
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.id_x = {}
        self.soduku_grid = GridLayout()
        self.soduku_grid.rows = 9
        self.soduku_grid.cols = 9
        self.box_ids = []
        for i in range(81):
            id_text = f'{i // 9}{i % 9}'
            self.box_ids.append(id_text)
            self.textinput = TextInput(multiline=False)
            self.textinput.halign = 'center'
            self.textinput.valign = 'center'
            self.textinput.font_size = '50sp'
            self.textinput.input_filter = 'int'
            if int(id_text[0]) // 3 in (0, 2) and int(id_text[1]) // 3 in (0, 2):
                # self.textinput.background_normal = ''
                self.textinput.background_color = (153/255, 217/255, 234/255, 1)
            elif int(id_text[0]) // 3 == int(id_text[1]) // 3 == 1:
                self.textinput.background_color = (153 / 255, 217 / 255, 234 / 255, 1)
            else:
                self.textinput.background_color = (239 / 255, 228 / 255, 176 / 255, 1)

            self.id_x[id_text] = self.textinput
            self.soduku_grid.add_widget(self.textinput)

        self.add_widget(self.soduku_grid)
        self.add_widget(
            Button(text="S   O   L   V   E", bold=True, size_hint_y=None, height=40, on_release=self.button))
        self.add_widget(Button(text="R   E   F   R   E   S   H", bold=True, size_hint_y=None, height=40, on_release=self.refresh))

    def refresh(self, ins):
        for i in self.box_ids:
            self.id_x[i].disabled = False
            self.id_x[i].text = ''

    def button(self, ins):
        sum_ = 0
        board = [[0 for i in range(9)] for i in range(9)]
        for i in self.box_ids:
            self.id_x[i].disabled = True
            try:
                num = int(self.id_x[i].text)
                board[int(i[0])][int(i[1])] = num
            except Exception:
                pass

        for i in range(9):
            sum_ += sum(board[i])
        if sum_ == 0:
            return
        if sudoku_solve.solve(board):
            for i in self.box_ids:
                self.id_x[i].text = str(board[int(i[0])][int(i[1])])
        else:
            for i in self.box_ids:
                self.id_x[i].disabled = False
            popup = Popup(title='WARNING', content=Label(text="Solution doesn't exist"), size_hint=(None, None),
                          size=(200, 200))
            popup.open()


class SudokuApp(App):

    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    SudokuApp().run()
