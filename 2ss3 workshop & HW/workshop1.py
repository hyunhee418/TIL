blood_type = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
count_a = 0
count_b = 0
count_o = 0
count_ab = 0
dict_blood = {}


for i in blood_type:
    if i == list(set(blood_type))[0]:
        count_a += 1
        dict_blood[i] = count_a
    elif i == list(set(blood_type))[1]:
        count_b += 1
        dict_blood[i] = count_b
    elif i == list(set(blood_type))[2]:
        count_o += 1
        dict_blood[i] = count_o
    else:
        count_ab += 1
        dict_blood[i] = count_ab

print(dict_blood)

student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
sum = 0
n = len(list(student.keys()))
stu_values = list(student.values())
for i in stu_values:
    sum = sum + i

print(sum / n)




student = {'python': 80, 'algorithm':99, 'django': 89, 'flask': 83}
sum(student.values()) / len(student)

