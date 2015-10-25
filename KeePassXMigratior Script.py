import sys
import xml.etree.ElementTree
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = xml.etree.ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent=" ")

inputFile = sys.argv[1]

db = xml.etree.ElementTree.parse(inputFile).getroot()

outputDb = xml.etree.ElementTree.Element('database')

outputGroup = xml.etree.ElementTree.SubElement(outputDb, 'group')

outputGroupTitle = xml.etree.ElementTree.SubElement(outputGroup, 'title')
outputGroupTitle.text = 'Migration'

for group in db.findall('group'):
	for entry in group.findall('entry'):
		outputEntry = xml.etree.ElementTree.SubElement(outputGroup, 'entry')
		
		xml.etree.ElementTree.SubElement(outputEntry, 'title').text = entry.find('title').text
		xml.etree.ElementTree.SubElement(outputEntry, 'username').text = entry.find('username').text
		xml.etree.ElementTree.SubElement(outputEntry, 'password').text = entry.find('password').text
		xml.etree.ElementTree.SubElement(outputEntry, 'url').text = entry.find('url').text
		xml.etree.ElementTree.SubElement(outputEntry, 'comment').text = entry.find('comment').text
		
print(prettify(outputDb))
