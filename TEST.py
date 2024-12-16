import xml.etree.ElementTree as ET

class TEIAnalyzer:
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()

    def get_all_tags(self):

        tags = {}
        for elem in self.root.iter():
            tag = elem.tag
            tags[tag] = tags.get(tag, 0) + 1
        return tags

    def get_tag_attributes(self):

        attributes = {}
        for elem in self.root.iter():
            if elem.attrib:
                tag = elem.tag
                attributes[tag] = attributes.get(tag, [])
                attributes[tag].append(elem.attrib)
        return attributes

    def get_terms_with_types(self):

        terms = []
        for elem in self.root.iter('term'):
            if 'type' in elem.attrib:
                terms.append((elem.text, elem.attrib['type']))
        return terms

    def print_tag_structure(self):

        def recursive_print(elem, level=0):
            indent = " " * (level * 2)
            print(f"{indent}<{elem.tag}>")
            for child in elem:
                recursive_print(child, level + 1)
        
        recursive_print(self.root)

    def analyze(self):

        print("---- Document Tag Count ----")
        tags = self.get_all_tags()
        for tag, count in tags.items():
            print(f"{tag}: {count}")

        print("\n---- Tag Attributes ----")
        attributes = self.get_tag_attributes()
        for tag, attrs in attributes.items():
            print(f"{tag}:")
            for attr in attrs:
                print(f"  {attr}")

        print("\n---- Terms with 'type' Attribute ----")
        terms = self.get_terms_with_types()
        for term, t_type in terms:
            print(f"Term: {term}, Type: {t_type}")

        print("\n---- Document Structure ----")
        self.print_tag_structure()


xml_file = 'path_to_your_tei.xml' 
analyzer = TEIAnalyzer(xml_file)
analyzer.analyze()