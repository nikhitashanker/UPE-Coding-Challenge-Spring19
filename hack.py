import requests

maze_tracker = []

#first i had right left down up
#def is_valid(dir):
	
	#if
def getcurrLoc(url):
	resp = requests.get(url) # get maze information
	body = resp.json()
	print(body)

def solve_maze(x, y, url, last_move):
	if (maze_tracker[x][y] == 1):
		return False
	maze_tracker[x][y] = 1

	headers = {'Content-type': 'application/x-www-form-urlencoded'}
	

	if (last_move != 'up'):

		resp_down = requests.post(url, data = {'action':'down'}, headers=headers) # start new session	#solve_maze()
		body_down = resp_down.json()
		result_down = body_down['result']


		if (result_down == 1):
			return True
		if (result_down == 0): 
			if (solve_maze(x, y+1, url, 'down')):
				return True
			else:
				requests.post(url, data = {'action':'up'}, headers=headers)
	if (last_move != 'left'):
		resp_right = requests.post(url, data = {'action':'right'}, headers=headers) # start new session	#solve_maze()
		body_right = resp_right.json()
		result_right = body_right['result']

		if (result_right == 1):
			return True
		if (result_right == 0): 
			if (solve_maze(x+1, y, url, 'right')):
				return True
			else:
				requests.post(url, data = {'action':'left'}, headers=headers)
	if (last_move != 'down'):
		resp_up = requests.post(url, data = {'action':'up'}, headers=headers) # start new session	#solve_maze()
		#getcurrLoc(url)
		body_up = resp_up.json()
		result_up = body_up['result']

		if (result_up == 1):
			return True
		if (result_up == 0):   
			if (solve_maze(x, y-1, url, 'up')):
				return True
			else:
				requests.post(url, data = {'action':'down'}, headers=headers)
	if (last_move != 'right'):
		resp_left = requests.post(url, data = {'action':'left'}, headers=headers) # start new session	#solve_maze()
		#getcurrLoc(url)
		body_left = resp_left.json()
		result_left = body_left['result']

		if (result_left == 1):
			return True
		if (result_left == 0): 
		 	if (solve_maze(x-1, y, url, 'left')):
		 		return True
		 	else:
		 		requests.post(url, data = {'action':'right'}, headers=headers)
	
	return False


url = 'http://ec2-34-212-54-152.us-west-2.compute.amazonaws.com' # server url
uid = '605105560' # your uid
headers = {'Content-type': 'application/x-www-form-urlencoded'}
resp = requests.post(url + '/session', data = {'uid':uid}, headers=headers) # start new session
body = resp.json()
access_token = body['token'] # retrieve access token from response body
full_url = url + '/game?token=' + access_token
resp = requests.get(url + '/game?token=' + access_token) # get maze information
body = resp.json()
print(body)

x = body['cur_loc'][0]
y = body['cur_loc'][1]

rows = body['size'][0]
cols = body['size'][1]

for row in range(rows): maze_tracker += [[0]*cols]



solve_maze(x, y, full_url, '')
getcurrLoc(full_url)