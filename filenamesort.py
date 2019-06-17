import os

path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'11\\')
print(path)

file_version_map ={}

for onefile in os.listdir(path):
    if os.path.isfile(os.path.join(path,onefile)):
        version = onefile.split('_')[1:6]
        aa = []
        for i in version:
            aa.append(int(i))

        file_version_map[tuple(aa)] = onefile

data =sorted(file_version_map.items(),key=lambda x:x[0])
#print(data)

with open('Plugin-Filter.txt','w') as f:
    for version,name in data:
        print(name,type(name))
        if name.startswith('Plugin-Filter'):
                f.write(name +  '\n')





