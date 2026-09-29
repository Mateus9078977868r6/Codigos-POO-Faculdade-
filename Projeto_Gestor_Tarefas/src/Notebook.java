import java.util.ArrayList;
import java.util.Iterator;

/**
 * A class to maintain an arbitrarily long list of notes.
 * Notes are numbered for external reference by a human user.
 * In this version, note numbers start at 0.
 *
 * @author David J. Barnes and Michael Kolling.
 * @version 2008.03.30
 */
public class Notebook
{
    // Storage for an arbitrary number of notes.
    private ArrayList<Tarefa> notes;
    /**
     * Perform any initialization that is required for the
     * notebook.
     */
    public Notebook()
    {
        notes = new ArrayList<Tarefa>();
    }

    /**
     * Store a new note into the notebook.
     * @param text The note to be stored.
     */
    public void storeNote(String text) // 1 // storeNote recebe uma String como parametro cujo nome é text
    {
        notes.add(new Tarefa(text)); // add é um metodo do tipo ArrayList que recebe como parametro um objeto da classe
        // Tarefa que criamos cuja referencia é o construtor
    }

    /**
     * @return The number of notes currently in the notebook.
     */
    public int numberOfNotes()
    {
        return notes.size();
    } // size é um metodo do ArrayList

    /**
     * Show a note.
     * @param noteNumber The number of the note to be shown.
     */
    public void showNote(int noteNumber)
    {
        if(noteNumber < 0) {
            // This is not a valid note number.
            System.out.println("Digite números maiores que 0!");
        }
        else if(noteNumber < numberOfNotes()) {
            // This is a valid note number, so we can print it.
            System.out.println("Nota requisitada: " + notes.get(noteNumber));
        }
        else {
            // This is not a valid note number.
            System.out.println("Número da nota não encontrada aqui!");
        }
    }
    public void showAllNotes()
    {
        int index = 1; // indice manual do for
        //for(String note: notes){
        //     System.out.println("Nota: " + note);
        //}
        Iterator<Tarefa> it = notes.iterator(); // instancia um objeto Iterator chamado it cujo tipo é a Classe Tarefa
        while(it.hasNext()){ // enquanto ainda tiver proximos itens
            System.out.println("(" + index + ") " + it.next()); // imprima o index + [] descricao
            index++; // incrementa no loop
        }
    }

    public void removeNote(int noteNumber) // remover com base no indice - recebe um numero
    {
        noteNumber = noteNumber - 1; // ajustar a contagem para seguir exatamente o valor digitado no teclado
        if(noteNumber < 0) {
            // This is not a valid note number.
            System.out.println("Digite números maiores que 0!");
        }
        else if(noteNumber < numberOfNotes()) {
            // This is a valid note number, so we can print it.
            System.out.println("Removida: " + notes.get(noteNumber));
            notes.remove(noteNumber); // remove (remove é um metodo de ArrayList)
        }
        else {
            // This is not a valid note number.
            System.out.println("Número de nota não encontrada aqui!");
        }
    }

    public void removeNoteWord(String word) {
        Iterator<Tarefa> it = notes.iterator();
        while (it.hasNext()){
            Tarefa nota = it.next();
            if(nota.getDescription().contains(word)){
                it.remove();
                System.out.printf("Tarefa Removida!\n");
            }
        }
    }

    public void concluirNote(int noteNumber)
    {
        noteNumber = noteNumber - 1;
        if(noteNumber < 0) {
            // This is not a valid note number.
            System.out.println("Digite números maiores que 0!");
        }
        else if(noteNumber < numberOfNotes()) {
            // This is a valid note number, so we can conclued it.
            notes.get(noteNumber).setRealized(true);
            System.out.printf("Tarefa Concluida!\n");
        }
        else {
            // This is not a valid note number.
            System.out.println("Número de nota não encontrada aqui!");
        }
    }

    public void concluirNoteWord(String word) {
        Iterator<Tarefa> it = notes.iterator();
        while (it.hasNext()){
            Tarefa nota = it.next();
            if(nota.getDescription().contains(word)){
                nota.setRealized(true);
                System.out.printf("Tarefa Concluida!\n");
            }
        }
    }
}
