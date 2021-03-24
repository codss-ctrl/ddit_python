package kr.aimaker.web;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import kr.aimaker.mybatis.MyBatisConnectionFactory;
import kr.aimaker.mybatis.SampleDAO;
import kr.aimaker.mybatis.SampleVO;



public class ConSample extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	 	response.setCharacterEncoding("UTF-8");
	 	
	 	HttpSession session = request.getSession();
	 	String emp_id = (String) session.getAttribute("emp_id");
	 	
	 	if(emp_id==null){
	 		response.sendRedirect("login.html");
	 		return;
	 	}
		
		SampleDAO dao = new SampleDAO(MyBatisConnectionFactory.getSqlSessionFactory());
		ArrayList<SampleVO> list =null;
		
		try {
			
			SampleVO pvo = new SampleVO();
			list = (ArrayList<SampleVO>) dao.myselect(pvo);
			
			System.out.println(list.size());
			
		} catch (Exception e) {
			System.out.println(e);
		}
		
		request.setAttribute("list",list);
	    RequestDispatcher rd = request.getRequestDispatcher("/consample.jsp");
	    rd.forward(request, response);
	    
	    
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
