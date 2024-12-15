from owlapy.owl_reasoner import SyncReasoner


def load_reasoner(name):
    ontology_path = "/home/vbatista/estudo/ontologias/datamodel/owl/DataModel.owl"
    return SyncReasoner(ontology=ontology_path, reasoner=name)