@app.route('api/token')
@auth.login_required
def get_auth_token():
	token =  g.user.generate_auth_token()
	return jsonify({'token': token.decode('ascii')})