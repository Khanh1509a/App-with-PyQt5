import sys
from PyQt5.QtWidgets import QHBoxLayout,QApplication, QWidget, QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtGui import QPalette, QLinearGradient, QColor
class themKhachHangWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #Thiet lap cac thuoc tinh cua so
        self.setWindowTitle("Them khach hang")
        self.setGeometry(500,100,800,1000)
        self.backGround()

        #tao layout
        self.mainlayout = QVBoxLayout()
        self.layoutten = QHBoxLayout()
        self.layoutemail = QHBoxLayout()
        self.layoutsdt = QHBoxLayout()


        #Tao cac widget
        self.ten_label = QLabel("Tên: ")
        self.ten_label.setStyleSheet("color: white")
        self.ten_input = QLineEdit(self)
        self.ten_input.setFixedSize(50, 30)
        self.ten_input.move(120, 20)


        self.email_label = QLabel("Email: ")
        self.email_label.setStyleSheet("color: white")
        self.email_input = QLineEdit()

        self.sdt_label = QLabel("Số điện thoại: ")
        self.sdt_label.setStyleSheet("color: white")
        self.sdt_input = QLineEdit()

        self.them_button = QPushButton('Thêm Khách Hàng')
        self.them_button.clicked.connect(self.them_khach_hang)

        #them cac widget vao layout
        self.layoutten.addWidget(self.ten_label)
        self.layoutten.addWidget(self.ten_input)

        self.layoutemail.addWidget(self.email_label)
        self.layoutemail.addWidget(self.email_input)

        self.layoutsdt.addWidget(self.sdt_label)
        self.layoutsdt.addWidget(self.sdt_input)

        self.mainlayout.addLayout(self.layoutten)
        self.mainlayout.addLayout(self.layoutemail)
        self.mainlayout.addLayout(self.layoutsdt)
        self.mainlayout.addWidget(self.them_button)

        #dat layout chinh cho cua so
        self.setLayout(self.mainlayout)

    def backGround(self):
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor(30, 87, 153))
        gradient.setColorAt(1.0, QColor(0, 0, 0))
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)

    def them_khach_hang(self):
        ten = self.ten_input.text()
        email = self.email_input.text()
        sdt = self.sdt_input.text()

        print(f'Da them khach hang: {ten}, {email}, {sdt}')
        #xoas cac truong da nhap khi them
        self.ten_input.clear()
        self.email_input.clear()
        self.sdt_input.clear()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = themKhachHangWindow()
    window.show()
    sys.exit(app.exec())
