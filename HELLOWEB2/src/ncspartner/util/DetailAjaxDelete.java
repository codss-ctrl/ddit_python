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

public class DetailAjaxDelete extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String exam_id 		= request.getParameter("exam_id");
		String e_seq 		= request.getParameter("e_seq");
		
		System.out.println("exam_id:"+exam_id);
		System.out.println("e_seq:"+e_seq);
		
		
		DetailVO vo = new DetailVO();
		vo.setExam_id(exam_id);
		vo.setE_seq(e_seq);
		
		
		int cnt = 0;
		DetailDAO dao = new DetailDAO();
		
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
