# -----------------------------------------------------------------------------
# Testing Minecraft Plugins
# main.py
# by drazz
# -----------------------------------------------------------------------------
# Description: The main script for launching the GUI and logic.
# -----------------------------------------------------------------------------
# Version: 1.0.0
# Last Updated: January 23, 2024
# -----------------------------------------------------------------------------

import shutil
import subprocess
import sys
import os
import json
import requests

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QFileDialog, QMessageBox, QProgressBar, QProgressDialog

class MainForm(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.load_config()

    def init_ui(self):

        self.selected_java_path = ""
        self.args = "<java> -Xmx3G -Dfile.encoding=UTF-8 -jar <jar> nogui"
        self.selected_core = "CraftBukkit"
        self.selected_version = "1.8"
        self.config_file = "versions.json"
        self.last_selected_folder = os.path.expanduser("C:\Program Files\Java")

        self.setGeometry(100, 100, 679, 261)
        self.setWindowTitle('Testing Plugins')
        self.setFixedSize(679, 261)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.setStyleSheet("background-color: DimGray;")

        self.main_label = QLabel('Testing Minecraft Plugins', self)
        self.main_label.setStyleSheet("font: bold 15pt 'Comic Sans MS'; color: black;")
        self.main_label.setGeometry(215, 9, 260, 29)

        self.launch_button = QPushButton('Launch', self)
        self.launch_button.setStyleSheet("font: 10pt 'Bahnschrift'; background-color: DimGray; color: white; border: 2px solid white; font-weight: bold;")
        self.launch_button.setGeometry(253, 207, 201, 41)
        self.launch_button.clicked.connect(self.launch_button_clicked)

        self.select_java_button = QPushButton('Select Java', self)
        self.select_java_button.setStyleSheet("font: 11pt 'Bahnschrift'; background-color: DimGray; color: white; border: 1px solid white; font-weight: regular;")
        self.select_java_button.setGeometry(10, 113, 146, 28)
        self.select_java_button.clicked.connect(self.select_java_button_clicked)

        self.selected_java_label = QLabel('Selected Java: None', self)
        self.selected_java_label.setStyleSheet("font: 11pt 'Bahnschrift'; color: black; font-weight: regular;")
        self.selected_java_label.setGeometry(10, 145, 400, 20)

        self.java_args_box = QLineEdit('<java> -Xmx3G -Dfile.encoding=UTF-8 -jar <jar> nogui', self)
        self.java_args_box.setGeometry(163, 59, 348, 23)
        self.java_args_box.setStyleSheet("font: 10pt 'Bahnschrift'; font-weight: regular; color: black; background-color: white;")
        self.java_args_box.setToolTip('When the error appears: Java Not Recognized. Add argument: -XX:MaxPermSize=256M')
        self.java_args_box.textChanged.connect(self.java_args_box_changed)

        self.java_args_text = QLabel('Java Arguments:', self)
        self.java_args_text.setStyleSheet("font: 13pt 'Bahnschrift'; color: black; font-weight: regular;")
        self.java_args_text.setGeometry(15, 59, 131, 19)

        self.open_folder_button = QPushButton('Open Server Files', self)
        self.open_folder_button.setStyleSheet("font: 11pt 'Bahnschrift'; background-color: DimGray; color: white; border: 1px solid white; font-weight: regular;")
        self.open_folder_button.setGeometry(522, 113, 146, 28)
        self.open_folder_button.clicked.connect(self.open_folder_button_clicked)

        self.select_core_box = QComboBox(self)
        self.select_core_box.setStyleSheet("font: 11pt 'Bahnschrift'; background-color: DimGray; color: white; border: 1px solid white; font-weight: regular;")
        self.select_core_box.setGeometry(167, 116, 169, 24)
        self.select_core_box.addItems([])
        self.select_core_box.currentIndexChanged.connect(self.select_core_box_changed)

        self.version_box = QComboBox(self)
        self.version_box.setStyleSheet("font: 11pt 'Bahnschrift'; background-color: DimGray; color: white; border: 1px solid white; font-weight: regular;")
        self.version_box.setGeometry(342, 116, 169, 24)
        self.version_box.addItems([])
        self.version_box.currentIndexChanged.connect(self.version_box_changed)

    def open_folder_button_clicked(self):
        settings_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "server_files")
        os.system(f'explorer.exe "{settings_path}"')

    def select_java_button_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Java Executable (java.exe)")
        file_dialog.setWindowTitle("Select Java Executable")

        file_dialog.setDirectory(self.last_selected_folder)

        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            self.selected_java_path = selected_file
            self.selected_java_label.setText(f"Selected Java: {selected_file}")
            self.last_selected_folder = os.path.dirname(selected_file)

    def launch_button_clicked(self):
        if not self.selected_java_path:
            QMessageBox.warning(self, 'Java Path', 'Java path is not selected.', QMessageBox.Ok)
            return

        if not self.args:
            QMessageBox.warning(self, 'Java Arguments', 'Java arguments are missing.', QMessageBox.Ok)
            return

        if not self.selected_core:
            QMessageBox.warning(self, 'Core', 'Choose a core!', QMessageBox.Ok)
            return

        if not self.selected_version:
            QMessageBox.warning(self, 'Version', 'Choose a version!', QMessageBox.Ok)
            return
        
        root_folder = os.path.dirname(os.path.abspath(sys.argv[0]))
        server_folder = os.path.join(root_folder, "servers", f"{self.selected_core}-{self.selected_version}")

        if os.path.exists(server_folder):
            self.launchServer(server_folder)
        else:
            self.createServer(server_folder)

    def java_args_box_changed(self):
        self.args = self.java_args_box.text()

    def version_box_changed(self):
        self.selected_version = self.version_box.currentText()

    def load_config(self):
            try:
                with open(self.config_file, 'r') as config_file:
                    self.config_data = json.load(config_file)

                    core_names = [core["name"] for core in self.config_data["cores"]]
                    self.select_core_box.addItems(core_names)
                    self.load_versions_for_core(core_names[0])

            except Exception as e:
                QMessageBox.warning(self, 'Config', 'Config loading error.', QMessageBox.Ok)

    def load_versions_for_core(self, core_name):
        self.version_box.clear()
        selected_core = next((core for core in self.config_data["cores"] if core["name"] == core_name), None)

        if selected_core:
            version_names = [version["version"] for version in selected_core["versions"]]
            self.version_box.addItems(version_names)

    def select_core_box_changed(self, index):
        selected_core_name = self.select_core_box.currentText()
        self.load_versions_for_core(selected_core_name)
        self.selected_core = self.select_core_box.currentText()

    def launchServer(self, server_folder):
        self.copy_files_to_server(server_folder)
        self.replace_launch_bat_args(server_folder)
        self.run_server(server_folder)

    def createServer(self, server_folder):
        self.copy_files_to_server(server_folder)
        self.download_server(server_folder)
        self.replace_launch_bat_args(server_folder)
        self.run_server(server_folder)

    def copy_files_to_server(self, server_folder):
        source_folder = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "server_files")
        try:
            shutil.copytree(source_folder, server_folder, dirs_exist_ok=True)
        except Exception as e:
            print(f"Error copying files to server: {e}")

    def replace_launch_bat_args(self, server_folder):
        try:
            formatted_args = ('@ECHO OFF\n' + ':server_start\n' + 'echo Developed by drazz\n' + f'cd {server_folder}\n' + self.args.replace("<java>", f'"{self.selected_java_path}"').replace("<jar>", f"{self.selected_core}-{self.selected_version}.jar") + '\ntimeout 5\n' + 'goto server_start')
            bat_file_path = f"{server_folder}/Launch.bat" 

            with open(bat_file_path, 'w') as bat_file:
                bat_file.write(formatted_args)

        except Exception as e:
            QMessageBox.warning(self, 'Error', 'Startup file update error.', QMessageBox.Ok)

    def run_server(self, server_folder):
        launch_bat_path = os.path.join(server_folder, "Launch.bat")
        try:
            CREATE_NEW_CONSOLE = 0x00000010
            subprocess.Popen(launch_bat_path, creationflags=CREATE_NEW_CONSOLE)
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Server startup error: {str(e)}', QMessageBox.Ok)

    def download_server(self, server_folder):
        selected_core_data = next((core for core in self.config_data["cores"] if core["name"] == self.selected_core), None)

        if selected_core_data:
            selected_version_data = next((version for version in selected_core_data["versions"] if version["version"] == self.selected_version), None)

            if selected_version_data:
                download_link = selected_version_data["downloadLink"]
                file_name = f"{self.selected_core}-{self.selected_version}.jar"
                file_path = os.path.join(server_folder, file_name)

                try:
                    response = requests.get(download_link, stream=True)
                    total_size = int(response.headers.get('content-length', 0))

                    progress_dialog = QProgressDialog(f'Download: {self.selected_core}-{self.selected_version}.jar', None, 0, total_size, self)
                    progress_dialog.setWindowTitle('Loading the kernel...')
                    progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
                    progress_dialog.setStyleSheet("font: 11pt 'Bahnschrift'; font-weight: regular;")
                    progress_dialog.setFixedSize(400, 100)

                    progress_dialog.setWindowFlags(progress_dialog.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint & ~QtCore.Qt.WindowContextHelpButtonHint)

                    with open(file_path, 'wb') as file:
                        for data in response.iter_content(chunk_size=1024):
                            progress_dialog.setValue(progress_dialog.value() + len(data))
                            file.write(data)

                    progress_dialog.setValue(total_size)
                    progress_dialog.accept()

                except Exception as e:
                    QMessageBox.warning(self, 'Error', f'Core download error: {str(e)}', QMessageBox.Ok)
            else:
                QMessageBox.warning(self, 'Error', 'Core download error.', QMessageBox.Ok)
        else:
            QMessageBox.warning(self, 'Error', 'Core download error.', QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('logo.ico'))
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())
