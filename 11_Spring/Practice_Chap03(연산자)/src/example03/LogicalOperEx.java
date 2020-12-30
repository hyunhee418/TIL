package example03;

public class LogicalOperEx {

	public static void main(String[] args) {
		// 논리연산자 (&&, || )에 대해 코드로 적용

		boolean result = false;
		int i = 10;
		char ch = 'b';
		
		result = (i > 5);
		System.out.println("(i>5) : " + result);

		result = (i >= 9) && (i < -8);
		System.out.println("(i >= 9) && (i < -8) : " + result);

		result = (i >= 9) || (i < -8);
		System.out.println("(i >= 9) || (i < -8) : " + result);

//		알파벳 소문자인지 확인하기
		result = (ch > 'a' && ch <= 'z'); 
		System.out.println("(ch > 'a' && ch <= 'z') : " + result);

//		ch에 저장되어진 값이 알파벳인지 확인하기
		result = (ch > 'a' && ch <= 'z') || (ch > 'A' && ch <= 'Z'); 
		System.out.println("알파벳 : " + result);
		
		
	}

}
