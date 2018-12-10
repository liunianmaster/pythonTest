from MySql import mysqlClass
import urllib.request
from bs4 import BeautifulSoup
import json
import chardet
import pymysql
import re

def urlRequest(url):
    request = urllib.request.urlopen(url)
    res = request.read()
    
    if isinstance(res, str):
        res = res.encode('utf-8')
    else:
        charset = chardet.detect(res)
        encoding = charset['encoding']
        if encoding != None:
            res = res.decode(encoding, 'ignore')

    return res

def IsChar(ch):
    # ch = str(char)
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        return True
    else:
        return False

def JsStr2StrJson(JSstr = ""):
    jsonRet = ""
    for i in range(0, len(JSstr)):
        if i == 0:
            jsonRet += JSstr[i]
        elif JSstr[i] == '\'' or JSstr[i] == '\"':
            jsonRet += '\"'
        elif JSstr[i-1] == '{' and IsChar(JSstr[i]):
            jsonRet += '\"'
            jsonRet += JSstr[i]
        elif JSstr[i-1] == ',' and IsChar(JSstr[i]):
            jsonRet += '\"'
            jsonRet += JSstr[i]
        elif IsChar(JSstr[i-1]) and JSstr[i] == ':':
            jsonRet += '\"'
            jsonRet += JSstr[i]
        else:
            jsonRet += JSstr[i]
    return jsonRet
    
def Json2Dict(strJson):
    return json.loads(strJson)

def getWeatherByMonth(citynum, month):
    url = "http://tianqi.2345.com/t/wea_history/js/"+str(month)+"/"+str(citynum)+"_"+str(month)+".js"
    
    strJSJson = urlRequest(url)
    strJSJson = strJSJson[16:len(strJSJson)-1]
    
    # print(strJSJson)
    so = BeautifulSoup(strJSJson, "html.parser")

    strJson = JsStr2StrJson(so.text)
    
    objDict = Json2Dict(strJson)

    return objDict

def saveOverAll(cid, dictdata):
    sql = mysqlClass()
    # sql.Insert_overall(cid,dictdata)

def getChinaWeather():
    list_year = [2017,2018]
    monthMax = 12
    for year in list_year:
        year_str = str(year)
        for month in range(monthMax):
            month += 1
            month_str = str(month)
            if month < 10:
                month_str = "0"+str(month)
            print(year_str+" "+month_str)
            dealChinaWeatherData(year_str,month_str)

def dealChinaWeatherData(year_str,month_str):
    
    url = "http://d1.weather.com.cn/calendar_new/2018/101110101_201805.html?_=1543991270495"
    url = "http://d1.weather.com.cn/calendar_new/"+year_str+"/101110101_"+year_str+month_str+".html?_=1543991270495"
    
    Cookie = "vjuids=4ae6c5afe.16163817b77.0.e1a8ff117ebd2; f_city=%E8%A5%BF%E5%AE%89%7C101110101%7C; UM_distinctid=1661a3bb7b36d3-0468b2562d3a45-43480420-1fa400-1661a3bb7b5603; vjlast=1517792886.1543980903.22; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1543980904,1543989330,1543989642; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1543989667; Wa_lvt_1=1543980904,1543989279,1543989330,1543989642; Wa_lpvt_1=1543989642"
    headers = {
        'Accept': '*/*',
        # 不要采用 gzip（压缩格式），数据会变乱码
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Encoding': 'deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        # 'Cookie': Cookie,
        'Host': 'd1.weather.com.cn',
        # 'Host':'tianqi.2345.com',
        'Referer': 'http://www.weather.com.cn/weather40d/101110101.shtml',
        # 'Referer':'http://tianqi.2345.com/wea_history/57036.htm',
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
        
    }
    # _ = 随机数
    url06 = "http://d1.weather.com.cn/calendar_new/2018/101110101_201806.html?_=1544002167834"
    # Cookie06 = "vjuids=4ae6c5afe.16163817b77.0.e1a8ff117ebd2; f_city=%E8%A5%BF%E5%AE%89%7C101110101%7C; UM_distinctid=1661a3bb7b36d3-0468b2562d3a45-43480420-1fa400-1661a3bb7b5603; vjlast=1517792886.1543980903.22; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1543980904,1543989330,1543989642; Wa_lvt_1=1543980904,1543989279,1543989330,1543989642; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1544001591; Wa_lpvt_1=1544001591"
    
    # url06 = "http://tianqi.2345.com/t/wea_history/js/201803/57036_201803.js"
    req = urllib.request.Request(url=url,data=None,headers=headers)

    res = urlRequest(req)
    if isinstance(res, str):
        print('str')
    res = res.split('var fc40 = ')[1]
    res_list = json.loads(res)
    res_data = ""
    sql_db = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db = 'pythondb',
        charset = 'utf8'
    )

    for i in res_list:
        res_data = {
            'alins':i['alins'],
            'nl':i['nl'],
            'nlyf':i['nlyf'],
            'time':i['time'],
            'date':i['date'],
            'hmax':i['hmax'],
            'hmin':i['hmin'],
            'hgl':i['hgl'],
            'wk':i['wk']
        }
        # print(res_data['date']+"农历："+res_data['nlyf']+res_data['nl']+",最高气温："+res_data['hmax']+",最低气温："+res_data['hmin']+",湿度："+res_data['hgl']+ ",星期"+res_data['wk'])

        sql_insert = "INSERT INTO china_weather(date,hmax,hmin,hgl)\
        VALUES(\'%s\',\'%s\',\'%s\',\'%s\')"%(res_data['date'],"最高气温："+res_data['hmax']+"℃","最低气温："+res_data['hmin']+"℃",res_data['hgl'])
        cursor = sql_db.cursor()
        cursor.execute(sql_insert)
        cursor.close()

        sql_db.commit()

    sql_db.close()
    # print(res)


