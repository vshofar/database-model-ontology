from owlready2 import *
from random import random

def remove_all_individuals(onto, keep=[]):
    for i in list(onto.individuals()):
        if i not in keep:
            destroy_entity(i)

def print_all_individuals(onto):
    print("Print all individuals..")
    for i in onto.individuals():
        print(i)

def load_ontology():
    ontology_file = "/home/vbatista/estudo/ontologias/datamodel/owl/DataModel.owl"
    onto = get_ontology(ontology_file).load()

    return onto

def sync_reasoner(onto=None):
    sync_reasoner_pellet(x=onto, infer_property_values = True, infer_data_property_values = True, debug = False)




