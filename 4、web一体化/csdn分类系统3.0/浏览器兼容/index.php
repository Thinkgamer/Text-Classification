<!DOCTYPE>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>CSDN博客智能分类系统</title>
<link rel="stylesheet"; type="text/css";  href="/css/index.css" />
</head>

<body>

	<div class="header">
      <div class="logo">
            <a href="http://www.thinkgamer.icoc.cc/">DjangoScikit</a> 
       </div>
    </div>
    
    <div class="center">
        <div class="center_top c">
          <div class="c_t_img">
            <img src="images/logo.jpg">
          </div>
          <div class="c_t_text">
                <ul class="c_t_ul">
                    <li>
                        <a href="http://blog.csdn.net/gamer_gyt" target="_blank">Thinkgamer的专栏</a>
                    </li>
                    <li>
                        <a href="http://my.csdn.net/?ref=toolbar" target="_blank">个人主页</a>|
                        <a href="index.php" target="_blank">我的博客</a>
                        <span><font size="+3" color="#FF0000">CSDN博客智能分类系统</font></span>
                    </li>
               </ul>
          </div>
        </div>
        
        <div class="center_cen c">
        	<div class="c_c_menu">
                 <ul class="c_c_ul">
                    <li><a href="/postedit"><span>发表文章</span></a></li>
                    <li><a href="/import"><span>博客搬家</span></a></li>
                    <li><a href="/postlist"><span>文章管理</span></a></li>
                    <li><a href="/category"><span>类别管理</span></a></li>
                    <li><a href="/feedback"><span>评论管理</span></a></li>
                    <li><a href="/configure"><span>博客配置</span></a></li>
                    <li><a href="/configure/column"><span>博客栏目</span></a></li>
                    <li><a href="/postlist/0/all/deleted"><span>回收站</ span></a></li>
                   <li><a href="/postedit">写新文章</a></li>
                   <li><a href="/import">博客搬家</a></li>
                 </ul>
            </div>
            
            <p class="c_c_title">文章标题
       	 		<span style="color: green; margin-center: 18px; display:inline">(尊重原创，请保证您的文章为原创作品)</span>
       		</p>
            <table border="0" width="99.4%">
                <tr>
                    <td width="80%">
                        <form class="abc" action="index.php" method="post">
                        <input type="text" id="txtTitle" name="title" class="title_input" maxlength="100" value="" />  
                    </td>
                    <td width="20%">
                        <div>
                            <select id="selType" size="1" name="D1" style="font-size: 17px" >
                                <option value="0" >请选择</option>
                                <option value="1">原创</option>
                                <option value="2">转载</option>
                                <option value="4">翻译</option>
                            </select>
                        </div>
                   </td>
                </tr>
        	</table>
            <p class="c_c_text">文章内容 <a href="/mdeditor" target="_blank">切换到MarkDown编辑器</a></p>
            <div class="section">
          		<textarea id="editor" rows="30" name="Text" style="width:99.9%;"></textarea>  
        	</div> 
        </div>
        
        <div class="center_but c">
        	<fieldset style="margin-top: 10px; padding: 4px 10px 10px 10px;">
                <div>
                    <p class="c_b_p">
                        文章标签（加Tag,结天下！）
                        <a href="index.php" target="_blank" style="font-size:12px;">打Tag,Why？</a>
                    </p>
                <div style="position:relative;">
                    <div id="d_tag2"></div>
                        <input type="text" name="tag" id="txtTag2" style="width:60%; height:20px;" maxlength="100" />
                        （最多5个“,”相隔）
                </div>
   			</fieldset>
    
    		<fieldset style="margin-top: 10px; padding: 4px 10px 10px 10px;">
    			<p class="c_b_p">
                	个人分类 (
                    <a href="http://write.blog.csdn.net/category" target="_blank">编辑分类</a>
                    )
                    </p>
    			<div>
                    <input type="text" name="self" id="txtTag" style="width:60%; height:20px;" maxlength="100" />
                    （分类间“,”相隔）
                    <div>
                        <div id="tagbox"></div>
                    </div>
    			</div>
    		</fieldset>
            
            <fieldset style="margin-top: 10px; padding: 4px 10px 10px 10px;">
    			<p class="subtit">请选择文章分类（稍后将于系统分类进行对比,累加并计算匹配成功率）</p>
              	<table>
                  <tr>
                    <td>
                      <input type='radio' name='radChl' id='radChl1' value='1' /><label for='radChl1'>移动开发</label>
                    </td>
                    <td>
                      <input type='radio' name='radChl' id='radChl2' value='2' /><label for='radChl2'>Web前端</label>
                    </td>
                    <td>
                      <input type='radio' name='radChl' id='radChl3' value='3' /><label for='radChl3'>架构设计</label>
                    </td>
                    <td>
                      <input type='radio' name='radChl' id='radChl4' value='4' /><label for='radChl4'>编程语言</label>
                    </td>
                    <td>
                      <input type='radio' name='radChl' id='radChl5' value='5' /><label for='radChl5'>互联网</label>
                    </td>
                    <td>
                      <input type='radio' name='radChl' id='radChl6' value='6' /><label for='radChl6'>数据库</label>
                    </td>
                    <td>
                      <input type='radio' name='radChl' id='radChl7' value='7' /><label for='radChl7'>系统运维</label>
                    </td>
                    <td>
                      <input type='radio' name='radChl' id='radChl8' value='8' /><label for='radChl8'>云计算</label>
                    </td>
                    <td>
                      <input type='radio' name='radChl' id='radChl9' value='9' /><label for='radChl9'>研发管理</label>
                    </td>
                    <td>
                      <input type='radio' name='radChl' id='radChl10' value='0' /><label for='radChl10'>综合</label>
                    </td>
                  </tr>
               </table> 
    		</fieldset>
            
            <fieldset style="margin-top: 10px; padding: 4px 10px 10px 10px;">
    		提示：请不要发布任何推广,广告（包括招聘）,政治,低俗等方面的内容,不要把博客当作SEO工具,否则可能会影响到您的使用。
    		</fieldset>
            
            <table width="100%">
        	  <tr>
            	<td align="center">
                	<input type="submit" name="r" value="重新输入" class="STYLE1" onclick="window.location='index.php'">
                </td>
                <td align="left">
                	<input type="submit" name="t" value="提交" class="STYLE1">
                </td>
                <td>
                	&nbsp
                </td>
              </tr>
          </table>  
      		</form>   
        </div> 
     </div>
    
    <div class="foot">
    	<table align="center" width="100%" border="0">
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
        	<td colspan="6" align="center"><font size="-1">2015&nbsp;ThinkC&nbsp&nbsp;京ICP证030173号&nbsp</font>
       	    </td></td>
        </tr>
   		</table>
    </div>
	<?php
	    $content=$_POST['title'];
		$a=$_POST['Text'];
		$b=$_POST['tag'];
		$c=$_POST['self'];
       if(!empty($content)||!empty($a)||!empty($b)||!empty($c))
		{ 
			$fp=fopen("content.txt","w");
			fwrite($fp,$content."\r\n".$a."\r\n".$b."\r\n".$c);//写入
		}
		
	?>
    <!--执行Python脚本，显示分类结果-->
    <?php
		if(!empty($content)&&@$_POST['t']=="提交")
		{
    		$p = popen("python result.py", "r");
			fscanf($p, "%s", $result);
			pclose($p);
			$str1 = "分类结果是：";
			$str = $str1."".$result;
            echo "<script> {window.alert('$str');location.href='index.php'} </script>"; 
		}
	?>    
</body>
</html>