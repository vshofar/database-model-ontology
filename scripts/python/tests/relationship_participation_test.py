import unittest

from python.experiment.owlapy.ontology_assert import OntologyAssert
from python.experiment.owlapy.ontology_query import OntologyQuery

from python.tests.utils import load_reasoner

class TestRelationshipParticipation(unittest.TestCase):

    def setUp(self):
        self.reasoner = load_reasoner("Pellet")
        self._assert = OntologyAssert(self.reasoner)
        self._query = OntologyQuery(self.reasoner.ontology)
    
    def test_given_thing_hasParticipationEntity_thing_should_infer(self):

        scenario = self._assert.object_property_value(
            "dependentsOfRelationshipParticipation",
            "hasParticipationEntity",
            "employee"
        )

        q1 = self._query.hasType("dependentsOfRelationshipParticipation", "RelationshipParticipation")

        self.assertTrue(scenario.evaluate(q1))


    def test_given_thing_hasParticipationCardinality_thing_should_infer(self):

        scenario = self._assert.object_property_value(
            "dependentsOfRelationshipParticipation",
            "hasParticipationCardinality",
            "one"
        )

        q1 = self._query.hasType("dependentsOfRelationshipParticipation", "RelationshipParticipation")

        self.assertTrue(scenario.evaluate(q1))


    def test_given_thing_hasParticipationLevel_thing_should_infer(self):

        scenario = self._assert.object_property_value(
            "dependentsOfRelationshipParticipation",
            "hasParticipationLevel",
            "total"
        )

        q1 = self._query.hasType("dependentsOfRelationshipParticipation", "RelationshipParticipation")

        self.assertTrue(scenario.evaluate(q1))

    def test_given_partial_participation_with_participation_entity_with_key_should_infer(self):
        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfEmployeeParticipation", "PartialRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasPartialKey", "name")
            .object_type("dependsOfDependentParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfDependentParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q1 = self._query.hasPropertyValue("dependsOf", "hasPartialParticipation", "dependsOfEmployeeParticipation")

        self.assertTrue(scenario.evaluate(q1))


    def test_given_total_participation_with_participation_entity_with_key_should_infer(self):
        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfEmployeeParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasPartialKey", "name")
            .object_type("dependsOfDependentParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfDependentParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q1 = self._query.hasPropertyValue("dependsOf", "hasTotalParticipation", "dependsOfEmployeeParticipation")

        self.assertTrue(scenario.evaluate(q1))














