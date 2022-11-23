package com.theos.threads;

import com.theos.building.elevator.Elevator;

public class ElevatorMovingThread extends Thread{
    private int elevatorSpeed;
    private int elevatorDoorsSpeed;

    public ElevatorMovingThread(Elevator elevator) {
        this.elevatorSpeed = elevator.getTimeBetweenFloors();
        this.elevatorDoorsSpeed = elevator.getTimeOpensDoors();
    }

    public void run() {

    }
}
