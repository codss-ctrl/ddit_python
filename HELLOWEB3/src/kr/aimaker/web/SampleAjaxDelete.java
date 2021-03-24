package kr.aimaker.web;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.aimaker.mybatis.MyBatisConnectionFactory;
import kr.aimaker.mybatis.SampleDAO;
import kr.aimaker.mybatis.SampleVO;


public class SampleAjaxDelete extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String col01 	= request.getParameter("col01");
		
		
		
		System.out.println("col01:"+col01);
		
		
		SampleVO vo = new SampleVO();
		vo.setCol01(col01);
		
		
		int cnt = 0;
		SampleDAO dao = new SampleDAO(MyBatisConnectionFactory.getSqlSessionFactory());
		
		try {
			cnt = dao.mydelete(vo);
			if (cnt ==1) {
				AjaxUtil.responseJson(response, "ok");
			}else {
				AjaxUtil.responseJson(response, "ng");
			}
		} catch (Exception e) {
			System.out.println(e);
		}
	
		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		doGet(request, response);
	}

}
