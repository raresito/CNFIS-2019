import re

with open('cnfis-raw-data.txt', 'r') as file:
    data = file.read()

# print(data)
new_list = re.compile(" U[0-9][0-9]").split(data)
new_list[0] = new_list[0][3:]

# for i in range(0, len(new_list)):
#     if i > 15:
#         j = i + 2
#     else:
#         j = i + 1
#     print(j, new_list[i])

testUni = new_list[0]

oneUniList = testUni.split(" ")
print(oneUniList)
finalDictionary = []
for oneUniList in new_list:
    oneUniList = oneUniList.split(" ");
    name = '';
    model_uni = {}
    model_uni['total_students'] = float(oneUniList[len(oneUniList) - 12])
    model_uni['buget_students'] = float(oneUniList[len(oneUniList) - 11])
    model_uni['tax_students'] = float(oneUniList[len(oneUniList) - 10])
    model_uni['total_licenta_students'] = float(oneUniList[len(oneUniList) - 9])
    model_uni['buget_licenta_students'] = float(oneUniList[len(oneUniList) - 8])
    model_uni['tax_licenta_students'] = float(oneUniList[len(oneUniList) - 7])
    model_uni['total_masterat_students'] = float(oneUniList[len(oneUniList) - 6])
    model_uni['buget_masterat_students'] = float(oneUniList[len(oneUniList) - 5])
    model_uni['tax_masterat_students'] = float(oneUniList[len(oneUniList) - 4])
    model_uni['total_doctorat_students'] = float(oneUniList[len(oneUniList) - 3])
    model_uni['buget_doctorat_students'] = float(oneUniList[len(oneUniList) - 2])
    model_uni['tax_doctorat_students'] = float(oneUniList[len(oneUniList) - 1])
    i = 13
    while i < len(oneUniList):
        name = oneUniList[len(oneUniList) - i] + ' ' + name;
        i = i + 1
    model_uni['name'] = name
    finalDictionary.append(model_uni);

print(finalDictionary);