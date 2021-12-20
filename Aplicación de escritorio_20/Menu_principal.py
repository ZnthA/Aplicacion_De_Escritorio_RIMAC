import sys
from PyQt5 import uic, QtWidgets
from ventanaClientes import *
from ventanaProductos import *
from arregloProductos import *
from arregloClientes import *
from ventanaVentas import *
from ventanaDetalleVentas import *
from ventanaFacturas import *

qtCreatorFile = "Menu_principal.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MenuPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnMClientes.clicked.connect(self.Abrir_MClientes)
        self.btnMProductos.clicked.connect(self.Abrir_MProductos)
        self.btnVentas.clicked.connect(self.Abrir_VVentas)
        self.btnDetalle.clicked.connect(self.Abrir_VDetalle)
        self.btnFacturas.clicked.connect(self.Abrir_VFacturas)
        self.btnSalir.clicked.connect(self.cerrar)
    def Abrir_MClientes(self):
    	self.ventanaMC=RegistroClientes()
    	self.ventanaMC.show()
    def Abrir_MProductos(self):
    	self.ventanaMP=RegistroProductos()
    	self.ventanaMP.show()
    def Abrir_VVentas(self):
        self.ventanaVV=VentanaVentas()
        self.ventanaVV.show()
    def Abrir_VDetalle(self):
        self.ventanaVDV=VentanaDetalleVentas()
        self.ventanaVDV.show()
    def Abrir_VFacturas(self):
        self.ventanaVF=VentanaFacturas()
        self.ventanaVF.show()
    def cerrar(self):
        self.close()





if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MenuPrincipal()
    window.show()
    sys.exit(app.exec_())