#!/usr/bin/python
# encoding: utf-8
# filename: artigoAceito.py
#
#  scriptLattes V8
#  Copyright 2005-2013: Jesús P. Mena-Chalco e Roberto M. Cesar-Jr.
#  http://scriptlattes.sourceforge.net/
#
#
#  Este programa é um software livre; você pode redistribui-lo e/ou 
#  modifica-lo dentro dos termos da Licença Pública Geral GNU como 
#  publicada pela Fundação do Software Livre (FSF); na versão 2 da 
#  Licença, ou (na sua opinião) qualquer versão.
#
#  Este programa é distribuído na esperança que possa ser util, 
#  mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
#  MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#  Licença Pública Geral GNU para maiores detalhes.
#
#  Você deve ter recebido uma cópia da Licença Pública Geral GNU
#  junto com este programa, se não, escreva para a Fundação do Software
#  Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

from producaoBibliografica import *
#from scriptLattes import *

class ArtigoAceito(ProducaoBibliografica):
	
	revista = None
	numero = None

	def __init__(self, idMembro, tipo, partesDoItem='', doi=''):
		ProducaoBibliografica.__init__(self, tipo, idMembro)
		if not partesDoItem=='': 
			# partesDoItem[0]: Numero (NAO USADO)
			# partesDoItem[1]: Descricao do artigo (DADO BRUTO)
			self.item = partesDoItem[1]
			self.doi = doi
			
			# Dividir o item na suas partes constituintes (autores e o resto)
			partes = self.item.partition(" . ")

			# Verificar quando há um numero de autores > que 25
			if partes[1]=='': # muitos autores (mais de 25) e o lattes insere etal. termina lista com ;
				partes = self.item.partition(" ; ")
				a = partes[0].partition(", et al.") # remocao do et al.
				a = a[0] + a[2] # estes autores nao estao bem separados pois falta ';'
				b = a.replace(', ','*') 
				c = b.replace(' ',' ; ')
				self.autores = c.replace('*',', ')
			else:
				self.autores = partes[0].strip()
			
			#Processando o resto (tudo menos autores)
			partes = partes[2].rpartition(", ")

			#print 'PARTES:', partes
			self.ano = partes[2].strip().rstrip(".")

			partes = partes[0].rpartition("p. ")
			if partes[1]=='': 			#Se nao existe paginas
				self.paginas = ''
				partes = partes[2]
			else:
				self.paginas = partes[2].strip()
				partes = partes[0]

			partes = partes.rpartition(", n. ")
			if partes[1]=='': # se nao existe numero
				self.numero = ''
				partes = partes[2]
			else:
				self.numero = partes[2].strip().rstrip(",")
				partes = partes[0]

			partes = partes.rpartition(", v. ")
			if partes[1]=='': # se nao existe volume
				self.volume = ''
				partes = partes[2]
			else:
				self.volume = partes[2].strip().rstrip(",")
				partes = partes[0]

			#print 'Partes', partes
			partes = partes.rpartition(". ")
			self.titulo = partes[0].strip()
			self.revista = partes[2].strip()
			if self.volume == None:
				 self.volume = ''
			
		else:
			self.doi = ''
			self.autores = ''
			self.titulo = ''
			self.revista = ''
			self.paginas = ''
			self.volume = ''
			self.numero = ''
			self.ano = ''

		#print 'AQUI', self.ano
	# ------------------------------------------------------------------------ #
	def __str__(self):
		s  = "\n[ARTIGO ACEITO PARA PUBLICACAO] \n"
		s += "+ID-MEMBRO   : " + str(self.idMembro) + "\n"
		s += "+RELEVANTE   : " + str(self.relevante) + "\n"
		s += "+DOI         : " + self.doi.encode('utf8','replace') + "\n"
		s += "+AUTORES     : " + self.autores.encode('utf8','replace') + "\n"
		s += "+TITULO      : " + self.titulo.encode('utf8','replace') + "\n"
		s += "+REVISTA     : " + self.revista.encode('utf8','replace') + "\n"
		s += "+PAGINAS     : " + self.paginas.encode('utf8','replace') + "\n"
		s += "+VOLUME      : " + self.volume.encode('utf8','replace') + "\n"
		s += "+NUMERO      : " + self.numero.encode('utf8','replace') + "\n"
		s += "+ANO         : " + str(self.ano) + "\n"
		s += "+item        : " + self.item.encode('utf8','replace') + "\n"
		return s
