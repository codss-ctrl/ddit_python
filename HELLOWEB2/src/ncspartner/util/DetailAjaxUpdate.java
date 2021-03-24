package ncspartner.util;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.naver.web.DetailDAO;
import com.naver.web.DetailVO;
import com.naver.web.EmpDAO;
import com.naver.web.EmpExamDAO;
import com.naver.web.EmpExamVO;
import com.naver.web.EmpVO;

public class DetailAjaxUpdate extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String exam_id 		= request.getParameter("exam_id");
		String e_seq 		= request.getParameter("e_seq");
		String question 	= request.getParameter("question");
		String q1 			= request.getParameter("q1");
		String q2			= request.getParameter("q2");
		String q3			= request.getParameter("q3");
		String q4			= request.getParameter("q4");
		String answer		= request.getParameter("answer");
		
		
		System.out.println("exam_id:"+exam_id);
		System.out.println("e_seq:"+e_seq);
		System.out.println("question:"+question);
		System.out.println("q1:"+q1);
		System.out.println("q2:"+q2);
		System.out.println("q3:"+q3);
		System.out.println("q4:"+q4);
		System.out.println("answer:"+answer);
		
		DetailVO vo = new DetailVO();
		vo.setExam_id(exam_id);
		vo.setE_seq(e_seq);
		vo.setQuestion(question);
		vo.setQ1(q1);
		vo.setQ2(q2);
		vo.setQ3(q3);
		vo.setQ4(q4);
		vo.setAnswer(answer);
		
		int cnt = 0;
		DetailDAO dao = new DetailDAO();
		
		try {
			cnt = dao.myupdate(vo);
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
