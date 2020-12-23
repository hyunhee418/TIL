package example01;

public class VarEx03 {

	public static void main(String[] args) {
		
		byte b1 = 127;
		// byte b2 = b1 + 2;  // 오버플로우
		byte b2 = (byte)(b1+2);
		System.out.println(b1);
		System.out.println("강제캐스팅 후 : " + b2);
		
		int i  = (int)(b1+2);
		System.out.println("자동캐스팅 후 : " + i );
		
		byte b3 = 127;
		int i2 = 350;
		b3 = (byte)i2;
		System.out.println(b3);
		// looping을 거쳐서 나온 값
		// 큰 바이트가 작은 바이트로 가면 데이터 손실 발생

		//정수와 실수간의 캐스팅 (저장하는 방식이 틀리기 때문에 반드시 데이터 손실)
		// 명시적으로 캐스팅 코드가 들어가야함 
		int i3 = 100;
		float f1 = (float)i3;
		System.out.println("정수 -> 실수 : " + f1);
		
		float f2 = 10.55f;
		int i4 = (int)f2;
		System.out.println("실수 -> 정수 : " + i4);
		
		char ch = 'a';
		int i5 = ch;
		// 문자 값을 정수 타입으로 바꾸게 되먄
		// 아스키 코드 값으로 바뀌어져 출력 됨.
		System.out.println("문자 -> 정수 : " + i5);
		
		// any type + "" -> 문자열
		int i6 = 100;
		String str = "자바" + i6;
		System.out.println(str);
	}

}
