public class Tarefa {
    String description;
    Boolean realized;

    public Tarefa(String description){
        this.description = description;
        this.realized = false;
    }

    public String getDescription(){
        return description;
    }

    public Boolean getRealized(){
        return realized;
    }
    public void setRealized(Boolean realized) {
        this.realized = realized;
    }
    @Override
    public String toString() {
        if (realized) {
            return "[X] " + description;
        } else {
            return "[ ] " + description;
        }
    }
}
