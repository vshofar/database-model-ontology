from owlapy.owl_reasoner import SyncReasoner
from ontology_query import OntologyQuery
from ontology_assert import OntologyAssert

ontology_path = "/home/vbatista/estudo/ontologias/datamodel/owl/DataModel.owl"
reasoner = SyncReasoner(ontology=ontology_path, reasoner="Pellet")

ontology_assert = OntologyAssert(reasoner)
ontology_query = OntologyQuery(reasoner.ontology)

scenario = (
    ontology_assert
        .object_property_assertion("employee", "hasKey", "employeeSSN")
        .object_property_assertion("dependent", "hasPartialKey", "dependentGender")
        .object_property_assertion("dependsOfEmployeeParticipation", "hasParticipationEntity", "employee")
        .object_property_assertion("dependsOfDependentParticipation", "hasParticipationEntity", "dependent")
        .object_property_assertion("dependsOf", "hasParticipation", "dependsOfDependentParticipation")
        .object_property_assertion("dependsOf", "hasParticipation", "dependsOfEmployeeParticipation")
)

query = ontology_query.hasPropertyValue("employeeSSN", "isForeignKeyOf", "dependent")
assert(scenario.evaluate(query) == True)

ontology_assert.clear()

scenario = (
    ontology_assert
        .object_property_assertion(
            "employee",
            "hasAttribute",
            "employeeGender"
        )
)

query = ontology_query.hasPropertyValue(
    "employeeGender",
    "isAttributeOf",
    "employee"
)

assert(scenario.evaluate(query) == True)














