def app(env, start_response):
	print(env)
	params = env["QUERY_STRING"].split('&')
	data = []
	
	start_response("200 OK",[("Content-type","text/plain")])
	return [data]
