def digimap(dig_map, digits, res):

    if len(digits)==0:
        return res
    
    if dig_map=={}:
        return "No mapping given"
    
    new_res = []
    d = digits[-1]

    if res==[]:
        for c in dig_map[d]:
            new_res.append(c)
    else:
        for r in res:
            for c in dig_map[d]:
                new_res.append(c+r)
    
    return digimap(dig_map, digits[:-1], new_res)

dig_map = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f']}
digits = "23"

print(digimap(dig_map, digits, []))

dig_map = {'1':['a','b','c'], '2':['a','c','d'], '3':['e','f','g']}
digits = "123"

print(digimap(dig_map, digits, []))

dig_map = {}

digits = "12"

print(digimap(dig_map, digits, []))