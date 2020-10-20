#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Script para tirar espacos vazios de um arquivo
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

def FileCheck(file):
	try:
		# first get all lines from file
		with open(file, 'r') as f:
			lines = f.readlines()
		
		# remove spaces
		lines = [line.replace(' ', '') for line in lines]
		
		# finally, write lines in the file
		with open(file, 'w') as f:
			f.writelines(lines)
	except IOError:
		print("Arquivo para remoção de espaços em branco não encontardo: " +file , sys.exc_info()[0])

if __name__ == "__main__":
	FileCheck(sys.argv[1])