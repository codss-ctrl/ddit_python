package com.naver.web;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class DetailCon extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setCharacterEncoding("UTF-8");
		
        DetailDAO dao = new DetailDAO();
		ArrayList<DetailVO> list =null;
		try {
			list = dao.myselect();
		} catch (Exception e) {
			System.out.println(e);
		}
		request.setAttribute("list",list);
	    RequestDispatcher rd = request.getRequestDispatcher("/detailcon.jsp");
	    rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
