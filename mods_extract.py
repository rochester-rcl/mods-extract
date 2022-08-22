import re
import os
import xml.dom.minidom

filehand = open('alma_export.xml', 'r', encoding='UTF-8')
mods = filehand.read()
mods = mods.replace('\t', '')
mods = mods.replace('\n', '')

mods_list = re.findall('<mods\sxmlns.*?mods>' , mods)

for record in mods_list:
    identifier = re.findall('<recordIdentifier>(.*?)</recordIdentifier>', record)
    pretty_xml = xml.dom.minidom.parseString(record)
    xml_pretty_str = pretty_xml.toprettyxml()
    fpath = os.path.join('mods_records', identifier[0] + '.xml')
    fhand = open(fpath, 'w', encoding='utf-8')
    fhand.write(xml_pretty_str)
    fhand.close()

filehand.close()