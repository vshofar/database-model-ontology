from owlapy.class_expression import OWLClass
from owlapy.owl_axiom import OWLObjectPropertyAssertionAxiom, OWLAxiom, OWLClassAssertionAxiom
from owlapy.owl_individual import OWLNamedIndividual
from owlapy.owl_ontology import Ontology
from owlapy.owl_property import OWLObjectProperty

from python.experiment.owlapy.utils import individual, property, onto_type


class OntologyQuery:

    ontology: Ontology

    def __init__(self, ontology):
        self.ontology = ontology

    def hasPropertyValue(self, sub, prop, obj):
        onto = self.ontology
        _sub = individual(onto, sub)
        _prop = property(onto, prop)
        _obj = individual(onto, obj)

        return self._object_property_question(_sub, _prop, _obj)

    def _object_property_question(self, sub: OWLNamedIndividual, prop: OWLObjectProperty, obj: OWLNamedIndividual):
        return OWLObjectPropertyAssertionAxiom(
                sub,
                prop,
                obj
            )

    def hasType(self, individual_name, individual_type):
        subject = individual(self.ontology, individual_name)
        t = onto_type(self.ontology, individual_type)

        return self._individual_type_assertion(subject, t)

    def _individual_type_assertion(self, sub: OWLNamedIndividual, t: OWLClass):
        return OWLClassAssertionAxiom(
                sub,
                t
            )



    
