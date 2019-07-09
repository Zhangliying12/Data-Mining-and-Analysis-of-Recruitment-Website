<%@page import="ruanko.newspublish.entity.Article"%>
<%@ page language="java" import="java.util.*" pageEncoding="gb2312"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
<%
	//从request里获取新闻
	Article article = (Article)request.getAttribute("article");
 %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>显示新闻内容</title>
    
  </head>
  
  <body>
    显示新闻详细内容 <br>
   新闻标题:<h1><%= article.getTitle() %></h1> 
   <br>作者:<%= article.getAuthor() %>
   <br>新闻内容:<%= article.getContent() %>
  </body>
</html>
