package com.naver.web;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class MyDb extends HttpServlet {


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setCharacterEncoding("UTF-8");
		PrintWriter out = response.getWriter();
		
		String s_name = request.getParameter("s_name");
		System.out.println("s_name:"+s_name);
		
		StockDAO dao = new StockDAO();
		ArrayList<StockVO> list =null;
		try {
			list = dao.myselect(s_name);
		} catch (Exception e) {
			System.out.println(e);
		}
		
		
		
		out.println("<html>");
		out.println("<head>");
		out.println("<meta charset='utf-8'>");
		
		out.println("</head>");
		out.println("<body>");
		
		out.println("<table>");
		out.println("<tr>");
		out.println("<td>종목코드</td>");
		out.println("<td>종목명</td>");
		out.println("<td>현재가</td>");
		out.println("<td>입력일시</td>");
		out.println("</tr>");
		
		for(int i=0;i<list.size();i++) {
			StockVO vo = list.get(i);
			out.println("<tr>");
			out.println("<td>"+vo.getS_code()+"</td>");
			out.println("<td>"+vo.getS_name()+"</td>");
			out.println("<td>"+vo.getCprice()+"</td>");
			out.println("<td>"+vo.getIn_time()+"</td>");
			out.println("</tr>");
		}
		
		out.println("</table>");
		
		out.println("</body>");
		out.println("</html>");
	}

	
	
	
	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
