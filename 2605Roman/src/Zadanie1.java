import java.util.Scanner;

public class Zadanie1 {

    public static void main(String[] args) {
        int x = 0;
        int y = 0;
        int z = 0;
        int a = 0;
        int b = 0;
        double answerFunction = 0;
        double answerPerimetr = 0;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Write down x: ");
        x = scanner.nextInt();
        System.out.println("Write down y: ");
        y = scanner.nextInt();
        System.out.println("Write down z: ");
        z = scanner.nextInt();
        answerFunction = func(x, y, z);
        System.out.println("Answer is: " + answerFunction);

        System.out.println("Write down a: ");
        a = scanner.nextInt();
        System.out.println("Write down b: ");
        b = scanner.nextInt();
        answerPerimetr = perimetr(a, b);
        System.out.println("Answer is: " + answerPerimetr);

    }

    public static double func(int x, int y, int z){
        double answer = 0;
        answer = middle(x, y) + middle(y, z) + middle(z, x);
        return answer;
    }

    public static double middle(int x, int y){
        return (x + y)/y;
    }

    public static double perimetr(int a, int b){
        double c = Math.sqrt(a*a + b*b);
        return a + b + c;
    }
}
