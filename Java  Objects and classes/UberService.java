class UberService{

   private String name;
   private int costPerMin;
   private int costPerKM;
   private int baseFee;
   private int cancellationFee;


   void setDetails(String name, int costPerMin, int costPerKM, int baseFee, int cancellationFee){
   // Set the details of this service to the given values
      this.name = name;
      this.costPerMin = costPerMin;
      this.costPerKM = costPerKM;
      this.baseFee = baseFee;
      this.cancellationFee = cancellationFee;
   
   
   }

   void setName(String name){
   // Set the service name
      this.name = name;
   }

   String getName(){
   // Obtain the service name.
      return name;
   
   }

   void setCostPerMinute(int cents){
   // Set the cost per minute
      costPerMin = cents;
   
   }

   int getCostPerMinute(){
   // Set the cost per minute in cents.
      return costPerMin;
   
   }

   void setCostPerKilometre(int cents){
   // Set the cost per kilometre.
      costPerKM = cents;
   
   }

   int getCostPerKilometre(){
   // get the cost per kilometre in cents.
      return costPerKM; 
      
   }

   void setBaseFare(int cents){
   // Set the base fare.
      baseFee = cents;
   
   }

   int getBaseFare(){
   // get the base fare in cents.
   
      return baseFee;
   
   }

   void setCancellationFee(int n){
   // Set the cancellation fee.
      cancellationFee = n;
   
   }

   int getCancellationFee(){
   // Obtain the cancellation fee in cents for this service
      return cancellationFee;
   
   }

   double calculateFare(double minutes, double distance){
      // Obtain the fare (in the form of a real number of cents) for a journey of the
      // given time and distance
     // base fare + cost for minutes + cost for distance
      return (baseFee + costPerMin*minutes + costPerKM*distance);
      
   }

}