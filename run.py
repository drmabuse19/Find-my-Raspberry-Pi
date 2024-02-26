from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QScrollArea,
    QHBoxLayout,
    QCheckBox,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette, QCursor
import sys
import socket
import nmap


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP


def ip_to_subnet(ip_address):
    subnet = ".".join(ip_address.split(".")[:3]) + ".0/24"
    return subnet


class NetworkScanner(QWidget):
    def __init__(self):
        super().__init__()
        self.isScanning = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Find my Raspberry Pi")
        self.setGeometry(100, 100, 400, 400)
        self.setFixedSize(400, 400)

        mainLayout = QVBoxLayout()

        networkRangeLayout = QHBoxLayout()
        self.rangeLabel = QLabel("Network Range:")
        networkRangeLayout.addWidget(self.rangeLabel)

        self.rangeEdit = QLineEdit(self)
        self.rangeEdit.setText(ip_to_subnet(get_local_ip()))
        networkRangeLayout.addWidget(self.rangeEdit)

        self.scanButton = QPushButton("Scan", self)
        self.scanButton.clicked.connect(self.scanNetwork)
        networkRangeLayout.addWidget(self.scanButton)

        mainLayout.addLayout(networkRangeLayout)

        self.onlyRaspberryCheckBox = QCheckBox("Only display Raspberry Pi devices")
        mainLayout.addWidget(self.onlyRaspberryCheckBox)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.resultLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setLayout(self.resultLayout)

        mainLayout.addWidget(self.scrollArea)

        self.setLayout(mainLayout)

    def scanNetwork(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)  # Set cursor to loading
        self.clearResults()
        scanner = nmap.PortScanner()
        network_range = self.rangeEdit.text()
        try:
            scanner.scan(hosts=network_range, arguments="-sn")
            for host in scanner.all_hosts():
                if "mac" in scanner[host]["addresses"]:
                    mac_address = scanner[host]["addresses"]["mac"]
                    isRaspberryPi = mac_address.startswith(
                        (
                            "28:CD:C1",
                            "2C:CF:67",
                            "B8:27:EB",
                            "D8:3A:DD",
                            "DC:A6:32",
                            "E4:5F:01",
                        )
                    )
                    if isRaspberryPi or not self.onlyRaspberryCheckBox.isChecked():
                        self.addDeviceRow(host, mac_address, isRaspberryPi)
        except Exception as e:
            self.addDeviceRow("Error", str(e), False)
        finally:
            QApplication.restoreOverrideCursor()  # Restore cursor to normal

    def clearResults(self):
        for i in reversed(range(self.resultLayout.count())):
            widget = self.resultLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def addDeviceRow(self, ip, mac, isRaspberryPi):
        text = f"<b>{'Raspberry Pi' if isRaspberryPi else 'Device'} found:</b> IP <b style='font-size:12pt;'>{ip}</b>, MAC {mac}"
        deviceRow = QLabel(text)
        deviceRow.setTextFormat(Qt.RichText)
        if isRaspberryPi:
            palette = deviceRow.palette()
            palette.setColor(QPalette.Window, QColor(Qt.green))
            deviceRow.setAutoFillBackground(True)
            deviceRow.setPalette(palette)
        self.resultLayout.addWidget(deviceRow)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = NetworkScanner()
    ex.show()
    sys.exit(app.exec_())
