# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_ImageEditor(object):
    def setupUi(self, ImageEditor):
        if not ImageEditor.objectName():
            ImageEditor.setObjectName(u"ImageEditor")
        ImageEditor.resize(757, 520)
        self.verticalLayout_24 = QVBoxLayout(ImageEditor)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(ImageEditor)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.imgPath = QLineEdit(ImageEditor)
        self.imgPath.setObjectName(u"imgPath")

        self.horizontalLayout_11.addWidget(self.imgPath)

        self.browseButton = QPushButton(ImageEditor)
        self.browseButton.setObjectName(u"browseButton")

        self.horizontalLayout_11.addWidget(self.browseButton)


        self.verticalLayout_23.addLayout(self.horizontalLayout_11)

        self.tabWidget = QTabWidget(ImageEditor)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(731, 451))
        self.basic = QWidget()
        self.basic.setObjectName(u"basic")
        self.verticalLayout_9 = QVBoxLayout(self.basic)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.basic)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)

        self.comboBox = QComboBox(self.basic)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_8.addWidget(self.comboBox)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.label_17 = QLabel(self.basic)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_8.addWidget(self.label_17)

        self.paramsvalues = QDoubleSpinBox(self.basic)
        self.paramsvalues.setObjectName(u"paramsvalues")

        self.horizontalLayout_8.addWidget(self.paramsvalues)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.basic)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.widget_3 = QWidget(self.basic)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(281, 211))
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.org1 = QLabel(self.widget_3)
        self.org1.setObjectName(u"org1")
        self.org1.setMinimumSize(QSize(241, 211))
        self.org1.setMaximumSize(QSize(257, 211))

        self.verticalLayout_5.addWidget(self.org1)


        self.verticalLayout_6.addWidget(self.widget_3)


        self.horizontalLayout_13.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.basic)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.widget_4 = QWidget(self.basic)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(271, 211))
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.fin1 = QLabel(self.widget_4)
        self.fin1.setObjectName(u"fin1")
        self.fin1.setMinimumSize(QSize(241, 211))
        self.fin1.setMaximumSize(QSize(247, 211))

        self.verticalLayout_4.addWidget(self.fin1)


        self.verticalLayout_7.addWidget(self.widget_4)


        self.horizontalLayout_13.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.tabWidget.addTab(self.basic, "")
        self.filter = QWidget()
        self.filter.setObjectName(u"filter")
        self.verticalLayout_10 = QVBoxLayout(self.filter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.filter)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.comboBox_2 = QComboBox(self.filter)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_7.addWidget(self.comboBox_2)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_2 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_16 = QLabel(self.filter)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_9.addWidget(self.label_16)

        self.iterations_2 = QSpinBox(self.filter)
        self.iterations_2.setObjectName(u"iterations_2")

        self.horizontalLayout_9.addWidget(self.iterations_2)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.binary = QCheckBox(self.filter)
        self.binary.setObjectName(u"binary")

        self.verticalLayout_3.addWidget(self.binary)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.filter)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.widget_5 = QWidget(self.filter)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(271, 211))
        self.org2 = QLabel(self.widget_5)
        self.org2.setObjectName(u"org2")
        self.org2.setGeometry(QRect(10, 5, 241, 211))
        self.org2.setMinimumSize(QSize(241, 211))
        self.org2.setMaximumSize(QSize(241, 211))

        self.verticalLayout_2.addWidget(self.widget_5)


        self.horizontalLayout_12.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.filter)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.widget_6 = QWidget(self.filter)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(271, 211))
        self.fin2 = QLabel(self.widget_6)
        self.fin2.setObjectName(u"fin2")
        self.fin2.setGeometry(QRect(10, 9, 241, 211))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fin2.sizePolicy().hasHeightForWidth())
        self.fin2.setSizePolicy(sizePolicy)
        self.fin2.setMinimumSize(QSize(241, 211))
        self.fin2.setMaximumSize(QSize(241, 211))

        self.verticalLayout.addWidget(self.widget_6)


        self.horizontalLayout_12.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)


        self.verticalLayout_10.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.filter, "")
        self.morph = QWidget()
        self.morph.setObjectName(u"morph")
        self.verticalLayout_16 = QVBoxLayout(self.morph)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.morph)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.comboBox_3 = QComboBox(self.morph)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout.addWidget(self.comboBox_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_15 = QLabel(self.morph)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_2.addWidget(self.label_15)

        self.iterations = QSpinBox(self.morph)
        self.iterations.setObjectName(u"iterations")

        self.horizontalLayout_2.addWidget(self.iterations)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_15.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.morph)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_14.addWidget(self.label_9)

        self.widget_7 = QWidget(self.morph)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_12 = QVBoxLayout(self.widget_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.org4 = QLabel(self.widget_7)
        self.org4.setObjectName(u"org4")
        self.org4.setMinimumSize(QSize(241, 211))
        self.org4.setMaximumSize(QSize(241, 211))

        self.verticalLayout_12.addWidget(self.org4)


        self.verticalLayout_14.addWidget(self.widget_7)


        self.horizontalLayout_14.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_6 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.morph)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_13.addWidget(self.label_10)

        self.widget_8 = QWidget(self.morph)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_11 = QVBoxLayout(self.widget_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.fin4 = QLabel(self.widget_8)
        self.fin4.setObjectName(u"fin4")
        self.fin4.setMinimumSize(QSize(241, 211))
        self.fin4.setMaximumSize(QSize(241, 211))

        self.verticalLayout_11.addWidget(self.fin4)


        self.verticalLayout_13.addWidget(self.widget_8)


        self.horizontalLayout_14.addLayout(self.verticalLayout_13)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)


        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.tabWidget.addTab(self.morph, "")
        self.hough = QWidget()
        self.hough.setObjectName(u"hough")
        self.verticalLayout_22 = QVBoxLayout(self.hough)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.hough)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.comboBox_4 = QComboBox(self.hough)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_4.addWidget(self.comboBox_4)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_14 = QLabel(self.hough)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_5.addWidget(self.label_14)

        self.threshold = QSlider(self.hough)
        self.threshold.setObjectName(u"threshold")
        self.threshold.setMaximum(150)
        self.threshold.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.threshold)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_21.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_11 = QLabel(self.hough)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_19.addWidget(self.label_11)

        self.widget = QWidget(self.hough)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_18 = QVBoxLayout(self.widget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.org3 = QLabel(self.widget)
        self.org3.setObjectName(u"org3")
        self.org3.setMinimumSize(QSize(241, 211))
        self.org3.setMaximumSize(QSize(241, 211))

        self.verticalLayout_18.addWidget(self.org3)


        self.verticalLayout_19.addWidget(self.widget)


        self.horizontalLayout_15.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_7 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_12 = QLabel(self.hough)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_20.addWidget(self.label_12)

        self.widget_2 = QWidget(self.hough)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_17 = QVBoxLayout(self.widget_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.fin3 = QLabel(self.widget_2)
        self.fin3.setObjectName(u"fin3")
        self.fin3.setMinimumSize(QSize(241, 211))
        self.fin3.setMaximumSize(QSize(241, 211))

        self.verticalLayout_17.addWidget(self.fin3)


        self.verticalLayout_20.addWidget(self.widget_2)


        self.horizontalLayout_15.addLayout(self.verticalLayout_20)


        self.verticalLayout_21.addLayout(self.horizontalLayout_15)


        self.verticalLayout_22.addLayout(self.verticalLayout_21)

        self.tabWidget.addTab(self.hough, "")

        self.verticalLayout_23.addWidget(self.tabWidget)


        self.verticalLayout_24.addLayout(self.verticalLayout_23)


        self.retranslateUi(ImageEditor)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(ImageEditor)
    # setupUi

    def retranslateUi(self, ImageEditor):
        ImageEditor.setWindowTitle(QCoreApplication.translate("ImageEditor", u"ImageEditor", None))
        self.label_13.setText(QCoreApplication.translate("ImageEditor", u"Charger une image", None))
        self.browseButton.setText(QCoreApplication.translate("ImageEditor", u"Browse", None))
        self.label.setText(QCoreApplication.translate("ImageEditor", u"Choisir la transformation", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("ImageEditor", u"Inversement", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("ImageEditor", u"Egalisation", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("ImageEditor", u"Etirement", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("ImageEditor", u"Fct Beta", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("ImageEditor", u"Fct Gamma", None))

        self.label_17.setText(QCoreApplication.translate("ImageEditor", u"Beta", None))
        self.label_2.setText(QCoreApplication.translate("ImageEditor", u"Image Originale", None))
        self.org1.setText(QCoreApplication.translate("ImageEditor", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("ImageEditor", u"Image Finale", None))
        self.fin1.setText(QCoreApplication.translate("ImageEditor", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.basic), QCoreApplication.translate("ImageEditor", u"Basiques", None))
        self.label_4.setText(QCoreApplication.translate("ImageEditor", u"Choisir un filtre", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("ImageEditor", u"Median", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("ImageEditor", u"Moyenne", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("ImageEditor", u"Sobel", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("ImageEditor", u"Prewitt", None))

        self.label_16.setText(QCoreApplication.translate("ImageEditor", u"Iterations", None))
        self.binary.setText(QCoreApplication.translate("ImageEditor", u"Avec binarisation", None))
        self.label_7.setText(QCoreApplication.translate("ImageEditor", u"Image Originale", None))
        self.org2.setText(QCoreApplication.translate("ImageEditor", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("ImageEditor", u"Image Finale", None))
        self.fin2.setText(QCoreApplication.translate("ImageEditor", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filter), QCoreApplication.translate("ImageEditor", u"Filtrage", None))
        self.label_5.setText(QCoreApplication.translate("ImageEditor", u"Choisir une morphologie", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("ImageEditor", u"Erosion", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("ImageEditor", u"Dilatation", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("ImageEditor", u"Contour", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("ImageEditor", u"Ouverture", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("ImageEditor", u"Fermeture", None))

        self.label_15.setText(QCoreApplication.translate("ImageEditor", u"Iterations", None))
        self.label_9.setText(QCoreApplication.translate("ImageEditor", u"Image Originale", None))
        self.org4.setText(QCoreApplication.translate("ImageEditor", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("ImageEditor", u"Image Finale", None))
        self.fin4.setText(QCoreApplication.translate("ImageEditor", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.morph), QCoreApplication.translate("ImageEditor", u"Morphologie", None))
        self.label_6.setText(QCoreApplication.translate("ImageEditor", u"Choisir un type", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("ImageEditor", u"Detection des droites", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("ImageEditor", u"Detection des cercles", None))

        self.label_14.setText(QCoreApplication.translate("ImageEditor", u"Threshold", None))
        self.label_11.setText(QCoreApplication.translate("ImageEditor", u"Image Originale", None))
        self.org3.setText(QCoreApplication.translate("ImageEditor", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("ImageEditor", u"Image Finale", None))
        self.fin3.setText(QCoreApplication.translate("ImageEditor", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hough), QCoreApplication.translate("ImageEditor", u"Hough", None))
    # retranslateUi

