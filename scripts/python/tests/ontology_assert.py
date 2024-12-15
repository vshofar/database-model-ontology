from owlapy.owl_axiom import OWLObjectPropertyAssertionAxiom, OWLAxiom
from owlapy.owl_individual import OWLNamedIndividual
from owlapy.owl_property import OWLObjectProperty
from owlapy.owl_reasoner import SyncReasoner

from python.tests.utils import individual, property


class OntologyAssert:

    reasoner: SyncReasoner

    def __init__(self, reasoner):
        self.reasoner = reasoner

    def _clear(self):
        for a in self.reasoner.ontology.get_abox_axioms():
            if type(a) == OWLObjectPropertyAssertionAxiom:
                self.reasoner.ontology.remove_axiom(a)
        return self

    def object_property_assertion(self, sub, prop, obj):
        onto = self.reasoner.ontology
        _sub = individual(onto, sub)
        _prop = property(onto, prop)
        _obj = individual(onto, obj)

        self._object_property_assertion(_sub, _prop, _obj)

        return self

    def _object_property_assertion(self, sub: OWLNamedIndividual, prop: OWLObjectProperty, obj: OWLNamedIndividual):
        self.reasoner.ontology.add_axiom(
            OWLObjectPropertyAssertionAxiom(
                sub,
                prop,
                obj
            )
        )

    def evaluate(self, axiom: OWLAxiom):
        self._clear()
        return self.reasoner.is_entailed(axiom)

    
