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
        scenario = self._assert.object_property_assertion(
            "dependsOfRelationship",
            "hasParticipation",
            "dependentsOfRelationshipParticipation"
        )

        q1 = self._query.hasType("dependsOfRelationship", "Relationship")
        
        self.assertTrue(scenario.evaluate(q1))

    def test_a_relationship_with_one_to_one_cardinality_should_infer(self):
        scenario = (
            self._assert
            .object_property_assertion("employee", "hasKey", "ssn")
                .object_property_assertion("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
                .object_property_assertion("dependsOfEmployeeParticipation", "hasParticipationCardinality", "oneParticipationCardinality")
            .object_property_assertion("dependent", "hasPartialKey", "name")
                .object_property_assertion("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
                .object_property_assertion("dependsOfDependentParticipation", "hasParticipationCardinality", "oneParticipationCardinality")
            .object_property_assertion("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_assertion("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .different_of_assertion(["dependsOfDependentParticipation","dependsOfEmployeeParticipation"])

        )

        q1 = self._query.hasType("dependsOf", "OneToOneRelationship")

        self.assertTrue(scenario.evaluate(q1))















