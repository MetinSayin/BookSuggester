# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/sayin/PycharmProjects/BookSuggester/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 679)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.searchBar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBar.setText("")
        self.searchBar.setObjectName("searchBar")
        self.gridLayout.addWidget(self.searchBar, 1, 0, 1, 2)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy)
        self.listWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listWidget_2.setBatchSize(1000)
        self.listWidget_2.setWordWrap(True)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 2, 2, 1, 1)
        self.bookPictures = QtWidgets.QLabel(self.centralwidget)
        self.bookPictures.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookPictures.sizePolicy().hasHeightForWidth())
        self.bookPictures.setSizePolicy(sizePolicy)
        self.bookPictures.setMinimumSize(QtCore.QSize(0, 0))
        self.bookPictures.setText("")
        self.bookPictures.setObjectName("bookPictures")
        self.gridLayout.addWidget(self.bookPictures, 2, 1, 1, 1)
        self.searchBookBt = QtWidgets.QPushButton(self.centralwidget)
        self.searchBookBt.setObjectName("searchBookBt")
        self.gridLayout.addWidget(self.searchBookBt, 1, 2, 1, 1)
        self.listSeachedBooks = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listSeachedBooks.sizePolicy().hasHeightForWidth())
        self.listSeachedBooks.setSizePolicy(sizePolicy)
        self.listSeachedBooks.setObjectName("listSeachedBooks")
        self.gridLayout.addWidget(self.listSeachedBooks, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchBookBt.setText(_translate("MainWindow", "Search For Books"))

