# This Python file uses the following encoding: utf-8
import sys
import cv2
import numpy as np

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Signal, Slot

import myform_ui


class ImageEditor(QWidget, myform_ui.Ui_ImageEditor):
    fileSelected = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.browseButton.clicked.connect(self.browse)

        self.fileSelected.connect(self.imgPath.setText)
        self.comboBox.activated.connect(self.update_transform_func)
        self.comboBox_2.activated.connect(self.update_filter_func)

    def browse(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if file_name:
            # Emit the fileSelected signal
            self.fileSelected.emit(file_name)
            original = self.load_image(self.imgPath.text())
            height, width, channels = original.shape
            bytes_per_line = 3 * width
            q_image = QImage(original.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_image)
            self.org1.setPixmap(pixmap)
            self.org2.setPixmap(pixmap)
            self.org3.setPixmap(pixmap)
            self.org4.setPixmap(pixmap)


    def load_image(self,path):
        return cv2.cvtColor(cv2.imread(path),cv2.COLOR_BGR2RGB)

    def inverse_img(self,img):
        return 255 - img

    def equalise_img(self,img):
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        return cv2.equalizeHist(img)

    def stretch_img(self,img):
        return np.uint8(255*(img-img.min())/(img.max()-img.min())*img)

    def filtreMoy(self,img,k):
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        kernel = np.zeros([2*k+1,2*k+1,1],np.uint8)
        imgFiltered = np.zeros(img.shape,np.uint8)
        for i in range(1,img.shape[0]-1):
            for j in range(1,img.shape[1]-1):
                kernel = img[i-k:i+k,j-k:j+k]
                tmp = np.sum(kernel)/((2*k+1)**2)
                imgFiltered[i,j] = tmp

        return imgFiltered

    def filtreMedian(self,img,k):
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        kernel = np.zeros([2*k+1,2*k+1,1],np.uint8)
        imgFiltered = np.zeros(img.shape,np.uint8)
        for i in range(1,img.shape[0]-1):
            for j in range(1,img.shape[1]-1):
                kernel = img[i-k:i+k,j-k:j+k]
                tmp = np.median(kernel)
                imgFiltered[i,j] = tmp

        return imgFiltered

    def update_transform_func(self):
        if self.comboBox.currentText() == "Inversement":
            img = self.inverse_img(self.load_image(self.imgPath.text()))

            height, width, channels = img.shape
            bytes_per_line = 3 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_image)
            self.fin1.setPixmap(pixmap)

        elif self.comboBox.currentText() == "Egalisation":
            img = self.equalise_img(self.load_image(self.imgPath.text()))

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(q_image)
            self.fin1.setPixmap(pixmap)

        elif self.comboBox.currentText() == "Etirement":
            img = self.stretch_img(self.load_image(self.imgPath.text()))

            height, width, channels = img.shape
            bytes_per_line = 3 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_image)
            self.fin1.setPixmap(pixmap)

        elif self.comboBox.currentText() == "Fct Beta":
            img = self.stretch_img(self.load_image(self.imgPath.text()))

            height, width, channels = img.shape
            bytes_per_line = 3 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_image)
            self.fin1.setPixmap(pixmap)


    def update_filter_func(self):
        if self.comboBox_2.currentText() == "Moyenne":
            img = self.filtreMoy(self.load_image(self.imgPath.text()),2)

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(q_image)
            self.fin2.setPixmap(pixmap)

        if self.comboBox_2.currentText() == "Median":
            img = self.filtreMedian(self.load_image(self.imgPath.text()),2)

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(q_image)
            self.fin2.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ImageEditor()
    widget.setWindowTitle("Image Editor")
    widget.show()

    sys.exit(app.exec())
