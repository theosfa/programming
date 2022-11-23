
# IsSoft Final Task
<h2>Algoritm:</h2>
First of all we have class Building, that has PeopleGeneratingThread<br>
in it's constructor. This thread generates people on random floor with random<br>
mass and random target floor in random time, that differs from 1 to 5 secs.<br> 
Than when we are sure that current floor differs than target floor we can <br>
add person to the queue on his spawnable floor.<hr>
All floors starts there own thread called FloorButtonClickedThread that checking<br>
is there any person in the queue and if someone spawned calls Button function clicked()<br>
This function will call nearest or empty elevator<hr>
Function for searching best elevator called searchClosestElevator() and located<br>
in Building class. It will get current floor and button pressed state as parameters.<br>
This function searches elevator through elevators array that located in building<br>
object. As variables it has bestElevatorIndex distanceBetween. It ckecks<br>
elevatorState that should be the same as button state or be AWAITING,<br>
that means that elevator doesn't moving at all. Also it checks distance<br>
between elevator and current floor, and is there any valid space for another<br>
person. When suitable elevator found it adds floor number to the elevator<br>
targetFloors array and launch ElevatorMovingThread with UP or DOWN state as<br>
parameter if elevator has AWAITING state.<hr>
ElevatorMovingThread is responsible for elevator's movement logic.