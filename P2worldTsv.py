# -*- coding: utf-8 -*- 
import sublime, sublime_plugin
import re

def getIn(list,index,i) :
	if index=="$" :
		return str(i)
	index=int(index)
	if len(list)>=index :
		return list[index-1]
	else :
		return ""

class P2worldTsvCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.edit=edit
		self.selectRange=self.view.sel()[0]
		self.tplArr=re.split(r'\$(\d+|\$)',self.view.substr(self.selectRange),re.U|re.S)		


		self.view.window().show_input_panel('insert tsv',"", self.on_done_data,None,None)


	def on_done_data(self,msg) :
		if re.match(r'^\d{1,3}$',msg):
			arr=[[] for i in range(int(msg))]
		else:
			# 消除末尾回车
			j=len(msg)
			while True :
				j-=1
				if not (msg[j] in ("\n","\r")) :
					break
					
			msg=msg[0:j+1]

			# 格式化xsl数据
			data=msg.splitlines();
			arr=[]
			for row in data:
				rowArr=row.split("\t")
				arr.append(rowArr)

		# 生成结果
		resultArr=[]
		index=0
		for row in arr :
			index+=1
			newRow=[]
			for i in range(0,len(self.tplArr)) :
				if i&1 :
					newRow.append(getIn(row,self.tplArr[i],index))
				else :
					newRow.append(self.tplArr[i])
			resultArr.append("".join(newRow))
		self.on_all_done(resultArr)


	def on_all_done(self,resultArr) :
		self.view.replace(self.edit, self.selectRange,"\n".join(resultArr) )


