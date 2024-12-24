import unittest

from funowl import ClassAxiom
from owlapy.class_expression import OWLClassExpression, OWLClass, OWLObjectSomeValuesFrom

from python.experiment.owlapy.ontology_assert import OntologyAssert
from python.experiment.owlapy.ontology_query import OntologyQuery
from python.experiment.owlapy.utils import print_query_result, print_ident

from python.tests.utils import load_reasoner

class TestRelationalRules(unittest.TestCase):

    def setUp(self):
        self.reasoner = load_reasoner("HermiT")
        self._assert = OntologyAssert(self.reasoner)
        self._query = OntologyQuery(self.reasoner.ontology)

    def test_given_two_entities_participates_of_some_relation_through_relationship_participations_then_they_should_relate_to_each_other(self):

        scenario = (
            self._assert
                .object_property_assertion("employee", "hasKey", "ssn")
                .object_property_assertion("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
                .object_property_assertion("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
                .object_property_assertion("dependent", "hasPartialKey", "name")
                .object_property_assertion("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
                .object_property_assertion("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
        )


        q1 = self._query.hasType("dependent", "Entity")
        q2 = self._query.hasType("dependsOf", "Relationship")
        q3 = self._query.hasPropertyValue("dependsOf", "hasParticipation", "dependsOfDependentParticipation")

        q4 = self._query.hasType("employee", "Entity")
        q5 = self._query.hasPropertyValue("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
        q6 = self._query.hasPropertyValue("dependent", "hasRelationshipWith", "employee")

        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))
        self.assertTrue(scenario.evaluate(q4))
        self.assertTrue(scenario.evaluate(q5))
        self.assertTrue(scenario.evaluate(q6))

    def test_given_string_and_weak_entity_participates_of_some_relation_through_relationship_participations_then_they_should_relate_to_each_other(
            self):
        scenario = (
            self._assert
            .object_property_assertion("employee", "hasKey", "ssn")
            .object_property_assertion("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_assertion("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_assertion("dependent", "hasPartialKey", "name")
            .object_property_assertion("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_assertion("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
        )

        q1 = self._query.hasPropertyValue("employee", "hasRelationshipWithWeakEntity", "dependent")

        self.assertTrue(scenario.evaluate(q1))
















