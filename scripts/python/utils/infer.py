#!/usr/bin/env python 

from owlready2 import *

#onto = get_ontology("/home/vbatista/estudo/ontologias/datamodel/owl/datamodel-owl.owl").load()
onto = get_ontology("/home/vbatista/estudo/ontologias/datamodel/owl/DataModel.owl").load()

def remove_all_individuals(onto):
    for i in list(onto.individuals()):
        destroy_entity(i)

def print_all_individuals(onto):
    print("Print all individuals..")
    for i in onto.individuals():
        print(i)

remove_all_individuals(onto)        

employee = Thing("employee",onto)
ssn = Thing("ssn", onto)
employee.hasKey = [ssn]

inferences = get_ontology("http://tests/Inferences.owl")


with inferences:
    sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)
    

assert(onto.employee in onto.Entity.instances())
assert(onto.employee in onto.StrongEntity.instances())
assert(onto.employee.hasAttribute == [onto.ssn])
assert(onto.ssn.isAttributeOf == [onto.employee])
assert(onto.ssn.isKeyOf == [onto.employee])














