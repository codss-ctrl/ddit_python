package com.naver.web;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class EmpDAO {
	public ArrayList<EmpVO> myselect() throws Exception{
		ArrayList<EmpVO> list = new ArrayList<EmpVO>();
		
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "select emp_id,emp_name,sex,mobile,address from emp";

		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		ResultSet rs = stmt.executeQuery(sql);
		while (rs.next()) {
			String emp_id = rs.getString("emp_id");
			String emp_name = rs.getString("emp_name");
			String sex = rs.getString("sex");
			String mobile = rs.getString("mobile");
			String address = rs.getString("address");
			
			EmpVO tempvo = new EmpVO();
			tempvo.setEmp_id(emp_id);
			tempvo.setEmp_name(emp_name);
			tempvo.setSex(sex);
			tempvo.setMobile(mobile);
			tempvo.setAddress(address);
			
			list.add(tempvo);
		}
		
		stmt.close();
		conn.close();
		
		return list;
	}
	
	
	public int myinsert(EmpVO vo) throws Exception {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "insert into emp (emp_id,emp_name,sex,mobile,address) values ('"+vo.getEmp_id()+"','"+vo.getEmp_name()+"','"+vo.getSex()+"','"+vo.getMobile()+"','"+vo.getAddress()+"')";

		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		return cnt;
	}
	
	
	public int myupdate(EmpVO vo) throws Exception {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "update emp set emp_name='"+vo.getEmp_name()+"',sex='"+vo.getSex()+"',mobile='"+vo.getMobile()+"',address='"+vo.getAddress()+"' where emp_id='"+vo.getEmp_id()+"'";

		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		return cnt;
	}
	
	public int mydelete(EmpVO vo) throws Exception {
	
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "delete from emp where emp_id='"+vo.getEmp_id()+"'";
	
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
	
		return cnt;
	}
	
	
	
	
	public static void main(String[] args) throws Exception {
		EmpDAO dao = new EmpDAO();
		
		
//		EmpVO vo = new EmpVO();
//		vo.setEmp_id("2");
//
//		int cnt = dao.mydelete(vo);
//		System.out.println("cnt:"+cnt);
		
		
//		EmpVO vo = new EmpVO();
//		vo.setEmp_id("2");
//		vo.setEmp_name("3");
//		vo.setSex("3");
//		vo.setMobile("3");
//		vo.setAddress("3");
//		
//		int cnt = dao.myupdate(vo);
//		System.out.println("cnt:"+cnt);
		
		
		
		
//		EmpVO vo = new EmpVO();
//		vo.setEmp_id("2");
//		vo.setEmp_name("2");
//		vo.setSex("2");
//		vo.setMobile("2");
//		vo.setAddress("2");
//		
//		int cnt = dao.myinsert(vo);
//		System.out.println("cnt:"+cnt);
		
		
		//emp_id,emp_name,sex,mobile,address
//		ArrayList<EmpVO> list  = dao.myselect();
//		
//		for(int i=0;i<list.size();i++) {
//			EmpVO tempvo = list.get(i);
//			System.out.print(tempvo.getEmp_id());
//			System.out.print(tempvo.getEmp_name());
//			System.out.print(tempvo.getSex());
//			System.out.print(tempvo.getMobile());
//			System.out.println(tempvo.getAddress());
//			
//		}
		
	}
	
	
	
	
	
}



