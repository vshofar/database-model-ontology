from collections.abc import Iterable

from owlapy.class_expression import OWLClass, OWLObjectSomeValuesFrom, OWLObjectHasValue
from owlapy.iri import IRI
from owlapy.owl_axiom import OWLObjectPropertyAssertionAxiom
from owlapy.owl_individual import OWLNamedIndividual
from owlapy.owl_object import OWLObject
from owlapy.owl_ontology import Ontology
from owlapy.owl_property import OWLObjectProperty, OWLObjectPropertyExpression, OWLPropertyExpression


def remove_object_property_assertions(onto):
    for a in onto.get_abox_axioms():
        if type(a) == OWLObjectPropertyAssertionAxiom:
            onto.remove_axiom(a)

def print_individuals(onto: Ontology):
    for i in onto.individuals_in_signature():
        print(i)

def print_a_box(onto):
    for a in onto.get_abox_axioms():
        print(a)

def print_t_box(onto):
    for a in onto.get_tbox_axioms():
        print(a)

def get_ontology_namespace(onto):
    return onto.get_ontology_id().get_ontology_iri().as_str()

def individual(onto, individual_name):
    ontology_namespace = get_ontology_namespace(onto)
    individual = OWLNamedIndividual(IRI.create(ontology_namespace + "#" + individual_name))

    return individual

def property(onto, property_name):
    prop = OWLObjectProperty(IRI.create(get_ontology_namespace(onto) + "#" + property_name))
    return prop

def some_class(onto, class_name):
    c = OWLClass(IRI.create(get_ontology_namespace(onto) + "#" + class_name))
    return c

def object_some_values_from(onto, property_name, class_name):
    return OWLObjectSomeValuesFrom(
        property(onto, property_name),
        some_class(onto, class_name)
    )

def object_has_value(onto, property_name, individual_name):
    return OWLObjectHasValue(
        property(onto, property_name),
        individual(onto, individual_name)
    )

def object_some_values_from(onto, property_name, class_name):
    return OWLObjectSomeValuesFrom(
        property(onto, property_name),
        some_class(onto, class_name)
    )

def onto_type(onto, t):
    return OWLClass(IRI.create(get_ontology_namespace(onto) + "#" + t))

def print_query_result(it: Iterable, only_name=False, ident=0):
    for i in it:
        if only_name:
            print_ident(i.reminder, ident)
        else:
            print_ident(+i, ident)

def print_ident(str, ident=0):
    ident_str=""
    for i in range(ident):
        ident_str+="    "

    print(ident_str+str)





