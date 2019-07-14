import operator

print("start")

names = {}
filepath = r'/home/mooli/Documents/WhatsApp/WhatsApp Chat with צוות יצורים.txt'
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1

    while line:
        toc = line.split(',')
        try:
            if(toc[0].count('/') == 2):
                name = (line.split(':')[1]).split('-')[1]
                names[name] = names.get(name, 0) + 1
        except:
            print(line)
        line = fp.readline()
        cnt += 1

sorted_name = sorted(names.items(), key=operator.itemgetter(1))

print(sorted_name)
