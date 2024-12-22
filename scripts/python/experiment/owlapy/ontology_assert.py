from owlapy.class_expression import OWLClass, OWLClassExpression
from owlapy.owl_axiom import OWLObjectPropertyAssertionAxiom, OWLAxiom, OWLClassAssertionAxiom
from owlapy.owl_individual import OWLNamedIndividual
from owlapy.owl_property import OWLObjectProperty
from owlapy.owl_reasoner import SyncReasoner

from python.experiment.owlapy.utils import individual, property, onto_type


class OntologyAssert:

    reasoner: SyncReasoner

    def __init__(self, reasoner):
        self.reasoner = reasoner
        self.clear()

    def clear(self):
        for a in self.reasoner.ontology.get_abox_axioms():
            if type(a) == OWLObjectPropertyAssertionAxiom:
                self.reasoner.ontology.remove_axiom(a)

    def _add_axiom(self, axiom: OWLAxiom):
        self.reasoner.ontology.add_axiom(axiom)

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
        internal_reasoner = SyncReasoner(self.reasoner.ontology, "HermiT")
        return internal_reasoner.is_entailed(axiom)

    def search(self, class_expression: OWLClassExpression):
        internal_reasoner = SyncReasoner(self.reasoner.ontology, "HermiT")
        return internal_reasoner.instances(class_expression)


    
