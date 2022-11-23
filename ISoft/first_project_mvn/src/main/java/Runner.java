import java.util.ArrayList;

import static java.lang.Thread.sleep;

public class Runner {

    public static void main(String[] args) {
        User u = new User("1", "Vasya", "Pupkin");

//        UserUpdateService.update

        u.setAge(new Age(30));
        final Age age = u.getAge();
//        MyThread myThread = new MyThread();
//        MyThread2 myThread2 = new MyThread2();
//        myThread.start();
//        myThread2.start();
//        for (int i = 0; i < 10; i++) {
//            System.out.println("Оосновной поток запущен");
//            try {
//                sleep(1000);
//            } catch (InterruptedException e) {
//                e.printStackTrace();
//            }
//        }

        ArrayList<String> floors = new ArrayList<String>();
        String[] floor = new String[3];
        floors.add("Hello");
        floors.add("it's");
        floors.add("me");
        floors.set(1,"No");
        System.out.println(floors.get(1));
    }
}
