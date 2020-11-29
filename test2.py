import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
# creation de la fenetre
fen = QWidget()
def appui_bouton1():
    print("Appui sur le bouton1")
def appui_bouton2():
    print("Appui sur le bouton2")

# creation du bouton
bouton1 = QPushButton("mon bouton1 avec une gestion d'appui")
# on connecte le signal "clicked" a la fonction appui_bouton
bouton1.clicked.connect(appui_bouton1)
# le bouton est rendu visible
bouton1.show()
# creation du bouton2
bouton2 = QPushButton("mon bouton2 avec une gestion d'appui")
# on connecte le signal "clicked" a la fonction appui_bouton
bouton2.clicked.connect(appui_bouton2)
# le bouton est rendu visible
bouton2.show()
# creation du gestionnaire de mise en forme de type QHBoxLayout
layout = QVBoxLayout()
# ajout du premier bouton au gestionnaire de mise en forme
layout.addWidget(bouton1)
# ajout du deuxieme bouton au gestionnaire de mise en forme
layout.addWidget(bouton2)
fen.setLayout(layout)
fen.show()

app.exec_()
