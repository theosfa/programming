package com.theos.building.floor;

import com.theos.person.Person;

import static com.theos.building.floor.ButtonState.DOWN;
import static com.theos.building.floor.ButtonState.UP;
import static java.lang.Thread.sleep;

public class Button {
    public Button() {
    }

    public void clicked(ButtonState buttonState, Floor floor) {
        Person person = null;
        if (buttonState == UP) {
            System.out.println("Button UP pressed on the " + floor.getNumber() + " floor");
            person = floor.deletingFirstPersonFromTheUpQueue();
        }
        if (buttonState == DOWN) {
            System.out.println("Button DOWN pressed on the " + floor.getNumber() + " floor");
            person = floor.deletingFirstPersonFromTheDownQueue();
        }
        try {
            sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Person with mass " + person.getMass() + " and target floor " + person.getTargetFloor());

    }
}
