# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfacegraphique.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 745)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_ajouter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ajouter.setGeometry(QtCore.QRect(160, 340, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter.setFont(font)
        self.pushButton_ajouter.setObjectName("pushButton_ajouter")
        self.label_numero = QtWidgets.QLabel(self.centralwidget)
        self.label_numero.setGeometry(QtCore.QRect(160, 25, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_numero.setFont(font)
        self.label_numero.setObjectName("label_numero")
        self.lineEdit_numero = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_numero.setGeometry(QtCore.QRect(160, 70, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_numero.setFont(font)
        self.lineEdit_numero.setObjectName("lineEdit_numero")
        self.textBrowser_afficher = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_afficher.setGeometry(QtCore.QRect(160, 520, 841, 171))
        self.textBrowser_afficher.setObjectName("textBrowser_afficher")
        self.lineEdit_nom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nom.setGeometry(QtCore.QRect(160, 240, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_nom.setFont(font)
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.label_nom = QtWidgets.QLabel(self.centralwidget)
        self.label_nom.setGeometry(QtCore.QRect(160, 200, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_nom.setFont(font)
        self.label_nom.setObjectName("label_nom")
        self.label_erreur_numero = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_numero.setEnabled(True)
        self.label_erreur_numero.setGeometry(QtCore.QRect(160, 140, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_numero.setFont(font)
        self.label_erreur_numero.setObjectName("label_erreur_numero")
        self.pushButton_supprimer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_supprimer.setGeometry(QtCore.QRect(490, 340, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_supprimer.setFont(font)
        self.pushButton_supprimer.setObjectName("pushButton_supprimer")
        self.pushButton_modifier = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_modifier.setGeometry(QtCore.QRect(330, 340, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_modifier.setFont(font)
        self.pushButton_modifier.setObjectName("pushButton_modifier")
        self.label_programme = QtWidgets.QLabel(self.centralwidget)
        self.label_programme.setGeometry(QtCore.QRect(470, 190, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_programme.setFont(font)
        self.label_programme.setObjectName("label_programme")
        self.comboBox_programme = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_programme.setGeometry(QtCore.QRect(470, 240, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_programme.setFont(font)
        self.comboBox_programme.setObjectName("comboBox_programme")
        self.comboBox_programme.addItem("")
        self.comboBox_programme.addItem("")
        self.comboBox_programme.addItem("")
        self.pushButton_sauvegarder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sauvegarder.setGeometry(QtCore.QRect(160, 420, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_sauvegarder.setFont(font)
        self.pushButton_sauvegarder.setObjectName("pushButton_sauvegarder")
        self.pushButton_afficher_listview = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_afficher_listview.setGeometry(QtCore.QRect(490, 420, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_afficher_listview.setFont(font)
        self.pushButton_afficher_listview.setObjectName("pushButton_afficher_listview")
        self.dateEdit_DNaiss = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_DNaiss.setGeometry(QtCore.QRect(670, 70, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_DNaiss.setFont(font)
        self.dateEdit_DNaiss.setObjectName("dateEdit_DNaiss")
        self.label_date_naiss = QtWidgets.QLabel(self.centralwidget)
        self.label_date_naiss.setGeometry(QtCore.QRect(670, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_date_naiss.setFont(font)
        self.label_date_naiss.setObjectName("label_date_naiss")
        self.pushButton_serealiser = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_serealiser.setGeometry(QtCore.QRect(330, 420, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_serealiser.setFont(font)
        self.pushButton_serealiser.setObjectName("pushButton_serealiser")
        self.label_erreur_nom = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_nom.setEnabled(True)
        self.label_erreur_nom.setGeometry(QtCore.QRect(160, 300, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_nom.setFont(font)
        self.label_erreur_nom.setObjectName("label_erreur_nom")
        self.label_erreur_date = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_date.setEnabled(True)
        self.label_erreur_date.setGeometry(QtCore.QRect(670, 120, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_date.setFont(font)
        self.label_erreur_date.setObjectName("label_erreur_date")
        self.label_erreur_Etu_Existe = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_Etu_Existe.setGeometry(QtCore.QRect(160, 120, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_Etu_Existe.setFont(font)
        self.label_erreur_Etu_Existe.setObjectName("label_erreur_Etu_Existe")
        self.label_erreur_Etu_Inexistant = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_Etu_Inexistant.setGeometry(QtCore.QRect(160, 130, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_Etu_Inexistant.setFont(font)
        self.label_erreur_Etu_Inexistant.setObjectName("label_erreur_Etu_Inexistant")
        self.label_erreur_fichier = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_fichier.setGeometry(QtCore.QRect(460, 480, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_fichier.setFont(font)
        self.label_erreur_fichier.setAutoFillBackground(True)
        self.label_erreur_fichier.setTextFormat(QtCore.Qt.RichText)
        self.label_erreur_fichier.setScaledContents(False)
        self.label_erreur_fichier.setWordWrap(False)
        self.label_erreur_fichier.setObjectName("label_erreur_fichier")
        self.label_Grandeur = QtWidgets.QLabel(self.centralwidget)
        self.label_Grandeur.setGeometry(QtCore.QRect(810, 260, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_Grandeur.setFont(font)
        self.label_Grandeur.setObjectName("label_Grandeur")
        self.comboBox_grandeur = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_grandeur.setGeometry(QtCore.QRect(810, 300, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_grandeur.setFont(font)
        self.comboBox_grandeur.setObjectName("comboBox_grandeur")
        self.comboBox_grandeur.addItem("")
        self.comboBox_grandeur.addItem("")
        self.comboBox_grandeur.addItem("")
        self.label_localisation = QtWidgets.QLabel(self.centralwidget)
        self.label_localisation.setGeometry(QtCore.QRect(810, 360, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_localisation.setFont(font)
        self.label_localisation.setObjectName("label_localisation")
        self.comboBox_localisation = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_localisation.setGeometry(QtCore.QRect(810, 400, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_localisation.setFont(font)
        self.comboBox_localisation.setObjectName("comboBox_localisation")
        self.comboBox_localisation.addItem("")
        self.comboBox_localisation.addItem("")
        self.comboBox_localisation.addItem("")
        self.label_numero_casier = QtWidgets.QLabel(self.centralwidget)
        self.label_numero_casier.setGeometry(QtCore.QRect(810, 160, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_numero_casier.setFont(font)
        self.label_numero_casier.setObjectName("label_numero_casier")
        self.lineEdit_numero_casier = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_numero_casier.setGeometry(QtCore.QRect(810, 190, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_numero_casier.setFont(font)
        self.lineEdit_numero_casier.setObjectName("lineEdit_numero_casier")
        self.label_erreur_numero_casier = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_numero_casier.setEnabled(True)
        self.label_erreur_numero_casier.setGeometry(QtCore.QRect(810, 240, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_numero_casier.setFont(font)
        self.label_erreur_numero_casier.setObjectName("label_erreur_numero_casier")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1147, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_ajouter, self.lineEdit_numero)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_ajouter.setText(_translate("MainWindow", "Ajouter"))
        self.label_numero.setText(_translate("MainWindow", "Numéro d\'étudiant"))
        self.label_nom.setText(_translate("MainWindow", "Nom de l\'étudiant"))
        self.label_erreur_numero.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\"> Numéro d\'étudiant invalide. Entrez une valeur numérique.</span></p></body></html>"))
        self.pushButton_supprimer.setText(_translate("MainWindow", "Supprimer"))
        self.pushButton_modifier.setText(_translate("MainWindow", "Modifier"))
        self.label_programme.setText(_translate("MainWindow", "Programme"))
        self.comboBox_programme.setItemText(0, _translate("MainWindow", "Technique de l\'informatique"))
        self.comboBox_programme.setItemText(1, _translate("MainWindow", "Sciences infirmières"))
        self.comboBox_programme.setItemText(2, _translate("MainWindow", "Administration"))
        self.pushButton_sauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.pushButton_afficher_listview.setText(_translate("MainWindow", " ListView"))
        self.label_date_naiss.setText(_translate("MainWindow", "Date de naissance"))
        self.pushButton_serealiser.setText(_translate("MainWindow", "Sérialiser"))
        self.label_erreur_nom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Nom d\'étudiant invalide. Entrez une valeur alphabétique.</span></p></body></html>"))
        self.label_erreur_date.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Date de naissance invalide. L\'âge doit être supérieur à 18 ans.</span></p></body></html>"))
        self.label_erreur_Etu_Existe.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">L\'étudiant existe déjà. Entrez un nouvel étudiant.</span></p></body></html>"))
        self.label_erreur_Etu_Inexistant.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">L\'étudiant n\'existe pas.</span></p></body></html>"))
        self.label_erreur_fichier.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_Grandeur.setText(_translate("MainWindow", "Grandeur de casier"))
        self.comboBox_grandeur.setItemText(0, _translate("MainWindow", "Petit"))
        self.comboBox_grandeur.setItemText(1, _translate("MainWindow", "Moyen"))
        self.comboBox_grandeur.setItemText(2, _translate("MainWindow", "Grand"))
        self.label_localisation.setText(_translate("MainWindow", "Localisation du casier"))
        self.comboBox_localisation.setItemText(0, _translate("MainWindow", "bloc A"))
        self.comboBox_localisation.setItemText(1, _translate("MainWindow", "bloc B"))
        self.comboBox_localisation.setItemText(2, _translate("MainWindow", "bloc C"))
        self.label_numero_casier.setText(_translate("MainWindow", "Numéro du Casier"))
        self.label_erreur_numero_casier.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Numéro du casier invalide. Entrez une valeur.</span></p></body></html>"))
