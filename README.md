# Data Class to XML Converter

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This Python utility provides a simple way to convert data class objects into XML format. The `dataclass_to_xml` function takes an instance of a data class as input and returns its XML representation.

## Usage

```python
import dataclasses
import xml.etree.ElementTree as ET
from typing import List

def dataclass_to_xml(data_class_obj):
    # ... (code snippet provided in the repository)


from dataclasses import dataclass

# Example usage
@dataclass
class Person:
    name: str
    age: int
    address: str

person_obj = Person(name="John Doe", age=30, address="123 Main St")
xml_representation = dataclass_to_xml(person_obj)
print(xml_representation)
```

## How it works

The `dataclass_to_xml` function converts the provided data class object into an XML string by recursively traversing the data class attributes. If an attribute is another data class, it creates a sub-element for it in the XML structure. Otherwise, it adds the attribute's value as the text content of the XML element.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to [open an issue](https://github.com/yourusername/dataclass-xml-converter/issues) or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Note: This utility is inspired by the Python `dataclasses` module and uses the `xml.etree.ElementTree` for XML handling.*