def get2345Weather():
    listMonth = [201809,201810,201811]
    cityInfo = [[1,72039],[2,72025],[3,57036]]
    cid = cityInfo[2][0] #西安
    cnumber = cityInfo[2][1]
    
    dict_city = {'sName':"西安", 'lName':"区域", 'number':57036}
    sql = mysqlClass()
    sql.showVersion()
    sql.Insert_2345City(dict_city)

    for i in listMonth:
        objDict = getWeatherByMonth(cnumber, i)
        objDictOverAll = {
            'maxWendu'  :objDict['maxWendu'],
            'minWendu'  :objDict['minWendu'],
            'avgAqi'    :objDict['avgAqi'],
            'avgbWendu' :objDict['avgbWendu'],
            'avgyWendu' :objDict['avgyWendu'],
            'city'      :objDict['city'],
            'maxAqiDate':objDict['maxAqiDate'],
            'maxAqiInfo':objDict['maxAqiInfo'],
            'maxAqiLevel':objDict['maxAqiLevel'],
            'minAqi'    :objDict['minAqi'],
            'minAqiDate':objDict['minAqiDate'],
            'minAqiInfo':objDict['minAqiInfo'],
            'minAqiLevel':objDict['minAqiLevel']
        }
        objListWea = objDict['tqInfo']
        # saveOverAll(cid,objDictOverAll)
        for j in objListWea:
            if(len(j) != 0):
                sql.Insert_2345history(cid, j)
def getPm25():
    headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36")
    city = "xian"
    url = "http://pm25.in/"+city
    data = urllib.request.urlopen(url).read().decode('utf-8')
    #构建数据更新时间的表达式
    # data_time='<div class="live_data_time">\s{1,}<p>数据更新时间：(.*?)</p>'
    data_time='<div class="live_data_time">\s{1,}<p>(.*?)</p>'

    datatime = re.compile(data_time, re.S).findall(data)
    print(datatime[0])

    so = BeautifulSoup(data, 'html.parser')
    detail = so.find_all('table',id='detail-data')[0]
    head_list = detail.find_all('thead')[0]
    
    for head in head_list:
        th_str = ""
        for i in head:
            if i != '\n':
                th_str += i.get_text() + ','
        if th_str != "":
            print("表头："+th_str)
    tbody_list = detail.find('tbody')
    for tbody in tbody_list:
        th_str = ""
        for i in tbody:
            if i != '\n':
                th_text = i.get_text()
                # replace 去除字符串内的空格和换行
                th_text = th_text.replace(' ','')
                th_text = th_text.replace('\n','')
                th_str += th_text+','
        if th_str != "":
            print(th_str)
    print("11")


if __name__ == "__main__":

    getPm25()
    # getChinaWeather()
    # get2345Weather()

