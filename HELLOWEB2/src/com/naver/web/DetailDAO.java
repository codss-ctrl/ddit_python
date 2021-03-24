package com.naver.web;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class DetailDAO {
	public ArrayList<DetailVO> myselect() throws Exception{
		ArrayList<DetailVO> list = new ArrayList<DetailVO>();
		
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "select exam_id,e_seq,question,q1,q2,q3,q4,answer from EXAM_DETAIL";

		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		ResultSet rs = stmt.executeQuery(sql);
		
		while (rs.next()) {
			String exam_id = rs.getString("exam_id");
			String e_seq = rs.getString("e_seq");
			String question = rs.getString("question");
			String q1 = rs.getString("q1");
			String q2 = rs.getString("q2");
			String q3 = rs.getString("q3");
			String q4 = rs.getString("q4");
			String answer = rs.getString("answer");
			
			DetailVO tempvo = new DetailVO();
			tempvo.setExam_id(exam_id);
			tempvo.setE_seq(e_seq);
			tempvo.setQuestion(question);
			tempvo.setQ1(q1);
			tempvo.setQ2(q2);
			tempvo.setQ3(q3);
			tempvo.setQ4(q4);
			tempvo.setAnswer(answer);;
			
			list.add(tempvo);
		}
		
		stmt.close();
		conn.close();
		
		return list;
	}
	
	public int myinsert(DetailVO vo) throws Exception {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "insert into EXAM_DETAIL (exam_id,e_seq,question,q1,q2,q3,q4,answer) values ('"+vo.getExam_id()+"','"+vo.getE_seq()+"','"+vo.getQuestion()+"','"+vo.getQ1()+"','"+vo.getQ2()+"','"+vo.getQ3()+"','"+vo.getQ4()+"','"+vo.getAnswer()+"')";

		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		return cnt;
	}
	public int myupdate(DetailVO vo) throws Exception {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "update EXAM_DETAIL set question='"+vo.getQuestion()+"',q1='"+vo.getQ1()+"',q2='"+vo.getQ2()+"',q3='"+vo.getQ3()+"',q4='"+vo.getQ4()+"',answer='"+vo.getAnswer()+"' where Exam_id='"+vo.getExam_id()+"' and e_seq='"+vo.getE_seq()+"'";

		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
		return cnt;
	}
	public int mydelete(DetailVO vo) throws Exception {
		
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		String sql = "delete from EXAM_DETAIL where exam_id='"+vo.getExam_id()+"' and e_seq='"+vo.getE_seq()+"'";
	
		Class.forName(driver);
		Connection conn = DriverManager.getConnection(url, "python", "python");
		Statement stmt = conn.createStatement();
		int cnt = stmt.executeUpdate(sql);
		
		stmt.close();
		conn.close();
	
		return cnt;
	}
	
	
	public static void main(String[] args) throws Exception{
		DetailDAO dao = new DetailDAO();
		DetailVO vo = new DetailVO();
		
		vo.setExam_id("1");
		vo.setE_seq("1");
		vo.setQuestion("1");
		vo.setQ1("2");
		vo.setQ2("2");
		vo.setQ3("2");
		vo.setQ4("2");
		vo.setAnswer("2");
		
		int cnt = dao.mydelete(vo);
		System.out.println("cnt:"+cnt);
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
