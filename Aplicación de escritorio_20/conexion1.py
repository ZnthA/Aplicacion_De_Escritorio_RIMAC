import pyodbc

class Registro_datos():
	def __init__(self):
		self.conexion=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-UINKAGU;DATABASE=RIMAC;UID=sa;PWD=123')
		
	def busca_users(self,Usuario):
		cursor=self.conexion.cursor()
		sql="SELECT * FROM RIMAC.DBO.usuarios WHERE Usuario={}".format(Usuario)
		cursor.execute(sql)
		usuariox=cursor.fetchall()
		cursor.close()
		return usuariox
	def busca_password(self,Contrasena):
		cursor=self.conexion.cursor()
		sql="SELECT * FROM RIMAC.DBO.usuarios WHERE Contrasena={}".format(Contrasena)
		cursor.execute(sql)
		contrasenax=cursor.fetchall()
		cursor.close()
		return contrasenax



	
		


	


