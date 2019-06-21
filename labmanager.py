from flask import Flask, render_template, request, jsonify
from sqlalchemy import desc

import config
import PB_V2
from exts import db
from models import Testline

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/testlinemanagement/',methods=['GET','POST'])
def testline():
    if request.method == 'GET':
        testline_list = Testline.query.order_by(desc(Testline.id)).all()
        return render_template('testline.html', testlines = testline_list)
    else:

        testline_name = request.form.get('testline_name')
        controlpc_ip = request.form.get('controlpc_ip')
        pc_account = request.form.get('pc_account')
        pc_password = request.form.get('pc_password')
        owner_name = request.form.get('owner_name')
        btsid = request.form.get('btsid')
        mplane_ip = request.form.get('mplane_ip')
        hwinfor = request.form.get('hwinfor')
        print hwinfor
        newtestline = Testline(
            test_line_name=testline_name,
            owner_name=owner_name,
            control_pc_ip=controlpc_ip,
            pc_account=pc_account,
            pc_pwd=pc_password,
            bts_id=btsid,
            mplane_ip=mplane_ip,
            hw_infor=hwinfor
        )
        db.session.add(newtestline)
        db.session.commit()
        return jsonify({"message": "Testline is already sucessfully updated!"})


@app.route('/deltestline/',methods=['POST'])
def deltestline():
    testline_id = request.form.get('testline_id')
    testline = Testline.query.filter(Testline.id == testline_id).first()
    if testline:
        db.session.delete(testline)
        db.session.commit()
        return jsonify({"message": "Testline is already sucessfully deleted!"})
    else:
        return jsonify({"message": "Testline is not exist"})


@app.route('/updatetestline/',methods=['POST'])
def updatetestline():
    testline_id = request.form.get('testline_id')
    testline = Testline.query.filter(Testline.id == testline_id).first()
    if testline:
        testline.test_line_name = request.form.get('testline_name')
        testline.control_pc_ip = request.form.get('controlpc_ip')
        testline.pc_account = request.form.get('pc_account')
        testline.pc_pwd = request.form.get('pc_password')
        testline.owner_name = request.form.get('owner_name')
        testline.bts_id = request.form.get('btsid')
        testline.mplane_ip = request.form.get('mplane_ip')
        testline.hw_infor = request.form.get('hwinfor')
        db.session.commit()
        return jsonify({"message": "Rule is already sucessfully updated!"})
    else:
        return jsonify({"message": "Testline is not exist"})


if __name__ == '__main__':
    app.run()
