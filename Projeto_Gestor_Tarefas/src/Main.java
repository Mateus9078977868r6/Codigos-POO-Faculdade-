// Providenciar a criação da classe Tarefa com os campos String - descricao e Boolean - realizada.
// importar a classe Scanner para ler dados do teclado
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // instanciar um objeto da classe Scanner para trabalharmos com ele no código
        Scanner scanner = new Scanner(System.in); // scanner
        // instanciar um objeto da classe Notebook para trabalharmos com todos os seus metodos (da Classe)
        Notebook note = new Notebook(); // note
        // Declaração de variaveis do teclado para leitura no main
        String tarefa, palavra;
        int op = 1;

        System.out.printf("--------------- Bloco de Notas ------------------"); // Apresentação

        while(op>=1 && op<=6){ // restringir o loop de 1 a 6 (tarefas requisitadas)
            System.out.printf("\nDeseja? \n");
            System.out.printf("1- Adicionar nova tarefa\n");
            System.out.printf("2- Listar todas as tarefas\n");
            System.out.printf("3- Remover tarefa pelo indice\n");
            System.out.printf("4- Remover tarefa por uma palavra\n");
            System.out.printf("5- Marcar tarefas como completas a partir do índice\n");
            System.out.printf("6- Marcar tarefas como completas, filtrando por por palavra chave\n");
            System.out.printf("7- Sair\n");

            op = scanner.nextInt(); // ler o numero (int) digitado e armazena na variavel "op"
            scanner.nextLine(); // limpar buffer (enter) do teclado

            if(op==1){
                System.out.printf("Digite o nome da tarefa: ");
                tarefa = scanner.nextLine(); // armazena em "tarefa" a string digitada
                note.storeNote(tarefa); // usa o metodo de Notebook "storeNote" que recebe um parametro do tipo string
            } else if(op==2){
                note.showAllNotes(); // metodo que usa o Itinerator para imprimir notas e indices correspondentes
            } else if(op==3){
                System.out.printf("Digite o indice que quer remover: ");
                int indice = scanner.nextInt(); // armazena em "indice" o int digitado
                note.removeNote(indice); // usa o metodo de Notebook "removeNote" que recebe um parametro do tipo int para remoção
            } else if(op==4){
                System.out.printf("Digite a palavra chave da tarefa que deseja remover: ");
                palavra = scanner.next(); // armazena em "tarefa" a string digitada
                if(palavra.length()>1){
                    note.removeNoteWord(palavra); // metodo que usa o Itinerator para percorrer a Classe Tarefa no atributo Description
                    // que vai comparar a string "palavra" recebida com um possivel igual atributo da Classe e remover
                }else{
                    System.out.printf("Digite uma palavra!\n");
                }
            } else if(op==5){
                System.out.printf("Qual indice se refere a tarefa que completou? ");
                int ind = scanner.nextInt(); // armazena em "ind" o int digitado
                note.concluirNote(ind); // chama o metodo da classe Notebook para setar o boolean true em uma tarefa pendente
                // mostrando na tela pelo metodo toString da classe Tarefa a marcação de concluida.
            } else if(op==6){
                System.out.printf("Digite a palavra chave da tarefa que deseja marcar como completa: ");
                String tar = scanner.next(); // armazena em "tar" a string digitada
                if(tar.length()>1){
                    note.concluirNoteWord(tar); // // metodo que usa o Itinerator para percorrer a Classe Tarefa no atributo Description
                    // que vai comparar a string "palavra" recebida com um possivel igual atributo da Classe e assim marcar como concluida
                }else{
                    System.out.printf("Digite uma palavra!\n");
                }
            }else if(op==7){
                System.exit(0);
            } else{
                System.out.printf("Valor Inválido.");
            }
        }
    }
}