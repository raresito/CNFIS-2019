import re

with open('cnfis-raw-data.txt', 'r') as file:
    data = file.read()

# print(data)
new_list = re.compile(" U[0-9][0-9]").split(data)
new_list[0] = new_list[0][3:]

# for i in range (0, len(new_list)):
    # if i > 15:
    #     j = i + 2
    # else: 
    #     j = i + 1
    # print(j, new_list[i])
testUni = new_list[0]

oneUniList = testUni.split(" ")
print(oneUniList)
for stri in oneUniList:
    model_uni = {
        'name': '',
        'total_students': 0,
        'buget_students': 0,
        'tax_students': 0,
        'total_licenta_students': 0,
        'buget_licenta_students': 0,
        'tax_licenta_students': 0,
        'total_masterat_students': 0,
        'buget_masterat_students': 0,
        'tax_masterat_students': 0,
        'total_doctorat_students': 0,
        'buget_doctorat_students': 0,
        'tax_doctorat_students': 0,
    }
    try:
        float(stri)
        print(stri, True)
    except ValueError:
        print(stri, False)