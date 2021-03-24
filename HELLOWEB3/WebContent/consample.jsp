<%@page import="kr.aimaker.mybatis.SampleVO"%>
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
function setData(col01,col02,col03){
	$("#col01").val(col01);
	$("#col02").val(col02);
	$("#col03").val(col03);

}
function fn_add() {
	
	var col01		= $("#col01").val();
	var col02		= $("#col02").val();
	var col03		= $("#col03").val();
	
	
	var param = "";
	param += "dummy=" + Math.random();
	param += "&col01="+col01;
	param += "&col02="+col02;
	param += "&col03="+col03;
	
	
	
	$.ajax({
		url : "sampleinsert.ajax",
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
	
	var col01	= $("#col01").val();
	var col02	= $("#col02").val();
	var col03	= $("#col03").val();
	
	
	var param = "";
	param += "dummy=" + Math.random();
	param += "&col01="+col01;
	param += "&col02="+col02;
	param += "&col03="+col03;
	
	
	
	$.ajax({
		url : "sampleupdate.ajax",
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
		alert("정상적으로 수정되었습니다.");
		location.reload();
		
	}else{
	alert("수정 도중 문제가 생겼습니다.");
	}
	
}

function fn_del() {
	
	var col01		= $("#col01").val();
	
	
	var param = "";
	param += "dummy=" + Math.random();
	param += "&col01="+col01;
	
	
	
	$.ajax({
		url : "sampledelete.ajax",
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
	ArrayList<SampleVO> list = (ArrayList<SampleVO>)request.getAttribute("list");
%>

<table border="2">
<tr>
<td>

	<table border="1">
		<tr>
			<td>col01</td>
			<td>col02</td>
			<td>col03</td>
		</tr>
	<%for(int i=0;i<list.size();i++) {%>
	<%SampleVO vo = list.get(i);%>
		<tr>
			<td><a href="javascript:setData('<%=vo.getCol01()%>','<%=vo.getCol02()%>','<%=vo.getCol03()%>')"><%=vo.getCol01()%></a></td>
			<td><%=vo.getCol02()%></td>
			<td><%=vo.getCol03()%></td>
		</tr>
	<%}%>	
	</table>

</td>
<td>

	<table border="1">
		<tr>
			<td>col01</td>
			<td><input type="text" id="col01"></td>
		</tr>
		<tr>
			<td>col02</td>
			<td><input type="text" id="col02"></td>
		</tr>
		<tr>
			<td>col03</td>
			<td><input type="text" id="col03"></td>
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














