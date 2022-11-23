import java.sql.SQLOutput;
import java.util.Random;
import java.util.Scanner;

public class LabRab2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Zadanie 1");
        System.out.println("Write down a");
        int a = scanner.nextInt();
        System.out.println("Write down b");
        int b = scanner.nextInt();
        System.out.println("Write down c");
        int c = scanner.nextInt();
        System.out.println("Write down d");
        int d = scanner.nextInt();
        boolean answerZadanieOne = zadanieOne(a, b, c, d);
        System.out.println("Answer for zadanie 1 is :" + answerZadanieOne);
        System.out.println("-------------------------------------------");
        System.out.println("Zadanie 2(while)");
        int[] answerTwoWhile;
        answerTwoWhile = zadanieTwoWhile();
        for (int i = 0; i < answerTwoWhile.length; i++) {
            if (answerTwoWhile[i] == 0){
                break;
            }
            System.out.println("Answer for zadanie(while) 2 is :" + answerTwoWhile[i]);
        }
        System.out.println("-------------------------------------------");
        System.out.println("Zadanie 2(for)");
        int[] answerTwoFor;
        answerTwoFor = zadanieTwoFor();
        for (int i = 0; i < answerTwoFor.length; i++) {
            if (answerTwoFor[i] == 0){
                break;
            }
            System.out.println("Answer for zadanie(for) 2 is :" + answerTwoFor[i]);
        }
        System.out.println("-------------------------------------------");
        System.out.println("Zadanie 3");
        System.out.println("Write down n");
        int n = scanner.nextInt();
        int answerThree = zadanieThree(n);
        System.out.println("Answer for zadanie 3 is :" + answerThree);
        System.out.println("-------------------------------------------");
        System.out.println("Zadanie 4");
        System.out.println("Write down columns");
        int column = scanner.nextInt();
        System.out.println("Write down lines");
        int lines = scanner.nextInt();
        int[][] A = new int[column][lines];
        for (int i = 0; i < column; i++) {
            for (int j = 0; j < lines; j++) {
                A[i][j] = scanner.nextInt();
            }
        }
        int[] answerFour;
        answerFour = zadanieFour(lines, column, A);
        for (int i = 0; i < column; i++) {
            System.out.println("Answer for zadanie 4 is :" + answerFour[i]);
        }
    }

    public static boolean zadanieOne(int a, int b, int c, int d){
        if ( a < b && b < c && c < d ){
            return true;
        }
        return false;
    }

    public static int[] zadanieTwoWhile(){
        int[] array = new int[10000];
        int index = 0;
        int n = 1000;
        int a = 0;
        int b = 0;
        int c = 0;
        int d = 0;
        while (n != 10000){
            a = n % 10;
            b = ((n - a) / 10) % 10;
            c = ((n - b*10 - a) / 100) % 10;
            d = n / 1000;
            if (a != b && a != c && a != d && b != c && b != d && c != d){
                array[index] = n;
                index++;
            }
            n++;
        }
        return array;
    }
    public static int[] zadanieTwoFor(){
        int[] array = new int[10000];
        int index = 0;
        int a = 0;
        int b = 0;
        int c = 0;
        int d = 0;
        for (int n = 1000; n < 10000; n++) {
            a = n % 10;
            b = ((n - a) / 10) % 10;
            c = ((n - b*10 - a) / 100) % 10;
            d = n / 1000;
            if (a != b && a != c && a != d && b != c && b != d && c != d){
                array[index] = n;
                index++;
            }
        }
        return array;
    }

    public static int zadanieThree(int n){
        int answer = 0;
        Random random = new Random();
        int[] array = new int[n];
        System.out.println("Array :");
        for (int i = 0; i < array.length; i++) {
            array[i] = random.nextInt(100);
            System.out.println(array[i]);
        }
        for (int i = 0; i < array.length; i++) {
            if (array.length / 2 > i){
                answer += array[i];
            }else{
                answer -= array[i];
            }
        }
        return answer;
    }

    public static int[] zadanieFour(int n, int m, int[][] array){
        int[] b = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                b[j] += array[i][j];
            }
        }
        return b;
    }
}
