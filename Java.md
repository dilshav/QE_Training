**Java**



* What is java? features of java.
* JVM,JRE, JDK
* class/file name should be same
* requirements for java- pom.xml file. We are going to use maven. Maven archtypes. 
* eclipse. create simple proj. skip archtype. so blank pom
* com.ibm - group id- org name
* artifact is - project name - anything we give
* pom.xml file -project object model

<properties>

&#x09;<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>

&#x09;<maven.compiler.source>25</maven.compiler.source>

&#x09;<maven.compiler.target>25</maven.compiler.target>

</properties>

* src/main/recources - resources for developers

src/test/java- testers

src/test/resources - resources for testers

src/main- main file for developers



* Variables - datatypes -primitive and non-primitive



* &#x09;
* <dataType> <variableName> = <value>;
* Immplicit and explicit typecast - highest precedence for String, int(larger to smallest)
* String manipulation, string is immutable- means the new one will be created and it will be pointed but the old one still remains
* Operators: Arithmetic, assignment, comparison, bitwise, logical
* Control Flow statements- if, else if, else, switch(Pattern Matching - lambda operator)

&#x09;

static String describeNumber(Number n) {

&#x20;   // Switch with guarded patterns(when)

&#x20;   String result = switch (n) {

&#x20;       case null                         -> "null";

&#x20;       case Integer i when i >= 0        -> "positive int: " + i;

&#x20;       case Integer i                    -> "negative int: " + i;

&#x20;       case Long l when l > 1\_000\_000    -> "big long: " + l;

&#x20;       case Long l                       -> "long: " + l;

&#x20;       default                           -> "other number: " + n;

&#x20;   };

&#x20;   

&#x20;   return result;

}



* Loops -for, while, do while, enhanced for(when an iterator is used you want to safely access ...?, when speed is needed we use for each loop)

public class forEachLoop {

&#x20;   public static void main(String args\[]) {

&#x20;       String array\[] = {"Ron", "Harry", "Hermoine"};

&#x20;       //enhanced for loop

&#x20;       for (String x:array) {

&#x20;           System.out.println(x);

&#x20;       }

&#x20;   }

}



* Arrays : String\[] carMake = {"BMW", "AUDI"} - once initialized cannot add or remove values, can modify elements

String\[] carMake = new String\[2];

carMake\[0] = "BMW";

carMake\[1] = "AUDI"; - older version



arr.length; - length is property not function



actual and formal parameters

int\[] num = 10;

Print array without loop(converts array to string): Arrays.toString(num)



* Loops : While : entry control loop
* Do while: exit control loop - dead
* Objects, classes, constructors(keywords like this, final, static)
* java uses right to left for assigning: List<Integer> numList = new ArrayList<>(); // this is array;list
* Inheritance - types
* Abstraction - omitting the info and letting child class show how to do. - has abstract and concrete methods
* Interfaces - methods are abstract by default, public and static by default, variables are final and static
* Encapsulation - 
* Access Modifiers - calsses and interface cannot be private, class can be protective
* Polymorphism - overloading, overriding
* Exception Handling



public class Activity1 {



&#x20;   public static void main(String\[] args) {

&#x20;       Car toyota = new Car();

&#x20;       toyota.make = 2014;

&#x20;       toyota.color = "Black";

&#x20;       toyota.transmission = "Manual";

&#x20;   

&#x20;       //Using Car class method

&#x20;       toyota.displayCharacterstics();

&#x20;       toyota.accelerate();

&#x20;       toyota.brake();

&#x20;   }



}



public class Car {

&#x20;   //Class Member Variables

&#x20;   String color;

&#x20;   int make;

&#x20;   String transmission;

&#x20;   int tyres;

&#x20;   int doors;

&#x09;

&#x20;   //Constructor

&#x20;   Car() {

&#x09;tyres = 4;

&#x09;doors = 4;

&#x20;   }



&#x20;   //Class Methods

&#x20;   public void displayCharacterstics(){

&#x09;System.out.println("Color of the Car: " + color);

&#x09;System.out.println("Make of the Car: " + make);

&#x09;System.out.println("Transmission of the Car: " + transmission);

&#x09;System.out.println("Number of doors on the car: " + doors);

&#x20;   	System.out.println("Number of tyres on the car: " + tyres);

&#x20;   }



&#x20;   public void accelerate() {

&#x09;System.out.println("Car is moving forward.");

&#x20;   }

&#x09;

&#x20;   public void brake() {

&#x09;System.out.println("Car has stopped.");

&#x20;   }

}











