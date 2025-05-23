from owlapy.class_expression import OWLClass, OWLClassExpression, OWLObjectSomeValuesFrom, OWLObjectAllValuesFrom, \
    OWLObjectOneOf, OWLObjectExactCardinality, OWLThing
from owlapy.owl_axiom import OWLObjectPropertyAssertionAxiom, OWLAxiom, OWLClassAssertionAxiom, \
    OWLDifferentIndividualsAxiom
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

    def object_type(self, individual_name, individual_type):
        onto = self.reasoner.ontology

        _sub = individual(onto, individual_name)
        _type = onto_type(onto, individual_type)

        assertion = OWLClassAssertionAxiom(
            _sub,
            _type
        )

        self._add_axiom(assertion)

        return self

    def object_property_only_with_individuals(self, sub, prop, individual_names):
        onto = self.reasoner.ontology
        _sub = individual(onto, sub)
        _prop = property(onto, prop)

        individuals = []
        for name in individual_names:
            individuals.append(individual(onto, name))

        _clas = OWLObjectAllValuesFrom(
            _prop,
            OWLObjectOneOf(individuals)
        )

        self._class_assertion(_sub, _clas)

        return self

    def object_property_exactly_n(self, sub, prop, n):
        onto = self.reasoner.ontology
        _sub = individual(onto, sub)
        _prop = property(onto, prop)

        _clas = OWLObjectExactCardinality(
            n,
            _prop,
            OWLThing
        )

        self._class_assertion(_sub, _clas)

        return self

    def _class_assertion(self, sub: OWLNamedIndividual, clas: OWLClassExpression):
        self._add_axiom(
            OWLClassAssertionAxiom(
                sub,
                clas
            )
        )

    def object_property_value(self, sub, prop, obj):
        onto = self.reasoner.ontology
        _sub = individual(onto, sub)
        _prop = property(onto, prop)
        _obj = individual(onto, obj)

        self._object_property_value_assertion(_sub, _prop, _obj)

        return self

    def _object_property_value_assertion(self, sub: OWLNamedIndividual, prop: OWLObjectProperty, obj: OWLNamedIndividual):
        self._add_axiom(
            OWLObjectPropertyAssertionAxiom(
                sub,
                prop,
                obj
            )
        )

    def different_of(self, individual_names):
        onto = self.reasoner.ontology
        individuals = []

        for name in individual_names:
            individuals.append(individual(onto, name))

        self._different_of_assertion(individuals)

        return self

    def _different_of_assertion(self, individuals):
        self._add_axiom(
            OWLDifferentIndividualsAxiom(individuals)
        )

    def evaluate(self, axiom: OWLAxiom):
        internal_reasoner = SyncReasoner(self.reasoner.ontology, "HermiT")
        return internal_reasoner.is_entailed(axiom)

    def search(self, class_expression: OWLClassExpression):
        internal_reasoner = SyncReasoner(self.reasoner.ontology, "HermiT")
        return internal_reasoner.instances(class_expression)


    
