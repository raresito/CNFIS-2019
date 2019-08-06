import re

with open('cnfis-raw-data.txt', 'r') as file:
    data = file.read()

# print(data)
new_list = re.compile(" U[0-9][0-9]").split(data)
new_list[0] = new_list[0][3:]

testUni = new_list[0]

oneUniList = testUni.split(" ")
print(oneUniList)
finalDictionary = []
index = 0
for oneUniList in new_list:
    oneUniList = oneUniList.split(" ")
    name = ''
    id = 'U'
    j = ''
    if index > 15:
        j = index + 2
    else:
        j = index + 1
    if j > 9:
        id = 'U' + str(j)
    else:
        id = 'U0' + str(j)
    model_uni = {
        'id': id,
        'id_num': j,
        'total_students': int(oneUniList[len(oneUniList) - 12].replace('.', '')),
        'buget_students': int(oneUniList[len(oneUniList) - 11].replace('.', '')),
        'tax_students': int(oneUniList[len(oneUniList) - 10].replace('.', '')),
        'total_licenta_students': int(oneUniList[len(oneUniList) - 9].replace('.', '')),
        'buget_licenta_students': int(oneUniList[len(oneUniList) - 8].replace('.', '')),
        'tax_licenta_students': int(oneUniList[len(oneUniList) - 7].replace('.', '')),
        'total_masterat_students': int(oneUniList[len(oneUniList) - 6].replace('.', '')),
        'buget_masterat_students': int(oneUniList[len(oneUniList) - 5].replace('.', '')),
        'tax_masterat_students': int(oneUniList[len(oneUniList) - 4].replace('.', '')),
        'total_doctorat_students': int(oneUniList[len(oneUniList) - 3].replace('.', '')),
        'buget_doctorat_students': int(oneUniList[len(oneUniList) - 2].replace('.', '')),
        'tax_doctorat_students': int(oneUniList[len(oneUniList) - 1].replace('.', ''))
    }
    i = 13
    while i < len(oneUniList):
        name = oneUniList[len(oneUniList) - i] + ' ' + name
        i = i + 1
    model_uni['name'] = name
    finalDictionary.append(model_uni)
    index = index + 1

print(finalDictionary)
