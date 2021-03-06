import psycopg2
import fileinput
import string

class Connection:
	parametros = None
	"""
	metodo open()
	recebe o nome do banco de dados e instancia o objeto de conexao
	@param name: nome do banco de dados
	"""
	@staticmethod
	def __open (arquivoConfigBanco):
		try:		
			parametros = {}
			string_conexao = ''

			for linha in fileinput.input(arquivoConfigBanco):
				linha = linha.replace("\r","")
				linha = linha.replace("\n","")
				#Divisao da linha
				p, v = linha.split("=",1)
				parametros[p.rstrip()] = v.lstrip()

			if 'pgsql' in parametros['type']:
				string_conexao = string.Template("""host=$host dbname=$name user=$user password=$pass""")		 
				return  psycopg2.connect(string_conexao.substitute(parametros))
		except:
			raise 

	def open(self, arquivoConfigBanco):
		self.__open(arquivoConfigBanco)
	#def close ():

	def status():
		if self.conexao == NULL:
			print 'O sistema nao esta conectado a %s em %s' % (self.banco, self.host)
			return
		else:
			print 'O sistema esta conectado a %s em %s' % (self.banco, self.host)
		
