from owlapy.owl_axiom import OWLObjectPropertyAssertionAxiom
from owlapy.owl_individual import *
from owlapy.owl_property import *
from owlapy.owl_reasoner import SyncReasoner

ontology_path = "/home/vbatista/estudo/ontologias/datamodel/owl/DataModel.owl"
reasoner = SyncReasoner(ontology=ontology_path, reasoner="HermiT")
ontology = reasoner.ontology

def remove_object_property_assertions(onto):
    for a in onto.get_abox_axioms():
        if type(a) == OWLObjectPropertyAssertionAxiom:
            onto.remove_axiom(a)

remove_object_property_assertions(ontology)

def get_ontology_namespace(onto):
    return onto.get_ontology_id().get_ontology_iri().as_str()

def individual(onto, individual_name):
    ontology_namespace = get_ontology_namespace(ontology)
    individual = OWLNamedIndividual(IRI.create(ontology_namespace + "#" + individual_name))

    return individual

def property(onto, property_name):
    prop = OWLObjectProperty(IRI.create(get_ontology_namespace(onto) + "#" + property_name))
    return prop

dependent = individual(ontology, "dependent")
dependent_gender = individual(ontology, "male")
employee = individual(ontology, "employee")
employee_ssn = individual(ontology, "employeeSSN")

has_hey = property(ontology, "hasKey")
has_partial_hey = property(ontology, "hasPartialKey")
has_participation = property(ontology, "hasParticipation")
has_participation_entity = property(ontology, "hasParticipationEntity")
is_foreign_key_of = property(ontology, "isForeignKeyOf")

depends_of_employee_participation = individual(ontology, "dependsOfEmployeeParticipation")
depends_of_dependent_participation = individual(ontology, "dependsOfDependentParticipation")
depends_of = individual(ontology, "dependsOfRelation")

ontology.add_axiom(
    OWLObjectPropertyAssertionAxiom(employee, has_hey, employee_ssn)
)

ontology.add_axiom(
    OWLObjectPropertyAssertionAxiom(dependent, has_partial_hey, dependent_gender)
)

ontology.add_axiom(
    OWLObjectPropertyAssertionAxiom(depends_of_dependent_participation, has_participation_entity, dependent)
)

ontology.add_axiom(
    OWLObjectPropertyAssertionAxiom(depends_of_employee_participation, has_participation_entity, employee)
)

ontology.add_axiom(
    OWLObjectPropertyAssertionAxiom(depends_of, has_participation, depends_of_dependent_participation)
)

ontology.add_axiom(
    OWLObjectPropertyAssertionAxiom(depends_of, has_participation, depends_of_employee_participation)
)

assertion = OWLObjectPropertyAssertionAxiom(employee_ssn, is_foreign_key_of, dependent)

print(reasoner.is_entailed(assertion))


