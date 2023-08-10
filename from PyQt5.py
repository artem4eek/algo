from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.show()
app.exec_()

main_win.setWindowTitle(‘Название’)
main_win.move(900, 70)
main_win.resize(400, 200)
winner = QLabel('Победитель:')
winner.setText('34')
winner.text()
button = QPushButton('Сгенерировать')
button.setText('Новый текст')
button.text()
v_line = QVBoxLayout()
v_line.addWidget(title, alignment = Qt.AlignCenter)
main_win.setLayout(v_line)