import sys
from PyQt5.QtWidgets import QHBoxLayout,QApplication, QWidget, QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtGui import QPalette, QLinearGradient, QColor
class luuKhachHangWindow(QWidget):
    def __init__(self):
        super().__init__()


        #Thiet lap cac thuoc tinh cua so
        self.setWindowTitle("Luu Thong tin khach hang")
        self.setGeometry(100,100,300,200)



        #tao layout
        self.mainlayout = QVBoxLayout()
        self.layoutten = QHBoxLayout()
        self.layoutemail = QHBoxLayout()
        self.layoutsdt = QHBoxLayout()


        #Tao cac widget
        self.ten_label = QLabel("Ten: ")
        self.ten_input = QLineEdit()

        self.email_label = QLabel("Email: ")
        self.email_input = QLineEdit()

        self.sdt_label = QLabel("So dien thoai: ")
        self.sdt_input = QLineEdit()

        self.them_button = QPushButton('Luu thong tin khach hang')
        self.them_button.clicked.connect(self.luu_khach_hang)

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

        #danh sach thong tin khach hang
        self.danhsachKH = []
    def luu_khach_hang(self):
        ten = self.ten_input.text()
        email = self.email_input.text()
        sdt = self.sdt_input.text()

        #taoj danh sach chua thong tin khach hang
        danh_sach = {
            'Ten':ten,
            'Email':email,
            'Sdt':sdt
        }

        #them thong tin vao danh sach
        self.danhsachKH.append(danh_sach)
        # In danh sách khách hàng để kiểm tra
        print('Danh sách khách hàng:', self.danhsachKH)


        #xoas cac truong da nhap khi them
        self.ten_input.clear()
        self.email_input.clear()
        self.sdt_input.clear()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = luuKhachHangWindow()
    window.show()
    sys.exit(app.exec())
