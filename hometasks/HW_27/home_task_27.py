"""

Написать скрипт, который преобразовывает xml файл в json файл.

"""

import xml.etree.ElementTree as ET
import json


def convert_xml_to_json(xml_path):
    root = ET.parse(xml_path).getroot()
    pages = {}
    for page in root.findall('page'):
        page_name = page.get('name')
        page_elements = {}
        for element in page.findall('element'):
            element_name = element.get('name')
            element_locators = {}
            for locator in element.findall('locator'):
                platform = locator.get('platform')
                locator_type = locator.get('locator_type')
                locator_value = locator.text
                element_locators[platform] = [locator_type, locator_value]
            page_elements[element_name] = element_locators
        pages[page_name] = page_elements
        with open('pages.json', 'w') as f:
            f.write(json.dumps(pages, indent=4))
    return "Converting is finished successfully"


xml_path = 'pages.xml'
json_data = convert_xml_to_json(xml_path)
print(json_data)