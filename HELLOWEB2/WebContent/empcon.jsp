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

function setData(emp_id,emp_name,sex,mobile,address){
	$("#emp_id").val(emp_id);
	$("#emp_name").val(emp_name);
	$("#sex").val(sex);
	$("#mobile").val(mobile);
	$("#address").val(address);

}

function fn_add() {
	
	var emp_id	= $("#emp_id").val();
	var emp_name= $("#emp_name").val();
	var sex		= $("#sex").val();
	var mobile	= $("#mobile").val();
	var address	= $("#address").val();
	
	var param = "";
	param += "dummy=" + Math.random();
	param += "&emp_id="+emp_id;
	param += "&emp_name="+emp_name;
	param += "&sex="+sex;
	param += "&mobile="+mobile;
	param += "&address="+address;
	
	$.ajax({
		url : "insert.ajax",
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
	var emp_name= $("#emp_name").val();
	var sex		= $("#sex").val();
	var mobile	= $("#mobile").val();
	var address	= $("#address").val();
	
	var param = "";
	param += "dummy=" + Math.random();
	param += "&emp_id="+emp_id;
	param += "&emp_name="+emp_name;
	param += "&sex="+sex;
	param += "&mobile="+mobile;
	param += "&address="+address;
	
	$.ajax({
		url : "update.ajax",
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

	
	var param = "";
	param += "dummy=" + Math.random();
	param += "&emp_id="+emp_id;

	$.ajax({
		url : "delete.ajax",
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
	ArrayList<EmpVO> list = (ArrayList<EmpVO>)request.getAttribute("list");
%>

<table border="2">
<tr>
<td>

	<table border="1">
		<tr>
			<td>사원번호</td>
			<td>사원명</td>
			<td>성별</td>
			<td>전화번호</td>
			<td>주소</td>
		</tr>
	<%for(int i=0;i<list.size();i++) {%>
	<%EmpVO vo = list.get(i);%>
		<tr>
			<td><a href="javascript:setData('<%=vo.getEmp_id()%>','<%=vo.getEmp_name()%>','<%=vo.getSex()%>','<%=vo.getMobile()%>','<%=vo.getAddress()%>')"><%=vo.getEmp_id()%></a></td>
			<td><%=vo.getEmp_name()%></td>
			<td><%=vo.getSex()%></td>
			<td><%=vo.getMobile()%></td>
			<td><%=vo.getAddress()%></td>
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
			<td>사원명</td>
			<td><input type="text" id="emp_name"></td>
		</tr>
		<tr>
			<td>성별</td>
			<td><input type="text" id="sex"></td>
		</tr>
		<tr>
			<td>전화번호</td>
			<td><input type="text" id="mobile"></td>
		</tr>
		<tr>
			<td>주소</td>
			<td><input type="text" id="address"></td>
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














