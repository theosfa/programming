import com.theos.building.Building;
import com.theos.threads.AllFloorsSpectatingThread;
import com.theos.threads.PeopleGeneratingThread;


import java.sql.Array;
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

import static com.theos.building.elevator.Elevator.generateElevator;
import static com.theos.building.floor.Floor.generateFloor;
import static java.lang.Thread.sleep;

public class Runner {

    public static void main(String[] args) throws InterruptedException {

        Building building = new Building(3, 1);
        System.out.println(building);
        AllFloorsSpectatingThread allFloorsSpectatingThread = new AllFloorsSpectatingThread(building);
    }

}
