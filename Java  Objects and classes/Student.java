

class Student{

   private String firstName;
   private String middleName;
   private String lastName;

   public void setNames(String first, String middle, String last){
   
      firstName = first;
      middleName = middle;
      lastName = last;
   
   }
   public String getFullName(){
   
      String fName = firstName +" "+ middleName.charAt(0)+". "+lastName;
      return fName;
   
   
   }











}