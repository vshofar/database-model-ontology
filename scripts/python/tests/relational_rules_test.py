#!/usr/bin/env -S python -W "ignore"

import unittest

from python.tests.utils import load_ontology, remove_all_individuals, sync_reasoner, get_base
from owlready2 import Thing


class TestRelationalRules(unittest.TestCase):

    def setUp(self):
        self.onto = load_ontology()
        remove_all_individuals(self.onto, [self.onto.simpleAttributeType])

    def tearDown(self):
        self.onto.destroy()

    def test_given_some_entity_map_to_relation(self):

        employee = Thing("employee",self.onto)
        gender = Thing("gender", self.onto)
        employee.hasAttribute.append(gender)

        sync_reasoner(self.onto)

        self.assertIn(employee, self.onto.Relation.instances())

    def test_given_some_entity_has_simple_attribute_map_it_to_attribute_relation(self):

        employee = Thing("employee", self.onto)
        gender = Thing("gender", self.onto)

        employee.hasAttribute.append(gender)
        gender.hasAttributeType.append(self.onto.simpleAttributeType)

        sync_reasoner(self.onto)

        self.assertIsInstance(employee,self.onto.Relation)
        self.assertIsInstance(gender,self.onto.RelationAttribute)
        self.assertIn(gender,employee.hasRelationAttribute)

    def test_given_some_entity_has_key_map_it_to_primary_key_relation(self):

        employee = Thing("employee", self.onto)
        employee_ssn = Thing("employeeSSN", self.onto)

        employee.hasKey.append(employee_ssn)

        sync_reasoner(self.onto)

        self.assertIsInstance(employee, self.onto.Relation)
        self.assertIsInstance(employee_ssn, self.onto.RelationAttribute)
        self.assertIn(employee_ssn, employee.hasPrimaryKey)

    def test_given_two_entities_participates_of_some_relation_through_relationship_participations_then_they_should_relate_to_each_other(self):

        employee = Thing("employee", self.onto)
        employee_ssn = Thing("employeeSSN", self.onto)
        employee.hasKey.append(employee_ssn)

        depends_of_relationship = Thing("dependsOfRelationship", self.onto)
        depends_of_employee_participation = Thing("dependsOfEmployeeParticipation", self.onto)
        depends_of_employee_participation.hasParticipationEntity.append(employee)
        depends_of_relationship.hasParticipation.append(depends_of_employee_participation)

        dependent = Thing("dependent", self.onto)
        dependent_name = Thing("dependentName", self.onto)
        dependent.hasPartialKey.append(dependent_name)

        depends_of_relationship = Thing("dependsOfRelationship", self.onto)
        depends_of_dependent_participation = Thing("dependsOfDependentParticipation", self.onto)
        depends_of_dependent_participation.hasParticipationEntity.append(dependent)
        depends_of_relationship.hasParticipation.append(depends_of_dependent_participation)

        sync_reasoner(self.onto)

        self.assertIsInstance(dependent, self.onto.Entity)
        self.assertIsInstance(depends_of_relationship, self.onto.Relationship)
        self.assertIn(depends_of_dependent_participation, depends_of_relationship.hasParticipation)

        self.assertIsInstance(employee, self.onto.Entity)
        self.assertIsInstance(depends_of_relationship, self.onto.Relationship)
        self.assertIn(depends_of_employee_participation, depends_of_relationship.hasParticipation)

        self.assertIn(employee, dependent.hasRelationshipWith)



    def test_given_relationship_between_strong_and_weak_entity_map_strong_primary_key_as_waeK_foreign_key(self):
        employee = Thing("employee", self.onto)
        employee_ssn = Thing("employeeSSN", self.onto)
        employee.hasKey.append(employee_ssn)

        depends_of_relationship = Thing("dependsOfRelationship", self.onto)
        depends_of_employee_participation = Thing("dependsOfEmployeeParticipation", self.onto)
        depends_of_employee_participation.hasParticipationEntity.append(employee)
        depends_of_relationship.hasParticipation.append(depends_of_employee_participation)

        dependent = Thing("dependent", self.onto)
        dependent_name = Thing("dependentName", self.onto)
        dependent.hasPartialKey.append(dependent_name)

        depends_of_dependent_participation = Thing("dependsOfDependentParticipation", self.onto)
        depends_of_dependent_participation.hasParticipationEntity.append(dependent)
        depends_of_relationship.hasParticipation.append(depends_of_dependent_participation)

        sync_reasoner(self.onto)
        sync_reasoner(self.onto)

        self.assertIn(dependent, employee_ssn.isForeignKeyOf)
















