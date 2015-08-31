from lxml import html,etree

tree = html.parse(file('D&D_5e.html','r'))
root = tree.getroot()

for child in root:
    print child.tag
    for cc in child:
        print '   ',cc.tag,'|',cc.label

file('out.html','w').writelines(etree.tostring(root,pretty_print=True))
