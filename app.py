# 使用PYTHON FLASK與MSSQL後，試寫實現 新增/修改/刪除等功能
from flask import Flask, render_template, url_for, request, redirect
import config as db
import time

app = Flask(__name__)


###############   index.html    ###########################


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        USER_NAME = request.form['USER_NAME']
        USER_PHONE = request.form['USER_PHONE']
        USER_MAIL = request.form['USER_MAIL']
        USER_ADD = request.form['USER_ADD']

        if USER_NAME != '' and USER_PHONE != '' and USER_MAIL != '' and USER_ADD != '':
            try:
                db.cursor.execute(
                    "insert into TESTTABLE (USER_NAME,USER_PHONE,USER_MAIL,USER_ADD,USER_DATETIME)" +
                    "values (?,?,?,?,?);",
                    (USER_NAME, USER_PHONE, USER_MAIL, USER_ADD, time.strftime("%Y%m%d %H%M%S", time.localtime())))
                db.conn.commit()
                return redirect('/')
            except:
                return 'add error.'
        else:
            return '各欄位不可空白。'

    else:
        datas = db.cursor.execute(
            "select ID,USER_NAME,USER_PHONE,USER_MAIL,USER_ADD,USER_DATETIME " +
            "from TESTTABLE",
        )
        return render_template('index.html', datas=datas, htmTitle='INDEX')

###############   delete.html    ####################


@app.route('/delete/<int:ID>')
def delete(ID):
    try:
        db.cursor.execute(
            "delete from TESTTABLE where ID = ?;", (ID)
        )
        db.conn.commit()
    except:
        return '刪除出現錯誤。'
    return redirect('/')

###############   update.html    ####################


@app.route('/update/<int:ID>', methods=['GET', 'POST'])
def update(ID):
    data = db.cursor.execute(
        "select ID,USER_NAME,USER_PHONE,USER_MAIL,USER_ADD,USER_DATETIME " +
        "from TESTTABLE where id =?;", (ID)
    )

    if request.method == 'POST':
        USER_NAME = request.form['USER_NAME']
        USER_PHONE = request.form['USER_PHONE']
        USER_MAIL = request.form['USER_MAIL']
        USER_ADD = request.form['USER_ADD']

        if USER_NAME != '' and USER_PHONE != '' and USER_MAIL != '' and USER_ADD != '':
            try:
                db.cursor.execute(
                    "update TESTTABLE set USER_NAME=?,USER_PHONE=?, USER_MAIL=?, USER_ADD=? WHERE ID =?;",
                    (USER_NAME, USER_PHONE, USER_MAIL, USER_ADD, ID))
                db.conn.commit()
                return redirect('/')
            except:
                return 'update error.'
        else:
            return '各欄位不可空白。'
    else:
        return render_template('update.html', data=data, htmTitle='UPDATE')


if __name__ == '__main__':
    app.run(debug=True)
