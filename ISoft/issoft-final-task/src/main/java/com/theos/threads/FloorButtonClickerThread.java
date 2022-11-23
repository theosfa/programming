package com.theos.threads;

import com.theos.building.floor.Button;
import com.theos.building.floor.Floor;

import static com.theos.building.floor.ButtonState.DOWN;
import static com.theos.building.floor.ButtonState.UP;


public class FloorButtonClickerThread extends Thread {

    private Floor floor;
    private final Button button = new Button();

    public FloorButtonClickerThread(Floor floor) {
        this.floor = floor;
        start();
    }

    public void run() {
        while(floor.getQueueDown().peek() != null || floor.getQueueUp().peek() != null) {
            if (floor.getQueueDown().peek() != null) {
                button.clicked(DOWN, floor);
            }
            if (floor.getQueueUp().peek() != null) {
                button.clicked(UP, floor);
            }
            try {
                sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

}
