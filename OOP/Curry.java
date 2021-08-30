public class Curry extends Food{


private String itemNo;
private String size;
private String cType;


public Curry(String itemNo,String size, String cType){
   super(itemNo, size,"Curry");
   this.itemNo = itemNo;
   this.size = size;
   this.cType = cType;
   

}

public String toString(){

return "Curry: "+itemNo+", "+size+", "+cType;

}














}