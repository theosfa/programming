package com.theos.building.elevator;


import com.theos.building.floor.ButtonState;
import com.theos.building.floor.Floor;
import com.theos.person.Person;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

import static com.theos.building.elevator.State.*;
import static java.lang.Thread.sleep;

public class Elevator {

    private final int maxWeight;
    private int currentFloor;
    private State state;
    private int timeBetweenFloors = 1000;
    private int timeOpensDoors = 500;
    private ArrayList<Integer> finalFloor = new ArrayList<>();
    private int availableWeight;
    private ArrayList<Person> listOfPersons = new ArrayList<>();

    private Elevator(int maxWeight) {
        this.maxWeight = maxWeight;
        this.currentFloor = 1;
        this.state = AWAITING;
        this.availableWeight = maxWeight;
    }

    public static Elevator generateElevator(int weight) {
        return new Elevator(weight);
    }

    public int getTimeOpensDoors() {
        return timeOpensDoors;
    }

    public int getMaxWeight() {
        return maxWeight;
    }

    public int getAvailableWeight() {
        return availableWeight;
    }

    public int getCurrentFloor() {
        return currentFloor;
    }

    public State getState() {
        return state;
    }

    public int getTimeBetweenFloors() {
        return timeBetweenFloors;
    }

    public ArrayList<Integer> getFinalFloor() {
        return finalFloor;
    }

    public void addFinalFloor(int finalFloor) {
        this.finalFloor.add(finalFloor);
    }

    public void moveOneFloorUp() {
        this.currentFloor++;
        this.state = UP;
        try {
            sleep(timeBetweenFloors);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    public void moveOneFloorDown() {
        this.currentFloor--;
        this.state = DOWN;
        try {
            sleep(timeBetweenFloors);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void openDoors() {
        try {
            sleep(timeOpensDoors);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void closeDoors() {
        try {
            sleep(timeOpensDoors);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void takePassanger(Floor floor, ButtonState buttonState) {
        if (buttonState == ButtonState.UP){
            int mass = floor.getMassOfFirstPersonFromQueueUp();
            if (availableWeight >= mass) {
                listOfPersons.add(floor.deletingFirstPersonFromTheUpQueue());
                availableWeight -= mass;
            }
        } else if (buttonState == ButtonState.DOWN){
            int mass = floor.getMassOfFirstPersonFromQueueDown();
            if (availableWeight >= mass) {
                listOfPersons.add(floor.deletingFirstPersonFromTheDownQueue());
                availableWeight -= mass;
            }
        }
    }
    
    public void removePassengerToFloor() {
        for (Person person: listOfPersons) {
            if (person.getTargetFloor() == currentFloor){
                listOfPersons.remove(person);
            }
        }
    }

}
