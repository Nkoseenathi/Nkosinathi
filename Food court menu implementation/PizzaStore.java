import java.util.Scanner;

/**
 * Pizza store simulator
 */
public class PizzaStore {

    private static Food[] pieces;

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Welcome to Great International Food Court");
        String option;
        pieces = new Food[100];
        int index = 0;
        do {
	    int returnIndex = 0; 
            System.out.println("MENU: add (P)izza, add (C)urry, add (S)oft drink, (D)elete, (L)ist, (Q)uit");
            option = s.nextLine();
            if ("p".equalsIgnoreCase(option)) {
                System.out.println("Enter the menu item number");
                String serial = s.nextLine();
                System.out.println("Enter the size");
                String size = s.nextLine();
                System.out.println("Enter the base");
                String base = s.nextLine();
                System.out.println("Enter extra cheese");
                String cheese = s.nextLine();
                System.out.println("Enter extra garlic");
                String garlic = s.nextLine();
                pieces[index] = new Pizza(serial, size, base, cheese, garlic);
            } else if ("c".equalsIgnoreCase(option)) {
                System.out.println("Enter the menu item number");
                String serial = s.nextLine();
                System.out.println("Enter the size");
                String size = s.nextLine();
                System.out.println("Enter the curry type");
                String curryType = s.nextLine();
                pieces[index] = new Curry(serial, size, curryType);
            } else if ("s".equalsIgnoreCase(option)) {
                System.out.println("Enter the menu item number");
                String serial = s.nextLine();
                System.out.println("Enter the size");
                String size = s.nextLine();
                System.out.println("Enter the flavour");
                String flavour = s.nextLine();
                System.out.println("Enter whether it is a bottle or can");
                String bottleType = s.nextLine();
                pieces[index] = new SoftDrink(serial, size, flavour, bottleType);
            } else if ("d".equalsIgnoreCase(option)) {
                System.out.println("Enter the menu item number");
                String serial = s.nextLine();
                returnIndex = delete(serial);
            } else if ("l".equalsIgnoreCase(option)) {
                for (Food e: pieces) {
                    if (e!=null) {
                        System.out.println(e);
                    }
                }
            }
            if (!option.equalsIgnoreCase("q")) {
               if (returnIndex >= 0) {
                   System.out.println("Done");
               } else {
                  System.out.println("Not found");
 	       }
	    }
            index++;

        } while (!option.equalsIgnoreCase("q"));
    }

    private static int delete(String serial) {
        int deleteIndex = -1;
        for (int i = 0; i < pieces.length; i++) {
            if (pieces[i] != null && pieces[i].menuItemNumber.equals(serial)) {
                deleteIndex = i;
                break;
            }
        }
        if (deleteIndex >= 0) {
            pieces[deleteIndex] = null;
        }
	
	return deleteIndex;
    }
}
