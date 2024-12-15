from owlapy.iri import IRI
from owlapy.owl_axiom import OWLObjectPropertyAssertionAxiom
from owlapy.owl_individual import OWLNamedIndividual
from owlapy.owl_property import OWLObjectProperty


def remove_object_property_assertions(onto):
    for a in onto.get_abox_axioms():
        if type(a) == OWLObjectPropertyAssertionAxiom:
            onto.remove_axiom(a)

def get_ontology_namespace(onto):
    return onto.get_ontology_id().get_ontology_iri().as_str()

def individual(onto, individual_name):
    ontology_namespace = get_ontology_namespace(onto)
    individual = OWLNamedIndividual(IRI.create(ontology_namespace + "#" + individual_name))

    return individual

def property(onto, property_name):
    prop = OWLObjectProperty(IRI.create(get_ontology_namespace(onto) + "#" + property_name))
    return prop



