package example01;

public class DenyEx {

	public static void main(String[] args) {
		
		boolean power = false;
		System.out.println("﻿power의 값 : " + power );
		
		power = !power;
		System.out.println("﻿power의 값 : " + power );
		
		power = !power;
		System.out.println("﻿power의 값 : " + power );

		if(!power) {
			System.out.println("if문이 실행됨");
	
		}
	}

}
