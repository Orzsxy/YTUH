{"name":"Wes",
 "places_lives":["US","Spain","China"],
 "pet":null,
 "siblings":[{"name":"Scott","age":25,"pet":"Zuko"},
 				{"name":"Kenvi","age":33,"pet":"Cisco"}
			 ]
	
}
 result = json.loads(examples\\obj)
 # json对象中的键都是字符串形式

# Py对象转化为json:
asjson = json.dumps(result)

siblings = DataFrame(result['siblings'],columns = ['name','age'])
