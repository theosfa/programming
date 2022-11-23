package com.theos.building;

import com.theos.building.elevator.Elevator;
import com.theos.building.floor.ButtonState;
import com.theos.building.floor.Floor;
import com.theos.person.Person;
import com.theos.threads.PeopleGeneratingThread;

import static com.theos.building.elevator.Elevator.generateElevator;
import static com.theos.building.floor.Floor.generateFloor;

public class Building {

    private int numberOfFloors;
    private int numberOfElevators;
    private int currentElevatorAddingIndex = 0;
    private int currentFloorAddingIndex = 0;
    private Floor[] floors;
    private Elevator[] elevators;

    public Building(int numberOfFloors, int numberOfElevators) {
        this.floors = new Floor[numberOfFloors];
        elevators = new Elevator[numberOfElevators];
        this.numberOfFloors = numberOfFloors;
        this.numberOfElevators = numberOfElevators;
        for (int i = 1; i < getNumberOfFloors()+1; i++){
            addFloor(generateFloor(i));
        }
        for (int i = 1; i < getNumberOfElevators()+1; i++){
            addElevator(generateElevator(150));
        }
        PeopleGeneratingThread peopleGeneratingThread = new PeopleGeneratingThread(this);
    }

    public void addPersonToTheFloor(int numberOfFloor, Person person) {
        floors[numberOfFloor-1].addingPersonToFloor(person);
    }
    public int getNumberOfFloors() {
        return numberOfFloors;
    }

    public int getNumberOfElevators() {
        return numberOfElevators;
    }

    public Floor[] getFloors() {
        return floors;
    }

    public Elevator[] getElevators() {
        return elevators;
    }

    public void addElevator(Elevator elevator) {
        elevators[currentElevatorAddingIndex] = elevator;
        currentElevatorAddingIndex++;
    }

    public void addFloor(Floor floor) {
        floors[currentFloorAddingIndex] = floor;
        currentFloorAddingIndex++;
    }

    public void checkClosestElevator(Floor floor, ButtonState buttonState) {

    }

}
