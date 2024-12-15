from owlapy.owl_axiom import OWLObjectPropertyAssertionAxiom, OWLAxiom
from owlapy.owl_individual import OWLNamedIndividual
from owlapy.owl_ontology import Ontology
from owlapy.owl_property import OWLObjectProperty

from utils import individual, property


class OntologyQuery:

    ontology: Ontology

    def __init__(self, ontology):
        self.ontology = ontology

    def object_property_question(self, sub, prop, obj):
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


    
