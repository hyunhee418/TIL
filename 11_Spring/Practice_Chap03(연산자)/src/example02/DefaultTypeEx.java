package example02;

public class DefaultTypeEx {

	public static void main(String[] args) {
		
		byte b1 = 127;
		byte b2 = 1;
		char ch = 'A';
		float f1 = 15.5f;
		double d1 = 10.5;
		// byte b3 = b1 + b2;
		// byte + byte = int + int = int
		//1번 째 방법 : int 형으로 받아준다 (자동 캐스팅)
		//2번 째 방법 : 강제 캐스팅 해야 된다.
		int i1 = b1 + b2;
		byte b3 = (byte)(b1 + b2);
		int i2 = ch + b2;
		// 정수형 + 실수형 => 표현 범위가 넓은 쪽으로 형 변환 되어 연산됨
		float f2 = b1 + f1;
		double d2 = f1 + d1;
		System.out.println(i1 + ", " + b3 + ", " + i2 + ", " + f2 + ", " + d2);
	}

}
