package example03;

public class StringEqualsEx {

	public static void main(String[] args) {
		// 참조형 타입 ==, !=에 대해 이해하기
		
		String str1 = "자바";
		String str2 = "자바";
		String str3 = new String("자바");
		
//		참조형 타입에서 서로 ==는 주소를 비교하고 있습니다.
		boolean result = (str1 == str2);
		System.out.println("str1 == str2 : " + result);
		
		result = (str1 == str3);
		System.out.println("str1 == str3 : " + result);

//		String 클래스의 equals()는 주소와 상관없이 값이 같다면, 
//		무조건 true를 리턴함.
		result = str1.equals(str3);
		System.out.println("str1.equals(str3) : " + result);
	
	}
}
