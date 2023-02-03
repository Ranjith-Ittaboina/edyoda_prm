dic = {1: ['apple', 'orange', 'banana', 'cherry'], 2 : ['tsc', 'wipro', 'infosys', 'techm'], 3 : ['father', 'mother', 'brother', 'sister']}
# print(dic)
# print(dic.values())
for i in dic.values():
    sorted_dic = sorted(i, key = lambda x: x[-2])
    print(sorted_dic)