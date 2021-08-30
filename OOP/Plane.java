public class Plane extends Vehicle{



 private String color;
 private int doors;
 private int passangers;
private String str; 
 public Plane(String color,int doors,String str,int passangers){
 
   super(passangers,color);
   this.color = color;
   this.doors = doors;
   this.passangers = passangers;
   this.str = str;
 
 }



    public String toString() {
        return color + " " + doors + " passengers "+str+" "+passangers;
    










}






}