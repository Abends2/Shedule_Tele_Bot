from openpyxl import load_workbook

#from bot import data

book = load_workbook(filename="../files/shedule.xlsx")
sheet = book["Shedule"]

#if data:
result = ''
for i in range(1, 32):
	cell = sheet['B' + str(i)].value
	if ";" in cell:
		cell = cell[0:cell.find(";") + 1] + '\n' + '   ' + cell[cell.find(";") + 2:]
	result += cell + '\n'
#else:
	#print("Err")