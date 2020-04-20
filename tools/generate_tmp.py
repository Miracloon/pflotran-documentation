import sys

min_args = 3
if len(sys.argv) <= min_args:
    sys.exit('Number of arguments must be greater than {}.'.format(min_args))

supported_modes = ['RICHARDS','TH','GENERAL','MPHASE','HYDRATE','WIPP_FLOW',
                   'RT','NWT']

filenames = sys.argv
mode = sys.argv[1]
if not mode in supported_modes:
    sys.exit('{} is not a supported mode in generate_tmp.py.'.format(mode))
outfilename = sys.argv[2]
filenames.pop(0) # remove the name of the script
filenames.pop(0) # remove mode
filenames.pop(0) # remove outfilename

print('Generating {}'.format(outfilename.split('/')[-1]))
     
dictionary = {}
for filename in filenames:
    f = open(filename,'r')
    list_ = []
    strings = []
    for line in f:
#        print(line)
        if line.startswith('#'):
            continue
        if len(line.rstrip()) > 0 and not line.startswith(' '):
            if list_ and not skip:
                list_.append(strings)
#                print(list_)
                if list_[0] in dictionary:
                    sys.exit('Key {} already exists in Python dictionary. '.
                             format(list_[0])+
                             'Currently constructing {}.'.format(outfilename))
                dictionary[list_[0]] = list_
            list_ = []
            strings = []
            skip = False
        if not list_ and len(line.strip()) > 0:
            w = line.split()
            list_.append(w[0].upper())
            list_.append(line.strip())
        elif line.strip().startswith('@'):
            skip = True
            applicable_modes = line.strip().strip('@').split()
            for local_mode in applicable_modes:
                if not local_mode in supported_modes:
                    sys.exit('Local mode {} is not a '.format(local_mode)+
                             'supportd mode in generate_tmp.py.')
                if local_mode == mode:
                    skip = False
                    break
        else:
            strings.append(line.strip())
    if len(strings) > 0:
        if list_ and not skip:
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