import java.util.\*;



public class Activity2 {

&#x20;   public static void main(String\[] args) {

&#x20;       //Initialize the array

&#x20;       int\[] numArr = {10, 77, 10, 54, -11, 10};

&#x20;       System.out.println("Original Array: " + Arrays.toString(numArr));

&#x20;       

&#x20;       //Set constants

&#x20;       int searchNum = 10;

&#x20;       int fixedSum = 30;



&#x20;       //Print result

&#x20;       System.out.println("Result: " + result(numArr, searchNum, fixedSum));

&#x20;   }



&#x20;   public static boolean result(int\[] numbers, int searchNum, int fixedSum) {

&#x20;       int temp\_sum = 0;

&#x20;       //Loop through array

&#x20;       for (int number : numbers) {

&#x20;           //If value is 10

&#x20;           if (number == searchNum) {

&#x20;               //Add them

&#x20;               temp\_sum += searchNum;

&#x20;           }



&#x20;           //Sum should not be more than 30

&#x20;           if (temp\_sum > fixedSum) {

&#x20;               break;

&#x20;           }

&#x20;       }



&#x20;       //Return true if condition satisfies

&#x20;       return temp\_sum == fixedSum;

&#x20;   }

}





https://www.springjavalab.com/2025/12/java-switch-expressions-pattern-matching-cleaner-code-guide.html







* Create a class named Activity3.

Create a method named adjustDevice(String device, int value). This function returns a String status.

The status value is set using a Switch-case with pattern matching with the following matches:

device is THERMOSTAT and value is 40  and above: Print: \[Thermostat] Warning: Temperature high.



device is THERMOSTAT and value is under40: Print: \[Thermostat] Temperature is set to <value>.



device is LIGHT: Print: \[Light] Adjusting brightness to <value>%.



Null Safety: Explicitly handle null case as well.









Switch - order -> null, standard, default

package activities;



public class Activity3 {



&#x09;public static void main(String\[] args) {

&#x09;	// TODO Auto-generated method stub

&#x09;	Activity3 obj= new Activity3();

&#x09;	System.out.println(obj.adjustDevice("THERMOSTAT",32));

&#x09;	System.out.println(obj.adjustDevice("LIGHT",42));

&#x09;	



&#x09;}

&#x09;

&#x09;public static String adjustDevice(String device, int value) {

&#x09;	String status =switch (device){

&#x09;	case null -> "Invalid device typr";

&#x09;	case String d when d.equals("THERMOSTAT") \&\& value>40 ->"Thermostat Warning: Temperature High";

&#x09;	case "THERMOSTAT" -> "Thermostat temperature is set to "+value;

&#x09;	case "LIGHT" -> "\[Light] Adjusting brightness to "+value+"%.";

&#x09;	default -> "Unknown device given";

&#x09;	};

&#x09;	return status;

&#x09;}



}



import java.util.Arrays;



class Activity4 {

&#x20;   static void ascendingSort(int array\[]) {

&#x20;       // Sorting logic

&#x20;       for (int i = 1; i < array.length; i++) {

&#x20;           int key = array\[i]; // Assign key

&#x20;           int j = i - 1; // Assign value to compare with

&#x20;           

&#x20;           while (j >= 0 \&\& key < array\[j]) {

&#x20;               // Swap if key is smaller

&#x20;               array\[j + 1] = array\[j];

&#x20;               j--;

&#x20;           }

&#x20;           // Move key to the next value

&#x20;           array\[j + 1] = key;

&#x20;       }

&#x20;   }

&#x20;   

&#x20;   public static void main(String args\[]) {

&#x20;       // Unsorted array

&#x20;       int\[] data = { 9, 5, 1, 4, 3 };

&#x20;       // Pass the unsorted array to the sorting function

&#x20;       ascendingSort(data);

&#x20;       // Print sorted array

&#x20;       System.out.println("Sorted Array in Ascending Order: ");

&#x20;       System.out.println(Arrays.toString(data));

&#x20;   }

}













