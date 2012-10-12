sublime-p2world-tsv（xsl生成代码模板）
===================

默认快捷键：alt+shift+e

1.选中整行代码（包含缩进符号）如：

    ··<a href="$1" class='link-$99'>$2</a>

2.按下快捷键

3.在弹出框中粘贴xsl中数据（末尾回车符可有可无）

    http://www.baidu.com	百度
    http://www.taobao.com	淘宝

4.按下回车

5.结果应为：

	··<a href="http://www.baidu.com" class='link-1'>百度</a>
	··<a href="http://www.taobao.com" class='link-2'>淘宝</a>

规则
-------------------
1. $加数字表示列，已 1 开始计数，若超出列数 返回空字符
2. $99 为行号 已 1 开始计数