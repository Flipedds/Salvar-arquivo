from fpdf import FPDF
try:
	pdf = FPDF()    
	pdf.add_page() 
   
	pdf.set_font("Arial", size = 15) 
	f = open("codigo.txt", "r") 
	for x in f: 
		pdf.cell(200, 10, txt = x, ln = 1, align = 'x') 
	pdf.output("otimizacao.pdf")    
except:
	print("não foi possível")

'''
	result =
	
	salvar_arquivo = input("qual nome deseja dar ao arquivo:\n")
	salvar_arquivo += ".pdf"
	arquivo = open(salvar_arquivo,'w')
	arquivo.write(result) 
	arquivo.close()
  '''