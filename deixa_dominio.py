#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Script para deixar so o dominio das urls em um arquivo
#tenho que passar por parametro o path+arquivo
#ou posso importar para outro arquivo usando :
#{from remove_espaco_arquivo import FileCheck} e chamando a funcao FileCheck("{path+arquivo}")

#                            _                        __                             _         __ _ _           _           
#       /\  /\___ _ __  _ __(_) __ _ _   _  ___    /\ \ \_   _ _ __   ___  ___    __| | __ _  / _(_) |_   _____(_)_ __ __ _ 
#      / /_/ / _ \ '_ \| '__| |/ _` | | | |/ _ \  /  \/ / | | | '_ \ / _ \/ __|  / _` |/ _` | \ \| | \ \ / / _ \ | '__/ _` |
#     / __  /  __/ | | | |  | | (_| | |_| |  __/ / /\  /| |_| | | | |  __/\__ \ | (_| | (_| | _\ \ | |\ V /  __/ | | | (_| |
#     \/ /_/ \___|_| |_|_|  |_|\__, |\__,_|\___| \_\ \/  \__,_|_| |_|\___||___/  \__,_|\__,_| \__/_|_| \_/ \___|_|_|  \__,_|
#                                |_|                                                                                       
#

import sys
from tldextract import extract

def LeaveDomain(file):
	try:
		ref_arquivo = open(file,"r")
		
		for line in ref_arquivo:
			xx = str(line)
			tsd, td, tsu = extract(xx) # prints abc, hostname, com
			url = td + '.' + tsu # will prints as hostname.com
			print(url)
	except IOError:
		print("Arquivo para remoção de espaços em branco não encontardo: " +file , sys.exc_info()[0])
		
if __name__ == "__main__":
	LeaveDomain(sys.argv[1])