import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class XoaKhachHangWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Thiết lập các thuộc tính của cửa sổ
        self.setWindowTitle('Xóa Khách Hàng')
        self.setGeometry(100, 100, 300, 150)

        # Tạo layout
        self.layout = QVBoxLayout()

        # Tạo các widget
        self.id_label = QLabel('ID Khách Hàng:')
        self.id_input = QLineEdit()

        self.xoa_button = QPushButton('Xóa Khách Hàng')
        self.xoa_button.clicked.connect(self.xoa_khach_hang)

        # Thêm các widget vào layout
        self.layout.addWidget(self.id_label)
        self.layout.addWidget(self.id_input)
        self.layout.addWidget(self.xoa_button)

        # Đặt layout cho cửa sổ
        self.setLayout(self.layout)

    def xoa_khach_hang(self):
        khach_hang_id = self.id_input.text()

        # Ở đây bạn có thể thực hiện xóa khách hàng từ cơ sở dữ liệu hoặc danh sách của mình
        print(f'Đã xóa khách hàng với ID: {khach_hang_id}')

        # Xóa trường nhập liệu sau khi xóa
        self.id_input.clear()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = XoaKhachHangWindow()
    window.show()
    sys.exit(app.exec())

