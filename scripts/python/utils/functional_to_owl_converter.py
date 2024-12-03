from rdflib import Graph
from funowl.converters.functional_converter import to_python

def convert(origin_path, dest_path):
    origin_representation = to_python(origin_path)

    g = Graph()
    origin_representation.to_rdf(g)
    xml_content = g.serialize(format="rdf/xml")

    f = open(dest_path, "w")
    f.write(xml_content)
    f.close()

convert("/home/vbatista/estudo/ontologias/datamodel/owl/datamodel-functional.ofn", "/home/vbatista/estudo/ontologias/datamodel/owl/datamodel-owl.owl")    




