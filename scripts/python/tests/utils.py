from owlready2 import *


def remove_all_individuals(onto, expect=[]):
    for i in list(onto.individuals()):
        if i not in expect:
            destroy_entity(i)

def print_all_individuals(onto):
    print("Print all individuals..")
    for i in onto.individuals():
        print(i)

def load_ontology():        
    onto = get_ontology("/home/vbatista/estudo/ontologias/datamodel/owl/DataModel.owl").load()
    return onto

def sync_reasoner():
    sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True, debug = False)