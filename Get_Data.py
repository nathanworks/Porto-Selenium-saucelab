import openpyxl

workbook = openpyxl.load_workbook('saucelab.xlsx')
sheet = workbook.active

items = [cell.value for cell in sheet['A'] if cell.value]