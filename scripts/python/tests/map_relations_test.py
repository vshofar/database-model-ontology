import unittest

from funowl import ClassAxiom
from owlapy.class_expression import OWLClassExpression, OWLClass, OWLObjectSomeValuesFrom

from python.experiment.owlapy.ontology_assert import OntologyAssert
from python.experiment.owlapy.ontology_query import OntologyQuery
from python.experiment.owlapy.utils import print_query_result, print_ident

from python.tests.utils import load_reasoner

class TestMapRelations(unittest.TestCase):

    def setUp(self):
        self.reasoner = load_reasoner("HermiT")
        self._assert = OntologyAssert(self.reasoner)
        self._query = OntologyQuery(self.reasoner.ontology)

    def test_given_some_entity_map_to_relation(self):

        scenario = self._assert.object_property_value("employee", "hasAttribute", "gender")

        q1 = self._query.hasType("employee", "Relation")

        self.assertTrue(scenario.evaluate(q1))


    def test_given_some_entity_has_simple_attribute_map_it_to_attribute_relation(self):

        scenario = (
            self._assert
                .object_property_value("gender", "hasAttributeType", "simpleAttributeType")
                .object_property_value("employee", "hasAttribute", "gender")
            )

        q1 = self._query.hasType("employee", "Relation")
        q2 = self._query.hasType("gender", "RelationAttribute")
        q3 = self._query.hasPropertyValue("employee", "hasRelationAttribute", "gender")


        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))


    def test_given_some_entity_has_key_map_it_to_primary_key_relation(self):

        scenario = self._assert.object_property_value("employee", "hasKey", "ssn")

        q1 = self._query.hasType("employee", "Relation")
        q2 = self._query.hasType("ssn", "RelationAttribute")
        q3 = self._query.hasPropertyValue("employee", "hasPrimaryKey", "ssn")

        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))

