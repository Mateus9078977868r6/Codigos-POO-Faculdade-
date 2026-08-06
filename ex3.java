//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
void main() {
    //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
    // to see how IntelliJ IDEA suggests fixing it.
    Scanner scanner = new Scanner(System.in);
    float[][] venda = new float[5][4];
    float total_mes=0;
    float[] total_ind = new float[5];
    float[] total_sem = new float[4];

    for(int i=0;i<5;i++) {
        for(int j=0;j<4;j++) {
            System.out.printf("Vendedor %d Digite o quanto você arrecadou na %d° semana: \n", i+1,j+1);
            venda[i][j] = scanner.nextFloat();
        }
    }
    for(int i=0;i<5;i++) {
        for(int j=0;j<4;j++) {
            total_mes = total_mes + venda[i][j];
        }
    }

    for(int j=0;j<4;j++) {
        for(int i=0;i<5;i++) {
            total_sem[j] = total_sem[j] + venda[i][j];
        }
        System.out.printf("Na semana %d venderam no total: R$ %.2f\n",j+1,total_sem[j]);
    }

    for(int i=0;i<5;i++) {
        for(int j=0;j<4;j++) {
            total_ind[i] = total_ind[i] + venda[i][j];
        }
        System.out.printf("O Vendedor %d vendeu no total: R$ %.2f\n",i+1,total_ind[i]);
    }

    System.out.printf("Total de venda no mês: R$ %.2f\n",total_mes);
}
