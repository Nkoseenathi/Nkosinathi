
public class SoftDrink extends Food{


private String itemNo;
private String size;
private String flavor;
private String bottleOrCan;


public SoftDrink(String itemNo,String size, String flavor,String bottleOrCan){

   super(itemNo, size,"Soft Drink");
   this.itemNo = itemNo;
   this.size = size;
   this.flavor = flavor;
   this.bottleOrCan = bottleOrCan;
   

}

public String toString(){

return "Soft Drink: "+itemNo+", "+size+", "+flavor+", "+bottleOrCan;

}

}