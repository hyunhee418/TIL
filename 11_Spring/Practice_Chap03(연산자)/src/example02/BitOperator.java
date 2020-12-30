package example02;

public class BitOperator {

	public static void main(String[] args) {
		
		int x = -8;
		int y = -5;
		
		System.out.println("x를 2진수로 변환한 결과 : " + Integer.toBinaryString(x));
		System.out.println("y를 2진수로 변환한 결과 : " + Integer.toBinaryString(y));
		
		System.out.println("x와 y 비트 & 연산 결과 : " + (x & y));
		System.out.println("x와 y 비트 | 연산 결과 : " + (x | y));
		System.out.println("x와 y 비트 베타적 논리합(XOR) 연산 결과 : " + (x ^ y));
		
	}

}
