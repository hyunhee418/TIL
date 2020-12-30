package example03;

public class AssignOperEx {

	public static void main(String[] args) {
		// 복합대입 연산자를 이해하자
		
		int result  = 0;
		
		// 복합대입 연산자는 값을 누적시킬 때 사용
		result += 10; // result = result + 10
		System.out.println("result : " + result);
		
		result -= 5; // result = result - 5
		System.out.println("result : " + result);

		result *= 5; // result = result * 5
		System.out.println("result : " + result);
		
		result /= 5; // result = result / 5
		System.out.println("result : " + result);
		
		result %= 5; // result = result % 5
		System.out.println("result : " + result);
		
	}

}
