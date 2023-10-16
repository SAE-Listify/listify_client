from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Sidebar(QWidget):
    def __init__(self, parent=None):
        super(Sidebar, self).__init__(parent)

        self.setFrameShape(QFrame.StyledPanel)
        self.setFixedWidth(150)  # Width of the sidebar

        self.layout = QVBoxLayout(self)
        self.setup_icons()
        self.setup_projects()

    def setup_icons(self):
        icons = ['path_to_icon1', 'path_to_icon2', 'path_to_icon3', 'path_to_icon4']

        for icon_path in icons:
            icon_label = QLabel(self)
            pixmap = QPixmap(icon_path)
            icon_label.setPixmap(pixmap)
            icon_label.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(icon_label)

        self.layout.addStretch()

    def setup_projects(self):
        # Create button
        create_button = QPushButton("Create", self)
        create_button.clicked.connect(self.create_project)  # Connect to a method to handle project creation
        self.layout.addWidget(create_button)

        # Project buttons
        project1_button = QPushButton("Project1", self)
        project1_button.clicked.connect(self.open_project1)
        self.layout.addWidget(project1_button)

        project2_button = QPushButton("Project2", self)
        project2_button.clicked.connect(self.open_project2)
        self.layout.addWidget(project2_button)

    def create_project(self):
        # Logic to handle project creation
        pass

    def open_project1(self):
        # Logic to open Project1
        pass

    def open_project2(self):
        # Logic to open Project2
        pass
