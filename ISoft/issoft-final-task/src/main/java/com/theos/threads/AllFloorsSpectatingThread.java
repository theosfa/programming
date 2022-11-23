package com.theos.threads;

import com.theos.building.Building;

public class AllFloorsSpectatingThread extends Thread{
    Building building;
    public AllFloorsSpectatingThread(Building building) {
        this.building = building;
        start();
    }

    public void run() {
        for (int i = 1; i < 10; i++) {
            System.out.println("Floor 1");
            if (!building.getFloors()[0].getQueueUp().isEmpty()){
                System.out.println("Queue up : " + building.getFloors()[0].getQueueUp().peek().getMass());
            }
            if (!building.getFloors()[0].getQueueDown().isEmpty()) {
                System.out.println("Queue down : " + building.getFloors()[0].getQueueDown().peek().getMass());
            }
            System.out.println("Floor 2");
            if (!building.getFloors()[1].getQueueUp().isEmpty()){
                System.out.println("Queue up : " + building.getFloors()[1].getQueueUp().peek().getMass());
            }
            if (!building.getFloors()[1].getQueueDown().isEmpty()) {
                System.out.println("Queue down : " + building.getFloors()[1].getQueueDown().peek().getMass());
            }
            System.out.println("Floor 3");
            if (!building.getFloors()[2].getQueueUp().isEmpty()){
                System.out.println("Queue up : " + building.getFloors()[2].getQueueUp().peek().getMass());
            }
            if (!building.getFloors()[2].getQueueDown().isEmpty()) {
                System.out.println("Queue down : " + building.getFloors()[2].getQueueDown().peek().getMass());
            }
            try {
                sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
