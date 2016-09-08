import xml.etree.ElementTree as ET

tree = ET.parse("data.xml_m")
root = tree.getroot()

#修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated","yes")

tree.write("xml_after_modify.xml_m")


#删除node
for country in root.findall('country'):
   rank = int(country.find('rank').text)
   if rank > 50:
     root.remove(country)

tree.write('xml_after_del.xml_m')