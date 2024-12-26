import unittest

from python.experiment.owlapy.ontology_assert import OntologyAssert
from python.experiment.owlapy.ontology_query import OntologyQuery

from python.tests.utils import load_reasoner

class TestRelationshipParticipation(unittest.TestCase):

    def setUp(self):
        self.reasoner = load_reasoner("HermiT")
        self._assert = OntologyAssert(self.reasoner)
        self._query = OntologyQuery(self.reasoner.ontology)
        
    def test_given_thing_hasRelationshipParticipation_thing_should_infer(self):
        scenario = self._assert.object_property_value(
            "dependsOfRelationship",
            "hasParticipation",
            "dependentsOfRelationshipParticipation"
        )

        q1 = self._query.hasType("dependsOfRelationship", "Relationship")
        
        self.assertTrue(scenario.evaluate(q1))

    def test_a_relationship_with_one_to_one_cardinality_should_infer(self):
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

        q1 = self._query.hasType("dependsOf", "OneToOneRelationship")

        self.assertTrue(scenario.evaluate(q1))

    def test_a_relationship_with_one_to_many_cardinality_should_infer(self):
        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfEmployeeParticipation", "PartialRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasPartialKey", "name")
            .object_type("dependsOfDependentParticipation", "ManyCardinalityRelationshipParticipation")
            .object_type("dependsOfDependentParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q1 = self._query.hasType("dependsOf", "OneToManyRelationship")

        self.assertTrue(scenario.evaluate(q1))
















