package example01;

public class VarEx01 {

	public static void main(String[] args) {
		
		char ch ='A';
		int year = 0;
		int age = 29;
		// �Ʒ� �ڵ忡���� L�� longŸ���� �����ϱ� ���ؼ� ���̻� L, l�� �ٿ���.
		long result = 10L;
		// �Ʒ� �ڵ忡���� F�� float�� �����ϱ� ���ؼ� ���̻� F,f�� �ٿ���.
		float result2 = 10.1F;
		double d = 9.999;
		
		System.out.println("ch : " + ch);
		System.out.println(result);
		System.out.println(result2);
		System.out.println(d);
		System.out.println(year + age);
		// class. ���� field . �޼���
		// sys�� ġ�� Ctrl + space�� ������ �ڵ��ϼ� ��� ����
		// ���ڸ�����(Intelligence) ���
		
		String str = new String("�ڹٴ�");
		System.out.println(str + "�m��");
		System.out.println(str.toString());
		
		// ����� ���� Ŭ�����̰ų� toString() �����Ǹ� ���� ����
		// Ŭ������ ���������� ����� �ϰ� �Ǹ�,
		// Ŭ����Ÿ�� @16����(�ּ�)
		Object obj1 = new Object();
		System.out.println(obj1 + "�ڹ�");
	}

}
