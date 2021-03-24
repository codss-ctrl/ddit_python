<%@page import="com.naver.web.DetailVO"%>
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

function setData(exam_id,e_seq,question,q1,q2,q3,q4,answer){
	$("#exam_id").val(exam_id);
	$("#e_seq").val(e_seq);
	$("#question").val(question);
	$("#q1").val(q1);
	$("#q2").val(q2);
	$("#q3").val(q3);
	$("#q4").val(q4);
	$("#answer").val(answer);

}
function fn_add() {
	
	var exam_id		= $("#exam_id").val();
	var e_seq		= $("#e_seq").val();
	var question	= $("#question").val();
	var q1			= $("#q1").val();
	var q2			= $("#q2").val();
	var q3			= $("#q3").val();
	var q4			= $("#q4").val();
	var answer		= $("#answer").val();
	
	var param = "";
	param += "dummy=" + Math.random();
	param += "&exam_id="+exam_id;
	param += "&e_seq="+e_seq;
	param += "&question="+question;
	param += "&q1="+q1;
	param += "&q2="+q2;
	param += "&q3="+q3;
	param += "&q4="+q4;
	param += "&answer="+answer;
	
	
	$.ajax({
		url : "detailinsert.ajax",
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
	
	var exam_id		= $("#exam_id").val();
	var e_seq		= $("#e_seq").val();
	var question	= $("#question").val();
	var q1			= $("#q1").val();
	var q2			= $("#q2").val();
	var q3			= $("#q3").val();
	var q4			= $("#q4").val();
	var answer		= $("#answer").val();
	
	var param = "";
	param += "dummy=" + Math.random();
	param += "&exam_id="+exam_id;
	param += "&e_seq="+e_seq;
	param += "&question="+question;
	param += "&q1="+q1;
	param += "&q2="+q2;
	param += "&q3="+q3;
	param += "&q4="+q4;
	param += "&answer="+answer;
	
	
	$.ajax({
		url : "detailupdate.ajax",
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
	
	var exam_id		= $("#exam_id").val();
	var e_seq		= $("#e_seq").val();

	var param = "";
	param += "dummy=" + Math.random();
	param += "&exam_id="+exam_id;
	param += "&e_seq="+e_seq;
	
	
	
	$.ajax({
		url : "detaildelete.ajax",
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
	ArrayList<DetailVO> list = (ArrayList<DetailVO>)request.getAttribute("list");
%>

<table border="2">
<tr>
<td>

	<table border="1">
		<tr>
			<td>시험번호</td>
			<td>문제번호</td>
			<td>Question</td>
			<td>Q1</td>
			<td>Q2</td>
			<td>Q3</td>
			<td>Q4</td>
			<td>Answer</td>
		</tr>
	<%for(int i=0;i<list.size();i++) {%>
	<%DetailVO vo = list.get(i);%>
		<tr>
			<td><a href="javascript:setData('<%=vo.getExam_id()%>','<%=vo.getE_seq()%>','<%=vo.getQuestion()%>','<%=vo.getQ1()%>','<%=vo.getQ2()%>','<%=vo.getQ3()%>','<%=vo.getQ4()%>','<%=vo.getAnswer()%>')"><%=vo.getExam_id()%>,<%=vo.getE_seq()%></a></td>
			<td><%=vo.getE_seq()%></td>
			<td><%=vo.getQuestion()%></td>
			<td><%=vo.getQ1()%></td>
			<td><%=vo.getQ2()%></td>
			<td><%=vo.getQ3()%></td>
			<td><%=vo.getQ4()%></td>
			<td><%=vo.getAnswer()%></td>
		</tr>
	<%}%>	
	</table>

</td>
<td>

	<table border="1">
		<tr>
			<td>시험번호</td>
			<td><input type="text" id="exam_id"></td>
		</tr>
		<tr>
			<td>문제번호</td>
			<td><input type="text" id="e_seq"></td>
		</tr>
		<tr>
			<td>Question</td>
			<td><input type="text" id="question"></td>
		</tr>
		<tr>
			<td>Q1</td>
			<td><input type="text" id="q1"></td>
		</tr>
		<tr>
			<td>Q2</td>
			<td><input type="text" id="q2"></td>
		</tr>
		<tr>
			<td>Q3</td>
			<td><input type="text" id="q3"></td>
		</tr>
		<tr>
			<td>Q4</td>
			<td><input type="text" id="q4"></td>
		</tr>
		<tr>
			<td>answer</td>
			<td><input type="text" id="answer"></td>
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














