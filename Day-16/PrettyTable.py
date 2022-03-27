from prettytable import PrettyTable

table = PrettyTable()   # Class: PrettyTable, Object: table
table.add_column("Students Name", ["Ayush", "Drashti", "Anand", "Keval"])
table.add_column("Last Name", ["Prajapati", "Kansare", "Suthar", "Shah"])       # Method: add_column
print(table)

print(table.align)  # Attribute: align

table.align = "l"
print(table)