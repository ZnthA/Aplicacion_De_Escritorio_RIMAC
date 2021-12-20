from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from arregloProductos import *
from arregloClientes import *
from arregloDetalleVenta import *
from arregloFactura import *
from ventanaVentas import *

class VentanaDetalleVentas(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaDetalleVentas,self).__init__(parent)
        uic.loadUi("ventanaDetalleVentas.ui", self)
    
        self.btnMostrar.clicked.connect(self.listar)

    def listar(self):
        aDetVent = ArregloDetalleVenta()
        self.tblDetalleVenta.setRowCount(aDetVent.tamañoDetalleVenta())
        self.tblDetalleVenta.setColumnCount(5)
        self.tblDetalleVenta.verticalHeader().setVisible(False)
        for i in range(0, aDetVent.tamañoDetalleVenta()):
            self.tblDetalleVenta.setItem(i, 0, QtWidgets.QTableWidgetItem(aDetVent.devolverDetalleVenta(i).getNDocumentoVenta()))
            self.tblDetalleVenta.setItem(i, 1, QtWidgets.QTableWidgetItem(str(aDetVent.devolverDetalleVenta(i).getNItem())))
            self.tblDetalleVenta.setItem(i, 2, QtWidgets.QTableWidgetItem(aDetVent.devolverDetalleVenta(i).getCodigoProducto()))
            self.tblDetalleVenta.setItem(i, 3, QtWidgets.QTableWidgetItem(str(aDetVent.devolverDetalleVenta(i).getPrecioVenta())))
            self.tblDetalleVenta.setItem(i, 4, QtWidgets.QTableWidgetItem(str(aDetVent.devolverDetalleVenta(i).getCantidad())))
