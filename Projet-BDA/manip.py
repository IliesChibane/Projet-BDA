from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPoint
from DBrequests import *
from json2html import *




def quitter():
    QCoreApplication.instance().quit() 

def minimizer(window):
    window.showMinimized()

def qst1(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("1. Determiner le nombre exact de pays ")
    textEdit.insertPlainText(f"{QST1()}")


def qst2(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("2. Lister les différents continents ")
    textEdit.insertPlainText(f"{QST2()}")

def qst3(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("3. Lister les informations de l’Algérie ")
    textEdit.insertHtml(f"{json2html.convert(json = QST3())}")

def qst4(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("4. Lister les pays du continent Africain, ayant une population inférieure à 100000 habitants ")
    textEdit.insertPlainText(f"{QST4()}")

def qst5(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("5. Lister les pays indépendant du continent océanique ")
    textEdit.insertPlainText(f"{QST5()}")

def qst6(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("6. Quel est le plus gros continent en termes de surface ? (un seul continent affiché à la fin) ")
    textEdit.insertHtml(f"{QST6()}")

def qst7(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("7. Donner par continents le nombre de pays, la population totale et en bonus le nombre de pays indépendant. ")
    textEdit.insertHtml(f"{json2html.convert(json = QST7())}")

def qst8(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("8. Donner la population totale des villes d’Algérie ")
    textEdit.insertPlainText(f"{QST8()}")

def qst9(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("9. Donner la capitale (uniquement nom de la ville et population) d’Algérie ")
    textEdit.insertPlainText(f"{QST9()}")

def qst10(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("10. Quelles sont les langues parlées dans plus de 15 pays ? ")
    textEdit.insertHtml(f"{json2html.convert(json = QST10())}")


def qst11(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("11. Calculer pour chaque pays le nombre de villes (pour les pays ayant au moins 100 villes), en les triant par ordre décroissant du nombre de villes ")
    textEdit.insertHtml(f"{json2html.convert(json = QST11())}")


def qst12(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("12. Lister les 10 villes les plus habitées, ainsi que leur pays, dans l’ordre décroissant de la population ")
    textEdit.insertHtml(f"{json2html.convert(json = QST12())}")


def qst13(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("13. Lister les pays pour lesquels l’Arabe est une langue officielle ")
    textEdit.insertPlainText(f"{QST13()}")


def qst14(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("14. Lister les 5 pays avec le plus de langues parlées ")
    textEdit.insertPlainText(f"{QST14()}")


def qst15(plainTextEdit, textEdit):
    plainTextEdit.clear()
    textEdit.clear()
    plainTextEdit.insertPlainText("15. Lister les pays pour lesquels la somme des populations des villes est supérieure à la population du pays.")
    textEdit.insertHtml(f"{json2html.convert(json = QST15())}")



