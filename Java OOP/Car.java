public class Car extends Vehicle{


 private String color;
 private int doors;
 private int passangers;
 
 public Car(String color,int doors,int passangers){
 
   super(passangers,color);
   this.color = color;
   this.doors = doors;
   this.passangers = passangers;
 
 }



    public String toString() {
        return color + " " + passangers + " passengers "+doors+" doors";
    }







}