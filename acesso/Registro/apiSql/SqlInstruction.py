"""
Classe SQLInstruction
Esta classe oferece os metodos em comum entre todas as instrucoes SQL:
	- SELECT
	- INSERT
	- UPDATE
	- DELETE
"""
#import criteria from Criteria

class SqlInstruction:
	sql 	 = ''	# Amazena a instrucao SQL
	criteria = ''	# Armazena o objeto criterio
	table 	 = '' 	# Armazena a tabela que sofre as operacoes

	""" 
	metodo setTable()
	Define o nome da tabela manipulada pela instrucao SQL
	@param table = tabela que sofre as operacoes
	"""
	def setTable(self, table):
		self.table = table
	""" 
	metodo getTable()
	Retorna o nome da tabela
	"""
	def getTable(self):
		return self.table
	""" 
	metodo setCriteria()
	Define um criterio de selecao para os dados usando composicao de um objeto 
	do tipo Criteria, que oferece uma interface para criar criterios	
	@param criteria = criterio de selecao dos dados (filtro)
	"""
	def setCriteria(self, criteria):
		self.criteria = criteria
	""" 
	metodo getInstruction()
	Seu comportamento sera distinto para cada subclasse (Polimorfismo).
	@abstractmethod
	"""
	def getInstruction (self):
		raise NotImplementedError('Acao deve ser definida na subclasse')
	
	"""
	metodo addSlashe()
	@param s: string com caracteres a serem escapados 
	"""	
	def addSlashes(self, s):
		if s is None:
			return
		'Adiciona os caracteres de escape'
		l = ["\\", '"', "'", "\0"]
		for i in l:
			if i in s: 
				s = s.replace(i, "'"+i)
				print s
		return s	
	
	


