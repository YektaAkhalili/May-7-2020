class ch9b{
	//remainder and quotient 
	public static void main(String[] args) {
		double quotient, remainder;
		final int DIVIDER = 3;
		quotient = 17/DIVIDER;
		remainder = 17%DIVIDER; 

		System.out.println("17/3, the quotient is: " + quotient);
		System.out.println("17/3, the remainder is: " + remainder);
		System.out.println("The original is: " + (quotient*DIVIDER + remainder));
		

	}
}
/*
The remainder operator can be used with negative integers. The rule is:

Perform the operation as if both operands were positive.
If the left operand is negative, then make the result negative.
If the left operand is positive, then make the result positive.
Ignore the sign of the right operand in all cases.


*/