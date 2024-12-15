from funowl.converters.functional_converter import to_python
from rdflib import Namespace, XSD, OWL, Literal
from funowl import *

ontology_path = "/home/vbatista/estudo/ontologias/datamodel/owl/scripts/DataModelFunctional.ofn"
ofn_content = open(ontology_path).read()

ontology = to_python(ofn_content)





