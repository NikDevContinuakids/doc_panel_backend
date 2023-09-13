import datetime
from logging import makeLogRecord
import logging
import math
import os
import hmac
#from application import mail
from sqlalchemy.orm import session
from sqlalchemy.sql.expression import false
import Common_Function.CommonFun
import Common_Function.MailFun
import Connection.const
import Model.models
import hashlib
import flask
#import crypto
import sys
import base64
import Constant.constant
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import threading

from flask import copy_current_request_context, jsonify
#from flask_mail import Mail
from flask_mail import  Message , Mail
#
#from app import mail

#mail = Mail()

Session = Connection.const.connectToDatabase()

#This is send registration confirmation mail to Doctor, Therapist and Others
# def SendRegistration_Mail(Name,UserName,Password,URL):
#     session=Session()
#     try:
#         # getAdminEmailID=Admin_Mail_Dtls()
#         # Admin_MailID=getAdminEmailID[0]
#         getSupportDtls=App_SupportDtls()
#         Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
#         CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
#         getMailCredential=Mail_Credential()
#         Sender_Mail=getMailCredential[0].MMC_From_MailID
#         Sender_Pwd=getMailCredential[0].MMC_Password
#         Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
#         Mail_host=getMailCredential[0].MMC_MailHost
#         Mail_Port=getMailCredential[0].MMC_MailPort
#         Mail_ISSSL= True #getMailCredential[0].MMC_ISSSL
#         MAIL_ISTLS= True
#         Reply_To=getMailCredential[0].MMC_ReplyTo
#         CC_MailID=getMailCredential[0].MMC_CC_MailID
#         BCC_MailID=getMailCredential[0].MMC_BCC_MailID
#         LinkUrl = getSupportDtls[0].MTD_URL
        
def SendRegistration_Mail(Name,email,UserName,Password,URL):
    session=Session()
    try:
        # getAdminEmailID=Admin_Mail_Dtls()
        # Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL= True #getMailCredential[0].MMC_ISSSL
        MAIL_ISTLS= True
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        
#changing the Password Cycle
        mail_body=  """
        <!doctype html>
                    <html>
                    <head>
                    <meta charset="utf-8" />
                    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <link rel="icon" type="image/png" href="favicon.png" />
                    <title>Your Registration is Successful!</title>
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center>
                    <a href='"""+URL+"""' target="_blank"><img src='http://3.111.190.80:8081/static/Mailer/continua_logo.png' alt="Continua Kids" title="Continua Kids"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                    </center>


                    <table align="center" width="500" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                    <tbody><tr>
                    <td align="center" colspan="2">
                    <h3><span data-markjs="true" class="markgkk7swyt2 _2mvHg_8QQFEuo2e0RlZLXB">Congratulations</span> """+Name+"""<br>

                    <span style="font-size:16px;">Your Registration is Successful !</span></h3>
                    </td>
                    </tr>
                    <tr>
                    <td align="center" colspan="2"><img data-imagetype="External" src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/success.png" width="60" height="60" style="padding:0 5px;"></td>
                    </tr>
					<tr>
                    <td width="40%" style="background-color:#f1f1f1;">URL:</td>
                    <td style="background-color:#f1f1f1;"><b>"""+URL+"""</b></td>
                    </tr>
                    <tr>
                    <td width="40%" style="background-color:#f1f1f1;">User Name:</td>
                    <td style="background-color:#f1f1f1;"><b>"""+UserName+"""</b></td>
                    </tr>
					<tr>
                    <td width="40%" style="background-color:#f1f1f1;">Password:</td>
                    <td style="background-color:#f1f1f1;"><b>"""+Password+"""</b></td>
                    </tr>
					
                    

                        <tr>
                        <td  colspan="2">
						
                            <p style="margin-top:50px; color:#999; font-size:12px;">If you believe you received this email in error, please contact <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a>.</p>
                            <p style="color:#999; font-size:12px;">Thank you, Click here to visit <a href='"""+URL+"""' target="_blank" style="color:#18aef4; font-size:12px;">Continua Kids</a>!</p></td>
                        </tr>
                    </tbody>
                    </table>
                    <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>6012, DLF phase 4, Sector 28, Gurugram<br>
                        </small></p>

                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Continua Kids</p>
                    </body>
                    </html>
                    """


        #The mail addresses and password
        sender_address = Sender_Mail#'vipulvict@gmail.com'
        sender_pass = Sender_Pwd#'8544388788'
        To_Add=email
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        #receiver_address=UserName
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        #message['From'] = Sender_DisplayName + f''+sender_address +''#sender_address
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Your Registration is Successful!'   #The subject line
        #The body and the attachments for the mail
        #message.attach(MIMEText(mail_content, 'plain'))
        message.attach(MIMEText(mail_body,'html'))
        text = message.as_string()
        # print(text)
        #Create SMTP session for sending the mail
        #session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session = smtplib.SMTP(Mail_host, Mail_Port) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        #print('Mail Sent')
    except Exception as identifier:
        print(identifier)
    finally:
        pass

