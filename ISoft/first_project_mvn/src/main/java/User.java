import com.google.common.base.Preconditions;

import java.util.StringTokenizer;

import static com.google.common.base.Preconditions.*;

public class User {

    //state
    private final String id;

    private final String firstName;
    private final String lastName;

    private Age age;

    //constructors
    public User(String id, String firstName, String lastName){
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    //behavior



    public String getId() {
        return id;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public Age getAge() {
        return age;
    }

    public void setAge(Age age) {
        this.age = age;
    }
}
