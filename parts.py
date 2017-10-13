import sys
from tabulate import tabulate


with open('partslist.txt', 'r') as f:
    contents = [line.strip() for line in f.readlines()]

realcontents = {}
current_key = ''
for line in contents:
    if line.endswith(':'):
      current_key = line[0:-1]
    else:
        if not current_key in realcontents:
            realcontents[current_key] = []
        if line:
            realcontents[current_key].append(line.split(' x '))


def get_parts(object):
    if type(object) == list:
        num = int(object[0])
        test = object[1]
    else:
        num = 1
        test = object
    if not test in realcontents:
        return object
    out = []
    for part in realcontents[test]:
        for i in range(num):
            gp = get_parts(part)
            if type(gp[0]) == list:
                out.extend(gp)
            else:
                out.append(gp)
    return out


def simp(plist):
    out = {}
    for i in plist:
        num = int(i[0])
        name = i[1]
        if not name in out:
            out[name] = num
        else:
            out[name] += num
    return out



if __name__ == "__main__":
    try:
        GET = sys.argv[1]
    except IndexError:
        GET = 'Adder-Subtractor'
    
    table = []
    if not GET in realcontents:
        table.append( (1, GET) )
    else:
        plist = simp(get_parts(GET))
        for i in plist.items():
            table.append( (i[1], i[0]) )
    
    print(tabulate(table, headers=["Num", "Part"]))
