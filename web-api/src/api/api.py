from flask import Flask, Blueprint, Response, request, jsonify

# creation for blueprint 
api = Blueprint('api', __name__, url_prefix='/api/v1')

# route for blueprint
@api.route('/')
def api_entrada():
    return Response('Hello World from API!', status=200)

#route for prompt, and file for parser with IA
#For the files is archive .pdf and .docx

@api.route('/prompt', methods=['POST'])
def prompt():
    try:
        if request.method =="POST":
            # from Json extract the prompt and the file
            prompt_input = request.json['prompt']
            # file = request.json['file']
            if prompt_input != None:
                return jsonify({"message": "Prompt and file received"}), 200
            else:
                return jsonify({"message": "Prompt or file not received"}), 400
        else:
            return jsonify({"message": "Method not allowed"}), 405
    except Exception as e:
        return jsonify({"message": "Error in the request"}), 400
    



    


