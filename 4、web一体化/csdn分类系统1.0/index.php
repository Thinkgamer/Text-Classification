<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>CSDN博客推荐系统</title>
<style type="text/css">
a:link {
	color: #906;
	text-decoration: none;
}
a:visited {
	text-decoration: none;
	color: #906;
}
a:hover {
	text-decoration: underline;
}
a:active {
	text-decoration: none;
}
</style>
</head>

<body bgcolor="#FFFFCC">
<table align="center" width="100%">
    	<tr><th align="center"><font color="#FF3300" size="+4">欢迎使用CSDN博客分类系统</font></th></tr>
    </table>

<table border="1" width="80%" height="450" align="center">
    	<tr>
        	<td></td>
            <td width="50%">
            	<div class="section" align="center">
                    <form action="index.php" method="post">
                        <textarea cols="90" rows="25" name="write"></textarea>
                        <br>
                        <input type="submit" name="r" value="重新输入" class="STYLE1" onclick="window.location='index.php'">			                             &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp;
                        <input type="submit" name="t" value="提交" class="STYLE1">
                    </form>
                </div>
            </td>
            <td></td>
        </tr>
    </table>
    
    
<table align="center" width="80%" border="0">
    	<tr align="center">
        	<td width="16%"><a href="http://i.youku.com/u/UMTM4NDk2OTUyMA==" target="_blank">优酷空间</a></td>
            <td width="16%"><a href="http://www.iqiyi.com/u/1214878054" target="_blank">爱奇艺</a></td>
            <td width="16%"><a href="http://blog.csdn.net/gamer_gyt" target="_blank">Thinkgamer的CSDN博客</a></td>
            <td width="16%"><a href="http://www.miaopai.com/u/wxsso_045vrrmaac" target="_blank">秒排空间</a></td>
            <td width="16%"><a href="http://www.rongshuxia.com/" target="_blank">榕树下</a></td>
        </tr>
        <tr align="center">
        	<td width="16%"><a href="https://www.baidu.com/" target="_blank">百度一下</a></td>
            <td width="16%"><a href="http://www.tmeishi.com/" target="_blank">Google</a></td>
            <td width="16%"><a href="http://weibo.com/234654758/home?wvr=5" target="_blank">新浪微博</a></td>
            <td width="16%"><a href="https://www.facebook.com/" target="_blank">FaceBook</a></td>
            <td width="16%"><a href="http://www.oschina.net/" target="_blank">开源中国</a></td>
        </tr>
    	<tr>
        	<td colspan="6" align="center"><font size="+1" color="#0000FF">本系统由Thinkgamer独立开发完成</font>
       	    </td></td>
        </tr>
        <tr>
        	<td colspan="6" align="center"><font size="-1">&copy;2015&nbsp;ThinkC&nbsp&nbsp;京ICP证030173号&nbsp</font>
       	    </td></td>
        </tr>
    </table>
    <!--接收textarea域中的文本并写入文件-->	
	<?php
        $contents = $_POST['write'];
        if(!empty($contents))
		{
			$fp=fopen("test.txt","w");
			fwrite($fp,$contents);//写入
		}
	?>
    <!--执行Python脚本，显示分类结果-->
    <?php
		if(!empty($contents)&&@$_POST['t']=="提交")
		{
    		$p = popen("python test.py", "r");
			fscanf($p, "%s", $result);
			pclose($p);
			$str1 = "分类结果是：";
			$str = $str1."".$result;
            echo "<script> {window.alert('$str');location.href='index.php'} </script>"; 
		}
	?>
</body>
</html>