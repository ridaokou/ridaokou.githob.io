
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton

class WindowA(QWidget): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("窗口A")
        self.resize(400, 300)
        self.move(200,200)
        self.setup_ui()
    def setup_ui(self):
        self.btn = QPushButton("显示窗口B",self)
        self.btn.clicked.connect(self.action)
    def action(self):
        if winb.isHidden():
            winb.show2()
            self.btn.setText("隐藏窗口B")
        else:
            winb.hide()
            self.btn.setText("显示窗口B")
    def show2(self):
        self.show()
class WindowB(QWidget): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("窗口B")
        self.resize(400, 300)
        self.move(700,200)
        self.setup_ui()
    def closeEvent(self,event):
        if wina.isHidden():
            wina.btn.setText("显示窗口B")
            wina.show()
    def setup_ui(self):
        self.btn = QPushButton("隐藏窗口A",self)
        self.btn.clicked.connect(self.action)
    def show2(self):
        self.show()
    def action(self):
        if wina.isHidden():
            wina.show2()
            self.btn.setText("隐藏窗口A")
        else:
            wina.hide()
            self.btn.setText("显示窗口A")
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    wina = WindowA()
    winb = WindowB()
    wina.show()
    sys.exit(app.exec_())