def SendChangePassword_Mail(Name,email,Password):
    session=Session()
    try:
        # getAdminEmailID=Admin_Mail_Dtls()
        # Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL= True #getMailCredential[0].MMC_ISSSL
        MAIL_ISTLS= True
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        
#changing the Password Cycle
        mail_body=  """
        <!doctype html>
                    <html>
                    <head>
                    <meta charset="utf-8" />
                    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <link rel="icon" type="image/png" href="favicon.png" />
                    <title>Password Changed Successful!</title>
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center>
                    <img src='http://3.111.190.80:8081/static/Mailer/continua_logo.png' alt="Continua Kids" title="Continua Kids"style="margin-top:20px; margin-bottom:20px;" height="60">
                    </center>


                    <table align="center" width="500" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                    <tbody><tr>
                    <td align="center" colspan="2">
                    <h3><span data-markjs="true" class="markgkk7swyt2 _2mvHg_8QQFEuo2e0RlZLXB">Hello</span> """+Name+""",<br>

                    <span style="font-size:16px;">Password Changed Successful !</span></h3>
                    </td>
                    </tr>
                    <tr>
                    <td align="center" colspan="2"><img data-imagetype="External" src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/success.png" width="60" height="60" style="padding:0 5px;"></td>
                    </tr>
					
					<tr>
						<td>If you did not initiate this request. please contact us immediately at <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></td>
					</tr>
                        <tr>
                        <td  colspan="2">
                           
                            <p style="color:#999; font-size:12px;">Thank you, Click here to visit <a href='"""+LinkUrl+"""' target="_blank" style="color:#18aef4; font-size:12px;">Continua Kids</a>!</p></td>
                        </tr>
                    </tbody>
                    </table>
                    <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>6012, DLF phase 4, Sector 28, Gurugram<br>
                        </small></p>

                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Continua Kids</p>
                    </body>
                    </html>
                    """


        #The mail addresses and password
        sender_address = Sender_Mail#'vipulvict@gmail.com'
        sender_pass = Sender_Pwd#'8544388788'
        To_Add=email
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        #receiver_address=UserName
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        #message['From'] = Sender_DisplayName + f''+sender_address +''#sender_address
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Password Changed Successful !'   #The subject line
        #The body and the attachments for the mail
        #message.attach(MIMEText(mail_content, 'plain'))
        message.attach(MIMEText(mail_body,'html'))
        text = message.as_string()
        # print(text)
        #Create SMTP session for sending the mail
        #session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session = smtplib.SMTP(Mail_host, Mail_Port) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        #print('Mail Sent')
    except Exception as identifier:
        print(identifier)
    finally:
        pass


