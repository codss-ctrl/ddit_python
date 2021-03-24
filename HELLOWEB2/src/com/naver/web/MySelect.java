package com.naver.web;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

public class MySelect {
	public static void main(String[] args) throws Exception {
		
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "select s_code,s_name,cprice,in_time from stock where s_name='»ï¼ºÀüÀÚ'";

		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		ResultSet rs = stmt.executeQuery(sql);
		while (rs.next()) {
			String s_code = rs.getString("s_code");
			String s_name = rs.getString("s_name");
			String cprice = rs.getString("cprice");
			String in_time = rs.getString("in_time");
			
			System.out.print("s_code:"+s_code);
			System.out.print("s_name:"+s_name);
			System.out.print("cprice:"+cprice);
			System.out.println("in_time:"+in_time);

		}
		
		stmt.close();
		conn.close();

	}
}




