# encoding: utf-8

from exts import db
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT


class Testline(db.Model):
    __tablename__ = 'testline'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    test_line_name = db.Column(db.String(50), nullable=False)
    owner_name = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(50), nullable=True)
    control_pc_ip = db.Column(db.String(20), nullable=True)
    pc_account = db.Column(db.String(20), nullable=True)
    pc_pwd = db.Column(db.String(50), nullable=True)
    mplane_ip = db.Column(db.String(20), nullable=False)
    bts_id = db.Column(db.String(20), nullable=False)
    enb_position = db.Column(db.String(20), nullable=True)
    hw_infor = db.Column(db.String(20), nullable=True)
    update_time = db.Column(db.DateTime, default=datetime.now)



class Module(db.Model):
    __tablename__ = 'module'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    module_name = db.Column(db.String(20), nullable=False)
    module_sn = db.Column(db.String(20), nullable=False)
    module_product_code = db.Column(db.String(20), nullable=False)
    module_position = db.Column(db.String(20), nullable=False)
    update_time = db.Column(db.DateTime,default=datetime.now)
    test_line_id = db.Column(db.Integer,db.ForeignKey('testline.id'))
    owner = db.relationship('Testline',backref=db.backref('module'))


