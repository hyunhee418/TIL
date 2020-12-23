package example01;

public class VarEx01 {

	public static void main(String[] args) {
		
		char ch ='A';
		int year = 0;
		int age = 29;
		// 아래 코드에서는 L는 long타입을 지정하기 위해서 접미사 L, l을 붙였다.
		long result = 10L;
		// 아래 코드에서는 F는 float를 지정하기 위해서 접미사 F,f를 붙였다.
		float result2 = 10.1F;
		double d = 9.999;
		
		System.out.println("ch : " + ch);
		System.out.println(result);
		System.out.println(result2);
		System.out.println(d);
		System.out.println(year + age);
		// class. 정적 field . 메서드
		// sys를 치고 Ctrl + space를 누르면 자동완성 기능 실행
		// 인텔리전스(Intelligence) 기능
		
		String str = new String("자바다");
		System.out.println(str + "헿ㅎ");
		System.out.println(str.toString());
		
		// 사용자 정의 클래스이거나 toString() 재정의를 하지 않은
		// 클래스의 참조변수는 출력을 하게 되면,
		// 클래스타입 @16진수(주소)
		Object obj1 = new Object();
		System.out.println(obj1 + "자바");
	}

}
