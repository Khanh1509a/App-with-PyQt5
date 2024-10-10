import sys
from PyQt5.QtWidgets import QMessageBox ,QHBoxLayout,QApplication, QWidget, QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtGui import QPalette, QLinearGradient, QColor
from PyQt5.QtCore import Qt
import pandas as pd
import numpy as np

class quanLyKhachHang(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.backGround()
        # Khởi tạo DataFrame và ID
        self.current_id = 1
        self.dsTen = []
        self.dsEmail = []
        self.dsSdt = []

    def initUI(self):
        # Thiet lap cac thuoc tinh cua so
        self.setWindowTitle("Cửa sổ chính")
        self.setGeometry(500, 200, 800, 500)
        # self.setMaximumSize(800,500)
        # self.setMinimumSize(800,500)
        # Thêm tiêu đề
        self.title_label = QLabel("Quản Lý Khách Hàng", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: white; font-size: 45px; font-weight: bold;")
        self.title_label.setGeometry(0, 10, 800, 50)  # Đặt tiêu đề ở giữa phía trên

        #Tên khách hàng
        self.ten_label = QLabel("Tên: ", self)
        self.ten_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.ten_label.move(50, 100)
        self.ten_input = QLineEdit(self)
        self.ten_input.setGeometry(200,100,500,30)
        self.ten_input.setPlaceholderText('Nhập tên khách hàng')

        #Email khách hàng
        self.email_label = QLabel("Email: ", self)
        self.email_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.email_label.move(50, 150)
        self.email_input = QLineEdit(self)
        self.email_input.setGeometry(200,150,500,30)
        self.email_input.setPlaceholderText('xyzabc@gmail.com')

        #Sdt khách hàng
        self.sdt_label = QLabel("Số điện thoại: ", self)
        self.sdt_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.sdt_label.move(50, 200)
        self.sdt_input = QLineEdit(self)
        self.sdt_input.setGeometry(200,200,500,30)
        self.sdt_input.setPlaceholderText('Nhập số điện thoại khách hàng')

        #Label chức năng
        self.chucNang = QLabel('CHỨC NĂNG', self)
        self.chucNang.move(50, 250)
        self.chucNang.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")

        # Nút thêm
        self.them = QPushButton("Thêm", self)
        self.them.setGeometry(50,300,100,40)
        self.them.setStyleSheet("background-color: #FFFF00; color: black; font-size: 15px; border-style: solid ;border-radius: 20px; font-weight: bold")
        self.them.enterEvent = self.enterEvent
        self.them.leaveEvent = self.leaveEvent
        self.them.clicked.connect(self.Them)

        #Nút sửa
        self.sua = QPushButton("Sửa", self)
        self.sua.setGeometry(200, 300, 100, 40)
        self.sua.setStyleSheet(
            "background-color: #FFA500; color: black; font-size: 15px; border-style: solid ;border-radius: 20px; font-weight: bold")
        self.sua.enterEvent = self.enterEvent
        self.sua.leaveEvent = self.leaveEvent
        self.sua.clicked.connect(self.Sua)

        # Nút xoá
        self.xoa = QPushButton("Xoá", self)
        self.xoa.setGeometry(350, 300, 100, 40)
        self.xoa.setStyleSheet(
            "background-color: #00FFFF; color: black; font-size: 15px; border-style: solid ;border-radius: 20px; font-weight: bold")
        self.xoa.enterEvent = self.enterEvent
        self.xoa.leaveEvent = self.leaveEvent
        self.xoa.clicked.connect(self.Xoa)

        #Danh sách
        self.ds = QPushButton("Lưu", self)
        self.ds.setGeometry(500, 300, 100, 40)
        self.ds.setStyleSheet(
            "background-color: #7FFFD4; color: black; font-size: 15px; border-style: solid ;border-radius: 20px; font-weight: bold")
        self.ds.enterEvent = self.enterEvent
        self.ds.leaveEvent = self.leaveEvent
        self.ds.clicked.connect(self.Luu)

        # Nút clear chữ
        self.clr = QPushButton("Clear", self)
        self.clr.setGeometry(650, 300, 100, 40)
        self.clr.setStyleSheet(
            "background-color: #FF0000; color: black; font-size: 15px; border-style: solid ;border-radius: 20px; font-weight: bold")
        self.clr.enterEvent = self.enterEvent
        self.clr.leaveEvent = self.leaveEvent
        self.clr.clicked.connect(self.Clr)

    def Clr(self):
        self.ten_input.clear()
        self.email_input.clear()
        self.sdt_input.clear()

    #Xử lý thêm
    def Them(self):
        ten = self.ten_input.text()
        email = self.email_input.text()
        sdt = self.sdt_input.text()
        # Hiển thị hộp thoại thông báo và chờ đợi người dùng nhấn nút OK
        QMessageBox.information(self, 'Thông báo!', f'Đã thêm thành công khách hàng: {ten}, {email}, {sdt}')



    #Xử lý sửa
    def Sua(self):
        ten = self.ten_input.text()
        email = self.email_input.text()
        sdt = self.sdt_input.text()
        # Hiển thị hộp thoại thông báo và chờ đợi người dùng nhấn nút OK
        QMessageBox.information(self, 'Thông báo!', f'Đã sửa thành công khách hàng: {ten}, {email}, {sdt}')


    #Xử lý xoá
    def Xoa(self):
        ten = self.ten_input.text()
        email = self.email_input.text()
        sdt = self.sdt_input.text()
        # Hiển thị hộp thoại thông báo và chờ đợi người dùng nhấn nút OK
        QMessageBox.information(self, 'Thông báo!', f'Đã xoá thành công khách hàng: {ten}, {email}, {sdt}')

    #Xử lý lưu
    # Xử lý lưu
    def Luu(self):
        self.ten = self.ten_input.text()
        self.email = self.email_input.text()
        self.sdt = self.sdt_input.text()

        # Thêm thông tin vào list
        self.dsTen.append(self.ten)
        self.dsEmail.append(self.email)
        self.dsSdt.append(self.sdt)

        self.danhSach = pd.DataFrame({'Tên': self.dsTen, 'Email': self.dsEmail, 'Sdt': self.dsSdt})
        # In danh sách khách hàng dưới dạng bảng
        print(self.danhSach)

    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)  # Thay đổi con trỏ chuột thành hình tay trỏ khi vào nút

    def leaveEvent(self, event):
        self.unsetCursor()  # Đặt lại con trỏ mặc định khi rời khỏi nút
    def backGround(self):
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor(30, 87, 153))
        gradient.setColorAt(1.0, QColor(0, 0, 0))
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = quanLyKhachHang()
    window.show()
    sys.exit(app.exec())