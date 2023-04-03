todos = open('todos.txt','w')

print("write This To File", file=todos)
print("Not this")
print("Hello My Name Is Gorge big one", file=todos)
print("Some random data 8898989", file=todos)
todos.close()

task = open('todos.txt')
##print("Not This", file=todos) <- ValueError: I/O operation on closed file.
for line in task:
    print(line)

task.close()

from flask import Flask, render_template,request,escape

app = Flask(__name__)

@app.route('/')
## @app.route('/JAKASSTRONA/')  http://127.0.0.1:5000/JAKASSTRONA/
def hello() ->str:
    return 'Hello Word'