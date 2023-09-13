import datetime
import math
import os
import hmac
from sqlalchemy import func 
import sqlalchemy

from sqlalchemy.orm import session
import Common_Function.CommonFun
import Connection.const
import hashlib
import flask
#import crypto
import sys
import base64
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

import Constant.constant
import Model.models

UPLOAD_FOLDER = '/home/shamsher'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class CommonFunction:
    def __init__(self):
        pass

    def get_my_ip(self):
        return str(flask.request.remote_addr)


# It will hash a string using sha512 method
def hashText(text):
    """
        Basic hashing function for a text using random unique salt.
    """
    # salt = uuid.uuid4().hex
    return hashlib.sha512(text.encode()).hexdigest()


def matchHashedText(hashedText, providedText):
    """
        Check for the text in the hashed text
    """
    _hashedText, salt = hashedText.split(':')
    return _hashedText == hashlib.sha256(salt.encode() + providedText.encode()).hexdigest()

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def encryptData(plainText):
    cipherText = base64.b64encode(plainText.encode())
    return cipherText.decode()


def decryptData(cipherText):
    plainText = base64.b64decode(cipherText.encode())
    return plainText.decode()


def cntAllFileFolderOnRoot(path):
    countFileFolder = []
    numberOfFolder = 0
    numberOfFile = 0
    for root, dirs, files in os.walk(path):
        for d in dirs:
            numberOfFolder = numberOfFolder+1
        for f in files:
            numberOfFile = numberOfFile+1
    countFileFolder.append(str(numberOfFolder))
    countFileFolder.append(str(numberOfFile))
    return countFileFolder


def cntCurrentFileFolderOnRoot(path):
    countCurrentFileFolder = []
    numberOfFolder = 0
    numberOfFile = 0
    for root, dirs, files in os.walk(path):
        for d in dirs:
            numberOfFolder = numberOfFolder+1
        for f in files:
            numberOfFile = numberOfFile+1
        break
    countCurrentFileFolder.append(str(numberOfFolder))
    countCurrentFileFolder.append(str(numberOfFile))
    return countCurrentFileFolder


Session = Connection.const.connectToDatabase()
session=Session()

def convertToJson(jsonFields, data):
    try:
        convertTxtToJson = [{col: getattr(
            d, col) for col in jsonFields} for d in data]
    except Exception as identifier:
        print('No parameter is passed.')
    return convertTxtToJson
def getOrg():
    session=Session()
    try:
        getOrg= convertToJson(
                Constant.constant.constant.getOrglist,
                session.query(Model.models.Application.M_Organisation.MOID.label('key'),
                            Model.models.Application.M_Organisation.MO_Name.label('label')
                                ).filter_by(MO_IsActive=1,MO_IsDeleted=0).order_by(Model.models.Application.M_Organisation.MO_Name).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getOrg

def getCountry():
    session=Session()
    try:
        getCountry= convertToJson(
                Constant.constant.constant.GetCountryid,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=1,TD_IsActive=1,TD_IsDeleted=0).order_by(Model.models.Application.T_Details.TD_Name).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getCountry

def getState():
    session=Session()
    try:
        getState = convertToJson(
                Constant.constant.constant.GetStateid,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=2,TD_IsActive=1,TD_IsDeleted=0).order_by(Model.models.Application.T_Details.TD_Name).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getState

def City():
    session=Session()
    try:
        getCity = convertToJson(
                Constant.constant.constant.GetCityid,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=3,TD_IsActive=1,TD_IsDeleted=0).order_by(Model.models.Application.T_Details.TD_Name).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getCity

def getPackagetype():
    session=Session()
    try:
        getpackage= convertToJson(
                Constant.constant.constant.getPackagetype,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=19,TD_IsActive=1,TD_IsDeleted=0).order_by(Model.models.Application.T_Details.TD_Name).all()
                        )
        
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getpackage

def getDiscountType():
    session=Session()
    try:
        getDiscount= convertToJson(
                Constant.constant.constant.getDiscountType,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=20,TD_IsActive=1,TD_IsDeleted=0).order_by(Model.models.Application.T_Details.TD_Name).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getDiscount
          
