from openpyxl import Workbook, load_workbook
from openpyxl.styles.alignment import Alignment

wb = load_workbook('Customers.xlsx')

ws = wb.active

ws.append(['JM Catamora', 'Dapdap', '09706228870', 'jmcatamora07@gmail.com', '06/22/22', '2 days', '999'])

for x in range(1, 101):
    for y in range(1, 101):
        ws.cell(row=x, column=y).alignment = Alignment(horizontal='center', vertical='center') #center cells value (horizontally and vertically)

for x in range(2, 5):
    for y in range(1, 8):
        cell = ws.cell(row=x, column=y).value
        print(cell)
wb.save('Customers.xlsx')