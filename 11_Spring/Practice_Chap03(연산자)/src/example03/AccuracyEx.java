package example03;

public class AccuracyEx {

	public static void main(String[] args) {
		// CPU의 연산 오차를 확인해보기
		
		int apple = 1;
		double unit = 0.1;
		int number = 7;
		
		double result = apple - (number * unit);
		double result2 = (number * unit);
		
		System.out.println(result2);		
		
		System.out.println("사과 한 개에서");
		System.out.println("0.7 조각을 빼면");
		System.out.println(result + " 조각이 남는다.");
		
	}

}
