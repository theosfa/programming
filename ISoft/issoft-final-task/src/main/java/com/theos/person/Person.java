package com.theos.person;

public class Person {

    private final int mass;
    private final int targetFloor;

    private Person(int mass, int targetFloor) {
        this.mass = mass;
        this.targetFloor = targetFloor;
    }

    public static Person createPerson(int mass, int targetFloor) {
        return new Person(mass, targetFloor);
    }

    public int getMass() {
        return mass;
    }

    public int getTargetFloor() {
        return targetFloor;
    }
}
