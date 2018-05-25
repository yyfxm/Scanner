#-*- coding:utf-8 -*-

import requests,re,random

#sql注入的测试语句，根据页面返回结果判断有无sql注入漏洞
BOOLEAN_TESTS = (" AND %d=%d"," OR NOT (%d=%d)")

DBMS_ERRORS = {
	"MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"valid MySQL result", r"MySqlClient\."),
	"PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"valid PostgreSQL result", r"Npgsql\."),
	"Microsoft SQL Server": (r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*mssql_.*", r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}", r"(?s)Exception.*\WSystem\.Data\.SqlClient\.", r"(?s)Exception.*\WRoadhouse\.Cms\."),
	"Microsoft Access": (r"Microsoft Access Driver", r"JET Database Engine", r"Access Database Engine"),
	"Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Oracle.*Driver", r"Warning.*\Woci_.*", r"Warning.*\Wora_.*"),
	"IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error", r"\bdb2_\w+\("),
	"SQLite": (r"SQLite/JDBCDriver", r"SQLite.Exception", r"System.Data.SQLite.SQLiteException", r"Warning.*sqlite_.*", r"Warning.*SQLite3::", r"\[SQLITE_ERROR\]"),
	"Sybase": (r"(?i)Warning.*sybase.*", r"Sybase message", r"Sybase.*Server message.*"),
}
#一个字典，用来存储各种数据库的特征

def sqlcheck(url):
	if(not url.find("?")):
		return False
	#先构造一个错误的url使报错
	_url = url + "%29%28%22%27"
	_content = request.get(_url).text
	for (dbms,regex) in ((dbms,regex) for dbms in DBMS_ERRORS for regex in DBMS_ERRORS[dbms]):
		if(re.search(regex,_content)):
			return True
	content = {}
	content["origin"] = request.get(_url).text
	for test_payload in BOOLEAN_TESTS:
		RANDINT = random.randint(1,255)
		_url = url + test_payload%(RANDINT,RANDINT)
		content["true"] = downloader.request(_url)
		_url = url + test_payload%(RANDINT,RANDINT+1)
		content["false") = downloader.request(_url)
		if content["origin"] == content["true"] != content["false"]:
			return "sql found: %" %url	 
