from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

@app.route('/')
def htmlindex():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("readAll.html", users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("create.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    user_id=User.save(request.form)
    print(user_id)
    user_id_last=User.get_last()
    return redirect(f'/user/show/{user_id_last[0]["id"]}')

@app.route('/user/edit/<int:id>') 
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html",user=User.get_just_one(data))

@app.route('/user/update',methods=['POST'])
def update():
    print(request.form)
    user_id=User.update(request.form)
    print(user_id)
    user_id_last=User.get_last()
    return redirect(f'/user/show/{user_id_last[0]["id"]}')

@app.route('/user/deleteInfo/<int:id>')
def deleteInfo(id):
    data ={
        "id": id
    }
    User.deleteInfo(data)
    return redirect('/users')

@app.route('/user/show/<int:id>') 
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_read_one.html",user=User.get_just_one(data))

if __name__=="__main__":
    app.run(debug=True)