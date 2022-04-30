from openpyxl import load_workbook

book = load_workbook(filename="./files/shedule.xlsx")
sheet = book["Shedule"]

result = ''
for i in range(1, 27):
	cell = sheet['A' + str(i)].value
	if ";" in cell:
		cell = cell[0:cell.find(";") + 1] + '\n' + '   ' + cell[cell.find(";") + 2:]
	result += cell + '\n'
