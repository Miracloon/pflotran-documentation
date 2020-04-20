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
expert_dictionary = {}
for filename in filenames:
    f = open(filename,'r')
    list_ = []
    strings = []
    skip = False
    expert = False
    for line in f:
        if line.startswith('#'):
            continue
        if len(line.rstrip()) > 0 and not line.startswith(' '):
            if list_ and not skip:
                keyword = list_[0]
                list_.append(strings)
                if keyword in dictionary or keyword in expert_dictionary:
                    sys.exit('Key {} already exists in Python dictionary. '.
                             format(keyword)+
                             'Currently constructing {}.'.format(outfilename))
                if expert:
                    expert_dictionary[keyword] = list_
                else:
                    dictionary[keyword] = list_
            list_ = []
            strings = []
            skip = False
            expert = False
        if not list_ and len(line.strip()) > 0:
            w = line.split()
            list_.append(w[0].upper())
            list_.append(line.strip())
        elif line.strip().startswith('@'):
            skip = True
            w = line.strip().lstrip('@').split()
            keyword = w[0].strip()
            w = w[1:]
            if keyword.strip().startswith('MODES'):
                applicable_modes = w
                for local_mode in applicable_modes:
                    if not local_mode in supported_modes:
                        sys.exit('Local mode {} is '.format(local_mode)+
                                 'not a supportd mode in generate_tmp.py.')
                    if local_mode == mode:
                        skip = False
                        break
            elif keyword.startswith('EXPERT'):
                expert = True
        else:
            strings.append(line.strip())
    if len(strings) > 0:
        if list_ and not skip:
            list_.append(strings)
            keyword = list_[0]
            if keyword in dictionary or keyword in expert_dictionary:
                sys.exit('Key {} already exists in Python dictionary. '.
                         format(keyword)+
                         'Currently constructing {}.'.format(outfilename))
            if expert:
                expert_dictionary[keyword] = list_
            else:
                dictionary[keyword] = list_
    f.close()
    
f = open(outfilename,'w')
for entry in sorted(dictionary):
    f.write('{}\n'.format(dictionary[entry][1].strip()))
    strings = dictionary[entry][2]
    for string in strings:
      f.write(' {}\n'.format(string.strip()))
if len(expert_dictionary) > 0:
    f.write('\n**Expert Settings**\n')
for entry in sorted(expert_dictionary):
    f.write('{}\n'.format(expert_dictionary[entry][1].strip()))
    strings = expert_dictionary[entry][2]
    for string in strings:
      f.write(' {}\n'.format(string.strip()))
f.close()
