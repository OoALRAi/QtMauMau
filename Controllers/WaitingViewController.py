from PyQt5.QtWidgets import QWidget


class WaitingViewController:
    def __init__(self, view: QWidget, mainView):
        self.view = view
        self.mainView = mainView

    def set_connected_players(self, num):
        self.view.num_of_players_label.setText(f'{num} players connected')
