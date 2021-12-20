import sys
from PyQt5 import uic, QtWidgets
from Menu_principal import *
from conexion1 import *
from arregloProductos import *
from arregloClientes import *
from ventanaClientes import *

qtCreatorFile = "Login.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Login(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnEntrar.clicked.connect(self.iniciar_sesion)
        self.datos=Registro_datos()
        self.btnMClientes.clicked.connect(self.Abrir_MClientes)


    def iniciar_sesion(self):
        self.lblU_incorrecto.setText('')
        self.lblC_incorrecto.setText('')
        u_entrar=self.txtUsuario.text()
        c_entrar=self.txtContra.text()

        u_entrar=str("'"+u_entrar+"'")
        c_entrar=str("'"+c_entrar+"'")

        dato1=self.datos.busca_users(u_entrar)
        dato2=self.datos.busca_password(c_entrar)

        if dato1 == [] and dato2 ==[]:
            self.lblU_incorrecto.setText('Usuario incorrecto')
            self.lblC_incorrecto.setText('Contraseña incorrecta')
        else:
            if dato1==[]:
                self.lblU_incorrecto.setText('Usuario incorrecto')
            else:
                dato1=dato1[0][1]
            if dato2==[]:
                self.lblC_incorrecto.setText('Contraseña incorrecta')
            else:
                dato2=dato2[0][2]
            if dato1 !=[] and dato2 !=[]:
                self.hide()
                self.ventana2=MenuPrincipal()
                self.ventana2.show()
                
    def Abrir_MClientes(self):
        self.ventanaMC=RegistroClientes()
        self.ventanaMC.show()

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())
