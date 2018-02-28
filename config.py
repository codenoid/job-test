from lib import *
"""
Sqlite3 used because it's simple, and you just dealing with
fopen(), lol 
"""
conn = sqlite3.connect("./db.sqlite", check_same_thread=False)

"""
convert list to dictionary (+ column name), column name come from
cursor (`c`) description 
https://stackoverflow.com/a/41956666/9137919
Example :
```
list = [["1colval1", "1colval2", "1colval3"]]
dict = [{"1key1": "1colval1", "1key2": "1colval2", "1key3": "1colval3"}]
```
"""
conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])


"""
make a cursor
"""
c = conn.cursor()


"""
do not serve static file, because API doesn't need that
`static_folder=None` will remove/disable default `static` folder
"""
app = Flask(__name__, static_folder=None)


UPLOAD_FOLDER = './upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER