import dataclasses
import xml.etree.ElementTree as ET
from typing import Optional

def dataclass_to_xml(data_class_obj):
    """
    Convert a data class object into XML format.

    Args:
        data_class_obj: An instance of a data class.

    Returns:
        str: The XML representation of the data class object.
    """
    if not dataclasses.is_dataclass(data_class_obj):
        raise ValueError("Input object is not a data class.")

    def _convert_to_xml(obj, root_element):
        for field in dataclasses.fields(obj):
            field_value = getattr(obj, field.name)

            if field_value is None:
                continue

            if dataclasses.is_dataclass(field_value):
                sub_element = ET.SubElement(root_element, field.name)
                _convert_to_xml(field_value, sub_element)
            else:
                ET.SubElement(root_element, field.name).text = str(field_value)

    root_element = ET.Element(data_class_obj.__class__.__name__)
    _convert_to_xml(data_class_obj, root_element)
    
    xml_str = ET.tostring(root_element, encoding='utf-8', method='xml').decode()
    element = ET.XML(xml_str)
    ET.indent(element)
    xml_str = ET.tostring(element, encoding='unicode')
    return xml_str
