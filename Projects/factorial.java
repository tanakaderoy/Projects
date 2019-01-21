import java.util.Random;

public class factorial {
    public static int fact(int n) {
    	//assuming n is positive int
    	if(n == 0) {
		return 1;
    	}else {
    		return n *fact(n-1);
    	}
    	
        
    }

	public static void main(String[] args) {
		Random generator = new Random(); 
		int i = generator.nextInt(10) + 1;
		System.out.println(fact(i));

	}

}