def SendForgetCredentials_Mail(Name,email,UserName,Password,URL):
    session=Session()
    try:
        # getAdminEmailID=Admin_Mail_Dtls()
        # Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL= True #getMailCredential[0].MMC_ISSSL
        MAIL_ISTLS= True
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        
#changing the Password Cycle
        mail_body=  """
        <!doctype html>
                    <html>
                    <head>
                    <meta charset="utf-8" />
                    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <link rel="icon" type="image/png" href="favicon.png" />
                    <title>Credentials Reset Successful !</title>
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center>
                    <a href='"""+URL+"""' target="_blank"><img src='http://3.111.190.80:8081/static/Mailer/continua_logo.png' alt="Continua Kids" title="Continua Kids"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                    </center>


                    <table align="center" width="500" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                    <tbody><tr>
                    <td align="center" colspan="2">
                    <h3><span data-markjs="true" class="markgkk7swyt2 _2mvHg_8QQFEuo2e0RlZLXB">Congratulations</span> """+Name+"""<br>

                    <span style="font-size:16px;">Credentials Reset Successful !</span></h3>
                    </td>
                    </tr>
                    <tr>
                    <td align="center" colspan="2"><img data-imagetype="External" src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/success.png" width="60" height="60" style="padding:0 5px;"></td>
                    </tr>
					<tr>
                    <td width="40%" style="background-color:#f1f1f1;">URL:</td>
                    <td style="background-color:#f1f1f1;"><b>"""+URL+"""</b></td>
                    </tr>
                    <tr>
                    <td width="40%" style="background-color:#f1f1f1;">User Name:</td>
                    <td style="background-color:#f1f1f1;"><b>"""+UserName+"""</b></td>
                    </tr>
					<tr>
                    <td width="40%" style="background-color:#f1f1f1;">Password:</td>
                    <td style="background-color:#f1f1f1;"><b>"""+Password+"""</b></td>
                    </tr>
					
                    

                        <tr>
                        <td  colspan="2">
						
                            <p style="margin-top:50px; color:#999; font-size:12px;">If you believe you received this email in error, please contact <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a>.</p>
                            <p style="color:#999; font-size:12px;">Thank you, Click here to visit <a href='"""+URL+"""' target="_blank" style="color:#18aef4; font-size:12px;">Continua Kids</a>!</p></td>
                        </tr>
                    </tbody>
                    </table>
                    <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>6012, DLF phase 4, Sector 28, Gurugram<br>
                        </small></p>

                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Continua Kids</p>
                    </body>
                    </html>
                    """


        #The mail addresses and password
        sender_address = Sender_Mail#'vipulvict@gmail.com'
        sender_pass = Sender_Pwd#'8544388788'
        To_Add=email
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        #receiver_address=UserName
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        #message['From'] = Sender_DisplayName + f''+sender_address +''#sender_address
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Credentials Reset Successful!'   #The subject line
        #The body and the attachments for the mail
        #message.attach(MIMEText(mail_content, 'plain'))
        message.attach(MIMEText(mail_body,'html'))
        text = message.as_string()
        # print(text)
        #Create SMTP session for sending the mail
        #session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session = smtplib.SMTP(Mail_host, Mail_Port) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        #print('Mail Sent')
    except Exception as identifier:
        print(identifier)
    finally:
        pass


def Approval_Mail_Admin():
    session=Session()
    try:
        pass
    except Exception as identifier:
        print(identifier)
    finally:
        session.close() 

def Blocked_Mail_Users():
    session=Session()
    try:
        pass
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()

def  Blocked_Mail_Admin():
    session=Session()
    try:
        pass
    except Exception as identifier:
        print(identifier)
    finally:
        session.close() 


def Admin_Mail_Dtls():
    session=Session()
    try:
        getAdminEmailID=session.query(Model.models.Admin.M_UserDetails.MUD_Admin_EmailID).filter_by(MUD_Type=0,MUD_IsActive=1,MUD_IsDeleted=0).first()
        return getAdminEmailID
    except Exception as identifier:
        print(identifier)

def Mail_Credential():
    session=Session()
    try:
        getMailCredential=session.query(Model.models.Application.M_MailCredentials.MMC_ID,Model.models.Application.M_MailCredentials.MMC_From_MailID,
                                        Model.models.Application.M_MailCredentials.MMC_Password,Model.models.Application.M_MailCredentials.MMC_MailDisplayName,
                                        Model.models.Application.M_MailCredentials.MMC_MailHost,Model.models.Application.M_MailCredentials.MMC_MailPort,
                                        Model.models.Application.M_MailCredentials.MMC_ISSSL,Model.models.Application.M_MailCredentials.MMC_ReplyTo,
                                        Model.models.Application.M_MailCredentials.MMC_CC_MailID,Model.models.Application.M_MailCredentials.MMC_BCC_MailID
                                        ).filter_by(MMC_IsActive=1,MMC_IsDeleted=0).order_by(Model.models.Application.M_MailCredentials.MMC_ID).all()
        return getMailCredential
    except Exception as identifier:
        print(identifier)
    finally:
        pass

def App_SupportDtls():
    session=Session()
    try:
        getSupportDtls=session.query(Model.models.Application.M_TechnicalDtls.MTD_SupportMailID,
                                     Model.models.Application.M_TechnicalDtls.MTD_SupportContact,
                                     Model.models.Application.M_TechnicalDtls.MTD_CopyRightYear,
                                     Model.models.Application.M_TechnicalDtls.MTD_SupportPersonMailId,
                                     Model.models.Application.M_TechnicalDtls.MTD_URL
                                     ).filter_by(MTD_IsActive=1,MTD_IsDeleted=0).all()
        return getSupportDtls
    except Exception as identifier:
        print(identifier)
    finally:
        pass

