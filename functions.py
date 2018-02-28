from lib import *
from config import *

ALLOWED_EXTENSIONS = ['mp4', '3gp', 'mov', 'mkv']
SET_ALLOWED_EXTENSIONS = set(ALLOWED_EXTENSIONS)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def validation(fields, post):
	error = []
	for k, v in post.iteritems():
		if k == "video_file":
			next
		if k in fields:
			if fields[k] == "str":
				if v.isalnum() or isinstance(v, basestring):
					next
				else:
					err = "expected type is str(), found type : " + typeof(v) + " for param : " + k
					print(bcolors.FAIL + err + bcolors.ENDC)
					error.append(err)
					next

			if fields[k] == 1:
				if v.isdigit():
					next
				else:
					err = "expected type is int(), found type : " + typeof(v) + " for param : " + k
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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in SET_ALLOWED_EXTENSIONS

def insert_video(arr):
	c.execute("INSERT INTO video (video_id, video_author, video_title, video_desc, video_file) VALUES (?,?,?,?,?);", arr)
	conn.commit()

def typeof(text):
	if text.isalnum():
		return "String & Int"
	elif text.isdigit():
		return "Int"
	elif text.isalpha():
		return "String"
	else:
		return text