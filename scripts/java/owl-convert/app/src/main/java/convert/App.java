package convert;

import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLDocumentFormat;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.model.OWLOntologyCreationException;
import org.semanticweb.owlapi.model.OWLOntologyManager;
import org.semanticweb.owlapi.model.OWLOntologyStorageException;
import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.io.OWLXMLOntologyFormat;

public class App {
    public String getGreeting() {
        return "Hello World!";
    }

    public static void main(String[] args) throws OWLOntologyCreationException, OWLOntologyStorageException {
        System.out.println(new App().getGreeting());

        OWLOntologyManager manager = OWLManager.createOWLOntologyManager();
        OWLOntology ontology = manager.loadOntology(IRI.create("file:////home/vbatista/estudo/ontologias/datamodel/owl/datamodel-functional.ofn"));        
        OWLDocumentFormat format = manager.getOntologyFormat(ontology);

        OWLXMLOntologyFormat owlxmlFormat = new OWLXMLOntologyFormat();
        if (format.isPrefixOWLDocumentFormat()) {
            owlxmlFormat.copyPrefixesFrom(format.asPrefixOWLDocumentFormat());
        }

        manager.saveOntology(ontology, owlxmlFormat, IRI.create("file:////home/vbatista/estudo/ontologias/datamodel/owl/datamodel-owl.owl"));
    }
}
