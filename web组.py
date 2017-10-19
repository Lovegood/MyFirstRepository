import xml.etree.ElementTree as ET
from openpyxl import Workbook

def main():
    wb = Workbook() #create a workbook
    ws = wb.get_active_sheet() #调用正在运行的工作表 worksheet
    ws.title = 'raw'
    rowCnt = 1

    xmlPath = 'allitems-cvrf-year-2017.xml'
    xmlTagPrefix = '{http://www.icasi.org/CVRF/schema/vuln/1.1}'
    tree = ET.ElementTree(file=xmlPath)
    root = tree.getroot()
    for child in root:
        if child.tag == xmlTagPrefix+'Vulnerability':
            dataNode = child
            CVEtitle = dataNode.find(xmlTagPrefix+'Title').text
            description = dataNode.find(xmlTagPrefix+'Notes').find(xmlTagPrefix+'Note').text
            ws.cell(row = rowCnt, column = 1).value = CVEtitle
            ws.cell(row = rowCnt, column = 2).value = description
            rowCnt += 1

    wb.save('raw.xlsx') # save

if __name__ == '__main__':
    main()
