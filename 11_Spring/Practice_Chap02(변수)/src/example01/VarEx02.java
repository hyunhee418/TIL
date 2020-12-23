package example01;

public class VarEx02 {

	public static void main(String[] args) {
		
		
		int number; // 4바이트 만큼 변수를 메모리(스택)를 할당
		number = 200;
		int number2 = 500; // 선언과 동시에 초기화
		int num = 65;
		

		System.out.println(number); 
		System.out.println(number2);
		
		String str = new String("옹돌꾸");
		System.out.println(str);
		// null은 '없다'
		str = null;
		System.out.println(str);
	}

}
