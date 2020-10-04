from django.shortcuts import render
from django.http import HttpResponse
from pyformlang.cfg import Production, Variable, Terminal, CFG, Epsilon


# Create your views here.
def home(request):
  return render(request,'home.html',{'name':'jaya'})
def index(request):
  return render(request,'index.html')

import re
def add(request):
  str_1 = request.GET["num1"]
  str_2 = request.GET["num2"]
  
  
  regular_ex = re.compile(str_1)
  match_input = regular_ex.match(str_2)
  try:
    answer = match_input.group()
  except AttributeError:
    answer=None
  if (answer == str_2):
      result="YES"
  else:
      result="NO"
  return render(request,'home.html',{'result':result})

def grammar(request):
  var1_1 = request.GET.get("numb1")
  var1_1=str(":" if var1_1 is None else var1_1)
  var1 = Variable(var1_1)
  str1 = request.GET.get("numb2")
  str1 =str(":" if str1 is None else str1)
  terimal=[]
  list1=[]
  for i in str1:
      if(i.islower()):
          terimal.append(Terminal(i))
      if(i.islower()):
          list1.append(Terminal(i))
      else:
          list1.append(Variable(i))
  #print(list1)
  #print(var1)

  var2_1 = request.GET.get("numb3")
  var2_1=str(":" if var2_1 is None else var2_1)
  var2=Variable(var2_1)

  str2= request.GET.get("numb4")
  str2 =str(":" if str2 is None else str2)
  list2=[]
  for i in str2:
      if(i.islower()):
          terimal.append(Terminal(i))
      if(i.islower()):
          list2.append(Terminal(i))
      else:
          list2.append(Variable(i))
  #print(list2)

  var3_1 = request.GET.get("numb5")
  var3_1=str(":" if var3_1 is None else var3_1)
  var3= Variable(var3_1)
  str3= request.GET.get("numb6")
  str3 =str(":" if str3 is None else str3)
  list3=[]
  for i in str3:
      if(i.islower()):
          terimal.append(Terminal(i))
      if(i.islower()):
          list3.append(Terminal(i))
      else:
          list3.append(Variable(i))
  #print(list3)

  var4_1 = request.GET.get("numb7")
  var4_1=str(":" if var4_1 is None else var4_1)
  var4 = Variable(var4_1)
  str4 = request.GET.get("numb8")
  str4 =str(":" if str4 is None else str4)
  list4=[]
  for i in str4:
      if(i.islower()):
          terimal.append(Terminal(i))
      if(i.islower()):
          list4.append(Terminal(i))
      else:
          list4.append(Variable(i))
  #print(list4)

  var5_1 = request.GET.get("numb9")
  var5_1=str(":" if var5_1 is None else var5_1)
  var5 = Variable(var5_1)
  str5 = request.GET.get("numb10")
  str5 =str(":" if str5 is None else str5)
  list5=[]
  for i in str5:
      if(i.islower()):
          terimal.append(Terminal(i))
      if(i.islower()):
          list5.append(Terminal(i))
      else:
          list5.append(Variable(i))
  #print(list5)
  terminal=set(terimal)
  #print(terminal)
  p0 = Production(var1, list1)
  p1 = Production(var2, list2)
  p2 = Production(var3, list3)
  p4 = Production(var4, list4)
  p5 = Production(var5, list5)
  #print(p0)
  #print(p1)
  #print(p2)
  #print(p4)
  #print(p5)

  vari = {var1,var2,var3,var4,var5}
  variable=set()
  for var in vari:
      if (var):
          variable.add(var)
  #print(variable)
  cfg = CFG(variable, 
          terminal, 
          "S", 
          {p0, p1, p2, p4, p5})
  ans = request.GET.get("numb11")
  ans =str(":" if ans is None else ans)
  list_ans=[]
  for j in ans:
    list_ans.append(j)
  val=cfg.contains(list_ans)
  if(val):
    answer_1="YES"
  else:
    answer_1="NO"
  return render(request,'grammar.html',{'result':answer_1})
