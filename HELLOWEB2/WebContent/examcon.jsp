<%@page import="com.naver.web.EmpExamVO"%>
<%@page import="com.naver.web.EmpVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="jquery-3.5.1.js"></script>
<script type="text/javascript">
function setData(emp_id,exam_id,kor,eng,mat){
	$("#emp_id").val(emp_id);
	$("#exam_id").val(exam_id);
	$("#kor").val(kor);
	$("#eng").val(eng);
	$("#mat").val(mat);

}
function fn_add() {
	
	var emp_id	= $("#emp_id").val();
	var exam_id	= $("#exam_id").val();
	var kor		= $("#kor").val();
	var eng		= $("#eng").val();
	var mat		= $("#mat").val();
	
	var param = "";
	param += "dummy=" + Math.random();
	param += "&emp_id="+emp_id;
	param += "&exam_id="+exam_id;
	param += "&kor="+kor;
	param += "&eng="+eng;
	param += "&mat="+mat;
	
	$.ajax({
		url : "examinsert.ajax",
		data : param,
		dataType : "json",
		type : "post",
		async: false,
		statusCode : {
			404 : function() {
				alert("네트워크가 불안정합니다. 다시 시도부탁드립니다.");
			}
		},
		success : function(data) {
			fn_add_callback(data);
		}
	});
}	
function fn_add_callback(data){
	if(data == null){
		return;
	}
	alert(data);
	if(data=="ok"){
		alert("정상적으로 추가되었습니다.");
		location.reload();
		
	}else{
	alert("추가 도중 문제가 생겼습니다.");
	}
	
}

function fn_upd() {
	
	var emp_id	= $("#emp_id").val();
	var exam_id	= $("#exam_id").val();
	var kor		= $("#kor").val();
	var eng		= $("#eng").val();
	var mat		= $("#mat").val();
	
	var param = "";
	param += "dummy=" + Math.random();
	param += "&emp_id="+emp_id;
	param += "&exam_id="+exam_id;
	param += "&kor="+kor;
	param += "&eng="+eng;
	param += "&mat="+mat;
	
	$.ajax({
		url : "examupdate.ajax",
		data : param,
		dataType : "json",
		type : "post",
		async: false,
		statusCode : {
			404 : function() {
				alert("네트워크가 불안정합니다. 다시 시도부탁드립니다.");
			}
		},
		success : function(data) {
			fn_upd_callback(data);
		}
	});
}	
function fn_upd_callback(data){
	if(data == null){
		return;
	}
	alert(data);
	if(data=="ok"){
		alert("정상적으로 수정되었습니다.");
		location.reload();
		
	}else{
	alert("수정 도중 문제가 생겼습니다.");
	}
	
}

function fn_del() {
	
	var emp_id	= $("#emp_id").val();
	var exam_id	= $("#exam_id").val();
	
	
	var param = "";
	param += "dummy=" + Math.random();
	param += "&emp_id="+emp_id;
	param += "&exam_id="+exam_id;
	
	
	$.ajax({
		url : "examdelete.ajax",
		data : param,
		dataType : "json",
		type : "post",
		async: false,
		statusCode : {
			404 : function() {
				alert("네트워크가 불안정합니다. 다시 시도부탁드립니다.");
			}
		},
		success : function(data) {
			fn_del_callback(data);
		}
	});
}	
function fn_del_callback(data){
	if(data == null){
		return;
	}
	alert(data);
	if(data=="ok"){
		alert("정상적으로 삭제되었습니다.");
		location.reload();
		
	}else{
	alert("삭제 도중 문제가 생겼습니다.");
	}
	
}
</script>
</head>
<body>
<%
	ArrayList<EmpExamVO> list = (ArrayList<EmpExamVO>)request.getAttribute("list");
%>

<table border="2">
<tr>
<td>

	<table border="1">
		<tr>
			<td>사원번호</td>
			<td>시험번호</td>
			<td>국어</td>
			<td>영어</td>
			<td>수학</td>
		</tr>
	<%for(int i=0;i<list.size();i++) {%>
	<%EmpExamVO vo = list.get(i);%>
		<tr>
			<td><a href="javascript:setData('<%=vo.getEmp_id()%>','<%=vo.getExam_id()%>','<%=vo.getKor()%>','<%=vo.getEng()%>','<%=vo.getMat()%>')"><%=vo.getEmp_id()%>,<%=vo.getExam_id()%></a></td>
			<td><%=vo.getExam_id()%></td>
			<td><%=vo.getKor()%></td>
			<td><%=vo.getEng()%></td>
			<td><%=vo.getMat()%></td>
		</tr>
	<%}%>	
	</table>

</td>
<td>

	<table border="1">
		<tr>
			<td>사원번호</td>
			<td><input type="text" id="emp_id"></td>
		</tr>
		<tr>
			<td>시험번호</td>
			<td><input type="text" id="exam_id"></td>
		</tr>
		<tr>
			<td>국어</td>
			<td><input type="text" id="kor"></td>
		</tr>
		<tr>
			<td>영어</td>
			<td><input type="text" id="eng"></td>
		</tr>
		<tr>
			<td>수학</td>
			<td><input type="text" id="mat"></td>
		</tr>
		<tr>
			<td colspan="2" >
				<input type="button" value="추가" onclick="fn_add()" >
				<input type="button" value="수정" onclick="fn_upd()" >
				<input type="button" value="삭제" onclick="fn_del()" >
			</td>
		</tr>
		
	
	</table>


</td>
</tr>
</table>



</body>
</html>














