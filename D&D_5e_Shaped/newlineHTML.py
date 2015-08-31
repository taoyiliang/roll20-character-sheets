infile = file('D&D_5e.html','r')

msg=''
for l,line in enumerate(infile):
    line = line.replace('>','>\n')
    line = line.replace('\n\n','\n')
    msg+=line

file('auto.html','w').writelines(msg)

