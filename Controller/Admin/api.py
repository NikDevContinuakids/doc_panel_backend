import flask
from pandas import json_normalize
import sqlalchemy
import Connection.const
from sqlalchemy.orm import session
from werkzeug.utils import redirect
import sys
import Model.models
import flask_mail
import smtplib
import cryptography.fernet
import datetime
from datetime import datetime as dt
from datetime import timedelta
import Constant.constant
import logging
import requests
import os
import traceback
from flask import Flask, jsonify, render_template, request
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask import Flask, current_app, request
from flask_mail import Mail, Message
import Common_Function.CommonFun
from Common_Function import Shared_Library as CommonModule

Session = Connection.const.connectToDatabase()
#app = flask.Flask(__name__)
#app.debug = True
#EntitySec_Blueprint = flask.Flask(__name__)
# EntitySec_Blueprint = flask.Blueprint('EntitySec_Blueprint', __name__)
# @EntitySec_Blueprint.route('/update', methods=['GET','POST'])
# def update():
#     session=Session()
#     id= flask.request.args.get('id')
#     try:
#         if flask.request.method=='GET':
#             if(id):
#                 result= Common_Function.CommonFun.convertToJson(
#                 Constant.constant.constant.EntityDtl, 
#                 session.query(Model.models.Corporate.M_Entities.ME_ID,
#                 Model.models.Corporate.M_Entities.ME_Name,
#                 Model.models.Corporate.M_Entities.ME_Nature,
#                 Model.models.Corporate.M_Entities.ME_EType,
#                 Model.models.Corporate.M_Entities.ME_CIN,
#                 Model.models.Corporate.M_Entities.ME_Business,
#                 Model.models.Corporate.M_Entities.ME_OfficeAdd,
#                 Model.models.Corporate.M_Entities.ME_PersonName,
#                 Model.models.Corporate.M_Entities.ME_Designation,
#                 Model.models.Corporate.M_Entities.ME_Authorization,
#                 Model.models.Corporate.M_Entities.ME_Contact,
#                 Model.models.Corporate.M_Entities.ME_Email,
#                 Model.models.Corporate.M_Entities.ME_Website,
#                 Model.models.Corporate.M_Entities.ME_SpclIntrst
#                 ).filter_by(ME_TCD_ID=id
#                 ).order_by(Model.models.Corporate.M_Entities.ME_TCD_ID
#                 ).all())
#             else:
#                 result= Common_Function.CommonFun.convertToJson(
#                 Constant.constant.constant.EntityDtl, 
#                 session.query(Model.models.Corporate.M_Entities.ME_ID,
#                 Model.models.Corporate.M_Entities.ME_Name,
#                 Model.models.Corporate.M_Entities.ME_Nature,
#                 Model.models.Corporate.M_Entities.ME_EType,
#                 Model.models.Corporate.M_Entities.ME_CIN,
#                 Model.models.Corporate.M_Entities.ME_Business,
#                 Model.models.Corporate.M_Entities.ME_OfficeAdd,
#                 Model.models.Corporate.M_Entities.ME_PersonName,
#                 Model.models.Corporate.M_Entities.ME_Designation,
#                 Model.models.Corporate.M_Entities.ME_Authorization,
#                 Model.models.Corporate.M_Entities.ME_Contact,
#                 Model.models.Corporate.M_Entities.ME_Email,
#                 Model.models.Corporate.M_Entities.ME_Website,
#                 Model.models.Corporate.M_Entities.ME_SpclIntrst
                
#                 ).order_by(Model.models.Corporate.M_Entities.ME_TCD_ID
#                 ).all())
#             if(len(result) == 0):
#                 return "<h1>No Record Found please check your Id(s)</h1>"
#             else:
#                 print(result)
#                 return jsonify(result)     
#         else:
#             return  "<h1>Wrong method used for this record</h1>"
#     except Exception as identifier:
#         #logging.error(identifier)
#         return "<h1>Something went wrong. Kindly retry</h1>"
#     finally:
#         session.close()