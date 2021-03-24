package com.naver.web;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class StockDAO {
	public ArrayList<StockVO> myselect(String p_s_name) throws Exception{
		ArrayList<StockVO> list = new ArrayList<StockVO>();
		
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "select s_code,s_name,cprice,in_time from stock where s_name='"+p_s_name+"'";

		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		ResultSet rs = stmt.executeQuery(sql);
		while (rs.next()) {
			String s_code = rs.getString("s_code");
			String s_name = rs.getString("s_name");
			String cprice = rs.getString("cprice");
			String in_time = rs.getString("in_time");
			
			StockVO tempvo = new StockVO();
			tempvo.setS_code(s_code);
			tempvo.setS_name(s_name);
			tempvo.setCprice(cprice);
			tempvo.setIn_time(in_time);
			
			list.add(tempvo);
		}
		
		stmt.close();
		conn.close();
		
		return list;
	}
	
	public int myinsert(StockVO vo) throws Exception {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "insert into stock (s_code,s_name,cprice,in_time) values ('"+vo.getS_code()+"','"+vo.getS_name()+"','"+vo.getCprice()+"','"+vo.getIn_time()+"')";

		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		return cnt;
	}
	
	public int myupdate(StockVO vo) throws Exception {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "update stock set s_name='"+vo.getS_name()+"',cprice='"+vo.getCprice()+"',in_time='"+vo.getIn_time()+"' where s_code='"+vo.getS_code()+"'";

		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		return cnt;
	}
	
	public int mydelete(StockVO vo) throws Exception {
	
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "delete from stock where s_code='"+vo.getS_code()+"'";
	
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
	
		return cnt;
	}
	
	public static void main(String[] args) throws Exception {
		StockDAO dao = new StockDAO();
		
		
		StockVO vo = new StockVO();
		vo.setS_code("1");
		
		int cnt = dao.mydelete(vo);
		System.out.println("cnt:"+cnt);
		
		
//		StockVO vo = new StockVO();
//		vo.setS_code("1");
//		vo.setS_name("2");
//		vo.setCprice("2");
//		vo.setIn_time("2");
//		
//		int cnt = dao.myupdate(vo);
//		System.out.println("cnt:"+cnt);
		
		
		
		
//		StockVO vo = new StockVO();
//		vo.setS_code("1");
//		vo.setS_name("1");
//		vo.setCprice("1");
//		vo.setIn_time("1");
//		
//		int cnt = dao.myinsert(vo);
//		System.out.println("cnt:"+cnt);
		
		
		
//		ArrayList<StockVO> list  = dao.myselect("�Ｚ����");
//		
//		for(int i=0;i<list.size();i++) {
//			StockVO tempvo = list.get(i);
//			System.out.print(tempvo.getS_code());
//			System.out.print(tempvo.getS_name());
//			System.out.print(tempvo.getCprice());
//			System.out.println(tempvo.getIn_time());
//			
//		}
		
	}
	
	
	
}












