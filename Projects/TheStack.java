
import java.util.*;
public class TheStack{
		
		
		private String[] stackArray;
		private int stackSize;
		private int topOfStack = -1;
		TheStack(int size){
			stackSize = size;
			stackArray = new String[size];
			Arrays.fill(stackArray, "-1");
			
		}
		public void push(String input) {
			if(topOfStack + 1 < stackSize) {
				topOfStack++;
				stackArray[topOfStack] = input;
				
			}else {
				System.out.println("Sorry But the Stack is Full");
			}
			displayTheStack();
			System.out.println("PUSH " + input + "Was Added to the Stack");
		}
		public String pop() {
			if(topOfStack >= 0) {
				displayTheStack();
				System.out.println("POP " + stackArray[topOfStack] + " Was removed from the stack\n");
				stackArray[topOfStack] = "-1";
			}else {
				displayTheStack();
				return "-1";
			}
		}
		public String peek() {
			return stackArray[topOfStack];
		}
		
		public static void main(String[] args) {
			TheStack theStack = new TheStack(10);
			theStack.push("10");
			
			
		}
	}