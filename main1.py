from flask import Flask,render_template,request,jsonify
app = Flask(__name__)
import json 

with open('data.json') as json_file:
    json_data = json.load(json_file)
    json.dumps(json_data,indent=4)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result",methods = ['POST','GET','PUT','DELETE'])
def result():
	print(request.method)
	if(request.method=="POST"):
		# following code works
		# author = request.form['author_name']
		# title = request.form['title']
		# return render_template("result.html",author=author,title=title)
		author = request.form['author_name']
		title = request.form['title']

		if(not json_data['books']):
			json_data['books'].append({'id':1,'author':author,'title':title})
		else:
			json_data['books'].append({'id': json_data['books'][-1]['id']+1,'author':author,'title':title})

		with open('data.json','w') as json_file:
			json.dump(json_data, json_file, sort_keys=True, indent=4)

		return render_template("result1.html",json=json_data)

	# elif(request.method=="PUT"):
	# 	print("hi")
	# 	_id=request.form['id']
	# 	author = request.form['author_name']
	# 	title = request.form['title']

	# 	books=json_data['books']
	# 	books = [book for book in books if book['id'] == _id]
	# 	print(books)
	# 	return render_template("result.html",json=json)

	elif(request.method=="GET"):
		_id = request.args.get('id','')
		if(not _id):
			return render_template("result1.html",json=json_data)
		else:
			return_list=[]
			for x in json_data['books']:
				if(int(_id) == x['id']):
					return_list.append(x)
			return render_template("result1.html",json=return_list)

	# if(request.method=="PUT" and request.form['request_type']=='PUT'):

	# 	author = request.form['author_name']
	# 	title = request.form['title']
	# 	json.update({'books':[{'author':author,'title':title}]})
	# 	#_id = create_object(json)
	# 	# json.update({'books':[
	# 	return render_template("result.html",json=json)

if __name__ == "__main__":
    app.run(debug=True)
