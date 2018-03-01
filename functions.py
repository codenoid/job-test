from lib import *
from config import *

"""
Define video extension, currently support : 'mp4', '3gp', 'mov', 'mkv'
`SET_ALLOWED_EXTENSIONS` will be used with `allowed_file()` to check
is this file have allowed format.
"""
ALLOWED_EXTENSIONS = ['mp4', '3gp', 'mov', 'mkv']
SET_ALLOWED_EXTENSIONS = set(ALLOWED_EXTENSIONS)


"""
define STDOUT / terminal color, if you use this bgcolors value,
make sure you close the string with `bcolors.ENDC`
"""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


"""
validate text POST method with `validation()`, this function need
list of used field and the actual post data, every key and param
will be checked
1. param validation

fields = {"video_id": 1, "video_author": "str", "video_title": "str", "video_desc": "str"}

if the POST method contain unused parameter, this function will be note that param as
error, or unused data : xxxx

if video_id contain non-numeric character, `validation()` will be note this as error
example :
```
expected type is Int, found type : String & Int for param : video_id
```
"""
def validation(fields, post):
	error = []
	for k, v in post.items():
		"""
		`next` if the key is `video_file`, because this is not for File validation
		but text-only validation
		"""
		if k == "video_file":
			next
		
		"""
		if k (key) registered in `fields`, then goto type validation, and if k (key)
		doesn't registered in `fields`, add += 1 error with message "Unused data xxkeyxx"
		"""
		if k in fields:
			if fields[k] == "str":
				if v.isalnum() or isinstance(v, str):
					next
				else:
					err = "expected type is String, found type : " + typeof(v) + " for param : " + k
					print(bcolors.FAIL + err + bcolors.ENDC)
					error.append(err)
					next

			if fields[k] == 1:
				if v.isdigit():
					next
				else:
					err = "expected type is Int, found type : " + typeof(v) + " for param : " + k
					print(bcolors.FAIL + err + bcolors.ENDC)
					error.append(err)
					next
		else:
			err = "Unused data " + k
			print(bcolors.WARNING + err + bcolors.ENDC)
			error.append(err)
			next

	ret = error if len(error) > 0 else True
	return ret


"""
simple function to check is file extension contain allowed extension
"""
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in SET_ALLOWED_EXTENSIONS


"""
to deal with sqlite (as database) & to make sure keep DRY, this function
used for inserting data to video table
"""
def insert_video(arr):
	c.execute("INSERT INTO video (video_id, video_author, video_title, video_desc, video_file) VALUES (?,?,?,?,?);", arr)
	conn.commit()


"""
function to define is `text` contain just one type or more type (currently String & Int)
example :
```
>>> typeof("tahun2018")
"String & Int"
>>> typeof("2018")
"Int"
>>> typeof("kokoal")
"String"
```
"""
def typeof(text):
	if text.isalnum():
		return "String & Int"
	elif text.isdigit():
		return "Int"
	elif text.isalpha() or isinstance(text, str):
		return "String"
	else:
		return text