<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
 
 
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	String dan = request.getParameter("dan");
	int i_dan = Integer.parseInt(dan); 
	
	out.print(i_dan+"*1="+(i_dan*1)+"<br>\n");
	out.print(i_dan+"*2="+(i_dan*2)+"<br>\n");
	out.print(i_dan+"*3="+(i_dan*3)+"<br>\n");
	                               
	out.print(i_dan+"*4="+(i_dan*4)+"<br>\n");
	out.print(i_dan+"*5="+(i_dan*5)+"<br>\n");
	out.print(i_dan+"*6="+(i_dan*6)+"<br>\n");
	                               
	out.print(i_dan+"*7="+(i_dan*7)+"<br>\n");
	out.print(i_dan+"*8="+(i_dan*8)+"<br>\n");
	out.print(i_dan+"*9="+(i_dan*9)+"<br>\n");

%>   
<!-- http://localhost:7070/HELLOWEB/hello.jsp?dan=7 -->
</body>
</html>