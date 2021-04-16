from  flask import Flask, request, Response
import json

app = Flask(__name__)

some_data = [{'name':'Alice', 'mail':'alice@mail.com'}, 
            {'name':'Bob', 'mail':'bob@mail.com'}]

# create new data with POST method
@app.route('/create-post', methods=['POST'])
def create_post():
    if request.data:
        data = json.loads(request.data)
        some_data.append(data)
        print_some_data()
        return Response('data was added to some_data', status=200)
    else:
        return Response('data was not added', status=500)

# update already existing data with POST method
@app.route('/post-endpoint/<string:mail>', methods=['POST'])
def post_endpoint(mail):
	if request.data:
		data = json.loads(request.data)
		for i, person in enumerate(some_data):
			if person['mail'] == mail:
				some_data[i] = data
				return Response('some_data was updated', status=200)
		return Response('some_data was not updated', status=500)
	else:
		return Response('some_data was not updated', status=500)

# update already existing data with PUT method
@app.route('/put-endpoint/<string:mail>', methods=['PUT'])
def put_endpoint(mail):
	if request.data:
		data = json.loads(request.data)
		for i, person in enumerate(some_data):
			if person['mail'] == mail:
				some_data[i] = data
				return Response('some_data was updated', status=200)
		return Response('some_data was not updated', status=500)
	else:
		return Response('some_data was not updated', status=500)

# partial update with PATCH method
# update one mail from some_data dict
@app.route('/patch-endpoint/<string:mail>', methods=['PATCH'])
def patch_endpoint(mail):
	if request.data:
		data = json.loads(request.data)
		for i, person in enumerate(some_data):
			if person['mail'] == mail:
				some_data[i]['mail'] = data['mail']
				return Response('some_data was updated', status=200)
		print_some_data()
		return Response('some_data was not updated', status=500)
	else:
		return Response('some_data was not updated', status=500)

# delete data with DELETE method
@app.route('/delete-endpoint/<string:mail>', methods=['DELETE'])
def delete_endpoint(mail):
	for i, person in enumerate(some_data):
		if person['mail'] == mail:
			del some_data[i]
			return Response('the person with that mail was removed', status=200)
	# Status = 404 because the resource was not found
	return Response('some_data was not removed', status=404) 

@app.route('/delete-with-args', methods=['DELETE'])
def delete_with_args(): # find person by mail and remove from people with DELETE method
	mail = request.args.get('mail')
	for i, person in enumerate(some_data):
		if person['mail'] == mail:
			del some_data[i]
			print_some_data()
			return Response('the person with that mail was removed', status=200)
	
	# status=404 because the resource was not found
	return Response('people was not removed', status=404)

def print_some_data():
	for person in some_data:
		print(person['mail'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)