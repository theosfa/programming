import static com.google.common.base.Preconditions.checkArgument;

public class Age {

    private final int val;

    public Age(int val){
        checkArgument( val >= 0, "Age must be positive");
        checkArgument( val <= 125, "Age must be <= 125");
        this.val = val;
    }

    public int intValue() {
        return val;
    }

    public Age incr(){
        return new Age(this.val);
    }
}
