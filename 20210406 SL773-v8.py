####生产建设项目土壤流失量测算导则(SL773-2018)
import math
##植被破坏型一般扰动地表
def Myz():
  R,K,B,E,Tv = map(float,input("请依次(共5)输入计算单元降雨侵蚀力因子R、土壤可蚀性因子K、植被覆盖因子B、工程措施因子E、耕作措施因子T，并以逗号隔开:").split(","))
  lamda_x,a,m = map(float,input("请依次(共3)输入计算单元斜坡长度λx、坡度θ、坡长指数m，并以逗号隔开：").split(","))
  aa=math.cos(math.radians(a))
  lamda=lamda_x*aa
  if lamda >= 100:
    lamda = 100
  Ly_v=(lamda/20)**m
  aa_2 = math.sin(math.radians(a))
  Sy_v=-1.5+17/(1+2.72**(2.3-6.1*aa_2))
  S=float(input("请输入计算单元宽度(单位:m):"))
  A = 10**(-4)*S*lamda_x*aa
  Myz_v=R*K*Ly_v*Sy_v*B*E*Tv*A
  lst = [Myz_v,100*Myz_v,R,K,Ly_v,lamda,lamda_x,m,a,Sy_v,B,E,Tv,S]
  return lst





  
  

##地表翻扰型土壤流失量计算
def Myd():
  telling = input("地表翻扰后土壤可蚀性因子增大系数N是否为实测获得，是输Y，否输N：")
  if telling == "Y":
    soil_loss_bf = float(input("请输入扰动前径流小区土壤流失量(单位:t):"))
    soil_loss_af = float(input("请输入扰动后径流小区土壤流失量(单位:t):"))
    N = soil_loss_af/soil_loss_bf
  else:
    N = 2.13
  R,K,B,E,Tv = map(float,input("请依次(共5)输入计算单元降雨侵蚀力因子R、土壤可蚀性因子K、植被覆盖因子B、工程措施因子E、耕作措施因子T，并以逗号隔开:").split(","))
  Kyd_v = N*K
  lamda_x,a,m = map(float,input("请依次(共3)输入计算单元斜坡长度λx、坡度θ、坡长指数m，并以逗号隔开：").split(","))
  aa=math.cos(math.radians(a))
  lamda=lamda_x*aa
  if lamda >= 100:
    lamda = 100
  Ly_v=(lamda/20)**m
  aa_2 = math.sin(math.radians(a))
  Sy_v=-1.5+17/(1+2.72**(2.3-6.1*aa_2))
  S=float(input("请输入计算单元宽度(单位:m):"))
  A = 10**(-4)*S*lamda_x*aa
  Myd_v=R*Kyd_v*Ly_v*Sy_v*B*E*Tv*A
  lst = [Myd_v,Myd_v*100,R,Kyd_v,K,N,Ly_v,lamda,lamda_x,m,a,Sy_v,B,E,Tv,S]
  return lst



  

  
  
  
  
###水力作用下工程开挖面土壤流失量测算
##上方无来水工程开挖面土壤流失量
def Mkw():
  SIL,CLA,p = map(float,input("请依次(共3)输入粉粒含量SIL、黏粒含量CLA、土体密度(单位：克/立方厘米)，并以逗号隔开：").split(","))
  Gkw = 0.004*2.72**((4.28*SIL*(1-CLA))/p)
  R,lamda_x,a = map(float,input("请依次(共3)输入计算单元降雨侵蚀力因子R、土质斜坡长度λx、坡度θ,并以逗号隔开：").split(","))
  aa = math.cos(math.radians(a))
  lamda = lamda_x*aa
  if lamda >= 100:
    lamda = 100
  Lkw = (lamda/5)**(-0.57)
  aa_2 = math.sin(math.radians(a))
  Skw = 0.80*aa_2+0.38
  S=float(input("请输入计算单元宽度(单位:m):"))
  A = 10**(-4)*S*lamda_x*aa
  Mkw_v = R*Gkw*Lkw*Skw*A
  lst = [Mkw_v,Mkw_v*100,Gkw,SIL,CLA,p,R,Lkw,lamda,lamda_x,a,Skw,S]
  return lst

  


