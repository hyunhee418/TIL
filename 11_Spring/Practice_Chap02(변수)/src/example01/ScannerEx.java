package example01;

import java.util.Scanner;

public class ScannerEx {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("���� ���ڸ��� �Է� : ");
		int num = sc.nextInt();
		System.out.println("����ڷκ��� �Է¹��� ���� : " + num);
		
		System.out.print("�Ǽ� ���ڸ��� �Է� : ");
		double dnum = sc.nextDouble();
		System.out.println("����ڷκ��� �Է¹��� ���� : " + dnum);
		
		System.out.print("���ڿ��� �Է� : ");
		String str = sc.next();
		String str1 = sc.nextLine();
		System.out.println("����ڷκ��� �Է¹��� ���ڿ� : " + str);
		
		int result = 100;
		String num2 = sc.nextLine();
		int temp = Integer.parseInt(num2);
		int total = result + temp;
		System.out.println("������ : " + total);
		
		sc.close();
	}

}
