package example01;

import java.util.Scanner;

public class ScannerEx {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("정수 한자리를 입력 : ");
		int num = sc.nextInt();
		System.out.println("사용자로부터 입력받은 숫자 : " + num);
		
		System.out.print("실수 한자리를 입력 : ");
		double dnum = sc.nextDouble();
		System.out.println("사용자로부터 입력받은 숫자 : " + dnum);
		
		System.out.print("문자열을 입력 : ");
		String str = sc.next();
		String str1 = sc.nextLine();
		System.out.println("사용자로부터 입력받은 문자열 : " + str);
		
		int result = 100;
		String num2 = sc.nextLine();
		int temp = Integer.parseInt(num2);
		int total = result + temp;
		System.out.println("연산결과 : " + total);
		
		sc.close();
	}

}