##上方有来水工程开挖面土壤流失量
def Mky():
  W = float(input("请输入上方单宽次来水总量(≤3 m³/m):"))
  Fky = 10000*W**0.95
  SIL,CLA,p = map(float,input("请依次(共3)输入粉粒含量SIL、黏粒含量CLA、土体密度(单位：克/立方厘米)，并以逗号隔开：").split(","))
  Gky = 0.004*2.72**(1.86*SIL*(1-CLA)/p)
  lamda_x,a = map(float,input("请依次(共2)输入计算单元土质斜坡长度λx、坡度θ,并以逗号隔开：").split(","))
  aa = math.cos(math.radians(a))
  lamda = lamda_x*aa
  if lamda >= 100:
    lamda = 100
  Lky = (lamda/5)**(-0.73)
  aa_2 = math.sin(math.radians(a))
  Sky = 1.18*aa_2+0.10
  Gkw = 0.004*2.72**((4.28*SIL*(1-CLA))/p)
  R= float(input("请输入计算单元降雨侵蚀力因子R:"))
  Lkw = (lamda/5)**(-0.57)
  Skw = 0.80*aa_2+0.38
  S=float(input("请输入计算单元宽度(单位:m):"))
  A = 10**(-4)*S*lamda_x*aa
  Mkw_v = R*Gkw*Lkw*Skw*A
  Mky_v = Fky*Gky*Lky*Sky*A + Mkw_v
  lst = [Mky_v,Mky_v*100,Gky,SIL,CLA,p,Fky,W,Lky,lamda,lamda_x,a,Sky,S]
  return lst
 


  
##工程堆积土壤流失量计算
##上方无来水工程堆积体土壤流失量计算
def Mdw():
  X,R = map(float,input("请依次(共2)输入工程堆积形态因子X、计算单元降雨侵蚀力因子R，并以逗号隔开：").split(","))
  a1,b1,delta = map(float,input("请依次(共3)输入上方无来水工程堆积体土石质因子系数a1、b1、计算单元侵蚀面土体砾石含量重量百分数δ,并以逗号隔开:").split(","))
  Gdw = a1*2.72**(b1*delta)
  lamda_x,a,d1,f1 = map(float,input("请依次(共4)输入计算单元斜坡长度λx、坡度θ、上方无来水工程堆积体坡度因子系数d1、上方无来水工程堆积体坡长因子系数f1,并以逗号隔开：").split(","))
  aa = math.cos(math.radians(a))
  lamda = lamda_x*aa
  if lamda >= 100:
    lamda = 100
  Sdw = (a/25)**d1
  Ldw = (lamda/5)**f1
  S=float(input("请输入计算单元宽度(单位:m):"))
  A = 10**(-4)*S*lamda_x*aa
  Mdw_v = X*R*Gdw*Ldw*Sdw*A
  lst = [Mdw_v,100*Mdw_v,Gdw,a1,b1,delta,R,X,Ldw,lamda,lamda_x,f1,a,Sdw,d1,S]
  return lst




##上方有来水工程堆积体土壤流失量计算
def Mdy():
  X,R = map(float,input("请依次(共2)输入工程堆积形态因子X、计算单元降雨侵蚀力因子R，并以逗号隔开：").split(","))
  a1,b1,delta = map(float,input("请依次(共3)输入上方无来水工程堆积体土石质因子系数a1、b1、计算单元侵蚀面土体砾石含量重量百分数δ,并以逗号隔开:").split(","))
  Gdw = a1*2.72**(b1*delta)
  lamda_x,a,d1,f1 = map(float,input("请依次(共4)输入计算单元斜坡长度λx、坡度θ、上方无来水工程堆积体坡度因子系数d1、上方无来水工程堆积体坡长因子系数f1,并以逗号隔开：").split(","))
  aa = math.cos(math.radians(a))
  lamda = lamda_x*aa
  if lamda >= 100:
    lamda = 100
  Sdw = (a/25)**d1
  Ldw = (lamda/5)**f1
  S=float(input("请输入计算单元宽度(单位:m):"))
  A = 10**(-4)*S*lamda_x*aa
  W = float(input("请输入上方单宽次来水总量(≤1.5m³/m):"))
  Fdy = 10000*W**0.95
  a2,b2,delta = map(float,input("请依次(共3)输入上方有来水工程堆积体土石质因子系数a2、b2、计算单元侵蚀面土体砾石含量重量百分数δ,并以逗号隔开:").split(","))
  Gdy = a2*2.72**(b2*delta)
  d2,f2 = map(float,input("请依次(共2)输入上方有来水工程堆积体坡度因子系数d2、上方无来水工程堆积体坡长因子f2,并以逗号隔开：").split(","))
  Sdy = (a/25)**d2
  Ldy = (lamda/5)**f2
  Mdw_v = X*R*Gdw*Ldw*Sdw*A
  Mdy_v = Fdy*Gdy*Ldy*Sdy*A + Mdw_v
  lst = [Mdy_v,100*Mdy_v,Gdy,a2,b2,delta,Fdy,W,Ldy,lamda,lamda_x,f2,a,Sdy,d2,S]
  return lst



