
package convert;

import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.model.OWLOntologyCreationException;
import org.semanticweb.owlapi.model.OWLOntologyManager;
import org.semanticweb.owlapi.apibinding.OWLManager;

public class App {
    public String getGreeting() {
        return "Hello World!";
    }

    public static void main(String[] args) throws OWLOntologyCreationException {
        System.out.println(new App().getGreeting());

        OWLOntologyManager manager = OWLManager.createOWLOntologyManager();
        OWLOntology ontology = manager.loadOntology(IRI.create("file:////home/vbatista/estudo/ontologias/datamodel/owl/owl-functional.ofn"));        
    }
}
