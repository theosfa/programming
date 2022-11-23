package com.theos.threads;

import com.theos.building.Building;
import com.theos.person.Person;

import java.util.Random;

import static com.theos.person.Person.createPerson;

public class PeopleGeneratingThread extends Thread {
    private int randomFloor;
    private int randomMass;
    private int randomTargetFloor;
    private Random random = new Random();
    private int buildingsNumberOfFloors;
    private Building building;

    public PeopleGeneratingThread(Building building) {
        this.building = building;
        this.buildingsNumberOfFloors = building.getNumberOfFloors();
        start();
    }

    public void run() {
        for (int i = 0; i < 5; i ++) {
            randomFloor = random.nextInt(buildingsNumberOfFloors) + 1;
            randomMass = random.nextInt(60) + 20;
            randomTargetFloor = random.nextInt(buildingsNumberOfFloors) + 1;
            while(randomTargetFloor == randomFloor){
                randomTargetFloor = random.nextInt(buildingsNumberOfFloors) + 1;
            }
            building.addPersonToTheFloor(randomFloor, createPerson(randomMass, randomTargetFloor));
            try {
                //random.nextInt(4000)+
                sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }


}