##综合计算
def cal(): 
  begin = int(input("请输入数字选择对应计算方法：\n\t1.植被破坏型\n\t2.地表翻扰型\n\t3.上方无来水开挖\n\t4.上方有来水开挖\n\t5.上方无来水堆积\n\t6.上方有来水堆积"))
  if begin == 1:
    variable = ["土壤流失量","土壤侵蚀模数","降雨侵蚀力因子","土壤可蚀性因子","坡长因子","投影坡长","斜坡坡长","坡长指数","坡度","坡度因子","植被覆盖因子","工程措施因子","耕作措施因子","计算单元宽度"]
    variable_v = Myz()
  elif begin == 2:
    variable_v = Myd()
    variable = ["土壤流失量","土壤侵蚀模数","降雨侵蚀力因子","翻扰后土壤可蚀性因子","土壤可蚀性因子","增加系数","坡长因子","投影坡长","斜坡坡长","坡长指数","坡度","坡度因子","植被覆盖因子","工程措施因子","耕作措施因子","计算单元宽度"]
  elif begin == 3:
    variable_v = Mkw()
    variable = ["土壤流失量","土壤侵蚀模数","无来水开挖面土石质因子","粉粒含量","黏粒含量","土体密度","降雨侵蚀力因子","无来水开挖面坡长因子","投影坡长","斜坡坡长","坡度","无来水开挖面坡度因子","计算单元宽度"]  
  elif begin == 4:
    variable_v = Mky()
    variable = ["土壤流失量","土壤侵蚀模数","有来水开挖土质因子","粉粒含量","黏粒含量","土体密度","有来水开挖面径流冲蚀力因子","上方单宽次来水总量","有来水开挖面坡长因子","投影坡长","斜坡坡长","坡度","有来水开挖面坡度因子","计算单元宽度"]
  elif begin == 5:
    variable_v = Mdw()
    variable = ["土壤流失量","土壤侵蚀模数","土石质因子","土石质因子系数","土石质因子系数","土体砾石含量","降雨侵蚀力因子","形态因子","坡长因子","投影坡长","斜坡坡长","坡长因子系数","坡度","坡度因子","坡度因子系数","计算单元宽度"]
  else:
    variable_v = Mdy()
    variable = ["土壤流失量","土壤侵蚀模数","有来水堆积土石质因子","有来水堆积土石质因子系数","有来水堆积土石质因子系数","土体砾石含量","有来水堆积体径流冲蚀力因子","上方单宽次来水总量","有来水堆积体坡长因子","投影坡长","斜坡坡长","有来水堆积体坡长因子系数","坡度","有来水堆积坡度因子","有来水堆积体坡度因子系数","计算单元宽度"]
  district = input("请输入计算单元分区名称：")
  import xlsxwriter
  directory = input("请输入保存路径，用/分级(示例:F:/20210405.xlsx)：")
  workbook=xlsxwriter.Workbook(directory, {'in_memory': True})
  sheet1 = workbook.add_worksheet("chart")
  bold=workbook.add_format()
  bold.set_bold()
  title = ["项目",district]
  data = [variable,variable_v]
 # mychart = workbook.add_chart({'type':'column'})
  sheet1.write_row('G1',title,bold)
  sheet1.write_column('G2',data[0])
  sheet1.write_column('H2',data[1])
  workbook.close()
  






 
