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
        self.comboBox_3.activated.connect(self.update_morph_func)
        self.comboBox_4.activated.connect(self.update_hough_func)

        self.paramsvalues.valueChanged.connect(self.update_transform_func)
        self.iterations.valueChanged.connect(self.update_morph_func)

        self.threshold.valueChanged.connect(self.update_hough_func)

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
            self.org1.setScaledContents(True)
            self.org2.setPixmap(pixmap)
            self.org2.setScaledContents(True)
            self.org3.setPixmap(pixmap)
            self.org3.setScaledContents(True)
            self.org4.setPixmap(pixmap)
            self.org4.setScaledContents(True)


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

    def load_img_binarized(self,img,threshold=(150,255)):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        _, img_th = cv2.threshold(img,threshold[0],threshold[1],cv2.THRESH_BINARY)
        return img_th

    def detect_lines(self,img,threshold):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,50,150,apertureSize=3)
        lines = cv2.HoughLinesP(edges,
                    1,
                    np.pi/180,
                    threshold=threshold,
                    minLineLength=5,
                    maxLineGap=10
                    )
        for points in lines:
            x1,y1,x2,y2=points[0]
            cv2.line(img,(x1,y1),(x2,y2),(125,0,125),2)
        return img

    def detect_circles(self,img,threshold):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray,9)
        rows = gray.shape[0]
        circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT, 1,rows/8,
                                   param1=70, param2=30,
                                   minRadius=0, maxRadius=threshold)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                center = (i[0], i[1])
                cv2.circle(img, center, 1, (0,100,100), 3)
                radius = i[2]
                cv2.circle(img, center, radius, (255,0,255), 3)

        return img

    def update_transform_func(self):
        if self.comboBox.currentText() == "Inversement":
            self.paramsvalues.setVisible(False)
            self.label_17.setVisible(False)

            img = self.inverse_img(self.load_image(self.imgPath.text()))

            height, width, channels = img.shape
            bytes_per_line = 3 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_image)
            self.fin1.setScaledContents(True)
            self.fin1.setPixmap(pixmap)

        elif self.comboBox.currentText() == "Egalisation":
            self.paramsvalues.setVisible(False)
            self.label_17.setVisible(False)
            img = self.equalise_img(self.load_image(self.imgPath.text()))

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(q_image)
            self.fin1.setScaledContents(True)
            self.fin1.setPixmap(pixmap)

        elif self.comboBox.currentText() == "Etirement":
            self.paramsvalues.setVisible(False)
            self.label_17.setVisible(False)
            img = self.stretch_img(self.load_image(self.imgPath.text()))

            height, width, channels = img.shape
            bytes_per_line = 3 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_image)
            self.fin1.setScaledContents(True)
            self.fin1.setPixmap(pixmap)

        elif self.comboBox.currentText() == "Fct Beta":
            self.label_17.setText("Beta")
            self.paramsvalues.setVisible(True)
            self.label_17.setVisible(True)
            img = self.load_image(self.imgPath.text())

            beta = self.paramsvalues.value()
            tran_img = np.uint8(255*(1-(1-(img/255))**beta))

            height, width, channels = tran_img.shape
            bytes_per_line = 3 * width
            q_image = QImage(tran_img.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_image)
            self.fin1.setScaledContents(True)
            self.fin1.setPixmap(pixmap)

        elif self.comboBox.currentText() == "Fct Gamma":
            self.label_17.setText("Gamma")
            self.paramsvalues.setVisible(True)
            self.label_17.setVisible(True)
            img = self.load_image(self.imgPath.text())

            gamma = self.paramsvalues.value()
            gamma_trans = np.uint8(255*((img/255)**gamma))

            height, width, channels = gamma_trans.shape
            bytes_per_line = 3 * width
            q_image = QImage(gamma_trans.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_image)
            self.fin1.setScaledContents(True)
            self.fin1.setPixmap(pixmap)


    def update_filter_func(self):
        if self.comboBox_2.currentText() == "Moyenne":

            img = self.filtreMoy(self.load_image(self.imgPath.text()),2)

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(q_image)
            self.fin2.setScaledContents(True)
            self.fin2.setPixmap(pixmap)

        if self.comboBox_2.currentText() == "Median":
            img = self.filtreMedian(self.load_image(self.imgPath.text()),2)

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(q_image)
            self.fin2.setScaledContents(True)
            self.fin2.setPixmap(pixmap)


    def update_morph_func(self):
        if self.comboBox_3.currentText()  == "Erosion":
            img = self.load_image(self.imgPath.text())
            img = self.load_img_binarized(img)

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(q_image)

            self.org4.setPixmap(pixmap)

            kernel = np.ones((3,3),np.uint8)
            img = cv2.erode(img,kernel,self.iterations.value())

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(q_image)
            self.fin4.setScaledContents(True)
            self.fin4.setPixmap(pixmap)

        elif self.comboBox_3.currentText()  == "Dilatation":
            img = self.load_image(self.imgPath.text())
            img = self.load_img_binarized(img)

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(q_image)

            self.org4.setPixmap(pixmap)

            kernel = np.ones((3,3),np.uint8)
            img = cv2.dilate(img,kernel,self.iterations.value())

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(q_image)
            self.fin4.setScaledContents(True)
            self.fin4.setPixmap(pixmap)

        elif self.comboBox_3.currentText()  == "Contour":
            img = self.load_image(self.imgPath.text())
            img = self.load_img_binarized(img)

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(q_image)

            self.org4.setPixmap(pixmap)

            kernel = np.ones((3,3),np.uint8)
            img = cv2.dilate(img,kernel,self.iterations.value()) - cv2.erode(img,kernel,self.iterations.value())

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(q_image)
            self.fin4.setScaledContents(True)
            self.fin4.setPixmap(pixmap)

        elif self.comboBox_3.currentText()  == "Ouverture":
            img = self.load_image(self.imgPath.text())
            img = self.load_img_binarized(img)

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(q_image)

            self.org4.setPixmap(pixmap)

            kernel = np.ones((3,3),np.uint8)
            img = cv2.dilate(cv2.erode(img,kernel,self.iterations.value()),kernel,self.iterations.value())
            print(self.iterations.value())

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(q_image)
            self.fin4.setScaledContents(True)
            self.fin4.setPixmap(pixmap)

        elif self.comboBox_3.currentText()  == "Fermeture":
            img = self.load_image(self.imgPath.text())
            img = self.load_img_binarized(img)

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(q_image)

            self.org4.setPixmap(pixmap)

            kernel = np.ones((3,3),np.uint8)
            img = cv2.erode(cv2.dilate(img,kernel,self.iterations.value()),kernel,self.iterations.value())

            height, width = img.shape
            bytes_per_line = 1 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(q_image)
            self.fin4.setScaledContents(True)
            self.fin4.setPixmap(pixmap)

    def update_hough_func(self):
        if self.comboBox_4.currentText() == 'Detection des droites':
            img = self.detect_lines(self.load_image(self.imgPath.text()),self.threshold.value())

            height, width, channels = img.shape
            bytes_per_line = 3 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_image)
            self.fin3.setScaledContents(True)
            self.fin3.setPixmap(pixmap)

        elif self.comboBox_4.currentText() == 'Detection des cercles':
            img = self.detect_circles(self.load_image(self.imgPath.text()),self.threshold.value())

            height, width, channels = img.shape
            bytes_per_line = 3 * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_image)
            self.fin3.setScaledContents(True)
            self.fin3.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ImageEditor()
    widget.setWindowTitle("Image Editor")
    widget.show()

    sys.exit(app.exec())
