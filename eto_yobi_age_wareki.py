# -*- coding: utf-8 -*-

import datetime
import sys

print("このスクリプトは入力された年、月、日に対応した現在の和暦、干支、曜日、年齢、数え年を返すプログラムです。\nこのスクリプトを利用して生じた不利益等には一切の責任を負いかねます。\n")

print("承諾する場合は 1 を入力して続行して下さい")

consent=bool(input())

if consent!=1:
  sys.exit()

print("\n年(西暦)を入力、もしくは 19700101 のようなフォーマットで入力して下さい")
input_char=str(input())

if int(input_char)>9999:
  year=int(input_char[:4])
  month=int(input_char[4:6])
  day=int(input_char[6:8])
  
else:
  year=int(input_char)
  print("\n月を入力して下さい")
  month=int(input())
  
  print("\n日を入力して下さい")
  day=int(input())

#ここから曜日計算
#---------------------------------------------------------------

#配列に曜日を設定
weekarray=["日","月","火","水","木","金","土"]

#年数に年数を4で割った値あまりを無視してを足す
year_calc=year+int(year/4)

#year_calcから年数を100で割った値を引く
year_calc-=int(year/100)

#year_calcに年数を400で割った値を足す
year_calc+=int(year/400)

#月に13をかけて8を足す
month_calc=month*13
month_calc+=8
month_calc=int(month_calc/5)

#year_calcとmonth_calcを足す
year_add_month_calc=year_calc+month_calc

#year_add_month_calcに日数を足す
year_add_month_calc+=day

#year_add_month_calcを7で割ったあまりを出す
weekday=year_add_month_calc%7

#変数weekにweekarrayから曜日を指定して代入
week=weekarray[weekday]
#---------------------------------------------------------------
#ここまでが曜日計算

#ここからが年齢計算
#---------------------------------------------------------------

#eto配列の添字
eto_key=(year+9)%12
#wareki配列の添字
wareki_key=0
#和暦年の保存
wareki_year=0
#年齢の保存
age=0
#数え
kazoe=0

#干支を保存する配列
eto=["亥","子","丑","寅","卯","辰","巳","牛","未","申","酉","戌"]

#和暦を保存する配列
wareki=["明治","大正","昭和","平成"]

today=datetime.date.today()

#年齢計算
if month<today.month:
  age=today.year-year
  kazoe=age+1
elif month==today.month:
  if day<today.day:
    age=today.year-year
    kazoe=age+1
  elif day==today.day:
    print("\n誕生日おめでとうございます。\n")
    age=today.year-year
    kazoe=age+1
  elif day>today.day:
    age=today.year-year-1
    kazoe=age+2
elif month>today.month:
  age=today.year-year-1
  kazoe=age+2


#和暦の対応
if year>=1867 and year<1912:
  wareki_key=0
  wareki_key=year-1867
elif year>=1912 and year<1926:
  wareki_key=2
  wareki_year=year-1911
elif year>=1926 and year<1989:
  wareki_key=2
  wareki_year=year-1925
elif year>=1989:
  wareki_key=3
  wareki_year=year-1988
elif year<1867:
  print (str(year)+"年"+str(month)+"月"+str(day)+"日は"+str(week)+"曜日です。")
  print ("この年に生まれた方は今"+str(age)+"歳で、数え年では、"+str(kazoe)+"歳になります。")
  sys.exit()
#----------------------------------------------------------------
#ここまでが年齢計算

#実行結果の表示
print ("\n"+str(year)+"年"+str(month)+"月"+str(day)+"日は"+str(week)+"曜日です。")

print ("\n"+str(year)+"年は"+str(wareki[wareki_key])+str(wareki_year)+"年であり、"+str(year)+"年"+str(month)+"月"+str(day)+"日"+"に生まれた方は現在"+str(age)+"歳で、数え年では"+str(kazoe)+"歳になります。")
