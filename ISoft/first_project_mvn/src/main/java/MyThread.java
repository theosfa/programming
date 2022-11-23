import javax.swing.text.View;
import java.util.Random;


public class MyThread extends Thread {
    private int randomFloor;
    private int randomMass;
    private int randomTargetFloor;
    private Random random = new Random();

    public void run() {
        for (int i = 0; i < 5; i ++) {
            randomFloor = random.nextInt(3) + 1;
            randomMass = random.nextInt(60) + 20;
            randomTargetFloor = random.nextInt(3) + 1;
            System.out.println(randomFloor + " " + randomMass + " " + randomTargetFloor);
            while(randomTargetFloor == randomFloor){
                randomTargetFloor = random.nextInt(3) + 1;
            }
            System.out.println(randomFloor + " " + randomMass + " " + randomTargetFloor);
            try {
                sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }
    }
}
