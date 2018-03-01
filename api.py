from lib import *
from config import *
from functions import *

"""
serve @app.route `/videos`, with method POST (Only),
form data supported is multipart/form-data because 
we will receive non-alphanumeric (file) and alphanumeric data
"""
@app.route("/videos", methods=["POST"])
def _videos():
	"""
	fields used for POST data validation, and will be used with
	`validation()`, `1` mean in dict value is stand for Int type
	and `"str"` value is used for representing String type
	"""
	fields = {"video_id": 1, "video_author": "str", "video_title": "str", "video_desc": "str"}

	post = {}
	for k, v in request.form.items():
		post[k] = v

	"""
	custom form validation, needed var : fields and post
	if validation does false, return 400 (Bad Request) code
	note : https://www.ietf.org/rfc/rfc2616.txt
	"""
	validate = validation(fields, post)
	if isinstance(validate, bool) == False:
		status = {"status": "failed", "code": 400, "msg": "failed to validate", "error": validate}
		return make_response(jsonify(status), 400)

	"""
	if this POST method doesn't contain param : `video_file`, response
	with 400 (Bad Request)
	"""
	if 'video_file' not in request.files:
		status = {"status": "failed", "code": 400, "msg": "POST doesn't contain `video_file` param"}
		return make_response(jsonify(status), 400)


	"""
	define file if POST method contain param `video_file`
	"""
	file = request.files['video_file']


	"""
	check when the file is empty, return 400 (Bad Request), with message
	`video_file value is empty`
	"""
	if file.filename == '':
		status = {"status": "failed", "code": 400, "msg": "video_file value is empty"}
		return make_response(jsonify(status), 400)


	"""
	get extension from a filename, split string with `.` and get last value
	in list, example :

	```
	filename = "myvideo.mp4"
	filename = filename.split(".") # => ["myvideo", "mp4"]
	fileext  = filename[-1] # => "mp4"
	```
	"""
	ext = str(file.filename).split(".")[-1]


	"""
	generate random filename for saving to storage, based on `time.time()` (UNIX)
	secure_filename() is for converting file name to safe name to be stored on a 
	regular file system and passed to :func:`os.path.join`
	secure_filename example :

    >>> secure_filename("My cool movie.mov")
    'My_cool_movie.mov'
    >>> secure_filename("../../../etc/passwd")
    'etc_passwd'
    >>> secure_filename(u'i contain cool \xfcml\xe4uts.txt')
    'i_contain_cool_umlauts.txt'
	
	new_name example : myvideo-1747281722.mp4
	"""
	file_name = secure_filename(str(file.filename)).split(".")[0] 
	new_name  = file_name + "-" + str(int(time.time())) + "." + ext

	"""
	generate list for sqlite document, order value :
	`video_id, video_author, video_title, video_desc, video_file`
	"""
	data = [post["video_id"], post["video_author"], post["video_title"], post["video_desc"], new_name]

	try:
		insert_video(data)
	except sqlite3.Error as e:
		status = {"status": "failed", "code": 500, "msg": "internal server error " + str(e)}
		return make_response(jsonify(status), 500)

	"""
	return True if `file.filename` have alowed file extension
	and save the file with `file.save` to UPLOAD_FOLDER path
	"""
	if file and allowed_file(file.filename):
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
	else:
		status = {"status": "failed", "code": 400, "msg": "Unallowed file extension, allowed ext is : " + ", ".join(ALLOWED_EXTENSIONS)}
		return make_response(jsonify(status), 400)

	"""
	return successfully uploaded msg, status_code = 200
	"""
	status = {"status": "success", "code": 200, "msg": "successfully uploaded"}
	return make_response(jsonify(status), 200)

"""
custom 404 page, represented as json return type, with status_code 404
and message : requested url not found
"""
@app.errorhandler(404)
def page_not_found(e):
	status = {"status": "failed", "code": 404, "msg": "requested url not found"}
	return make_response(jsonify(status), 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3500)