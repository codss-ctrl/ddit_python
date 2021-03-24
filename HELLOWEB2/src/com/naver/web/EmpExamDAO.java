package com.naver.web;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class EmpExamDAO {
	public ArrayList<EmpExamVO> myselect () throws Exception {
		ArrayList<EmpExamVO> list = new ArrayList<EmpExamVO>();
		
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String sql = "select * from empexam";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		ResultSet rs = stmt.executeQuery(sql);
		while (rs.next()) {
			String id = rs.getString("emp_id");
			String name = rs.getString("exam_id");
			String kor = rs.getString("kor");
			String eng = rs.getString("eng");
			String mat = rs.getString("mat");
			
			EmpExamVO tEmpExamVO = new EmpExamVO();
			tEmpExamVO.setEmp_id(id);
			tEmpExamVO.setExam_id(name);
			tEmpExamVO.setEng(kor);
			tEmpExamVO.setKor(eng);
			tEmpExamVO.setMat(mat);
			
			list.add(tEmpExamVO);
		}
		stmt.close();
		conn.close();
		
		return list;
	}
	
	public int myinsert (EmpExamVO vo) throws Exception {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String sql = "insert into empexam (emp_id,exam_id,eng,kor,mat) values ('"+vo.getEmp_id()+"','"+vo.getExam_id()+"',"+vo.getEng()+","+vo.getKor()+","+vo.getMat()+")";
		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		stmt.close();
		conn.close();
		return cnt;
	}
	
	public int myupdate (EmpExamVO vo) throws Exception {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String sql = "update empexam set kor='"+vo.getKor()+"', eng='"+vo.getEng()+"', mat='"+vo.getMat()+"' where emp_id='"+vo.getEmp_id()+"' and exam_id='"+vo.getExam_id()+"'";		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		return cnt;
	}
	
	public int mydelete (EmpExamVO vo) throws Exception  {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String sql = "delete from empexam where emp_id='"+vo.getEmp_id()+"' and exam_id='"+vo.getExam_id()+"'";		
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		return cnt;
	}
	
	public static void main(String[] args) throws Exception {

		
		EmpExamDAO dao = new EmpExamDAO();
		
		
		EmpExamVO vo = new EmpExamVO();
		vo.setEmp_id("2");
		vo.setExam_id("2");

		int cnt = dao.mydelete(vo);
		System.out.println("cnt:"+cnt);
		
		
//		EmpExamVO vo = new EmpExamVO();
//		vo.setEmp_id("2");
//		vo.setExam_id("2");
//		vo.setKor("3");
//		vo.setEng("3");
//		vo.setMat("3");
//		
//		int cnt = dao.myupdate(vo);
//		System.out.println("cnt:"+cnt);
		
		
		
		
//		EmpExamVO vo = new EmpExamVO();
//		vo.setEmp_id("2");
//		vo.setExam_id("2");
//		vo.setKor("2");
//		vo.setEng("2");
//		vo.setMat("2");
//		
//		int cnt = dao.myinsert(vo);
//		System.out.println("cnt:"+cnt);
		
		
		//emp_id,exam_id,eng,kor,mat
//		ArrayList<EmpExamVO> list  = dao.myselect();
//		
//		for(int i=0;i<list.size();i++) {
//			EmpExamVO tempvo = list.get(i);
//			System.out.print(tempvo.getEmp_id());
//			System.out.print(tempvo.getExam_id());
//			System.out.print(tempvo.getEng());
//			System.out.print(tempvo.getKor());
//			System.out.println(tempvo.getMat());
//			
//		}
		
		
		
		
		
		
		
		
		
	}
}