import unittest

from python.experiment.owlapy.ontology_assert import OntologyAssert
from python.experiment.owlapy.ontology_query import OntologyQuery

from python.tests.utils import load_reasoner

class TestRelationalRules(unittest.TestCase):

    def setUp(self):
        self.reasoner = load_reasoner("HermiT")
        self._assert = OntologyAssert(self.reasoner)
        self._query = OntologyQuery(self.reasoner.ontology)

    def test_given_some_entity_map_to_relation(self):

        scenario = self._assert.object_property_assertion("employee", "hasAttribute", "gender")

        q1 = self._query.hasType("employee", "Relation")

        self.assertTrue(scenario.evaluate(q1))


    def test_given_some_entity_has_simple_attribute_map_it_to_attribute_relation(self):

        scenario = (
            self._assert
                .object_property_assertion("gender", "hasAttributeType", "simpleAttributeType")
                .object_property_assertion("employee", "hasAttribute", "gender")
            )

        q1 = self._query.hasType("employee", "Relation")
        q2 = self._query.hasType("gender", "RelationAttribute")
        q3 = self._query.hasPropertyValue("employee", "hasRelationAttribute", "gender")


        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))


    def test_given_some_entity_has_key_map_it_to_primary_key_relation(self):

        scenario = self._assert.object_property_assertion("employee", "hasKey", "ssn")

        q1 = self._query.hasType("employee", "Relation")
        q2 = self._query.hasType("ssn", "RelationAttribute")
        q3 = self._query.hasPropertyValue("employee", "hasPrimaryKey", "ssn")

        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))


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

    def test_given_relationship_between_strong_and_weak_entity_map_strong_primary_key_as_waeK_foreign_key(self):

        scenario = (
            self._assert
                .object_property_assertion("employee", "hasKey", "ssn")
                .object_property_assertion("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
                .object_property_assertion("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
                .object_property_assertion("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
                .object_property_assertion("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
                .object_property_assertion("dependent", "hasPartialKey", "name")
        )

        q1 = self._query.hasPropertyValue("ssn", "isForeignKeyOf", "dependent")

        self.assertTrue(scenario.evaluate(q1))

    def test_given_relationship_between_strong_and_weak_entity_map_reference_origin(self):

        scenario = (
            self._assert
                .object_property_assertion("employee", "hasKey", "ssn")
                .object_property_assertion("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
                .object_property_assertion("dependent", "hasPartialKey", "name")
                .object_property_assertion("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
                .object_property_assertion("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
                .object_property_assertion("dependsOf", "hasParticipation", "dependsOfDependentParticipation")

        )

        q1 = self._query.hasType("dependsOfDependentParticipation", "ReferenceParticipation")
        q2 = self._query.hasPropertyValue("dependsOfDependentParticipation", "hasReferenceParticipationRelation", "dependent")
        q3 = self._query.hasPropertyValue("dependsOfDependentParticipation", "hasReferenceParticipationRelationAttribute", "ssn")
        q4 = self._query.hasPropertyValue("dependsOfDependentParticipation", "hasReferenceParticipationSide", "originReferenceParticipationSide")


        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))
        self.assertTrue(scenario.evaluate(q4))

    def test_given_relationship_between_strong_and_weak_entity_map_reference_target(self):

        scenario = (
            self._assert
                .object_property_assertion("employee", "hasKey", "ssn")
                .object_property_assertion("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
                .object_property_assertion("dependent", "hasPartialKey", "name")
                .object_property_assertion("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
                .object_property_assertion("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
                .object_property_assertion("dependsOf", "hasParticipation", "dependsOfDependentParticipation")

        )

        q1 = self._query.hasType("dependsOfEmployeeParticipation", "ReferenceParticipation")
        q2 = self._query.hasPropertyValue("dependsOfEmployeeParticipation", "hasReferenceParticipationRelation", "employee")
        q3 = self._query.hasPropertyValue("dependsOfEmployeeParticipation", "hasReferenceParticipationRelationAttribute", "ssn")
        q4 = self._query.hasPropertyValue("dependsOfEmployeeParticipation", "hasReferenceParticipationSide", "targetReferenceParticipationSide")


        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))
        self.assertTrue(scenario.evaluate(q4))
















