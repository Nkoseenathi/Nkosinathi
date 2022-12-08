public class Food{

public String menuItemNumber;
private String size;
private String type;

public Food (String itemNo,String size,String type){

   menuItemNumber = itemNo;
   this.size = size;
   this.type = type;


}

public String toString(){

return type+": "+menuItemNumber+","+size;

}











}