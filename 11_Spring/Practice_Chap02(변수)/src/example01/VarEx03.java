package example01;

public class VarEx03 {

	public static void main(String[] args) {
		
		byte b1 = 127;
		// byte b2 = b1 + 2;  // �����÷ο�
		byte b2 = (byte)(b1+2);
		System.out.println(b1);
		System.out.println("����ĳ���� �� : " + b2);
		
		int i  = (int)(b1+2);
		System.out.println("�ڵ�ĳ���� �� : " + i );
		
		byte b3 = 127;
		int i2 = 350;
		b3 = (byte)i2;
		System.out.println(b3);
		// looping�� ���ļ� ���� ��
		// ū ����Ʈ�� ���� ����Ʈ�� ���� ������ �ս� �߻�

		//������ �Ǽ����� ĳ���� (�����ϴ� ����� Ʋ���� ������ �ݵ�� ������ �ս�)
		// ��������� ĳ���� �ڵ尡 ������ 
		int i3 = 100;
		float f1 = (float)i3;
		System.out.println("���� -> �Ǽ� : " + f1);
		
		float f2 = 10.55f;
		int i4 = (int)f2;
		System.out.println("�Ǽ� -> ���� : " + i4);
		
		char ch = 'a';
		int i5 = ch;
		// ���� ���� ���� Ÿ������ �ٲٰ� �ǐ�
		// �ƽ�Ű �ڵ� ������ �ٲ���� ��� ��.
		System.out.println("���� -> ���� : " + i5);
		
		// any type + "" -> ���ڿ�
		int i6 = 100;
		String str = "�ڹ�" + i6;
		System.out.println(str);
	}

}
