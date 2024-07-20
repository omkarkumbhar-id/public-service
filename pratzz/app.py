import openpyxl

workbook_location = 'input/tryout-openpyxl.xlsx'
# Open the Excel file
workbook = openpyxl.load_workbook(workbook_location)

# Select the active sheet
sheet = workbook.active

# Read data from a specific cell
value = sheet['A1'].value
print(f"Value in cell A1: {value}")

# Write data to a specific cell
sheet['A1'] = "Hello, World!"

# Save the changes
workbook.save(workbook_location)