def getClinic():
    session=Session()
    try:
        getClinic= convertToJson(
                Constant.constant.constant.getClinics,
                session.query(Model.models.Application.M_Branch.MBID.label('key'),
                            Model.models.Application.M_Branch.MB_Name.label('label')
                            ).filter_by(MB_IsActive=1,MB_IsDeleted=0).order_by(Model.models.Application.M_Branch.MB_Name).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getClinic
                  
def getPaymentMode():
    session=Session()
    try:
        getPayment= convertToJson(
                Constant.constant.constant.getPaymentMode,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=21,TD_IsActive=1,TD_IsDeleted=0).order_by(Model.models.Application.T_Details.TD_Name).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getPayment

def getservice():
    session=Session()
    try:               
        getService=convertToJson(
                Constant.constant.constant.getService,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=15,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getService

def getPatient():
    session=Session()
    try:               
        getPatient= convertToJson(
                        Constant.constant.constant.getPatients,
                        session.query(Model.models.Application.M_Patient.MPID.label('key'),
                                    Model.models.Application.M_Patient.MP_Name.label('label')
                                        ).filter_by(MP_IsActive=1,MP_IsDeleted=0).order_by(Model.models.Application.M_Patient.MP_Name).all()
                                )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getPatient

def getPackage():
    session=Session()
    try:               
        getPackage= convertToJson(
                        Constant.constant.constant.getPackage,
                        session.query(Model.models.Application.M_Package.MPID.label('key'),
                                    Model.models.Application.M_Package.MP_Name.label('label')
                                        ).filter_by(MP_IsActive=1,MP_IsDeleted=0).order_by(Model.models.Application.M_Package.MP_Name).all()
                                )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getPackage

def Validation():
    session=Session()
    try:
        Validation= convertToJson(
                Constant.constant.constant.Validation,
                session.query(Model.models.Application.M_validations.MV_Name.label('name'),
                            Model.models.Application.M_validations.MV_Pattern.label('pattern'),
                            Model.models.Application.M_validations.MV_Message.label('message')
                                ).filter_by(MV_Type='required',MV_IsActive=1,MV_IsDeleted=0).order_by(Model.models.Application.M_validations.MVID).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Validation

def Checked():
    session=Session()
    try:
        Validation= convertToJson(
                Constant.constant.constant.checked,
                session.query(Model.models.Application.M_validations.MV_Name.label('name')
                                ).filter_by(MV_Type='checked',MV_IsActive=1,MV_IsDeleted=0).order_by(Model.models.Application.M_validations.MVID).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Validation


def yesno():
    session=Session()
    try:               
        getService=convertToJson(
                Constant.constant.constant.yesno,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=22,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getService

def Loudness():
    session=Session()
    try:               
        getService=convertToJson(
                Constant.constant.constant.Loudness,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=29,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getService



def Delivery():
    session=Session()
    try:               
        getService=convertToJson(
                Constant.constant.constant.Delivery,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=23,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getService

def DeliveryLocation():
    session=Session()
    try:               
        getService=convertToJson(
                Constant.constant.constant.DeliveryLocation,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=24,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getService
def Pregnancies():
    session=Session()
    try:               
        getService=convertToJson(
                Constant.constant.constant.Pregnancies,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=25,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getService
def ChildBirth():
    session=Session()
    try:               
        getService=convertToJson(
                Constant.constant.constant.ChildBirth,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=26,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getService

def BirthCry():
    session=Session()
    try:               
        getService=convertToJson(
                Constant.constant.constant.BirthCry,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=27,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getService

def education():
    session=Session()
    try:               
        getService=convertToJson(
                Constant.constant.constant.education,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=28,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getService


def familyType():
    session=Session()
    try:               
        getService=convertToJson(
                Constant.constant.constant.familyType,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=29,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getService

def achievement():
    session=Session()
    try:               
        getachievement=convertToJson(
                Constant.constant.constant.achievement,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=30,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getachievement

def consistancy():
    session=Session()
    try:               
        getconsistancy=convertToJson(
                Constant.constant.constant.consistancy,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=31,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getconsistancy

def review():
    session=Session()
    try:               
        getreview=convertToJson(
                Constant.constant.constant.review,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=32,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getreview


def Aroused():
    session=Session()
    try:               
        getAroused=convertToJson(
                Constant.constant.constant.Aroused,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=33,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getAroused

def Attendance():
    session=Session()
    try:               
        getAttendance=convertToJson(
                Constant.constant.constant.Attendance,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=34,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getAttendance

def verbalComm():
    session=Session()
    try:               
        getverbalComm=convertToJson(
                Constant.constant.constant.verbalComm,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=35,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getverbalComm

def Cognitive():
    session=Session()
    try:               
        getCognitive=convertToJson(
                Constant.constant.constant.Cognitive,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=36,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getCognitive

def Loudness():
    session=Session()
    try:               
        getLoudness=convertToJson(
                Constant.constant.constant.Loudness,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=37,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getLoudness

def Quality():
    session=Session()
    try:               
        getQuality=convertToJson(
                Constant.constant.constant.Quality,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=38,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getQuality

def Observation():
    session=Session()
    try:               
        getObservation=convertToJson(
                Constant.constant.constant.Observation,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=39,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getObservation

def Articulation():
    session=Session()
    try:               
        getArticulation=convertToJson(
                Constant.constant.constant.Articulation,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=39,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getArticulation

def LipsMovements():
    session=Session()
    try:               
        TongueMovements=convertToJson(
                Constant.constant.constant.LipsMovements,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=42,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return TongueMovements

def TongueAppearance():
    
    session=Session()
    try:               
        TongueAppearance=convertToJson(
                Constant.constant.constant.TongueAppearance,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=43,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return TongueAppearance

def TongueMovements():
    session=Session()
    try:               
        TongueMovements=convertToJson(
                Constant.constant.constant.TongueMovements,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=44,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return TongueMovements

def TeethAppearance():
    session=Session()
    try:               
        TeethAppearance=convertToJson(
                Constant.constant.constant.TeethAppearance,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=45,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return TeethAppearance

def TeethMovements():
    session=Session()
    try:               
        TeethMovements=convertToJson(
                Constant.constant.constant.TeethMovements,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=46,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return TeethMovements

def HardPalateAppearance():
    session=Session()
    try:               
        HardPalateAppearance=convertToJson(
                Constant.constant.constant.HardPalateAppearance,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=47,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HardPalateAppearance

def SoftPalateAppearance():
    session=Session()
    try:               
        SoftPalateAppearance=convertToJson(
                Constant.constant.constant.SoftPalateAppearance,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=48,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return SoftPalateAppearance

def SoftPalateMovements():
    session=Session()
    try:               
        SoftPalateMovements=convertToJson(
                Constant.constant.constant.SoftPalateMovements,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=49,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return SoftPalateMovements

def UvulaAppearance():
    session=Session()
    try:               
        UvulaAppearance=convertToJson(
                Constant.constant.constant.UvulaAppearance,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=50,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return UvulaAppearance

def UvulaMovements():
    session=Session()
    try:               
        UvulaMovements=convertToJson(
                Constant.constant.constant.UvulaMovements,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=51,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return UvulaMovements

def MandibleAppearance():
    session=Session()
    try:               
        MandibleAppearance=convertToJson(
                Constant.constant.constant.MandibleAppearance,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=52,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return MandibleAppearance

def MandibleMovements():
    session=Session()
    try:               
        MandibleMovements=convertToJson(
                Constant.constant.constant.MandibleMovements,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=53,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return MandibleMovements

def Drooling():
    session=Session()
    try:               
        Drooling=convertToJson(
                Constant.constant.constant.Drooling,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=54,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Drooling

def Designation():
    session=Session()
    try:
        Designation= convertToJson(
                Constant.constant.constant.Designation,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=135,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Designation

def Comprehension():
    session=Session()
    try:               
        Comprehension=convertToJson(
                Constant.constant.constant.Comprehension,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=56,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Comprehension

def Expression():
    session=Session()
    try:               
        Expression=convertToJson(
                Constant.constant.constant.Expression,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=55,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Expression

def ShoulderScapular():
    session=Session()
    try:               
        ShoulderScapular=convertToJson(
                Constant.constant.constant.ShoulderScapular,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=56,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return ShoulderScapular

def ShoulderandScapular():
    session=Session()
    try:               
        ShoulderandScapular=convertToJson(
                Constant.constant.constant.ShoulderandScapular,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=58,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return ShoulderandScapular

def ShouldernScapular():
    session=Session()
    try:               
        ShouldernScapular=convertToJson(
                Constant.constant.constant.ShouldernScapular,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=59,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return ShouldernScapular

def RibcageandChest():
    session=Session()
    try:               
        RibcageandChest=convertToJson(
                Constant.constant.constant.RibcageandChest,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=60,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return RibcageandChest

def Trunk():
    session=Session()
    try:               
        Trunk=convertToJson(
                Constant.constant.constant.Trunk,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=61,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Trunk
def Trunks():
    session=Session()
    try:               
        Trunks=convertToJson(
                Constant.constant.constant.Trunks,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=62,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Trunks

def PelvicComplexRight():
    session=Session()
    try:               
        PelvicComplexRight=convertToJson(
                Constant.constant.constant.PelvicComplexRight,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=63,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return PelvicComplexRight

def PelvicComplexLeft():
    session=Session()
    try:               
        PelvicComplexLeft=convertToJson(
                Constant.constant.constant.PelvicComplexLeft,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=64,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return PelvicComplexLeft

def HipjointRotation():
    session=Session()
    try:               
        HipjointRotation=convertToJson(
                Constant.constant.constant.HipjointRotation,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=65,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HipjointRotation

def BaseofSupport():
    session=Session()
    try:               
        BaseofSupport=convertToJson(
                Constant.constant.constant.BaseofSupport,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=66,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return BaseofSupport

def CenterofMass():
    session=Session()
    try:               
        CenterofMass=convertToJson(
                Constant.constant.constant.CenterofMass,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=67,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return CenterofMass
def Strategiesposture():
    session=Session()
    try:               
        Strategiesposture=convertToJson(
                Constant.constant.constant.Strategiesposture,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=68,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Strategiesposture
def MuscleArchitecture():
    session=Session()
    try:               
        MuscleArchitecture=convertToJson(
                Constant.constant.constant.MuscleArchitecture,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=69,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return MuscleArchitecture

def Howdoesthe():
    session=Session()
    try:               
        Howdoesthe=convertToJson(
                Constant.constant.constant.Howdoesthe,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=70,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Howdoesthe

def Childgenerallyperformsactivitie():
    session=Session()
    try:               
        Childgenerallyperformsactivitie=convertToJson(
                Constant.constant.constant.Childgenerallyperformsactivitie,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=71,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Childgenerallyperformsactivitie
def Rangespeedmovement():
    session=Session()
    try:               
        Rangespeedmovement=convertToJson(
                Constant.constant.constant.Rangespeedmovement,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=72,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Rangespeedmovement

def StabilityMobility():
    session=Session()
    try:               
        StabilityMobility=convertToJson(
                Constant.constant.constant.StabilityMobility,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=73,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return StabilityMobility

def Initiation():
    session=Session()
    try:               
        Initiation=convertToJson(
                Constant.constant.constant.Initiation,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=74,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Initiation

def Sustenance():
    session=Session()
    try:               
        Sustenance=convertToJson(
                Constant.constant.constant.Sustenance,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=75,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Sustenance

def Termination():
    session=Session()
    try:               
        Termination=convertToJson(
                Constant.constant.constant.Termination,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=76,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Termination
def ContractionConcentric():
    session=Session()
    try:               
        ContractionConcentric=convertToJson(
                Constant.constant.constant.ContractionConcentric,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=77,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return ContractionConcentric

def ContractionIsometric():
    session=Session()
    try:               
        ContractionIsometric=convertToJson(
                Constant.constant.constant.ContractionIsometric,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=78,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return ContractionIsometric

def ContractionEccentric():
    session=Session()
    try:               
        ContractionEccentric=convertToJson(
                Constant.constant.constant.ContractionEccentric,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=79,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return ContractionEccentric


def RightLeft():
    session=Session()
    try:               
        RightLeft=convertToJson(
                Constant.constant.constant.RightLeft,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=80,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return RightLeft

def PoorGood():
    session=Session()
    try:               
        PoorGood=convertToJson(
                Constant.constant.constant.PoorGood,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=81,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return PoorGood

def Skeletalcomments():
    session=Session()
    try:               
        Skeletalcomments=convertToJson(
                Constant.constant.constant.Skeletalcomments,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=82,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Skeletalcomments

def modulationissues():
    session=Session()
    try:               
        modulationissues=convertToJson(
                Constant.constant.constant.modulationissues,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=83,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return modulationissues

def Visualsystem():
    session=Session()
    try:               
        Visualsystem=convertToJson(
                Constant.constant.constant.Visualsystem,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=84,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Visualsystem

def Oromotorsystem():
    session=Session()
    try:               
        Oromotorsystem=convertToJson(
                Constant.constant.constant.Oromotorsystem,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=85,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Oromotorsystem

def Postivenegative():
    session=Session()
    try:               
        Postivenegative=convertToJson(
                Constant.constant.constant.Postivenegative,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=86,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Postivenegative

def Couldnotresist():
    session=Session()
    try:               
        Couldnotresist=convertToJson(
                Constant.constant.constant.Couldnotresist,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=87,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Couldnotresist

def HARS():
    session=Session()
    try:               
        HARS=convertToJson(
                Constant.constant.constant.HARS,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=88,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HARS

def PHQ():
    session=Session()
    try:               
        PHQ=convertToJson(
                Constant.constant.constant.PHQ,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=89,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return PHQ

# def HRDSDepressedMood():
#     try:               
#         HRDSDepressedMood=convertToJson(
#                 Constant.constant.constant.HRDSDepressedMood,
#                 session.query(Model.models.Application.T_Details.TDID.label('key'),
#                             Model.models.Application.T_Details.TD_Name.label('label')
#                                 ).filter_by(M_Details_MDID=90,TD_IsActive=1,TD_IsDeleted=0).all()
#                         )
#         session.commit()
#     except Exception as identifier:
#         print('No parameter is passed.')
#     return HRDSDepressedMood

def HRDSDepressedMood():
    session=Session()
    try:               
        HRDSDepressedMood=convertToJson(
                Constant.constant.constant.HRDSDepressedMoods,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=90,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HRDSDepressedMood

def HRDSFeelingGuilt():
    session=Session()
    try:               
        HRDSFeelingGuilt=convertToJson(Constant.constant.constant.HRDSFeelingGuilt,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=91,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HRDSFeelingGuilt 
def HRDSSucide():
    session=Session()
    try:               
        HRDSSucide=convertToJson(
                Constant.constant.constant.HRDSSucide,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=92,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HRDSSucide
def HRDSInsomnia():
    session=Session()
    try:               
        HRDSInsomnia=convertToJson(
                Constant.constant.constant.HRDSInsomnia,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=93,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HRDSInsomnia

def HRDSMidNight():
    session=Session()
    try:               
        HRDSMidNight=convertToJson(
                Constant.constant.constant.HRDSMidNight,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=94,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HRDSMidNight

def HRDSEarlyMorning():
    session=Session()
    try:               
        HRDSEarlyMorning=convertToJson(
                Constant.constant.constant.HRDSEarlyMorning,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=95,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HRDSEarlyMorning
def HRDSWork():
    session=Session()
    try:               
        HRDSWork=convertToJson(
                Constant.constant.constant.HRDSWork,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=96,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HRDSWork
def HRDSRetardation():
    session=Session()
    try:               
        HRDSRetardation=convertToJson(
                Constant.constant.constant.HRDSRetardation,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=97,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HRDSRetardation
def HRDSAgitation():
    session=Session()
    try:               
        HRDSAgitation=convertToJson(
                Constant.constant.constant.HRDSAgitation,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=98,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HRDSAgitation
def HRDSPsychic():
    session=Session()
    try:               
        HRDSPsychic=convertToJson(
                Constant.constant.constant.HRDSPsychic,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=99,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HRDSPsychic
def HRDSAnxietySomatic():
    session=Session()
    try:               
        HRDSAnxietySomatic=convertToJson(
                Constant.constant.constant.HRDSAnxietySomatic,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=100,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HRDSAnxietySomatic
def HRDSSomatic():
    session=Session()
    try:               
        HRDSSomatic=convertToJson(
                Constant.constant.constant.HRDSSomatic,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=101,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HRDSSomatic
def HDRSGeneralSomatic():
    session=Session()
    try:               
        HDRSGeneralSomatic=convertToJson(
                Constant.constant.constant.HDRSGeneralSomatic,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=102,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HDRSGeneralSomatic
def HDRSLossOfLibido():
    session=Session()
    try:               
        HDRSLossOfLibido=convertToJson(
                Constant.constant.constant.HDRSLossOfLibido,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=103,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HDRSLossOfLibido
def HDRSHypochondriasis():
    session=Session()
    try:               
        HDRSHypochondriasis=convertToJson(
                Constant.constant.constant.HDRSHypochondriasis,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=104,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HDRSHypochondriasis
def HDRSLossofWeight():
    session=Session()
    try:               
        HDRSLossofWeight=convertToJson(
                Constant.constant.constant.HDRSLossofWeight,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=105,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HDRSLossofWeight
def HDRSInsight():
    session=Session()
    try:               
        HDRSInsight=convertToJson(
                Constant.constant.constant.HDRSInsight,
                session.query(Model.models.Application.T_Details.TD_Name.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=106,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return HDRSInsight

def Started():
    session=Session()
    try:               
        Started=convertToJson(
                Constant.constant.constant.Started,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=107,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Started

def todayfeeling():
    session=Session()
    try:               
        todayfeeling=convertToJson(
                Constant.constant.constant.todayfeeling,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=108,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return todayfeeling

def dotoday():
    session=Session()
    try:               
        dotoday=convertToJson(
                Constant.constant.constant.dotoday,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=109,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return dotoday

def FollowAfter():
    session=Session()
    try:               
        FollowAfter=convertToJson(
                Constant.constant.constant.FollowAfter,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=110,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return FollowAfter

def ServiceStatus():
    session=Session()
    try:               
        ServiceStatus=convertToJson(
                Constant.constant.constant.ServiceStatus,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=111,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return ServiceStatus

def getClinicRights(ids):
    session=Session()
    try:
        
        Branch = session.query(Model.models.Application.M_AssignRole.M_Users_MUID,
                            Model.models.Application.M_AssignRole.M_Branch_MBID
                            ).filter_by(M_Users_MUID=int(ids),MP_IsActive=1,MP_IsDeleted=0
                            ).group_by(Model.models.Application.M_AssignRole.M_Branch_MBID).all()
        Branch_MBID = [b['M_Branch_MBID'] for b in Branch]
        getClinicRights= convertToJson(
                Constant.constant.constant.getClinicRights,
                session.query(Model.models.Application.M_Branch.MBID.label('key'),
                            Model.models.Application.M_Branch.MB_Name.label('label')
                            ).filter(Model.models.Application.M_Branch.MBID.in_(Branch_MBID)
                            ).filter_by(MB_IsActive=1,MB_IsDeleted=0).order_by(Model.models.Application.M_Branch.MB_Name).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getClinicRights

def getDoctor(branchId):
    session=Session()
    try: 
        
        # getDoctor= session.query(sqlalchemy.func.concat(Model.models.Application.M_DoctorDetails.MDD_FirstName,' ',Model.models.Application.M_DoctorDetails.MDD_LastName)
        #                                 ).filter_by(MDD_IsActive=1,MDD_IsDeleted=0
        #                         ).order_by(Model.models.Application.M_DoctorDetails.MDD_FirstName).all()
        # session.commit()                       
        getDoctor= session.query(func.concat(Model.models.Application.M_DoctorDetails.MDD_FirstName, ' ', Model.models.Application.M_DoctorDetails.MDD_LastName,' ',Model.models.Application.M_DoctorDetails.MDD_Suffix).label('MDD_FirstName'),
                                 Model.models.Application.M_DoctorDetails.MDDID
                                        # ).filter_by(MDD_IsActive=1,MDD_IsDeleted=0,MDD_Clinic = int(branchId)
                                        ).filter_by(MDD_IsActive=1,MDD_IsDeleted=0
                                        ).filter(Model.models.Application.M_DoctorDetails.MDD_Clinic.contains([branchId])
                                ).order_by(Model.models.Application.M_DoctorDetails.MDD_Suffix,Model.models.Application.M_DoctorDetails.MDD_FirstName).all()
        session.commit()                      

    except Exception as identifier:
        print('No parameter is passed.')
    return getDoctor

def Coupons():
    session=Session()
    try:               
        Coupons=convertToJson(
                Constant.constant.constant.Coupons,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=112,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Coupons

def getDoctorList():
    session=Session()
    try: 
        
        getDoctorList= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.getDoctorList,
                        session.query(Model.models.Application.M_DoctorDetails.MDDID.label('key'),
                                    Model.models.Application.M_DoctorDetails.MDD_FirstName.label('label')
                                        ).filter_by(MDD_IsActive=1,MDD_IsDeleted=0).order_by(Model.models.Application.M_DoctorDetails.MDD_FirstName).all()
                                )
        session.commit()

    except Exception as identifier:
        print('No parameter is passed.')
    return getDoctorList


def AddPartnerOrganisation():
    session=Session()
    try: 
        
        AddPartnerOrganisation= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.AddPatrnerOrganisationlist,
                        session.query(Model.models.Application.M_PartnerOrg.MPID.label('key'),
                                    Model.models.Application.M_PartnerOrg.OrgName.label('label')
                                        ).filter_by(MP_IsActive=1,MP_IsDeleted=0).order_by(Model.models.Application.M_PartnerOrg.OrgName).all()
                                )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return AddPartnerOrganisation

def getBranch():
    session=Session()
    try:
        getBranch= convertToJson(
                Constant.constant.constant.getBranch,
                session.query(Model.models.Application.M_Branch.MBID.label('key'),
                            Model.models.Application.M_Branch.MB_Name.label('label')
                            ).filter_by(MB_IsActive=1,MB_IsDeleted=0).order_by(Model.models.Application.M_Branch.MB_Name).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getBranch

def Status():
    session=Session()
    try:
        Status= convertToJson(
                Constant.constant.constant.Status,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=114,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Status

def Title():
    session=Session()
    try:
        Title= convertToJson(
                Constant.constant.constant.Title,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=113,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Title

def Code():
    session=Session()
    try:
        Code= convertToJson(
                Constant.constant.constant.Code,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=115,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Code

def ExpenseStatus():
    session=Session()
    try:
        ExpenseStatus= convertToJson(
                Constant.constant.constant.ExpenseStatus,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=116,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return ExpenseStatus

def Gender():
    session=Session()
    try:
        Gender= convertToJson(
                Constant.constant.constant.Gender,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=4,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Gender

def BloodGroup():
    session=Session()
    try:
        BloodGroup= convertToJson(
                Constant.constant.constant.BloodGroup,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=7,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return BloodGroup

# def Rights():
#     session=Session()
#     try:
#         Rights= session.query(Model.models.Application.M_Rights.MR_Name
#                                         ).filter_by(MR_IsActive=1,MR_IsDeleted=0
#                                 ).all()
#         session.commit() 
#     except Exception as identifier:
#         print('No parameter is passed.')
#     return Rights

def Pages():
    session=Session()
    try:
        Pages= convertToJson(
                Constant.constant.constant.Pages,
                session.query(Model.models.Application.M_Pages.MPID.label('S. No'),
                              Model.models.Application.M_Pages.MPID.label('PageId'),
                              Model.models.Application.M_Pages.MP_PageName.label('Page'),
                              Model.models.Application.M_Pages.MP_PageParent.label('Menu')
                                        ).filter_by(MP_IsActive=1,MP_IsDeleted=0
                                ).all())
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Pages

def getPageId(pageUrl):
    session=Session()
    try:
        Pages= session.query(Model.models.Application.M_Pages.MPID.label('S. No'),
                              Model.models.Application.M_Pages.MPID.label('PageId'),
                              Model.models.Application.M_Pages.MP_PageName.label('Page'),
                              Model.models.Application.M_Pages.MP_PageParent.label('Menu')
                                        ).filter_by(MP_IsActive=1,MP_IsDeleted=0,MP_PageParent=pageUrl
                                ).all()
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Pages[0].PageId

def getpolicyId(branchId,userId):
    session=Session()
    try:
        Pages= session.query(Model.models.Application.M_AssignRole.M_Users_MUID,
                              Model.models.Application.M_AssignRole.M_Policy_MPID,
                              Model.models.Application.M_AssignRole.M_Branch_MBID
                            ).filter_by(MP_IsActive=1,MP_IsDeleted=0,M_Branch_MBID=branchId,M_Users_MUID=userId
                                ).order_by(Model.models.Application.M_AssignRole.MARID.desc()).all()
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Pages[0].M_Policy_MPID


def UserType():
    session=Session()
    try:
        UserType= convertToJson(
                Constant.constant.constant.UserType,
                session.query(Model.models.Application.M_UserType.MU_UserType.label('key'),
                            Model.models.Application.M_UserType.MU_UserName.label('label')
                            ).filter_by(MU_IsActive=1,MU_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return UserType

def RightsCols():
    session=Session()
    try:
        RightsCols= convertToJson(
                Constant.constant.constant.RightsCols,
                session.query(Model.models.Application.M_Rights.MR_Name.label('name'),
                            Model.models.Application.M_Rights.MR_Label.label('label'),
                            Model.models.Application.M_Rights.MR_required.label('required'),
                            Model.models.Application.M_Control.MC_ControlType.label('type')
                            ).filter_by(MR_IsActive=1,MR_IsDeleted=0
                            ).join(Model.models.Application.M_Control, Model.models.Application.M_Control.MCID==Model.models.Application.M_Rights.MR_Type                        
                                        ).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return RightsCols

def Users():
    session=Session()
    try:
        getClinic= convertToJson(
                Constant.constant.constant.Users,
                session.query(Model.models.Application.M_Users.MUID.label('key'),
                            Model.models.Application.M_Users.MU_Name.label('label')
                            ).filter_by(MU_IsActive=1,MU_IsDeleted=0).order_by(Model.models.Application.M_Users.MU_Name).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return getClinic

def Policy():
    session=Session()
    try:
        Policy= convertToJson(
                Constant.constant.constant.Policy,
                session.query(Model.models.Application.M_Policy.MPID.label('key'),
                            Model.models.Application.M_Policy.MP_PolicyName.label('label')
                            ).filter_by(MP_IsActive=1,MP_IsDeleted=0
                                        ).order_by(Model.models.Application.M_Policy.MP_PolicyName).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Policy


def servicePackageType():
    session=Session()
    try:
        servicePackageType= convertToJson(
                Constant.constant.constant.servicePackageType,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=118,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return servicePackageType

def serviceStatus():
    session=Session()
    try:
        serviceStatus= convertToJson(
                Constant.constant.constant.serviceStatus,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=119,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return serviceStatus

def PromotionType():
    session=Session()
    try:
        PromotionType= convertToJson(
                Constant.constant.constant.PromotionType,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=120,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return PromotionType

def ServiceCatType():
    session=Session()
    try:
        UserType= convertToJson(
                Constant.constant.constant.ServiceCatType,
                session.query(Model.models.Application.M_Service.MSID.label('key'),
                            Model.models.Application.M_Service.MS_CategoryName.label('label')
                            ).filter_by(MS_IsActive=1,MS_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return UserType

def Inventorytype():
    session=Session()
    try:
        Inventorytype= convertToJson(
                Constant.constant.constant.Inventorytype,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=121,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Inventorytype

def Months():
    session=Session()
    try:
        Months= convertToJson(
                Constant.constant.constant.Months,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=122,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Months


def Years():
    session=Session()
    try:
        Years= convertToJson(
                Constant.constant.constant.Years,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=123,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Years

def ProductCatalogType():
    session=Session()
    try:
        ProductCatalogType= convertToJson(
                Constant.constant.constant.ProductCatalogType,
                session.query(Model.models.Application.M_ProductCatalogCateg.MPCID.label('key'),
                            Model.models.Application.M_ProductCatalogCateg.MPC_CategoryName.label('label')
                            ).filter_by(MPC_IsActive=1,MPC_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return ProductCatalogType

def CatelogItemtype():
    session=Session()
    try:
        CatelogItemtype= convertToJson(
                Constant.constant.constant.CatelogItemtype,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                            ).filter_by(M_Details_MDID=124,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return CatelogItemtype

def MedecineType():
    session=Session()
    try:               
        Coupons=convertToJson(
                Constant.constant.constant.MedecineType,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=125,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Coupons

def RoutesType():
    session=Session()
    try:               
        Coupons=convertToJson(
                Constant.constant.constant.MedecineType,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=126,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Coupons


def timesADayType():
    session=Session()
    try:               
        Coupons=convertToJson(
                Constant.constant.constant.MedecineType,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=127,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Coupons

def DurationType():
    session=Session()
    try:               
        Coupons=convertToJson(
                Constant.constant.constant.MedecineType,
                session.query(Model.models.Application.T_Details.TDID.label('key'),
                            Model.models.Application.T_Details.TD_Name.label('label')
                                ).filter_by(M_Details_MDID=128,TD_IsActive=1,TD_IsDeleted=0).all()
                        )
        session.commit()
    except Exception as identifier:
        print('No parameter is passed.')
    return Coupons
