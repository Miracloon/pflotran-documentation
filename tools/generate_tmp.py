import sys

if len(sys.argv) < 3:
    sys.exit("Number of arguments must be greater than 1.")

filenames = sys.argv
outfilename = sys.argv[1]
filenames.pop(0) # remove the name of the script
filenames.pop(0) # remove outfilename

print('Generating {}'.format(outfilename.split('/')[-1]))
     
dictionary = {}
for filename in filenames:
    f = open(filename,'r')
    list_ = []
    strings = []
    for line in f:
#        print(line)
        if len(line.rstrip()) > 0 and not line.startswith(' '):
            if list_:
                list_.append(strings)
#                print(list_)
                if list_[0] in dictionary:
                    sys.exit('Key {} already exists in Python dictionary. '.
                             format(list_[0])+
                             'Currently constructing {}.'.format(outfilename))
                dictionary[list_[0]] = list_
            list_ = []
            strings = []
        if not list_ and len(line.strip()) > 0:
            w = line.split()
            list_.append(w[0].upper())
            list_.append(line.strip())
        else:
            strings.append(line.strip())
    if len(strings) > 0:
        if list_:
            list_.append(strings)
            dictionary[list_[0]] = list_
    f.close()
    
f = open(outfilename,'w')
for entry in sorted(dictionary):
#    print(entry)
    f.write('{}\n'.format(dictionary[entry][1].strip()))
    strings = dictionary[entry][2]
    for string in strings:
      f.write(' {}\n'.format(string.strip()))
f.close()
