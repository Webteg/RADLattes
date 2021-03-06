from atuacaoProfissional import *
class VinculoFuncional(AtuacaoProfissional):
	cargaHoraria = ''
	regime	= ''
	tipoVinculo = ''
	enquadramento = ''
	listaAtividades = None		#As atividades relacionadas a um vinculo funcional
	listaInformacoes = None		#As informacoes associadas ao vinculo

	#Flag's de apoio
	achouDescricao = 0	
	
	listaCampos = None
	def __init__(self, partesDoItem):
		#partesDoItem[0] = periodo da atuacao
		#partesDoItem[1] = descricao
		try:	
			self.periodo = partesDoItem.pop(0)
			if len(partesDoItem) > 0:
				partesDoVinculo = partesDoItem.pop()
				self.achouDescricao = 1
		except:
			raise IndexError("LISTA VAZIA - VINCULO SEM DESCRICAO.")
			pass 

		self.listaCampos = []
		if self.achouDescricao:
			partesDoVinculo = partesDoVinculo.split(',')
			#print 'Partes do vinculo ',partesDoVinculo
			for item in partesDoVinculo:
				self.listaCampos.append(item.split(':'))
			for campo in self.listaCampos:	
				if len(campo) > 1:
					nome, descricao = campo
				#else:
					#descricao = campo
				if u'nculo' in nome:
					self.tipoVinculo = descricao.strip()
				if 'Enquadramento' in nome:
					self.enquadramento = descricao.strip()
				if 'Carga' in nome:
					self.cargaHoraria = descricao.strip()
				if 'Regime' in nome:
					self.regime = descricao.strip()
	
				self.listaAtividades  = []
				self.listaInformacoes = []

	def add(self, atuacaoProfissional):
		try:
			self.listaAtividade.append(atuacaoProfissonal)
		except:
			print 'ERRO AO INSERIR ATUACAO PROFISSIONAL'
			pass	

	def __str__(self):
        	s  = "\n[ATUACAO PROFISSIONAL - VINCULO FUNCIONAL] \n"
        	s += "+ PERIODO  : " + str(self.descricao) + "\n"
        	s += "+ ATIVIDADE: " + str(self.nivel) + "\n"
		s += "+ PERIODO  : " + str(self.descricao) + "\n"
        	s += "+ ATIVIDADE: " + str(self.nivel) + "\n"
        	return s

	def showData(self):
		s  = "\n[ATUACAO PROFISSIONAL - VINCULO FUNCIONAL]\n"
        	s += "+ PERIODO      : " + str(self.periodo.encode('utf8', 'replace')) + "\n"
        	s += "+ VINCULO      : " + str(self.tipoVinculo.encode('utf8', 'replace')) + "\n"
		s += "+ ENQUADRAMENTO: " + str(self.enquadramento.encode('utf8', 'replace')) + "\n"
        	s += "+ CARGA HORARIA: " + str(self.cargaHoraria.encode('utf8', 'replace')) + "\n"
		s += "+ REGIME       : " + str(self.regime.encode('utf8', 'replace')) + "\n"
		return s
		
