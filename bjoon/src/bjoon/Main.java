package bjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Iterator;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] arr = new int[10];
		int cnt = 0;
		int res = 0;
		
		for (int i = 0; i <arr.length; i++) {
			arr[i] = Integer.parseInt(br.readLine())%42;
		}
		
		
		for (int i = 0; i < arr.length; i++) {
			cnt =0;
			for (int j = i + 1; j < 10; j++) {
				if (arr[i]==arr[j]) {
					cnt ++;
				}
			}
			 if (cnt == 0) {
				 res++;
	            }
			
		}
		System.out.println(res);
		br.close();
	}
}
