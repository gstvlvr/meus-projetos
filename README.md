import java.util.Scanner;

public class wVotos {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int voto;
        int votosJair = 0, votosCarlos = 0, 
        votosNeves = 0, votosNulos = 0, 
        votosBrancos = 0, totalVotos = 0;

        do {
            System.out.println("\nUrna Eletrônica");
            System.out.println("As opções são:");
            System.out.println("1. Candidato Jair Rodrigues");
            System.out.println("2. Candidato Carlos Luz");
            System.out.println("3. Candidato Neves Rocha");
            System.out.println("4. Nulo");
            System.out.println("5. Branco");
            System.out.println("6. Encerrar votação");
            System.out.print("Entre com o seu voto: ");
            voto = sc.nextInt();

            switch (voto) {
                case 1:
                    votosJair++;
                    break;
                case 2:
                    votosCarlos++;
                    break;
                case 3:
                    votosNeves++;
                    break;
                case 4:
                    votosNulos++;
                    break;
                case 5:
                    votosBrancos++;
                    break;
                case 6:
                    System.out.println("Encerrando votação...");
                    break;
                default:
                    System.out.println("Voto inválido! Tente novamente.");
            }
            if (voto >= 1 && voto <= 5) {
                totalVotos++;
            }
        } while (voto != 6);
         // Calcular porcentagens
         float porcentagemNulos = (votosNulos / (float) totalVotos) * 100;
         float porcentagemBrancos = (votosBrancos / (float) totalVotos) * 100;
 
         // Determinar o vencedor
         String vencedor;
         if (votosJair > votosCarlos && votosJair > votosNeves) {
             vencedor = "Candidato Jair Rodrigues";
         } else if (votosCarlos > votosJair && votosCarlos > votosNeves) {
             vencedor = "Candidato Carlos Luz";
         } else if (votosNeves > votosJair && votosNeves > votosCarlos) {
             vencedor = "Candidato Neves Rocha";
         } else {
             vencedor = "Empate";
         }
 
         // Exibir resultados
         System.out.println("\nResultado da votação:");
         System.out.println("Votos para Jair Rodrigues: " + votosJair);
         System.out.println("Votos para Carlos Luz: " + votosCarlos);
         System.out.println("Votos para Neves Rocha: " + votosNeves);
         System.out.println("Votos nulos: " + votosNulos + " (" + porcentagemNulos + "%)");
         System.out.println("Votos brancos: " + votosBrancos + " (" + porcentagemBrancos + "%)");
         System.out.println("Candidato vencedor: " + vencedor);
 
         sc.close();

        

    }
    
}
