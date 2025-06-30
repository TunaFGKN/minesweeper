from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

# Screens
class MainMenuScreen(Screen):
    pass

class DifficultyScreen(Screen):
    pass

class CustomBoardScreen(Screen):
    def start_custom_game(self):
        rows = int(self.ids.rows_input.text)
        cols = int(self.ids.cols_input.text)
        mines = int(self.ids.mines_input.text)
        
        game_screen = self.manager.get_screen('game')
        game_screen.setup_board(rows, cols, mines)
        self.manager.current = 'game'

class GameScreen(Screen):
    def setup_board(self, rows, cols, num_mines):
        # Önce eski tahtayı temizle
        self.ids.board_area.clear_widgets()

        # GridLayout oluştur
        board = GridLayout(cols=cols, rows=rows, spacing=2, size_hint=(1, 1))

        for i in range(rows * cols):
            btn = Button(text='', size_hint=(1, 1))
            btn.bind(on_press=self.on_cell_pressed)
            board.add_widget(btn)

        self.ids.board_area.add_widget(board)

    def on_cell_pressed(self, instance):
        instance.text = "X"  # Örnek: Tıklayınca X yazıyor

class MinesweeperApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='menu'))
        sm.add_widget(DifficultyScreen(name='difficulty'))
        sm.add_widget(CustomBoardScreen(name='custom'))
        sm.add_widget(GameScreen(name='game'))
        return sm

if __name__ == '__main__':
    MinesweeperApp().run()
