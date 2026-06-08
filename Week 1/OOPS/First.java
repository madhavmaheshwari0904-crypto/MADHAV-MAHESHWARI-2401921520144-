public interface LibraryUser {
    void registerAccount();
    void requestBook();
}
public class KidUsers implements LibraryUser {
    int age;
    String bookType;
    public KidUsers() {}
    public KidUsers(int age, String bookType) {
        this.age = age;
        this.bookType = bookType;
    }
    @Override
    public void registerAccount() {
        if (age < 12) {
            System.out.println("You have successfully registered under a Kids Account");
        } else if (age > 12) {
            System.out.println("Sorry, Age must be less than 12 to register as a kid");
        }
    }

    @Override
    public void requestBook() {
        if ("Kids".equals(bookType)) {
            System.out.println("Book Issued successfully, please return the book within 10 days");
        } else {
            System.out.println("Oops, you are allowed to take only kids books");
        }
    }
}
public class AdultUser implements LibraryUser {
    int age;
    String bookType;
    public AdultUser() {}
    public AdultUser(int age, String bookType) {
        this.age = age;
        this.bookType = bookType;
    }
    @Override
    public void registerAccount() {
        if (age > 12) {
            System.out.println("You have successfully registered under an Adult Account");
        } else if (age < 12) {
            System.out.println("Sorry, Age must be greater than 12 to register as an adult");
        }
    }

    @Override
    public void requestBook() {
        if ("Fiction".equals(bookType)) {
            System.out.println("Book Issued successfully, please return the book within 7 days");
        } else {
            System.out.println("Oops, you are allowed to take only adult Fiction books");
        }
    }
}
public class LibraryInterfaceDemo {
    public static void main(String[] args) {
        System.out.println("--- Test Case #1: Kid User ---");
        KidUsers kid1 = new KidUsers();
        kid1.age = 10;
        kid1.bookType = "Kids";
        kid1.registerAccount();
        kid1.requestBook();
        
        System.out.println();
        KidUsers kid2 = new KidUsers();
        kid2.age = 18;
        kid2.bookType = "Fiction";
        kid2.registerAccount();
        kid2.requestBook();
        System.out.println("--- Test Case #2: Adult User ---");
        AdultUser adult1 = new AdultUser();
        adult1.age = 25;
        adult1.bookType = "Fiction";
        adult1.registerAccount();
        adult1.requestBook();

        System.out.println();
        AdultUser adult2 = new AdultUser();
        adult2.age = 5;
        adult2.bookType = "Kids";
        adult2.registerAccount();
        adult2.requestBook();
    }
}
    
