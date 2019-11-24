
import cleanse


def test_traverse_nodes():
    xml_string = '<root><test>blah</test></root>'
    cleanse.traverse_nodes(xml_string)
