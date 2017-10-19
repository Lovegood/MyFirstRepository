import xml.etree.ElementTree as ET

def main():
    xmlPath = 'allitems-cvrf-year-2017.xml'

    xmlTagPrefix = '{http://www.icasi.org/CVRF/schema/vuln/1.1}'

    tree = ET.ElementTree(file=xmlPath)
    root = tree.getroot()
    for child in root:
        if child.tag == xmlTagPrefix+'Vulnerability':
            dataNode = child
            CVEtitle = dataNode.find(xmlTagPrefix+'Title').text
            description = dataNode.find(xmlTagPrefix+'Notes').find(xmlTagPrefix+'Note').text

if __name__ == '__main__':
    main()
