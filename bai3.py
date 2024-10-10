import sys
from PyQt5.QtWidgets import QHBoxLayout,QApplication, QWidget, QLabel,QLineEdit,QPushButton,QVBoxLayout

class ChinhSuaKhachHangWindow(QWidget):
    def __init__(self):
        super().__init__()

        #Thiet lap cac thuoc tinh cua so
        self.setWindowTitle("Chinh sua thong tin khach hang")
        self.setGeometry(100,100,300,200)

        #tao layout
        self.mainlayout = QVBoxLayout()

        self.layoutid = QHBoxLayout()
        self.layoutten = QHBoxLayout()
        self.layoutemail = QHBoxLayout()
        self.layoutsdt = QHBoxLayout()


        #Tao cac widget
        self.id_label = QLabel("ID: ")
        self.id_input = QLineEdit()

        self.ten_label = QLabel("Ten: ")
        self.ten_input = QLineEdit()

        self.email_label = QLabel("Email: ")
        self.email_input = QLineEdit()

        self.sdt_label = QLabel("So dien thoai: ")
        self.sdt_input = QLineEdit()

        self.them_button = QPushButton('Chinh sua thoong tin khach hang')
        self.them_button.clicked.connect(self.chinh_sua_khach_hang)

        #them cac widget vao layout
        self.layoutid.addWidget(self.id_label)
        self.layoutid.addWidget(self.id_input)

        self.layoutten.addWidget(self.ten_label)
        self.layoutten.addWidget(self.ten_input)

        self.layoutemail.addWidget(self.email_label)
        self.layoutemail.addWidget(self.email_input)

        self.layoutsdt.addWidget(self.sdt_label)
        self.layoutsdt.addWidget(self.sdt_input)

        self.mainlayout.addLayout(self.layoutid)
        self.mainlayout.addLayout(self.layoutten)
        self.mainlayout.addLayout(self.layoutemail)
        self.mainlayout.addLayout(self.layoutsdt)
        self.mainlayout.addWidget(self.them_button)

        #dat layout chinh cho cua so
        self.setLayout(self.mainlayout)

    def chinh_sua_khach_hang(self):
        id = self.id_input.text()
        ten = self.ten_input.text()
        email = self.email_input.text()
        sdt = self.sdt_input.text()

        print(f'Da chinh sua thong tin khach hang voi ID: {id} {ten}, {email}, {sdt}')
        print(f'Ten moi: {ten}')
        print(f'Email moi: {email}')
        print(f'Sdt moi: {sdt}')

        #xoas cac truong da nhap khi them
        self.id_input.clear()
        self.ten_input.clear()
        self.email_input.clear()
        self.sdt_input.clear()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = ChinhSuaKhachHangWindow()
    window.show()
    sys.exit(app.exec())
