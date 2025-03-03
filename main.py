import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Простое приложение на PyQt5")
        self.setGeometry(100, 100, 400, 600)  # Размер окна

        # Основной вертикальный макет
        layout = QVBoxLayout(self)
        
        # 1. Шапка
        self.header = QLabel("Моё приложение", self)
        self.header.setStyleSheet("background-color: #1976D2; color: white; font-size: 20px; padding: 10px;")
        self.header.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.header)

        # 2. Центральная область (контейнер для страниц)
        self.pages = QStackedWidget(self)
        self.page_home = QLabel("Главная страница", self)
        self.page_search = QLabel("Поиск", self)
        self.page_settings = QLabel("Настройки", self)

        self.pages.addWidget(self.page_home)
        self.pages.addWidget(self.page_search)
        self.pages.addWidget(self.page_settings)
        layout.addWidget(self.pages)

        # 3. Нижняя панель навигации
        self.navbar = QHBoxLayout()
        self.btn_home = QPushButton("🏠 Главная")
        self.btn_search = QPushButton("🔍 Поиск")
        self.btn_settings = QPushButton("⚙️ Настройки")

        self.btn_home.clicked.connect(lambda: self.pages.setCurrentIndex(0))
        self.btn_search.clicked.connect(lambda: self.pages.setCurrentIndex(1))
        self.btn_settings.clicked.connect(lambda: self.pages.setCurrentIndex(2))

        self.navbar.addWidget(self.btn_home)
        self.navbar.addWidget(self.btn_search)
        self.navbar.addWidget(self.btn_settings)

        layout.addLayout(self.navbar)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())