import sys
from PyQt5 import uic, QtWidgets
from arregloClientes import *


aCli = ArregloClientes()

qtCreatorFile = "ventanaClientes.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class RegistroClientes(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.listar()
        self.show()
        self.btnModificar.setEnabled(False)
        self.btnGrabar.setEnabled(False)
        self.btnSalir.clicked.connect(self.cerrar)

    #Metodos
    def obtenerDni(self):
        return self.txtDni.text()
    
    def obtenerNombres(self):
        return self.txtNombres.text()
    
    def obtenerApellidoPaterno(self):
        return self.txtApellidoPaterno.text()
    
    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()
    
    def obtenerDireccion(self):
        return self.txtDireccion.text()
    
    def obtenerTelefono(self):
        return self.txtTelefono.text()


    def limpiarTabla(self):
    	self.tblClientes.clearContents()
    	self.tblClientes.setRowCount(0)

    def valida(self):
    	if self.txtDni.text()=="":
    		self.txtDni.setFocus()
    		return "DNI del Cliente...!!!"
    	elif self.txtNombres.text()=="":
    		self.txtNombres.setFocus()
    		return "Nombre del Cliente...!!!"
    	elif self.txtApellidoPaterno.text()=="":
    		self.txtApellidoPaterno.setFocus()
    		return "Apellido Paterno...!!!"
    	elif self.txtApellidoMaterno.text()=="":
    		self.txtApellidoMaterno.setFocus()
    		return "Apellido Materno...!!!"
    	elif self.txtDireccion.text()=="":
    		self.txtDireccion.setFocus()
    		return "Direccion...!!!"
    	elif self.txtTelefono.text()=="":
    		self.txtTelefono.setFocus()
    		return "Telefono...!!!"
    	else:
    		return ""
    
    #Metodo para listar
    def listar(self):

    	self.tblClientes.setRowCount(aCli.tamañoArregloCliente())
    	self.tblClientes.setColumnCount(6)
    	self.tblClientes.verticalHeader().setVisible(False)

    	for i in range(0,aCli.tamañoArregloCliente()):
    		self.tblClientes.setItem(i,0,QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDniCliente()))
    		self.tblClientes.setItem(i,1,QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getNombresCliente()))
    		self.tblClientes.setItem(i,2,QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidoPaternoCliente()))
    		self.tblClientes.setItem(i,3,QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidoMaternoCliente()))
    		self.tblClientes.setItem(i,4,QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDireccionCliente()))
    		self.tblClientes.setItem(i,5,QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getTelefonoCliente()))

    #Metodo para limpiar cajas
    def limpiarControles(self):
    	self.txtDni.clear()
    	self.txtNombres.clear()
    	self.txtApellidoPaterno.clear()
    	self.txtApellidoMaterno.clear()
    	self.txtDireccion.clear()
    	self.txtTelefono.clear()



    #Metodo Registrar cliente
    def registrar(self):

    	if self.valida() == "":
    		objCli = Cliente(self.obtenerDni(),self.obtenerNombres(),self.obtenerApellidoPaterno(),self.obtenerApellidoMaterno(),self.obtenerDireccion(),self.obtenerTelefono())
    		dni = self.obtenerDni()
    		if aCli.buscarCliente(dni) == -1:
    			aCli.adicionaCliente(objCli)
    			self.limpiarControles()
    			self.listar()
    			self.btnModificar.setEnabled(True)
                
    		else:
    			QtWidgets.QMessageBox.information(self, "Registrar Cliente", "El DNI ingesado ya existe...!!!", QtWidgets.QMessageBox.Ok)

    	else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Error en " +self.valida(), QtWidgets.QMessageBox.Ok)

    #Meotodo para consultar
    def consultar(self):
    	self.limpiarTabla()
    	if aCli.tamañoArregloCliente()==0:
    		QtWidgets.QMessageBox.information(self, "Consultar Cliente", "No existen clientes a consultar...!!!",QtWidgets.QMessageBox.Ok)
    	else:
    		dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Cliente", "Ingrese el DNI a consultar")
    		pos = aCli.buscarCliente(dni)
    		if pos == -1:
    			QtWidgets.QMessageBox.information(self, "Consultar Cliente", "El DNI ingresado no existe...!!! ",QtWidgets.QMessageBox.Ok)
    		else:
    			self.tblClientes.setRowCount(1)
    			self.tblClientes.setItem(0,0,QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getDniCliente()))
	    		self.tblClientes.setItem(0,1,QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getNombresCliente()))
	    		self.tblClientes.setItem(0,2,QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getApellidoPaternoCliente()))
	    		self.tblClientes.setItem(0,3,QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getApellidoMaternoCliente()))
	    		self.tblClientes.setItem(0,4,QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getDireccionCliente()))
	    		self.tblClientes.setItem(0,5,QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getTelefonoCliente()))

	#Metodo para eliminar
    def eliminar(self):
        if aCli.tamañoArregloCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "No existen clientes a eliminar...!!!",QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblClientes.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                dni = self.tblClientes.item(indiceFila, 0).text()
                pos = aCli.buscarCliente(dni)
                aCli.eliminarCliente(pos)
                self.limpiarTabla()
                self.listar()
                


            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "Debe seleccionar una fila...!!!",QtWidgets.QMessageBox.Ok)
	
    
    def modificar(self):
        if aCli.tamañoArregloCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Cliente", "No existen clientes a modificar...!!!",QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Modificar Cliente", "Ingrese el DNI a modificar")
            pos = aCli.buscarCliente(dni)
            if pos != -1:
                objCliente = aCli.devolverCliente(pos)
                self.btnModificar.setEnabled(False)
                self.btnGrabar.setEnabled(True)
                self.txtDni.setText(objCliente.getDniCliente())
                self.txtDni.setEnabled(False)                   
                self.txtNombres.setText(objCliente.getNombresCliente())
                self.txtApellidoPaterno.setText(objCliente.getApellidoPaternoCliente())
                self.txtApellidoMaterno.setText(objCliente.getApellidoMaternoCliente())
                self.txtDireccion.setText(objCliente.getDireccionCliente())
                self.txtTelefono.setText(objCliente.getTelefonoCliente())




    #Metodo para grabar cliente
    def grabar(self):
    	
    	try:
    		pos = aCli.buscarCliente(self.obtenerDni())
    		objCliente = aCli.devolverCliente(pos)
    		objCliente.setNombresCliente(self.obtenerNombres())
    		objCliente.setApellidoPaternoCliente(self.obtenerApellidoPaterno())
    		objCliente.setApellidoMaternoCliente(self.obtenerApellidoMaterno())
    		objCliente.setDireccionCliente(self.obtenerDireccion())
    		objCliente.setTelefonoCliente(self.obtenerTelefono())
    		self.btnModificar.setEnabled(True)
    		self.btnGrabar.setEnabled(False)
    		self.limpiarTabla()
    		self.limpiarControles()
    		self.listar()
    		self.txtDni.setEnabled(True)
    		self.lblDni.setVisible(True)

    	except:
    		QtWidgets.QMessageBox.information(self, "Modificar Cliente", "Modificado correctamente...!!!",QtWidgets.QMessageBox.Ok)

    def cerrar(self):
        self.close()


    
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = RegistroClientes()
    window.show()
    sys.exit(app.exec_())