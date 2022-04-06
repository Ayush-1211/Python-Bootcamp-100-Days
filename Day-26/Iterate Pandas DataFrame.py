import pandas

student_dict = {
    "student": ["Ayush", "Drashti", "Anand"],
    "score": [90, 97, 96]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

print("--------------------------------------------")

for(index, row) in student_data_frame.iterrows():
    #print(index)
    #print(row)
    #print(row.student)
    if row.student == "Ayush":
        print(row.score)