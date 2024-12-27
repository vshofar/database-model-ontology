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

    def test_given_one_to_one_relationship_with_total_participation_map_total_relation_references(self):

        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfEmployeeParticipation", "PartialRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasKey", "name")
            .object_type("dependsOfDependentParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfDependentParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q0 = self._query.hasPropertyValue("ssn", "isForeignKeyOf", "dependent")
        q1 = self._query.hasType("dependsOfDependentParticipation", "ReferenceParticipation")
        q2 = self._query.hasPropertyValue("dependsOfDependentParticipation", "hasReferenceParticipationRelation",
                                          "dependent")
        q3 = self._query.hasPropertyValue("dependsOfDependentParticipation",
                                          "hasReferenceParticipationRelationAttribute", "ssn")
        q4 = self._query.hasPropertyValue("dependsOfDependentParticipation", "hasReferenceParticipationSide",
                                          "originReferenceParticipationSide")

        self.assertTrue(scenario.evaluate(q0))
        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))
        self.assertTrue(scenario.evaluate(q4))

    def test_given_one_to_one_relationship_with_total_participation_map_partial_relation_references(self):

        scenario = (
            self._assert
            .object_property_value("employee", "hasKey", "ssn")
            .object_type("dependsOfEmployeeParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfEmployeeParticipation", "PartialRelationshipParticipation")
            .object_property_value("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
            .object_property_value("dependent", "hasKey", "name")
            .object_type("dependsOfDependentParticipation", "OneCardinalityRelationshipParticipation")
            .object_type("dependsOfDependentParticipation", "TotalRelationshipParticipation")
            .object_property_value("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
            .object_property_value("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
            .object_property_only_with_individuals("dependsOf", "hasParticipation", ["dependsOfEmployeeParticipation",
                                                                                     "dependsOfDependentParticipation"])
        )

        q1 = self._query.hasType("dependsOfEmployeeParticipation", "ReferenceParticipation")
        q2 = self._query.hasPropertyValue("dependsOfEmployeeParticipation", "hasReferenceParticipationRelation",
                                          "employee")
        q3 = self._query.hasPropertyValue("dependsOfEmployeeParticipation",
                                          "hasReferenceParticipationRelationAttribute", "ssn")
        q4 = self._query.hasPropertyValue("dependsOfEmployeeParticipation", "hasReferenceParticipationSide",
                                          "targetReferenceParticipationSide")

        self.assertTrue(scenario.evaluate(q1))
        self.assertTrue(scenario.evaluate(q2))
        self.assertTrue(scenario.evaluate(q3))
        self.assertTrue(scenario.evaluate(q4))




















