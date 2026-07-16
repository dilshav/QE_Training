#### **UAML diagram**



Exercise 1:

The Setup: A user wants to withdraw money. The machine starts at the Idle screen. 

Once a card is inserted, it moves to the PIN Entry state. If the user enters the correct PIN, 

it moves to the Account Access state, where they can choose to withdraw money. After cash is dispensed, 

or if the user cancels at any point, the machine returns to Idle.



State Transitions:

Current State  | Event (Action)         | Next State

Idle           | Insert Card            | PIN Entry

PIN Entry      | Enter Correct PIN      | Account Access

PIN Entry      | Cancel                 | Idle

Account Access | Select Cash \& Dispense | Idle

Account Access | Cancel                 | Idle

Create a State Transition diagram for the above table.





Exercise 2:

The Setup: A smart microwave starts in a Standby state. Opening the door shifts it to the Door Open state. Closing the door brings it back to Standby. From Standby, pressing the "30 Seconds" button puts it into the Cooking state. If the timer hits zero, it alerts the user and goes back to Standby. If the user presses "Stop" while it is cooking, it shifts to Paused. From Paused, pressing "Stop" again clears the timer and resets it to Standby.



State Transitions:

Current State | Event (Action)  | Next State

Standby       | Open Door       | Door Open

Door Open     | Close Door      | Standby

Standby       | Press "30 Sec"  | Cooking

Cooking       | Timer Reaches 0 | Standby

Cooking       | Press "Stop"    | Paused

Paused        | Press "Stop"    | Standby

