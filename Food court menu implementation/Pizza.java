public class Pizza extends Food{


private String itemNo;
private String size;
private String eCheese;
private String eGarlic;
private String base;


public Pizza(String itemNo , String size, String base, String eCheese, String eGarlic){
   super(itemNo, size,"Pizza");
   this.itemNo = itemNo;
   this.size = size;
   this.eCheese = eCheese;
   this.eGarlic = eGarlic;
   this.base = base;
   

}

public String toString(){

return "Pizza: "+itemNo+", "+size+", "+base+", "+eCheese+", "+eGarlic;

}














}