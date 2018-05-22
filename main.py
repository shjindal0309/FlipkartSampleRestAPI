from flask import Flask,render_template,request,jsonify
app = Flask(__name__)
import json 

with open('data.json') as json_file:
    json_data = json.load(json_file)
    json.dumps(json_data,indent=4)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/post",methods = ['POST'])
def post_data():
	
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

	return render_template("post.html",json=json_data)


@app.route("/get",methods = ['GET'])
def get_data():

	_id = request.args.get('id','')
	if(not _id):
		return render_template("get.html",json=json_data)
	else:
		return_list=[]
		for x in json_data['books']:
			if(int(_id) == x['id']):
				return_list.append(x)
		# return (jsonify(return_list))
		return render_template("get.html",json=return_list)

@app.route("/put",methods = ['PUT'])
def put_data():
	
	_id=request.form['id']
	author = request.form['author_name']
	title = request.form['title']

	books=json_data['books']
	books = [book for book in books if book['id'] == _id]
	
	if(not book):
		return render_template("put.html",json="No such book")

	for book in books:
		book['author'] = author
		book['title'] = title

	return render_template("put.html",json=json_data)

@app.route("/delete",methods = ['DELETE'])
def delete_data():
	if(request.method=="DELETE"):
		books = [book for book in books if book['id'] == _id]
		books.remove()

if __name__ == "__main__":
	app.run(debug=True)