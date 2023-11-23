#Criando método para retirar os acentos das palavras dentro deste dataset:
def substituir_caracteres(columns):  
  columns = columns.replace('Á','A').replace('Â','A').replace('Ã','A').replace('À','A').replace('É','E').replace('Ê','E').replace('È','E').replace('Í','I').replace('Ì','I').replace('Î','I').replace('Ó','O').replace('Ò','O').replace('Õ','O').replace('Ô','O').replace('Ú','U').replace('Ù','U').replace('Û','U').replace('Ç','C').replace('á','a').replace('â','a').replace('ã','a').replace('à','a').replace('é','e').replace('ê','e').replace('è','e').replace('í','i').replace('ì','i').replace('î','i').replace('ó','o').replace('ò','o').replace('õ','o').replace('ô','o').replace('ú','u').replace('ù','u').replace('û','u').replace('ç','c').replace('-', ' ').replace('.','')
  return columns
