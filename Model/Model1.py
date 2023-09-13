import sqlalchemy
from sqlalchemy import sql
from sqlalchemy.dialects.mysql import LONGTEXT
import datetime
import Connection.const
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

class Application:
    class M_Organisation(Connection.const.Connect.Base):
        __tablename__='m_organisation'
        MOID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'm_organisation_MOID'),primary_key=True)
        MO_Name= sqlalchemy.Column(sqlalchemy.String(250))
        MO_Email= sqlalchemy.Column(sqlalchemy.String(250))
        MO_Mobile=sqlalchemy.Column(sqlalchemy.String(30))
        MO_About=sqlalchemy.Column(sqlalchemy.String(2500))

        MO_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MO_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MO_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MO_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MO_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MO_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MO_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    class M_Details(Connection.const.Connect.Base):
        __tablename__='m_details'
        MDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Details_MDID'),primary_key=True)
        MD_Name= sqlalchemy.Column(sqlalchemy.String(250))
        MD_AddUser= sqlalchemy.Column(sqlalchemy.String(250))
        MD_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MD_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MD_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MD_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MD_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MD_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class T_Details(Connection.const.Connect.Base):
        __tablename__='T_Details'
        TDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'T_Details_TDID'),primary_key=True)
        TD_Name= sqlalchemy.Column(sqlalchemy.String(250))
        TD_Parent_TDID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Details_MDID = sqlalchemy.Column(sqlalchemy.Integer)
        TD_AddUser= sqlalchemy.Column(sqlalchemy.String(250))
        TD_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        TD_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        TD_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        TD_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        TD_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        TD_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Branch(Connection.const.Connect.Base):
        __tablename__='m_branch'
        MBID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'm_branch_MBID'),primary_key=True)
        M_Organisation_MOID = sqlalchemy.Column(sqlalchemy.Integer)
        MB_Name= sqlalchemy.Column(sqlalchemy.String(250))
        MB_Email= sqlalchemy.Column(sqlalchemy.String(250))
        MB_Mobile = sqlalchemy.Column(sqlalchemy.String(30))
        MB_Address = sqlalchemy.Column(sqlalchemy.String(1000))
        MB_City = sqlalchemy.Column(sqlalchemy.String(100))
        MB_State = sqlalchemy.Column(sqlalchemy.String(100))
        MB_Country = sqlalchemy.Column(sqlalchemy.String(100))
        MB_Code = sqlalchemy.Column(sqlalchemy.String(100))
        MB_PinCode = sqlalchemy.Column(sqlalchemy.String(10))
        MB_latlong = sqlalchemy.Column(sqlalchemy.String(1000))
        MB_OpenTime = sqlalchemy.Column(sqlalchemy.String(100))
        MB_CloseTime = sqlalchemy.Column(sqlalchemy.String(100))
        MB_ClinicTime = sqlalchemy.Column(sqlalchemy.String(100))
        MB_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MB_AddIP=sqlalchemy.Column(sqlalchemy.String(100))
        MB_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)

        MB_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MB_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MB_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MB_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ClinicTiming(Connection.const.Connect.Base):
        __tablename__='M_ClinicTiming'
        MCTID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ClinicTiming_MCTID'),primary_key=True)
        M_Organisation_MOID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.String(250))
        MCT_ClinicOpenTime= sqlalchemy.Column(sqlalchemy.String(250))
        MCT_ClinicOpenTimePeriod = sqlalchemy.Column(sqlalchemy.Integer)
        MCT_ClinicCloseTime = sqlalchemy.Column(sqlalchemy.String(1000))
        MCT_ClinicCloseTimePeriod = sqlalchemy.Column(sqlalchemy.Integer)
        MCT_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCT_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MCT_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MCT_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCT_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MCT_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MCT_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Floor(Connection.const.Connect.Base):
        __tablename__='M_Floor'
        MFID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Floor_MFID'),primary_key=True)
        MF_FloorName = sqlalchemy.Column(sqlalchemy.String(100))
        MF_AliasName= sqlalchemy.Column(sqlalchemy.String(100))
        MF_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MF_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MF_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MF_ModDate = sqlalchemy.Column(sqlalchemy.Integer)
        MF_ModUser = sqlalchemy.Column(sqlalchemy.DateTime)
        MF_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MF_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_validations(Connection.const.Connect.Base):
        __tablename__='M_validations'
        MVID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_validations_MVID'),primary_key=True)
        MV_Name = sqlalchemy.Column(sqlalchemy.String(100))
        MV_Pattern= sqlalchemy.Column(sqlalchemy.String(100))
        MV_Message= sqlalchemy.Column(sqlalchemy.String(100))
        MV_Type= sqlalchemy.Column(sqlalchemy.String(100))
        MV_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MV_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MV_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MV_ModDate = sqlalchemy.Column(sqlalchemy.Integer)
        MV_ModUser = sqlalchemy.Column(sqlalchemy.DateTime)
        MV_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MV_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Room(Connection.const.Connect.Base):
        __tablename__='M_Room'
        MRID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Room_MRID'),primary_key=True)
        M_Organisation_MOID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Floor_MFID= sqlalchemy.Column(sqlalchemy.Integer)
        MR_RoomName = sqlalchemy.Column(sqlalchemy.String(250))
        MR_RoomNumber = sqlalchemy.Column(sqlalchemy.String(100))
        MR_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MR_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MR_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MR_ModDate = sqlalchemy.Column(sqlalchemy.Integer)
        MR_ModUser = sqlalchemy.Column(sqlalchemy.DateTime)
        MR_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MR_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class T_RoomPurpose(Connection.const.Connect.Base):
        __tablename__='T_RoomPurpose'
        MRPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'T_RoomPurpose_MRPID'),primary_key=True)
        MRP_Purpose = sqlalchemy.Column(sqlalchemy.Integer)
        M_Room_MRID= sqlalchemy.Column(sqlalchemy.String(250))
        MR_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MR_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MR_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MR_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MR_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MR_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MR_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Forms(Connection.const.Connect.Base):
        __tablename__='M_Forms'
        MFID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Forms_MFID'),primary_key=True)
        MF_FormName = sqlalchemy.Column(sqlalchemy.String(300))
        MF_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MF_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MF_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MF_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MF_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MF_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MF_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Control(Connection.const.Connect.Base):
        __tablename__='M_Control'
        MCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Control_MCID'),primary_key=True)
        MC_ControlName = sqlalchemy.Column(sqlalchemy.String(250))
        MC_ControlType= sqlalchemy.Column(sqlalchemy.String(250))
        MC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MC_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Menu(Connection.const.Connect.Base):
        __tablename__='M_Menu'
        MMID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Menu_MMID'),primary_key=True)
        MM_State = sqlalchemy.Column(sqlalchemy.String(250))
        MM_Name= sqlalchemy.Column(sqlalchemy.String(250))
        MM_Type= sqlalchemy.Column(sqlalchemy.String(250))
        MM_Icon= sqlalchemy.Column(sqlalchemy.String(250))
        MM_Level= sqlalchemy.Column(sqlalchemy.Integer)
        MM_Parent= sqlalchemy.Column(sqlalchemy.Integer)
        MM_preference= sqlalchemy.Column(sqlalchemy.Integer)
        MM_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MM_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MM_ISIP = sqlalchemy.Column(sqlalchemy.String(100))
        MM_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MM_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MM_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MM_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_FormControl(Connection.const.Connect.Base):
        __tablename__='M_FormControl'
        MFCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_FormControl_MFCID'),primary_key=True)
        MFC_FormName = sqlalchemy.Column(sqlalchemy.String(250))
        M_Control_MCID= sqlalchemy.Column(sqlalchemy.Integer)
        MFC_Label= sqlalchemy.Column(sqlalchemy.String(800))
        MFC_SetId= sqlalchemy.Column(sqlalchemy.Integer)
        MFC_FormId= sqlalchemy.Column(sqlalchemy.Integer)
        MFC_Required= sqlalchemy.Column(sqlalchemy.Boolean, unique=False, default=False)
        MFC_Regex= sqlalchemy.Column(sqlalchemy.String(250))
        MFC_InitialValue= sqlalchemy.Column(sqlalchemy.String(250))
        MFC_Data_M_Details_MDID= sqlalchemy.Column(sqlalchemy.Integer)
        MFC_Data_Column=sqlalchemy.Column(sqlalchemy.String(250))
        MFC_Data_Table=sqlalchemy.Column(sqlalchemy.String(250))
        MFC_Style=sqlalchemy.Column(sqlalchemy.String(250))
        MFC_preference= sqlalchemy.Column(sqlalchemy.Integer)
        MFC_Name=sqlalchemy.Column(sqlalchemy.String(250))
        controlType=sqlalchemy.Column(sqlalchemy.String(250))
        MFC_Path=sqlalchemy.Column(sqlalchemy.String(250))
        MFC_Align=sqlalchemy.Column(sqlalchemy.String(250))
        MFC_Validations=sqlalchemy.Column(sqlalchemy.String(250))
        MFC_Options=sqlalchemy.Column(sqlalchemy.String(250))
        MFC_Multiline=sqlalchemy.Column(sqlalchemy.Boolean, unique=False, default=0)
        MFC_Class_Name=sqlalchemy.Column(sqlalchemy.String(250))
        MFC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MFC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MFC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MFC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MFC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MFC_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MFC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Patient(Connection.const.Connect.Base):
        __tablename__='M_Patient'
        MPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Patient_MPID'),primary_key=True)
        MP_UHID = sqlalchemy.Column(sqlalchemy.String(250))
        MP_RefferedBy= sqlalchemy.Column(sqlalchemy.String(250))
        MP_Code= sqlalchemy.Column(sqlalchemy.String(250))
        MP_Name= sqlalchemy.Column(sqlalchemy.String(250))
        MP_Email= sqlalchemy.Column(sqlalchemy.String(250))
        MP_Mobile= sqlalchemy.Column(sqlalchemy.String(250))
        MP_Address= sqlalchemy.Column(sqlalchemy.String(250))
        MP_Gender= sqlalchemy.Column(sqlalchemy.Integer)
        MP_DOB= sqlalchemy.Column(sqlalchemy.Date)
        MP_Age= sqlalchemy.Column(sqlalchemy.Integer)
        MP_Procedure= sqlalchemy.Column(sqlalchemy.Integer)
        MP_City= sqlalchemy.Column(sqlalchemy.String(150))
        MP_State= sqlalchemy.Column(sqlalchemy.String(150))
        MP_Country= sqlalchemy.Column(sqlalchemy.String(150))
        M_Organisation_MOID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        M_IdentityType= sqlalchemy.Column(sqlalchemy.Integer)
        MP_BloodGroup= sqlalchemy.Column(sqlalchemy.Integer)
        MP_Allergies= sqlalchemy.Column(sqlalchemy.String(500))
        MP_PreExMed= sqlalchemy.Column(sqlalchemy.String(500))
        M_IdentityNumber= sqlalchemy.Column(sqlalchemy.String(250))
        MP_PassportNo= sqlalchemy.Column(sqlalchemy.String(150))
        MP_CountryCode= sqlalchemy.Column(sqlalchemy.String(150))
        
        MP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MP_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PatientDetails(Connection.const.Connect.Base):
        __tablename__='M_PatientDetails'
        MPDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PatientDetails_MPDID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MPD_AttndntName= sqlalchemy.Column(sqlalchemy.String(250))
        MPD_AttndntRelation= sqlalchemy.Column(sqlalchemy.String(250))
        M_IdentityType_MITID= sqlalchemy.Column(sqlalchemy.Integer)
        MPD_IdentityVal= sqlalchemy.Column(sqlalchemy.String(250))
        MPD_ContactNumber= sqlalchemy.Column(sqlalchemy.String(250))
        MPD_AttndntAddress= sqlalchemy.Column(sqlalchemy.String(250))
        MPD_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPD_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPD_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPD_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPD_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPD_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MPD_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    
    class M_PackageForPatient(Connection.const.Connect.Base):
        __tablename__='M_PackageForPatient'
        MPPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PackageForPatient_MPPID'),primary_key=True)
        MPP_PackageName = sqlalchemy.Column(sqlalchemy.String(250))
        MPP_BranchId= sqlalchemy.Column(sqlalchemy.Integer)
        MPP_Date= sqlalchemy.Column(sqlalchemy.Date)
        MPP_PackagePrice= sqlalchemy.Column(sqlalchemy.String(10))
        MPP_TaxDiscount= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_Total= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_DiscountPersent= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_Discount= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_DiscountReason= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_TotalPayable= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_AmountPaid= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_DueBalance= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_Cash= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_Cheque= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_Card= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_Online= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_UPI= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_Prepaid= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_BankName= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_CardType= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_LastDigit= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_Comments= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_PackageId= sqlalchemy.Column(sqlalchemy.String(250))
        MPP_PatientId= sqlalchemy.Column(sqlalchemy.String(250))
        
        MPP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPP_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MPP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    
    class M_InvoiceForPatient(Connection.const.Connect.Base):
        __tablename__='M_InvoiceForPatient'
        MIPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_InvoiceForPatient_MIPID'),primary_key=True)
        MIP_InvoiceType = sqlalchemy.Column(sqlalchemy.String(250))
        MIP_BranchId= sqlalchemy.Column(sqlalchemy.Integer)
        MIP_Date= sqlalchemy.Column(sqlalchemy.Date)
        MIP_MedicineDetails= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_InvoiceTotal= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_cgst= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_sgst= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_DiscountPercent= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_Discount= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_DiscountReason= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_TotalPayable= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_AmountPaid= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_DueBalance= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_Cash= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_Cheque= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_Card= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_Online= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_UPI= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_Prepaid= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_BankName= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_CardType= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_LastDigit= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_Comments= sqlalchemy.Column(sqlalchemy.String(250))
        MIP_PatientId= sqlalchemy.Column(sqlalchemy.String(250))
        
        MIP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MIP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MIP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MIP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MIP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MIP_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MIP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_InvoiceMedicines(Connection.const.Connect.Base):
        __tablename__='M_InvoiceMedicines'
        MIMID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_InvoiceMedicines_MIMID'),primary_key=True)
        MIM_Service = sqlalchemy.Column(sqlalchemy.String(250))
        MIM_Batch= sqlalchemy.Column(sqlalchemy.String(250))
        MIM_Cost= sqlalchemy.Column(sqlalchemy.String(250))
        MIM_Item= sqlalchemy.Column(sqlalchemy.String(250))
        MIM_Quantity= sqlalchemy.Column(sqlalchemy.String(250))
        MIM_Tax= sqlalchemy.Column(sqlalchemy.String(250))
        MIM_TotalCost= sqlalchemy.Column(sqlalchemy.String(250))
        MIM_TotalTax= sqlalchemy.Column(sqlalchemy.String(250))
        MIM_Invoice= sqlalchemy.Column(sqlalchemy.String(250))
        
        
        MIM_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MIM_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MIM_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MIM_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MIM_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MIM_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MIM_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    
    class M_PackageInvoiceForAppointment(Connection.const.Connect.Base):
        __tablename__='M_PackageInvoiceForAppointment'
        MPIAID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PackageInvoiceForAppointment_MPIAID'),primary_key=True)
        MPIA_ServiceName = sqlalchemy.Column(sqlalchemy.String(250))
        MPIA_Price= sqlalchemy.Column(sqlalchemy.String(250))
        MPIA_TaxInr= sqlalchemy.Column(sqlalchemy.String(250))
        MPIA_TotalCost= sqlalchemy.Column(sqlalchemy.String(250))
        MPIA_Cgst= sqlalchemy.Column(sqlalchemy.String(250))
        MPIA_Sgst= sqlalchemy.Column(sqlalchemy.String(250))
        MPIA_InvoiceTotal= sqlalchemy.Column(sqlalchemy.String(250))
        MPIA_SessionName= sqlalchemy.Column(sqlalchemy.String(250))
        MPIA_TotalSessions= sqlalchemy.Column(sqlalchemy.String(250))
        MPIA_UsedSession= sqlalchemy.Column(sqlalchemy.String(250))
        MPIA_PaymentMode= sqlalchemy.Column(sqlalchemy.String(250))
        MPIA_PatientId= sqlalchemy.Column(sqlalchemy.String(250))
        MPIA_AppointId= sqlalchemy.Column(sqlalchemy.String(250))
        
        
        MPIA_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPIA_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPIA_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPIA_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPIA_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPIA_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MPIA__IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_IdentityType(Connection.const.Connect.Base):
        __tablename__='M_IdentityType'
        MITID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_IdentityType_MITID'),primary_key=True)
        MIT_Name = sqlalchemy.Column(sqlalchemy.String(300))

        MIT_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MIT_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MIT_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MIT_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MIT_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MIT_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MIT_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    
    class M_CountryCode(Connection.const.Connect.Base):
        __tablename__='M_CountryCode'
        MCCId=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_CountryCode_MCCId'),primary_key=True)
        MCC_Iso = sqlalchemy.Column(sqlalchemy.String(300))
        MCC_Name = sqlalchemy.Column(sqlalchemy.String(300))
        MCC_Nicname = sqlalchemy.Column(sqlalchemy.String(300))
        MCC_Iso3 = sqlalchemy.Column(sqlalchemy.String(300))
        MCC_Numcode = sqlalchemy.Column(sqlalchemy.String(300))
        MCC_Phonecode = sqlalchemy.Column(sqlalchemy.String(300))

        MCC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MCC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MCC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MCC_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MCC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_DoctorDetails(Connection.const.Connect.Base):
        __tablename__='M_DoctorDetails'
        MDDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_DoctorDetails_MDDID'),primary_key=True)
        MDD_FirstName = sqlalchemy.Column(sqlalchemy.String(250))
        MDD_LastName= sqlalchemy.Column(sqlalchemy.Integer)
        MDD_OnlineFeeINR= sqlalchemy.Column(sqlalchemy.Integer)
        MDD_OnlineFeeUSD= sqlalchemy.Column(sqlalchemy.Integer)
        MDD_visitFeeINR= sqlalchemy.Column(sqlalchemy.Integer)
        MDD_visitFeeUSD= sqlalchemy.Column(sqlalchemy.Integer)
        MDD_Status= sqlalchemy.Column(sqlalchemy.Boolean, unique=False, default=1)
        MDD_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MDD_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MDD_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MDD_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MDD_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MDD_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MDD_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PatientFiles(Connection.const.Connect.Base):
        __tablename__='M_PatientFiles'
        MPFID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PatientFiles_MPFID'),primary_key=True)
        MPF_PatientID = sqlalchemy.Column(sqlalchemy.Integer)
        MPF_Name= sqlalchemy.Column(sqlalchemy.String(250))
        MPF_FilePath= sqlalchemy.Column(sqlalchemy.String(250))
        MPF_FileType= sqlalchemy.Column(sqlalchemy.String(250))
        MPF_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPF_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPF_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPF_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPF_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPF_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MPF_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PatientConsentForm(Connection.const.Connect.Base):
        __tablename__='M_PatientConsentForm'
        MPCFID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PatientConsentForm_MPCFID'),primary_key=True)
        MPCF_PatientID = sqlalchemy.Column(sqlalchemy.String(250))
        MPCF_Name= sqlalchemy.Column(sqlalchemy.Integer)
        MPCF_FilePath= sqlalchemy.Column(sqlalchemy.Integer)
        MPCF_FileType= sqlalchemy.Column(sqlalchemy.Integer)
        MPCF_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPCF_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPCF_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPCF_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPCF_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPCF_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MPCF_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_DoctorPracticeDetails(Connection.const.Connect.Base):
        __tablename__='M_DoctorPracticeDetails'
        MDPDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_DoctorPracticeDetails_MDPDID'),primary_key=True)
        M_Organisation_MOID = sqlalchemy.Column(sqlalchemy.Integer)

        MDPD_DoctorId = sqlalchemy.Column(sqlalchemy.Integer)
        MDPD_Address= sqlalchemy.Column(sqlalchemy.String(250))
        MDPD_Mobile1= sqlalchemy.Column(sqlalchemy.String(50))
        MDPD_HideMobile1= sqlalchemy.Column(sqlalchemy.String(250))
        MDPD_Mobile2= sqlalchemy.Column(sqlalchemy.String(250))
        MDPD_HideMobile2= sqlalchemy.Column(sqlalchemy.String(250))
        MDPD_Pincode= sqlalchemy.Column(sqlalchemy.Integer)
        MDPD_city = sqlalchemy.Column(sqlalchemy.String(250))
        MDPD_cliniccponsultfee= sqlalchemy.Column(sqlalchemy.Integer)
        MDPD_clinicname= sqlalchemy.Column(sqlalchemy.String(250))
        MDPD_country= sqlalchemy.Column(sqlalchemy.Integer)
        MDPD_digitalSign= sqlalchemy.Column(sqlalchemy.String(250))
        MDPD_DigitalSIgnPath = sqlalchemy.Column(sqlalchemy.String(250))
        MDPD_landline= sqlalchemy.Column(sqlalchemy.String(250))
        MDPD_onlinefeeusd= sqlalchemy.Column(sqlalchemy.String(250))
        MDPD_onlinefeeinr= sqlalchemy.Column(sqlalchemy.String(250))
        MDPD_state= sqlalchemy.Column(sqlalchemy.Integer)
        MDPD_visitfeeusd= sqlalchemy.Column(sqlalchemy.Integer)
        MDPD_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MDPD_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MDPD_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MDPD_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MDPD_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MDPD_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MDPD_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    class M_VaccineType(Connection.const.Connect.Base):
        __tablename__='M_VaccineType'
        MVTID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_VaccineType_MVTID'),primary_key=True)
        MVT_Name = sqlalchemy.Column(sqlalchemy.String(300))

        MVT_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MVT_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MVT_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MVT_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MVT_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MVT_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MVT_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Expertise(Connection.const.Connect.Base):
        __tablename__='M_Expertise'
        MEID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Expertise_MEID'),primary_key=True)
        ME_ExpertiseName = sqlalchemy.Column(sqlalchemy.String(300))
        M_DoctorDetails_MDDID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Organisation_MOID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID = sqlalchemy.Column(sqlalchemy.Integer)
        ME_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        ME_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        ME_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        ME_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        ME_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        ME_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        ME_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_VaccinationDetails(Connection.const.Connect.Base):
        __tablename__='M_VaccinationDetails'
        MVDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_VaccinationDetails_MVDID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.String(250))
        MVD_Date= sqlalchemy.Column(sqlalchemy.Integer)
        MVD_Time= sqlalchemy.Column(sqlalchemy.Integer)
        MVD_Age= sqlalchemy.Column(sqlalchemy.String(250))
        M_VaccineType_MVTID= sqlalchemy.Column(sqlalchemy.String(250))
        MVD_TotalDose= sqlalchemy.Column(sqlalchemy.String(250))
        MVD_ConsumedDose= sqlalchemy.Column(sqlalchemy.String(250))

        MVD_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MVD_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MVD_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MVD_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MVD_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MVD_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MVD_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Appointment(Connection.const.Connect.Base):
        __tablename__='M_Appointment'
        MAID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Appointment_MAID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MP_Procedure= sqlalchemy.Column(sqlalchemy.Integer)
        MA_Date= sqlalchemy.Column(sqlalchemy.String(250))
        MA_Time= sqlalchemy.Column(sqlalchemy.String(250))
        MP_Duration= sqlalchemy.Column(sqlalchemy.String(250))
        MP_AppointmentType= sqlalchemy.Column(sqlalchemy.Integer)
        M_DoctorDetails_MDDID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Organisation_MOID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Room_MRID= sqlalchemy.Column(sqlalchemy.Integer)
        MP_Status= sqlalchemy.Column(sqlalchemy.Integer)
        MP_Notes= sqlalchemy.Column(sqlalchemy.String(250))
        MP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MP_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)
        MP_IsCancelled = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)
    Connection.const.createTable()


    class M_Credit(Connection.const.Connect.Base):
        __tablename__='M_Credit'
        MCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Credit_MCID'),primary_key=True)
        MC_CreditType = sqlalchemy.Column(sqlalchemy.Integer)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Organisation_MOID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        MC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MC_Date = sqlalchemy.Column(sqlalchemy.DateTime)
        MC_TotalAmount= sqlalchemy.Column(sqlalchemy.Float)
        MC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MC_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class T_Credit(Connection.const.Connect.Base):
        __tablename__='T_Credit'
        TCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'T_Credit_TCID'),primary_key=True)
        M_Credit_MCID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Organisation_MOID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        TC_PaymentMode= sqlalchemy.Column(sqlalchemy.Integer)
        TC_Date = sqlalchemy.Column(sqlalchemy.DateTime)
        TC_ServiceID = sqlalchemy.Column(sqlalchemy.Integer)
        TC_Amount= sqlalchemy.Column(sqlalchemy.Float)
        TC_BankName = sqlalchemy.Column(sqlalchemy.String(250))
        TC_CardType= sqlalchemy.Column(sqlalchemy.Integer)
        TC_CardNumber= sqlalchemy.Column(sqlalchemy.String(50))
        TC_CreditType= sqlalchemy.Column(sqlalchemy.Integer)
        TC_PatientID= sqlalchemy.Column(sqlalchemy.Integer)
        TC_Comment = sqlalchemy.Column(sqlalchemy.String(250))
        TC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        TC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        TC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        TC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        TC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        TC_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        TC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Package(Connection.const.Connect.Base):
        __tablename__='M_Package'
        MPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Package_MPID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MP_Name= sqlalchemy.Column(sqlalchemy.String(100))
        MP_PackageType= sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MP_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PackageDetails(Connection.const.Connect.Base):
        __tablename__='M_PackageDetails'
        MPDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PackageDetails_MPDID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        MPD_Date= sqlalchemy.Column(sqlalchemy.DateTime)
        MPD_Price = sqlalchemy.Column(sqlalchemy.Float)
        MPD_Discount= sqlalchemy.Column(sqlalchemy.Float)
        MPD_Payable= sqlalchemy.Column(sqlalchemy.Float)
        MPD_Paid = sqlalchemy.Column(sqlalchemy.Float)
        MPD_Balance= sqlalchemy.Column(sqlalchemy.Float)
        MPD_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPD_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPD_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPD_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPD_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPD_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MPD_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PackageServiceDetails(Connection.const.Connect.Base):
        __tablename__='M_PackageServiceDetails'
        MPSDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PackageServiceDetails_MPSDID'),primary_key=True)
        M_Package_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        MPSD_ServiceName= sqlalchemy.Column(sqlalchemy.String(100))
        MPSD_Price = sqlalchemy.Column(sqlalchemy.Float)
        MPSD_Session= sqlalchemy.Column(sqlalchemy.String(100))
        MPSD_Payable= sqlalchemy.Column(sqlalchemy.Float)
        MPSD_Cost = sqlalchemy.Column(sqlalchemy.Float)
        MPSD_validity= sqlalchemy.Column(sqlalchemy.Integer)
        MPSD_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPSD_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPSD_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPSD_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPSD_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPSD_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MPSD_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Payment(Connection.const.Connect.Base):
        __tablename__='M_Payment'
        MPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Payment_MPID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        MP_PaymentType= sqlalchemy.Column(sqlalchemy.Integer)
        MP_PaymentMode = sqlalchemy.Column(sqlalchemy.Integer)
        MP_Amount= sqlalchemy.Column(sqlalchemy.Float)
        MP_Comment= sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MP_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()



    class T_Package(Connection.const.Connect.Base):
        __tablename__='T_Package'
        TPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'T_Package_MPID'),primary_key=True)
        M_Package_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Organisation_MOID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        TP_Tax= sqlalchemy.Column(sqlalchemy.Float)
        TP_Amount = sqlalchemy.Column(sqlalchemy.Float)
        TP_Discount = sqlalchemy.Column(sqlalchemy.String(50))
        TP_DiscountType= sqlalchemy.Column(sqlalchemy.Integer)
        TP_DiscountReason = sqlalchemy.Column(sqlalchemy.String(250))
        TP_AmountPayable= sqlalchemy.Column(sqlalchemy.Float)
        TP_AmountPaid= sqlalchemy.Column(sqlalchemy.Float)
        TP_AmountBalance = sqlalchemy.Column(sqlalchemy.Float)
        TP_PaymentMode = sqlalchemy.Column(sqlalchemy.Integer)
        TP_EffectiveDate= sqlalchemy.Column(sqlalchemy.DateTime)
        TP_BankName = sqlalchemy.Column(sqlalchemy.String(250))
        TP_CardType= sqlalchemy.Column(sqlalchemy.Integer)
        TP_CardNumber= sqlalchemy.Column(sqlalchemy.String(50))
        TP_Comment= sqlalchemy.Column(sqlalchemy.String(250))
        TP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        TP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        TP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        TP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        TP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        TP_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        TP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Invoice(Connection.const.Connect.Base):
        __tablename__='M_Invoice'
        MIID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Invoice_MIID'),primary_key=True)
        MI_AppointmentId = sqlalchemy.Column(sqlalchemy.Integer)
        M_Organisation_MOID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MI_Date= sqlalchemy.Column(sqlalchemy.DateTime)
        MI_bankName= sqlalchemy.Column(sqlalchemy.String(100))
        MI_Card= sqlalchemy.Column(sqlalchemy.String(100))
        MI_CardType= sqlalchemy.Column(sqlalchemy.Integer)
        MI_Cash = sqlalchemy.Column(sqlalchemy.String(100))
        MI_CGST = sqlalchemy.Column(sqlalchemy.String(100))
        MI_SGST= sqlalchemy.Column(sqlalchemy.String(100))
        MI_Discount = sqlalchemy.Column(sqlalchemy.String(100))
        MI_discountPercent = sqlalchemy.Column(sqlalchemy.String(100))
        MI_DiscountReason= sqlalchemy.Column(sqlalchemy.String(100))
        MI_Cheque = sqlalchemy.Column(sqlalchemy.String(100))
        MI_Comments = sqlalchemy.Column(sqlalchemy.String(100))
        MI_DueBalance= sqlalchemy.Column(sqlalchemy.String(100))
        MI_InvoiceTotal= sqlalchemy.Column(sqlalchemy.String(100))
        MI_invoiceType= sqlalchemy.Column(sqlalchemy.String(100))
        MI_lastDigits= sqlalchemy.Column(sqlalchemy.String(100))
        MI_Online= sqlalchemy.Column(sqlalchemy.String(100))
        MI_Prepaid= sqlalchemy.Column(sqlalchemy.String(100))
        MI_TotalPayable= sqlalchemy.Column(sqlalchemy.String(100))
        MI_Upi= sqlalchemy.Column(sqlalchemy.String(100))
        MI_AmountPaid= sqlalchemy.Column(sqlalchemy.String(100))

        MI_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MI_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MI_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MI_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MI_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MI_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MI_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_MedicineDtls(Connection.const.Connect.Base):
        __tablename__='M_MedicineDtls'
        MDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_MedicineDtls_MDID'),primary_key=True)
        M_Organisation_MOID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Invoice_MIID= sqlalchemy.Column(sqlalchemy.Integer)
        MD_Batch= sqlalchemy.Column(sqlalchemy.String(100))
        MD_Cost= sqlalchemy.Column(sqlalchemy.String(100))
        MD_Item= sqlalchemy.Column(sqlalchemy.String(100))
        MD_Quantity= sqlalchemy.Column(sqlalchemy.String(100))
        MD_Tax = sqlalchemy.Column(sqlalchemy.String(100))
        MD_TotalCost = sqlalchemy.Column(sqlalchemy.String(100))
        MD_TotalTax= sqlalchemy.Column(sqlalchemy.String(100))

        MD_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MD_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MD_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MD_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MD_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MD_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MD_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class T_Invoice(Connection.const.Connect.Base):
        __tablename__='T_Invoice'
        TIID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'T_Invoice_TIID'),primary_key=True)
        M_Invoice_MIID = sqlalchemy.Column(sqlalchemy.Integer)
        M_Organisation_MOID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        TI_PaymentMode= sqlalchemy.Column(sqlalchemy.Integer)
        TI_Date = sqlalchemy.Column(sqlalchemy.DateTime)
        TI_ServiceID = sqlalchemy.Column(sqlalchemy.Integer)
        TI_Amount= sqlalchemy.Column(sqlalchemy.Float)
        TI_BankName = sqlalchemy.Column(sqlalchemy.String(250))
        TI_CardType= sqlalchemy.Column(sqlalchemy.Integer)
        TI_CardNumber= sqlalchemy.Column(sqlalchemy.String(50))

        TI_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        TI_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        TI_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        TI_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        TI_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        TI_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        TI_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()



    class M_ReasonForVisit(Connection.const.Connect.Base):
        __tablename__='M_ReasonForVisit'
        MRVID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ReasonForVisit_MRVID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MRV_PresentConcerns= sqlalchemy.Column(sqlalchemy.String(400))
        MRV_InformedBy= sqlalchemy.Column(sqlalchemy.String(400))
        MRV_AgeWhenNoticed = sqlalchemy.Column(sqlalchemy.String(400))

        MRV_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MRV_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MRV_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MRV_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MRV_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MRV_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MRV_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PastHistory(Connection.const.Connect.Base):
        __tablename__='M_PastHistory'
        MPHID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PastHistory_MPHID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MPH_PastInvestigations= sqlalchemy.Column(sqlalchemy.String(400))
        MPH_PastTreatments= sqlalchemy.Column(sqlalchemy.String(400))
        MPH_PastMedications = sqlalchemy.Column(sqlalchemy.String(400))

        MPH_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPH_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPH_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPH_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPH_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPH_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MPH_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PastHistoryFiles(Connection.const.Connect.Base):
        __tablename__='M_PastHistoryFiles'
        MPHFID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PastHistoryFiles_MPHFID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        M_PastHistory_MPHID= sqlalchemy.Column(sqlalchemy.Integer)
        MPHF_PastFiles= sqlalchemy.Column(sqlalchemy.String(400))
        MPHF_PastFilePath = sqlalchemy.Column(sqlalchemy.String(400))

        MPHF_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPHF_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPHF_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPHF_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPHF_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPHF_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MPHF_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PrenatalHistory(Connection.const.Connect.Base):
        __tablename__='M_PrenatalHistory'
        MPHID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PrenatalHistory_MPHID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MPH_MotheraAgeAtConception= sqlalchemy.Column(sqlalchemy.String(400))
        MPH_MotherHealthAtPregnancy= sqlalchemy.Column(sqlalchemy.String(400))
        MPH_HistoryofAbortions = sqlalchemy.Column(sqlalchemy.Integer)
        MPH_GestationalDiabetes= sqlalchemy.Column(sqlalchemy.Integer)
        MPH_NeurologicalDisorder= sqlalchemy.Column(sqlalchemy.Integer)
        MPH_PhysicalEmotionalTrauma = sqlalchemy.Column(sqlalchemy.Integer)
        MPH_RhInompatibility= sqlalchemy.Column(sqlalchemy.Integer)
        MPH_Jaundice= sqlalchemy.Column(sqlalchemy.Integer)
        MPH_Seizures = sqlalchemy.Column(sqlalchemy.Integer)
        MPH_TraumaInjury= sqlalchemy.Column(sqlalchemy.Integer)
        MPH_Bleedinginlatepregnancy= sqlalchemy.Column(sqlalchemy.Integer)
        MPH_AdequateNutrition = sqlalchemy.Column(sqlalchemy.Integer)
        MPH_Infections= sqlalchemy.Column(sqlalchemy.Integer)
        MPH_Smoking= sqlalchemy.Column(sqlalchemy.Integer)
        MPH_Observations = sqlalchemy.Column(sqlalchemy.String(400))

        MPH_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPH_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPH_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPH_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPH_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPH_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MPH_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PatientBirthHistory(Connection.const.Connect.Base):
        __tablename__='M_PatientBirthHistory'
        MPBHID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PatientBirthHistory_MPBHID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MPBH_MotherHealth= sqlalchemy.Column(sqlalchemy.String(400))
        MPBH_DeliveryType= sqlalchemy.Column(sqlalchemy.Integer)
        MPBH_typeofdelivery = sqlalchemy.Column(sqlalchemy.String(400))
        MPBH_DeliveryLocationh= sqlalchemy.Column(sqlalchemy.Integer)
        MPBH_MultiplePregnancies= sqlalchemy.Column(sqlalchemy.Integer)
        MPBH_ComplicationDuringPregnancy = sqlalchemy.Column(sqlalchemy.String(400))
        MPBH_ChildBirth= sqlalchemy.Column(sqlalchemy.Integer)
        MPBH_ChildBirthWeek= sqlalchemy.Column(sqlalchemy.Integer)
        MPBH_BirthWeight = sqlalchemy.Column(sqlalchemy.String(400))
        MPBH_BirthCry= sqlalchemy.Column(sqlalchemy.Integer)
        MPBH_NeonatalConditionint= sqlalchemy.Column(sqlalchemy.String(400))
        MPBH_SpecialCareAny = sqlalchemy.Column(sqlalchemy.String(400))
        MPBH_AnyMedicalEvents= sqlalchemy.Column(sqlalchemy.String(400))
        MPBH_Congenital= sqlalchemy.Column(sqlalchemy.String(400))
        MPBH_Observations = sqlalchemy.Column(sqlalchemy.String(400))

        MPBH_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPBH_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPBH_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPBH_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPBH_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPBH_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MPBH_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()


    class M_DevelopmentalHistory(Connection.const.Connect.Base):
        __tablename__='M_DevelopmentalHistory'
        MDHID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_DevelopmentalHistory_MDHID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MDH_HoldUpHeadAge= sqlalchemy.Column(sqlalchemy.String(400))
        MDH_Rolloverage= sqlalchemy.Column(sqlalchemy.String(400))
        MDH_SitAge = sqlalchemy.Column(sqlalchemy.String(400))
        MDH_StandAloneAge= sqlalchemy.Column(sqlalchemy.String(400))
        MDH_WalkAge= sqlalchemy.Column(sqlalchemy.String(400))
        MDH_TalkAge = sqlalchemy.Column(sqlalchemy.String(400))
        MDH_ToiletTrainAge= sqlalchemy.Column(sqlalchemy.String(400))
        MDH_FeedAge= sqlalchemy.Column(sqlalchemy.String(400))
        MDH_DresshimAge = sqlalchemy.Column(sqlalchemy.String(400))
        MDH_Observations= sqlalchemy.Column(sqlalchemy.String(400))

        MDH_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MDH_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MDH_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MDH_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MDH_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MDH_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MDH_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_SpeechDevelopmentalHistory(Connection.const.Connect.Base):
        __tablename__='M_SpeechDevelopmentalHistory'
        MSDHID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_SpeechDevelopmentalHistory_MSDHID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MSDH_Vocalization= sqlalchemy.Column(sqlalchemy.String(400))
        MSDH_Babbling= sqlalchemy.Column(sqlalchemy.String(400))
        MSDH_FirstWord = sqlalchemy.Column(sqlalchemy.String(400))
        MSDH_Phrases= sqlalchemy.Column(sqlalchemy.String(400))
        MSDH_SimpleSentences= sqlalchemy.Column(sqlalchemy.String(400))
        MSDH_Observations = sqlalchemy.Column(sqlalchemy.String(400))

        MSDH_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSDH_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSDH_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSDH_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSDH_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSDH_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSDH_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_SocialHistory(Connection.const.Connect.Base):
        __tablename__='M_SocialHistory'
        MSHID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_SocialHistory_MSHID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MSH_Recognises= sqlalchemy.Column(sqlalchemy.String(400))
        MSH_Socialises= sqlalchemy.Column(sqlalchemy.String(400))
        MSH_Irritable = sqlalchemy.Column(sqlalchemy.String(400))
        MSH_Distractible= sqlalchemy.Column(sqlalchemy.String(400))
        MSH_Aggressive= sqlalchemy.Column(sqlalchemy.String(400))

        MSH_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSH_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSH_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSH_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSH_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSH_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSH_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_MedicalHistory(Connection.const.Connect.Base):
        __tablename__='M_MedicalHistory'
        MSHID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_MedicalHistory_MSHID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MMH_observations= sqlalchemy.Column(sqlalchemy.String(400))
        MMH_CurrentMedication= sqlalchemy.Column(sqlalchemy.String(400))
        MMH_InvestigationsConducted = sqlalchemy.Column(sqlalchemy.String(400))

        MMH_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MMH_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MMH_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MMH_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MMH_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MMH_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MMH_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_FamilyHistory(Connection.const.Connect.Base):
        __tablename__='M_FamilyHistory'
        MFHID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_FamilyHistory_MFHID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MFH_fatherage= sqlalchemy.Column(sqlalchemy.Integer)
        MFH_fatherhealth= sqlalchemy.Column(sqlalchemy.String(400))
        MFH_motherage = sqlalchemy.Column(sqlalchemy.Integer)
        MFH_motherhealth= sqlalchemy.Column(sqlalchemy.String(400))
        MFH_Familytype= sqlalchemy.Column(sqlalchemy.Integer)
        MFH_Consanguinity = sqlalchemy.Column(sqlalchemy.String(400))
        MFH_deafness= sqlalchemy.Column(sqlalchemy.Integer)
        MFH_Bloodrelative= sqlalchemy.Column(sqlalchemy.String(400))
        MFH_Observations = sqlalchemy.Column(sqlalchemy.String(400))

        MFH_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MFH_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MFH_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MFH_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MFH_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MFH_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MFH_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    class M_EducationHistory(Connection.const.Connect.Base):
        __tablename__='M_EducationHistory'
        MEHID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_EducationHistory_MEHID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MEH_SchoolType= sqlalchemy.Column(sqlalchemy.String(400))
        MEH_AdmsnAge= sqlalchemy.Column(sqlalchemy.String(400))
        MEH_CommunicationMode = sqlalchemy.Column(sqlalchemy.String(400))

        MEH_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MEH_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MEH_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MEH_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MEH_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MEH_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MEH_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_WeekDays(Connection.const.Connect.Base):
        __tablename__='M_WeekDays'
        MWDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_WeekDays_MWDID'),primary_key=True)

        MWD_Day= sqlalchemy.Column(sqlalchemy.String(400))


        MWD_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MWD_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MWD_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MWD_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MWD_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MWD_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MWD_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class T_DoctorPracticeTimeSlot(Connection.const.Connect.Base):
        __tablename__='T_DoctorPracticeTimeSlot'
        TDPSID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'T_DoctorPracticeTimeSlot_TDPSID'),primary_key=True)

        TDPS_MDPDID= sqlalchemy.Column(sqlalchemy.Integer)
        TDPS_DayID= sqlalchemy.Column(sqlalchemy.Integer)
        TDPS_FromTime= sqlalchemy.Column(sqlalchemy.Time)
        TDPS_ToTime= sqlalchemy.Column(sqlalchemy.Time)

        TDPS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        TDPS_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        TDPS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        TDPS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        TDPS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        TDPS_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        TDPS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_GeneralExamForm(Connection.const.Connect.Base):
        __tablename__='M_GeneralExamForm'
        MGEFID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_GeneralExamForm_MGEFID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MGEF_Height= sqlalchemy.Column(sqlalchemy.String(200))
        MGEF_Weight= sqlalchemy.Column(sqlalchemy.String(200))
        MGEF_HeadCircumference= sqlalchemy.Column(sqlalchemy.String(200))
        MGEF_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MGEF_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MGEF_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MGEF_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MGEF_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MGEF_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MGEF_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MGEF_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_VitalsExamForm(Connection.const.Connect.Base):
        __tablename__='M_VitalsExamForm'
        MVEFID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_VitalsExamForm_MVEFID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MVEF_BloodPressure= sqlalchemy.Column(sqlalchemy.String(200))
        MVEF_PulseRate= sqlalchemy.Column(sqlalchemy.String(200))
        MVEF_RespiratoryRate= sqlalchemy.Column(sqlalchemy.String(200))
        MVEF_Temperator= sqlalchemy.Column(sqlalchemy.String(200))

        MVEF_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MVEF_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MVEF_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MVEF_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MVEF_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MVEF_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MVEF_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    class M_SystemicExam(Connection.const.Connect.Base):
        __tablename__='M_SystemicExam'
        MSEID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_SystemicExam_MSEID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSE_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MSE_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSE_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSE_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSE_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSE_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSE_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSE_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    class M_PragmaticSkills(Connection.const.Connect.Base):
        __tablename__='M_PragmaticSkills'
        MSEID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PragmaticSkills_MSEID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MPS_InitiationSkills= sqlalchemy.Column(sqlalchemy.String(200))
        MPS_RespondingSkills= sqlalchemy.Column(sqlalchemy.String(200))
        MPS_MaintenanceSkills= sqlalchemy.Column(sqlalchemy.String(200))
        MPS_TerminationSkills= sqlalchemy.Column(sqlalchemy.String(200))
        MPS_Observations= sqlalchemy.Column(sqlalchemy.String(200))
        MPS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPS_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPS_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MPS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_STOroperipheralExam(Connection.const.Connect.Base):
        __tablename__='M_STOroperipheralExam'
        MSPEID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_STOroperipheralExam_MSPEID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSPE_LipsAppearance= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_LipsMovements= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_TongueAppearance= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_TongueMovements= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_TeethAppearance= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_TeethMovements= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_HardPalateAppearance= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_SoftPalateAppearance= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_SoftPalateMovements= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_UvulaAppearance= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_UvulaMovements= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_MandibleAppearance= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_MandibleMovements= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_Drooling= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_Blowing= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_Biting= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_Sucking= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_Swallowing= sqlalchemy.Column(sqlalchemy.String(300))
        MSPE_Observations= sqlalchemy.Column(sqlalchemy.String(300))

        MSPE_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSPE_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSPE_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSPE_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSPE_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSPE_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSPE_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_STArticulationSpeechIntelligibility(Connection.const.Connect.Base):
        __tablename__='M_STArticulationSpeechIntelligibility'
        MSSIID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_STArticulationSpeechIntelligibility_MSSIID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSSI_Noonecan= sqlalchemy.Column(sqlalchemy.String(300))
        MSSI_memberscan= sqlalchemy.Column(sqlalchemy.Integer)
        MSSI_Strangerscan= sqlalchemy.Column(sqlalchemy.Integer)
        MSSI_Observations= sqlalchemy.Column(sqlalchemy.Integer)

        MSSI_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSSI_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSSI_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSSI_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSSI_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSSI_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSSI_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_STArticulationVoice(Connection.const.Connect.Base):
        __tablename__='M_STArticulationVoice'
        MSAVID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_STArticulationVoice_MSAVID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSAV_Pitch= sqlalchemy.Column(sqlalchemy.String(300))
        MSAV_Loudness= sqlalchemy.Column(sqlalchemy.Integer)
        MSAV_Quality= sqlalchemy.Column(sqlalchemy.Integer)
        MSAV_Observations= sqlalchemy.Column(sqlalchemy.Integer)

        MSAV_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSAV_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSAV_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSAV_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSAV_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSAV_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSAV_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_CognitivePrerequites(Connection.const.Connect.Base):
        __tablename__='M_CognitivePrerequites'
        MCPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_CognitivePrerequites_MCPID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MCP_Imitation= sqlalchemy.Column(sqlalchemy.String(200))
        MCP_Objectpermanence= sqlalchemy.Column(sqlalchemy.Integer)
        MCP_Timeconcept= sqlalchemy.Column(sqlalchemy.Integer)
        MCP_Colourconcept= sqlalchemy.Column(sqlalchemy.Integer)
        MCP_Moneyconcept= sqlalchemy.Column(sqlalchemy.Integer)
        MCP_Sequencing= sqlalchemy.Column(sqlalchemy.Integer)
        MCP_Matching= sqlalchemy.Column(sqlalchemy.Integer)
        MCP_Meanendrelationship= sqlalchemy.Column(sqlalchemy.Integer)
        MCP_Observations= sqlalchemy.Column(sqlalchemy.Integer)

        MCP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MCP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MCP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MCP_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MCP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_STVerbalCommunication(Connection.const.Connect.Base):
        __tablename__='M_STVerbalCommunication'
        MVCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_STVerbalCommunication_MVCID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MVC_Expression= sqlalchemy.Column(sqlalchemy.Integer)
        MVC_Comprehension= sqlalchemy.Column(sqlalchemy.Integer)
        MVC_Observations= sqlalchemy.Column(sqlalchemy.String(300))

        MVC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MVC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MVC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MVC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MVC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MVC_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MVC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_OTHandFunctions(Connection.const.Connect.Base):
        __tablename__='M_OTHandFunctions'
        MHFID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_OTHandFunctions_MHFID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MHF_HandDominance= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_HandPreference= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_ReachForward= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_ReachBackward= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_ReachLateral= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_ReachDownward= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_GraspUlnarPalmar= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_GraspPalmar= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_GraspRadialPalmar= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_GraspRadialDigital= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_GraspInferiorPincer= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_ReachUpward= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_GraspNeatPincer= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_GraspPalmarsupinate= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_GraspDigitalpronate= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_GraspStatictripod= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_GraspDynamictripod= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_PrehensionPadtoPad= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_PrehensionTiptoTip= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_PrehensionPadtoSide = sqlalchemy.Column(sqlalchemy.String(300))

        MHF_InHandManipulationFingertoPalmTranslation= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_InHandManipulationPalmtoFingerTranslation= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_InHandManipulationShift= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_InHandManipulationSimpleRotation= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_InHandComplexRotation= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_Observations= sqlalchemy.Column(sqlalchemy.String(300))
        MHF_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MHF_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MHF_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MHF_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MHF_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MHF_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MHF_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_NonEquilibrium(Connection.const.Connect.Base):
        __tablename__='M_NonEquilibrium'
        MNEID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_NonEquilibrium_MNEID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MNE_Fingertonose= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Fingertotherapistfinger= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Fingertofinger= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Alternatnosefinger= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Fingeropposition= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Massgrasp= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Pronationsupination= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Reboundtest= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Tappinghand= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Tappingfeet= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Pointingandpastpointing= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Alternateheeltokneeheeltoe= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Toetoexaminersfinger= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Heeltoshin= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Drawingacircle= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Fixationorpositionholding= sqlalchemy.Column(sqlalchemy.String(300))

        MNE_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MNE_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MNE_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MNE_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MNE_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MNE_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MNE_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Equilibrium(Connection.const.Connect.Base):
        __tablename__='M_Equilibrium'
        MNEID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Equilibrium_MNEID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MNE_Standingwithnormalbaseofsupport= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Standingwithnarrowbaseofsupport= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Standingintandemposition= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Standingononefeet= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Perturbation= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Standinginfunctionalreach= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Standinglateralflexionofthetrunktoeachside= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Tandemwalking= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_WalkingInastraightline= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Walksidewaysbackwards= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Walkinhorizontalvertical= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Marchinplace= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Startstopabruptly= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Walkandpivotincommand= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Walkincircle= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Walkonheelsandtoes= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Turnsoncommand= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Stepoveraroundobstacles= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Stairclimbingwithhandrails= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Jumpingjacks= sqlalchemy.Column(sqlalchemy.String(300))
        MNE_Sittingontherapybal= sqlalchemy.Column(sqlalchemy.String(300))

        MNE_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MNE_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MNE_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MNE_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MNE_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MNE_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MNE_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_OTCognition(Connection.const.Connect.Base):
        __tablename__='M_OTCognition'
        MOCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_OTCognition_MOCID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MOC_Praxis= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Rightleftdiscrimination= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Fingerindentification= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Orientationtoperson= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Orientationtoplace= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Conceputalseriescompletion= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Selectiveattention= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Focusedattention= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Spatialperception= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Visualmemory= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Verbalmemory= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Identificationofobjects= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Proverbinterpretation= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Randomlettertest= sqlalchemy.Column(sqlalchemy.String(300))
        MOC_Overlappingfigures= sqlalchemy.Column(sqlalchemy.String(300))

        MOC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MOC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MOC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MOC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MOC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MOC_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MOC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PosturalSystemAlignments(Connection.const.Connect.Base):
        __tablename__='M_PosturalSystemAlignments'
        MPSAID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PosturalSystemAlignments_MPSAID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_HeadNeck= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_ShoulderScapular= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_ShoulderandScapular= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_ShouldernScapular= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_RibcageandChest= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_Trunk= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_Trunks= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_PelvicComplexRight= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_PelvicComplexLeft= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_HipjointAbduction= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_HipjointAdduction= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_HipjointRotation= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_Symmetrical= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_Assymetrical= sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_Observations= sqlalchemy.Column(sqlalchemy.String(300))

        MPSA_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPSA_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPSA_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPSA_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPSA_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MPSA_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PosturalSystemBOS(Connection.const.Connect.Base):
        __tablename__='M_PosturalSystemBOS'
        MPSBID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PosturalSystemBOS_MPSBID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MPSB_BaseofSupport= sqlalchemy.Column(sqlalchemy.Integer)

        MPSB_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPSB_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPSB_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPSB_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPSB_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPSB_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MPSB_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PosturalSystemCOM(Connection.const.Connect.Base):
        __tablename__='M_PosturalSystemCOM'
        MPSCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PosturalSystemCOM_MPSCID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MPSC_CenterofMass= sqlalchemy.Column(sqlalchemy.Integer)
        MPSC_Withinsupport= sqlalchemy.Column(sqlalchemy.Integer)
        MPSC_Strategiesposture= sqlalchemy.Column(sqlalchemy.Integer)

        MPSC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPSC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPSC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPSC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPSC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPSC_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MPSC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PosturalSystemImpairments(Connection.const.Connect.Base):
        __tablename__='M_PosturalSystemImpairments'
        MPSIID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PosturalSystemImpairments_MPSIID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MPSI_MuscleArchitecture= sqlalchemy.Column(sqlalchemy.Integer)
        MPSI_Anycallosities= sqlalchemy.Column(sqlalchemy.Integer)
        MPSI_Anyotherspecificposture= sqlalchemy.Column(sqlalchemy.String(300))
        MPSI_Observations= sqlalchemy.Column(sqlalchemy.String(300))

        MPSI_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPSI_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPSI_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPSI_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPSI_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPSI_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MPSI_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PTMovementSystem(Connection.const.Connect.Base):
        __tablename__='M_PTMovementSystem'
        MPMSID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTMovementSystem_MPMSID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MPMS_Cantheyovercome= sqlalchemy.Column(sqlalchemy.Integer)
        MPMS_Howdoesthe= sqlalchemy.Column(sqlalchemy.Integer)
        MPMS_Strategiesused= sqlalchemy.Column(sqlalchemy.String(300))

        MPMS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPMS_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPMS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPMS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPMS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPMS_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MPMS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PTRangeSpeed(Connection.const.Connect.Base):
        __tablename__='M_PTRangeSpeed'
        MPMSID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTRangeSpeed_MPMSID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MRS_Rangespeedmovement= sqlalchemy.Column(sqlalchemy.Integer)
        MRS_atTrunk= sqlalchemy.Column(sqlalchemy.String(300))
        MRS_HowisitatExtremities= sqlalchemy.Column(sqlalchemy.String(300))

        MRS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MRS_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MRS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MRS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MRS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MRS_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MRS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PTStabilityMobility(Connection.const.Connect.Base):
        __tablename__='M_PTStabilityMobility'
        MSMID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTStabilityMobility_MSMID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSM_StrategiesforStabilityMobility= sqlalchemy.Column(sqlalchemy.Integer)

        MSM_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSM_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSM_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSM_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSM_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSM_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSM_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PTNeurometerSystem(Connection.const.Connect.Base):
        __tablename__='M_PTNeurometerSystem'
        MNSID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTNeurometerSystem_MNSID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MNS_Initiation= sqlalchemy.Column(sqlalchemy.Integer)
        MNS_Sustenance= sqlalchemy.Column(sqlalchemy.Integer)
        MNS_Termination= sqlalchemy.Column(sqlalchemy.Integer)
        MNS_Controlandgradation = sqlalchemy.Column(sqlalchemy.String(300))
        MNS_ContractionConcentric = sqlalchemy.Column(sqlalchemy.Integer)
        MNS_ContractionIsometric = sqlalchemy.Column(sqlalchemy.Integer)
        MNS_ContractionEccentric = sqlalchemy.Column(sqlalchemy.Integer)
        MNS_CoactivationReciprocalinhibition = sqlalchemy.Column(sqlalchemy.String(300))
        MNS_MasssynergyIsolatedwork = sqlalchemy.Column(sqlalchemy.String(300))
        MNS_Dynamicstiffness = sqlalchemy.Column(sqlalchemy.String(300))
        MNS_Extraneousmovement = sqlalchemy.Column(sqlalchemy.String(300))
        MNS_Observations = sqlalchemy.Column(sqlalchemy.String(300))

        MNS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MNS_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MNS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MNS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MNS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MNS_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MNS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PTMusculoskeletalSystem(Connection.const.Connect.Base):
        __tablename__='M_PTMusculoskeletalSystem'
        MKSID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTMusculoskeletalSystem_MKSID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MKS_Muscleendurance= sqlalchemy.Column(sqlalchemy.Integer)
        MKS_Skeletalcomments= sqlalchemy.Column(sqlalchemy.Integer)
        MKS_TardieuScaleTR1= sqlalchemy.Column(sqlalchemy.Integer)
        MKS_TardieuScaleTR2 = sqlalchemy.Column(sqlalchemy.String(300))
        MKS_TardieuScaleTR3 = sqlalchemy.Column(sqlalchemy.Integer)
        MKS_TardieuscaleHamsR1 = sqlalchemy.Column(sqlalchemy.Integer)
        MKS_TardieuscaleHamsR2 = sqlalchemy.Column(sqlalchemy.Integer)
        MKS_Observations = sqlalchemy.Column(sqlalchemy.String(300))

        MKS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MKS_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MKS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MKS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MKS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MKS_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MKS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PTSensorySystem(Connection.const.Connect.Base):
        __tablename__='M_PTSensorySystem'
        MSSID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTSensorySystem_MSSID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSS_sensorymodulationissues= sqlalchemy.Column(sqlalchemy.Integer)
        MSS_Visualsystem= sqlalchemy.Column(sqlalchemy.Integer)
        MSS_Auditorysystem= sqlalchemy.Column(sqlalchemy.Integer)
        MSS_AuditorysystemResponse = sqlalchemy.Column(sqlalchemy.Integer)
        MSS_Vestibularsystem = sqlalchemy.Column(sqlalchemy.Integer)
        MSS_Somatosensorysystem = sqlalchemy.Column(sqlalchemy.Integer)
        MSS_Oromotorsystem = sqlalchemy.Column(sqlalchemy.Integer)
        MSS_Olfactorysystem = sqlalchemy.Column(sqlalchemy.Integer)
        MSS_Observations = sqlalchemy.Column(sqlalchemy.String(300))

        MSS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSS_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSS_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PTMovementStrategies(Connection.const.Connect.Base):
        __tablename__='M_PTMovementStrategies'
        MMSID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTMovementStrategies_MMSID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MMS_Childgenerallyperformsactivitie= sqlalchemy.Column(sqlalchemy.Integer)
        MMS_CanperformLateralweightshifts= sqlalchemy.Column(sqlalchemy.Integer)
        MMS_CanperformLateralweightshiftsleft= sqlalchemy.Column(sqlalchemy.Integer)
        MMS_CanperformDiagonalweightRight = sqlalchemy.Column(sqlalchemy.Integer)
        MMS_CanperformDiagonalweightLeft = sqlalchemy.Column(sqlalchemy.Integer)
        MMS_CanperformneckthoracicspineRight = sqlalchemy.Column(sqlalchemy.Integer)
        MMS_CanperformneckthoracicspineLeft = sqlalchemy.Column(sqlalchemy.Integer)
        MMS_HowarethedissociationsPelvicfemoral = sqlalchemy.Column(sqlalchemy.Integer)
        MMS_HowaredissociationsInterlimb = sqlalchemy.Column(sqlalchemy.Integer)
        MMS_HowthedissociationsScapulohumeral = sqlalchemy.Column(sqlalchemy.Integer)
        MMS_HowthedissociationsUpperLowerbody = sqlalchemy.Column(sqlalchemy.Integer)

        MMS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MMS_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MMS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MMS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MMS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MMS_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MMS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_STNonVerbalCommunication(Connection.const.Connect.Base):
        __tablename__='M_STNonVerbalCommunication'
        MNVCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_STNonVerbalCommunication_MNVCID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MNVC_Expression= sqlalchemy.Column(sqlalchemy.Integer)
        MNVC_Comprehension= sqlalchemy.Column(sqlalchemy.Integer)
        MNVC_Observations= sqlalchemy.Column(sqlalchemy.String(300))

        MNVC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MNVC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MNVC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MNVC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MNVC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MNVC_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MNVC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_OTSensoryExam(Connection.const.Connect.Base):
        __tablename__='M_OTSensoryExam'
        MSEID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_OTSensoryExam_MSEID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.String(200))
        MSE_Visualtracking= sqlalchemy.Column(sqlalchemy.Integer)
        MSE_Choreiformmovements= sqlalchemy.Column(sqlalchemy.Integer)
        MSE_Tremor= sqlalchemy.Column(sqlalchemy.Integer)
        MSE_Exaggeratedassociated= sqlalchemy.Column(sqlalchemy.Integer)
        MSE_Graphesthesis= sqlalchemy.Column(sqlalchemy.Integer)
        MSE_Stereognosis= sqlalchemy.Column(sqlalchemy.Integer)
        MSE_Weightbearinghands= sqlalchemy.Column(sqlalchemy.Integer)
        MSE_Proneextensionpattern= sqlalchemy.Column(sqlalchemy.Integer)

        MSE_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSE_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSE_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSE_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSE_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSE_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSE_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    class M_OTSensoryProfile(Connection.const.Connect.Base):
        __tablename__='M_OTSensoryProfile'
        MSPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_OTSensoryProfile_MSPID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSP_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MSP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSP_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Addtionalinfo(Connection.const.Connect.Base):
        __tablename__='M_Addtionalinfo'
        MAIID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Addtionalinfo_MAIID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MAI_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MAI_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MAI_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MAI_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MAI_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MAI_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MAI_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MAI_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PTFunctionalAbilities(Connection.const.Connect.Base):
        __tablename__='M_PTFunctionalAbilities'
        MFAID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTFunctionalAbilities_MFAID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MFA_GrossMotor= sqlalchemy.Column(sqlalchemy.String(200))
        MFA_FineMotor= sqlalchemy.Column(sqlalchemy.String(200))
        MFA_CommunicationSpeech= sqlalchemy.Column(sqlalchemy.String(200))
        MFA_Feeding= sqlalchemy.Column(sqlalchemy.String(200))
        MFA_Playskills= sqlalchemy.Column(sqlalchemy.String(200))
        MFA_ADL= sqlalchemy.Column(sqlalchemy.String(200))

        MFA_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MFA_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MFA_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MFA_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MFA_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MFA_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MFA_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    class M_PTFunctionalLimitations(Connection.const.Connect.Base):
        __tablename__='M_PTFunctionalLimitations'
        MFLID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTFunctionalLimitations_MFLID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MFL_GrossMotor= sqlalchemy.Column(sqlalchemy.String(200))
        MFL_FineMotor= sqlalchemy.Column(sqlalchemy.String(200))
        MFL_CommunicationSpeech= sqlalchemy.Column(sqlalchemy.String(200))
        MFL_Feeding= sqlalchemy.Column(sqlalchemy.String(200))
        MFL_Playskills= sqlalchemy.Column(sqlalchemy.String(200))
        MFL_ADL= sqlalchemy.Column(sqlalchemy.String(200))

        MFL_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MFL_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MFL_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MFL_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MFL_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MFL_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MFL_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PTAnticipatoryControl(Connection.const.Connect.Base):
        __tablename__='M_PTAnticipatoryControl'
        MACID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTAnticipatoryControl_MACID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MAC_Canchildanti= sqlalchemy.Column(sqlalchemy.Integer)
        MAC_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MAC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MAC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MAC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MAC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MAC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MAC_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MAC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    class M_PTPosturalCounterbalance(Connection.const.Connect.Base):
        __tablename__='M_PTPosturalCounterbalance'
        MPCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTPosturalCounterbalance_MPCID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MPC_Observations= sqlalchemy.Column(sqlalchemy.Integer)


        MPC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPC_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MPC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PTMovementSystemImpairment(Connection.const.Connect.Base):
        __tablename__='M_PTMovementSystemImpairment'
        MSIID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTMovementSystemImpairment_MSIID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSI_Excessivemovementfortasks= sqlalchemy.Column(sqlalchemy.String(200))
        MSI_Lackofmovementstaticpostures= sqlalchemy.Column(sqlalchemy.String(200))
        MSI_IntegrationofPostureMovement= sqlalchemy.Column(sqlalchemy.String(200))
        MSI_Howdoeschildmaintainbalanceintransitions= sqlalchemy.Column(sqlalchemy.String(200))
        MSI_Accuracyofmovements= sqlalchemy.Column(sqlalchemy.String(200))
        MSI_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MSI_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSI_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSI_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSI_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSI_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSI_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSI_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PTRegulatorySystem(Connection.const.Connect.Base):
        __tablename__='M_PTRegulatorySystem'
        MRSID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTRegulatorySystem_MRSID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MRS_Affect= sqlalchemy.Column(sqlalchemy.Integer)
        MRS_Arousal= sqlalchemy.Column(sqlalchemy.Integer)
        MRS_Attention= sqlalchemy.Column(sqlalchemy.Integer)
        MRS_Action= sqlalchemy.Column(sqlalchemy.Integer)
        MRS_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MRS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MRS_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MRS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MRS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MRS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MRS_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MRS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PTCognitiveSystem(Connection.const.Connect.Base):
        __tablename__='M_PTCognitiveSystem'
        MCSID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PTCognitiveSystem_MCSID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MCS_Intelligence= sqlalchemy.Column(sqlalchemy.String(200))
        MCS_Memory= sqlalchemy.Column(sqlalchemy.String(200))
        MCS_Adaptability= sqlalchemy.Column(sqlalchemy.String(200))
        MCS_MotorPlanning= sqlalchemy.Column(sqlalchemy.String(200))
        MCS_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MCS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCS_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MCS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MCS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MCS_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MCS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_NICHQVanderbiltADHDParent(Connection.const.Connect.Base):
        __tablename__='M_NICHQVanderbiltADHDParent'
        MVAID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_NICHQVanderbiltADHDParent_MVAID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MVA_Score= sqlalchemy.Column(sqlalchemy.String(200))
        MVA_Interpretation= sqlalchemy.Column(sqlalchemy.String(200))

        MVA_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MVA_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MVA_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MVA_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MVA_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MVA_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MVA_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_SequinFormBoardTest(Connection.const.Connect.Base):
        __tablename__='M_SequinFormBoardTest'
        MSFBID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_SequinFormBoardTest_MSFBID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSFB_MentalAge= sqlalchemy.Column(sqlalchemy.String(200))
        MSFB_IQ= sqlalchemy.Column(sqlalchemy.String(200))
        MSFB_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MSFB_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSFB_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSFB_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSFB_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSFB_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSFB_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSFB_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ChildhoodAutismRatingScale(Connection.const.Connect.Base):
        __tablename__='M_ChildhoodAutismRatingScale'
        MCARID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ChildhoodAutismRatingScale_MCARID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MCAR_Scores= sqlalchemy.Column(sqlalchemy.String(200))
        MCAR_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MCAR_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCAR_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MCAR_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MCAR_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCAR_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MCAR_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MCAR_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_VinelandSocialMaturityScale(Connection.const.Connect.Base):
        __tablename__='M_VinelandSocialMaturityScale'
        MVAMID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_VinelandSocialMaturityScale_MVAMID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MVAM_SocialAge= sqlalchemy.Column(sqlalchemy.String(200))
        MVAM_IQ= sqlalchemy.Column(sqlalchemy.String(200))
        MVAM_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MVAM_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MVAM_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MVAM_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MVAM_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MVAM_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MVAM_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MVAM_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_GeselsDrawingTestofintelligence(Connection.const.Connect.Base):
        __tablename__='M_GeselsDrawingTestofintelligence'
        MGDIID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_GeselsDrawingTestofintelligence_MGDIID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MGDI_MentalAge= sqlalchemy.Column(sqlalchemy.String(200))
        MGDI_IQ= sqlalchemy.Column(sqlalchemy.String(200))
        MGDI_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MGDI_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MGDI_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MGDI_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MGDI_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MGDI_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MGDI_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MGDI_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_MalinIntelligenceScaleforIndianChildren(Connection.const.Connect.Base):
        __tablename__='M_MalinIntelligenceScaleforIndianChildren'
        MISIID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_MalinIntelligenceScaleforIndianChildren_MISIID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MISI_VerbalQuotient = sqlalchemy.Column(sqlalchemy.String(200))
        MISI_PerformanceQuotient= sqlalchemy.Column(sqlalchemy.String(200))
        MISI_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MISI_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MISI_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MISI_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MISI_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MISI_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MISI_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MISI_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()
    class M_ChildBehaviorChecklist(Connection.const.Connect.Base):
        __tablename__='M_ChildBehaviorChecklist'
        MCBCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ChildBehaviorChecklist_MISIID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MCBC_Scores = sqlalchemy.Column(sqlalchemy.String(200))
        MCBC_Tscores= sqlalchemy.Column(sqlalchemy.String(200))
        MCBC_Range= sqlalchemy.Column(sqlalchemy.String(200))
        MCBC_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MCBC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCBC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MCBC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MCBC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCBC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MCBC_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MCBC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_DevelopmentalProfile(Connection.const.Connect.Base):
        __tablename__='M_DevelopmentalProfile'
        MDPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_DevelopmentalProfile_MDPID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MDP_StandardScore = sqlalchemy.Column(sqlalchemy.String(200))
        MDP_confidenceband= sqlalchemy.Column(sqlalchemy.String(200))
        MDP_Descriptivecategory= sqlalchemy.Column(sqlalchemy.String(200))
        MDP_Ageequivalent= sqlalchemy.Column(sqlalchemy.String(200))
        MDP_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MDP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MDP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MDP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MDP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MDP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MDP_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MDP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ConnersParentRatingScale(Connection.const.Connect.Base):
        __tablename__='M_ConnersParentRatingScale'
        MCPRID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ConnersParentRatingScale_MISIID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MCPR_Scores = sqlalchemy.Column(sqlalchemy.String(200))
        MCPR_Tscores= sqlalchemy.Column(sqlalchemy.String(200))
        MCPR_Range= sqlalchemy.Column(sqlalchemy.String(200))
        MCPR_Observations= sqlalchemy.Column(sqlalchemy.String(200))

        MCPR_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCPR_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MCPR_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MCPR_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCPR_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MCPR_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MCPR_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_RavenStandardProgressiveMatrices(Connection.const.Connect.Base):
        __tablename__='M_RavenStandardProgressiveMatrices'
        MRSPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_RavenStandardProgressiveMatrices_MRSPID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MRSP_RawScore = sqlalchemy.Column(sqlalchemy.String(200))
        MRSP_Percentile= sqlalchemy.Column(sqlalchemy.String(200))
        MRSP_Grade= sqlalchemy.Column(sqlalchemy.String(200))
        MRSP_Interpretation= sqlalchemy.Column(sqlalchemy.String(200))

        MRSP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MRSP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MRSP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MRSP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MRSP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MRSP_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MRSP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ReceptiveLanguageAssessment(Connection.const.Connect.Base):
        __tablename__='M_ReceptiveLanguageAssessment'
        MRLAID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ReceptiveLanguageAssessment_MRLAID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Comprehendssounds = sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Comprehendsloud= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Comprehendscategorizesounds= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Comprehendsanimalsounds= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Comprehendsfruitsname= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Comprehendscolorsname = sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Comprehendsanimalname= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Comprehendsvegetablename= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Comprehendsshapesname= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Comprehendsbodyparts= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Comprehendsvehiclenames = sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Understandingrhymes= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Respondscorrectly= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Identifiessounds= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Actsoutcommands= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Comprehendsstepscommands = sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Understandinggreeting= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_Understanding= sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MRLA_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MRLA_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MRLA_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MRLA_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MRLA_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_StutteringAssessment(Connection.const.Connect.Base):
        __tablename__='M_StutteringAssessment'
        MSAID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_StutteringAssessment_MSAID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSA_Behaviouralassessment = sqlalchemy.Column(sqlalchemy.String(200))
        MSA_Cognitiveassessment= sqlalchemy.Column(sqlalchemy.String(200))
        MSA_Impacteducationalparticipation= sqlalchemy.Column(sqlalchemy.String(200))
        MSA_thechildlikelytoachieve= sqlalchemy.Column(sqlalchemy.String(200))
        MSA_prognosisforeffect= sqlalchemy.Column(sqlalchemy.Integer)

        MSA_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSA_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSA_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSA_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSA_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSA_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSA_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ExpressiveLanguageAssessment(Connection.const.Connect.Base):
        __tablename__='M_ExpressiveLanguageAssessment'
        MELAID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ExpressiveLanguageAssessment_MELAID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Imitatesenvironmentalsounds = sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Imitatesloudandsoftsounds= sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Imitateslexicalcategories= sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Imitatescolorsname= sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Imitatesbodyparts= sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Imitatessingingandphrases = sqlalchemy.Column(sqlalchemy.Integer)
        MELA_ImitatesalphabetsAtoZ= sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Usesnounwitharticles= sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Watchesfaceandbody= sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Imitatescounting= sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Clapstobeatoffamiliarsongs = sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Respondstosinglesigns= sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Imitatessocialgreetings= sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Occassionallytrytoimitate= sqlalchemy.Column(sqlalchemy.Integer)
        MELA_Imitatescommonsyllables= sqlalchemy.Column(sqlalchemy.Integer)

        MELA_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MELA_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MELA_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MELA_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MELA_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MELA_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MELA_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_SpecialEdassessmenttwoyears(Connection.const.Connect.Base):
        __tablename__='M_SpecialEdassessmenttwoyears'
        MSATWID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_SpecialEdassessmenttwoyears_MSATWID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Respondstoname = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Makeseyecontact= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Respondstolightandsoundtoys= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canmoveeyesupanddown= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canmoveeyesleftandright= sqlalchemy.Column(sqlalchemy.Integer)

        MSATW_repeatswords= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_knowsidentificationofnumber= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canrollpoundandsqueezeclay= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularyMom= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularyDad= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Vocabularydog = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularycat= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularytree= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularytable= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularychair= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularycow = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularycrayons= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularybus= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularycar= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularybook = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularyapple= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularybanana= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularybottle= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Candostacking= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canmaketower = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_respondstobubbles= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Identifieshappyandsad= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Knowsshapes= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_knowscolors= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_knowsanimals = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_knowsvehicles= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_knowsbodyparts= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_knowsidentificationofalphabets= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_knowsmoreorless= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_knowsbigandsmall = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_knowsnearandfar= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canidentifhisorher= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canidentifybag= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canidentifyshoes= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canidentifybottle = sqlalchemy.Column(sqlalchemy.Integer)

        MSATW_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSATW_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSATW_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSATW_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSATW_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_SpecialEdassessmentThreeyears(Connection.const.Connect.Base):
        __tablename__='M_SpecialEdassessmentThreeyears'
        MSATWID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_SpecialEdassessmentThreeyears_MSATWID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_respondstoname = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_makeseyecontact= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cansitformins= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canmoveeyesupanddown= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canmoveeyesleftandright= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cananswerfullname= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularybodyparts= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canfollowstepsinstruction= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cananswerold= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cananswerwhatsyourmothersname= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cananswerwhichisyoufavoritecolour= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canfixpiecepuzzle= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularyshapescircle = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularycolors= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularywild= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Vocabularyfruits= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canfollowstepinstruction= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cansingrhymes = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cangiveanswerseeinsky= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cangiveanswerswiminwater= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cangiveanswerseeontree= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_knowsidentificationofalphabets = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_knowsidentificationofnumbers= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Canholdapencilcrayon= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canscribble= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cancoloringivenshape= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cantearandpaste = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canidentifyemotionshappy= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canidentifyemotionssad= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canidentifyemotionsangry= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canidentifyemotionsupset= sqlalchemy.Column(sqlalchemy.Integer)

        MSATW_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSATW_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSATW_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSATW_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSATW_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_SpecialAssessmentthrefourYrs(Connection.const.Connect.Base):
        __tablename__='M_SpecialAssessmentthrefourYrs'
        MSATWID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_SpecialAssessmentthrefourYrs_MSATWID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_doesrespondtonamecall = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_doesmakeseyecontact= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_initiatesinteractiontoward= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cansitformins= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_understandinstructionslikestand= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_getthatputthere= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_givemegetthis= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_runwalkjump= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_lookdownup= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cananswerwhatis= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cananswerfavoritecolour= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canfixpiecepuzzle= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularyshapes = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularycolors= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularywild= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularyfruits= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularybodyparts= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Canunderstandpositions = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cansingrhymes= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canunderstandstories= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canWhatquestions= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canidentifybasicobjects = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canholdacrayonpencil= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canmaketower= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canimitate= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canplaydoughballs= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canheshethrow = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canrecognisealphabet= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Canrecognisenumerals= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cancolourgivenshape= sqlalchemy.Column(sqlalchemy.Integer)

        MSATW_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSATW_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSATW_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSATW_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSATW_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_SpecialAssessmentfourYrs(Connection.const.Connect.Base):
        __tablename__='M_SpecialAssessmentfourYrs'
        MSATWID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_SpecialAssessmentfourYrs_MSATWID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_respondnamecall = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_makeseyecontact= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_interactiontowardothers= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cansitformins= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cananswerwhatname= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_answerfavoritecolour= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canfixpiecepuzzle= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularyshapes= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularycolors= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularywild= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_vocabularybody= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Vocabularyfruits= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canunderstandpositions = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cansingrhymes= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canunderstandstories= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_replyWhatquestions= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_identifybasicobjects= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_holdcrayonpencil = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canimitate= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_doughmakeballs= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canthrow= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_recognisealphabets = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_recognisenumerals= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cancolourshape= sqlalchemy.Column(sqlalchemy.Integer)

        MSATW_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSATW_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSATW_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSATW_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSATW_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_SpecialAssessmentSevenYrs(Connection.const.Connect.Base):
        __tablename__='M_SpecialAssessmentSevenYrs'
        MSATWID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_SpecialAssessmentSevenYrs_MSATWID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_putneedsminimalassistance = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_eathandsonly= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_fixasandwich= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_givefirstlastname= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_cangiveaddress= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_awareofemotions= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canzipper= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_independentlyassistanct= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_asksmeaningfulquestions= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_tellsstorieswords= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_Doestellage= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_canobeysimplecommands= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_readsimplewords = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_writesimplewords= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_namethingsaround= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_alternatesfeetupdownstairs= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_pedaltricycle= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_catchandthrowball = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_towersmallblocks= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_doughmakeballs= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_tieshoes= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_holdpencilproperly = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_drawsanyshape= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_usescissorscutshape= sqlalchemy.Column(sqlalchemy.Integer)

        MSATW_learnseasily= sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_manyfingershand = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_countbeyond= sqlalchemy.Column(sqlalchemy.Integer)

        MSATW_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSATW_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSATW_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSATW_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSATW_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSATW_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PHQAssessment(Connection.const.Connect.Base):
        __tablename__='M_PHQAssessment'
        MPAID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PHQAssessment_MPAID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MPA_AnyPleasure = sqlalchemy.Column(sqlalchemy.Integer)
        MPA_AnyDepression= sqlalchemy.Column(sqlalchemy.Integer)
        MPA_AnyTrouble= sqlalchemy.Column(sqlalchemy.Integer)
        MPA_Anytiredness= sqlalchemy.Column(sqlalchemy.Integer)
        MPA_AnyOvereat= sqlalchemy.Column(sqlalchemy.Integer)
        MPA_Anybadfeel = sqlalchemy.Column(sqlalchemy.Integer)
        MPA_TroubledbyAnything= sqlalchemy.Column(sqlalchemy.Integer)
        MPA_MovingAroundAlot= sqlalchemy.Column(sqlalchemy.Integer)
        MPA_AnyHurtYourself= sqlalchemy.Column(sqlalchemy.Integer)

        MPA_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPA_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPA_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPA_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPA_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPA_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MPA_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_HARSAssessment(Connection.const.Connect.Base):
        __tablename__='M_HARSAssessment'
        MHAID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_HARSAssessment_MHAID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_anyAnxiousMood = sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnyTensionFeeling= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnyFearsfeeling= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnyInsomnia= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnyIntellectual= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnyDipressedMood = sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnySomaticpains= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnySomaticWeekness= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnyCardiovascular= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnyRespiratory= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnyGastrontedtinal = sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnyGenitourinarySymptoms= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnyAutonomicSymptoms= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AnyBehaviouratInterview= sqlalchemy.Column(sqlalchemy.Integer)

        MHA_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MHA_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MHA_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MHA_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MHA_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MHA_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_HRDSAssessment(Connection.const.Connect.Base):
        __tablename__='M_HRDSAssessment'
        MHAID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_HRDSAssessment_MHAID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HRDSDepressedMood = sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HRDSFeelingGuilt= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HRDSSuide= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HRDSInsomnia= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HRDSMidNight= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HRDSEarlyMorning = sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HRDSWork= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HRDSRetardation= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HRDSAgitation= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HRDSPsychic= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HRDSAnxietySomatic = sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HRDSSomatic= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HDRSGeneralSomatic= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HDRSLossOfLibido= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HDRSHypochondriasis= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HDRSLossofWeight= sqlalchemy.Column(sqlalchemy.Integer)
        MHA_HDRSInsight= sqlalchemy.Column(sqlalchemy.Integer)

        MHA_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MHA_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MHA_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MHA_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MHA_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MHA_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MHA_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_CKASAssessment(Connection.const.Connect.Base):
        __tablename__='M_CKASAssessment'
        MCAID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_CKASAssessment_MCAID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASConsistentEyeContact = sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASPointsTowardsObject= sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASFollowSimpleCommand= sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASRespondWhencalled= sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASTryToCopy= sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASCallOutMama = sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASInterestInplaying= sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASLimitedUseofLanguage= sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASFrequentEyeBlinkt= sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASClimbWithoutScare= sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASSpeakNonContextly = sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASIndicateTowardsObject= sqlalchemy.Column(sqlalchemy.Integer)
        MCA_CKASAnyRegression= sqlalchemy.Column(sqlalchemy.Integer)

        MCA_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCA_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MCA_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MCA_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MCA_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MCA_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MCA_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_SessionNotes(Connection.const.Connect.Base):
        __tablename__='M_SessionNotes'
        MSNID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_SessionNotes_MSNID'),primary_key=True)
        M_Patient_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        MSN_started = sqlalchemy.Column(sqlalchemy.Integer)
        MSN_todayfeeling= sqlalchemy.Column(sqlalchemy.Integer)
        MSN_dotoday= sqlalchemy.Column(sqlalchemy.Integer)
        MSN_Notes= sqlalchemy.Column(sqlalchemy.String(800))
        MSN_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSN_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSN_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSN_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSN_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSN_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MSN_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PatientUplpoadFiles(Connection.const.Connect.Base):
        __tablename__='M_PatientUplpoadFiles'
        MPFID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PatientUplpoadFiles_MPFID'),primary_key=True)
        MPF_PatientID = sqlalchemy.Column(sqlalchemy.Integer)
        MPF_Name= sqlalchemy.Column(sqlalchemy.String(100))
        MPF_FilePath= sqlalchemy.Column(sqlalchemy.String(100))
        MPF_FileType= sqlalchemy.Column(sqlalchemy.String(100))
        MPF_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPF_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPF_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPF_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPF_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPF_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MPF_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ProvisionalDiagnosis(Connection.const.Connect.Base):
        __tablename__='M_ProvisionalDiagnosis'
        MPDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ProvisionalDiagnosis_MPDID'),primary_key=True)
        M_PatientID = sqlalchemy.Column(sqlalchemy.Integer)
        MPD_ProvisionalDiagnosis= sqlalchemy.Column(sqlalchemy.String(100))
        MPD_ICDCode= sqlalchemy.Column(sqlalchemy.String(100))
        MPD_ICDDescription= sqlalchemy.Column(sqlalchemy.String(100))
        MPD_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPD_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPD_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPD_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPD_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPD_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MPD_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PatientReview(Connection.const.Connect.Base):
        __tablename__='M_PatientReview'
        MPRID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PatientReview_MPRID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MPR_FollowAfter= sqlalchemy.Column(sqlalchemy.String(100))
        MPR_FollowDate= sqlalchemy.Column(sqlalchemy.String(100))
        MPR_Comments= sqlalchemy.Column(sqlalchemy.String(300))
        MPR_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPR_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPR_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPR_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPR_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPR_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MPR_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Prescription(Connection.const.Connect.Base):
        __tablename__='M_Prescription'
        MPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Prescription_MPID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MP_PresentConcerns= sqlalchemy.Column(sqlalchemy.String(400))
        MP_InformedBy= sqlalchemy.Column(sqlalchemy.String(400))
        MP_AgeWhenNoticed = sqlalchemy.Column(sqlalchemy.String(400))

        MP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MP_IsActive = sqlalchemy.Column(
           sqlalchemy.Boolean, unique=False, default=1)
        MP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Services(Connection.const.Connect.Base):
        __tablename__='M_Services'
        MPDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Services_MPDID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        MS_ServiceName= sqlalchemy.Column(sqlalchemy.String(100))
        MS_Quantity= sqlalchemy.Column(sqlalchemy.String(100))
        MS_TotalCost= sqlalchemy.Column(sqlalchemy.String(300))
        MS_Comments=sqlalchemy.Column(sqlalchemy.String(300))
        MS_Status=sqlalchemy.Column(sqlalchemy.String(300))
        MS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MS_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MS_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Coupons(Connection.const.Connect.Base):
        __tablename__='M_Coupons'
        MCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Coupons_MCID'),primary_key=True)
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        CouponType= sqlalchemy.Column(sqlalchemy.String(100))
        SelectHCP= sqlalchemy.Column(sqlalchemy.String(100))
        Discount= sqlalchemy.Column(sqlalchemy.String(300))
        ValidityDays=sqlalchemy.Column(sqlalchemy.String(300))
        CouponCode=sqlalchemy.Column(sqlalchemy.String(300))
        MC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MC_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PartnerOrg(Connection.const.Connect.Base):
        __tablename__='M_PartnerOrg'
        MPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PartnerOrg_MPID'),primary_key=True)
        OrgName= sqlalchemy.Column(sqlalchemy.String(100))

        MP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MP_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()


    class M_LabTest(Connection.const.Connect.Base):
        __tablename__='M_LabTest'
        MLID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_LabTest_MLID'),primary_key=True)
        LabTestName= sqlalchemy.Column(sqlalchemy.String(100))
        M_Patient_MPID = sqlalchemy.Column(sqlalchemy.Integer)
        FileName= sqlalchemy.Column(sqlalchemy.String(100))
        FilePath= sqlalchemy.Column(sqlalchemy.String(100))
        ML_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        ML_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        ML_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        ML_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        ML_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        ML_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        ML_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Therapist(Connection.const.Connect.Base):
        __tablename__='M_Therapist'
        MTID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Therapist_MTID'),primary_key=True)
        mobile= sqlalchemy.Column(sqlalchemy.String(100))
        CKid = sqlalchemy.Column(sqlalchemy.String(100))
        title= sqlalchemy.Column(sqlalchemy.Integer)
        fullname= sqlalchemy.Column(sqlalchemy.String(100))
        emailid= sqlalchemy.Column(sqlalchemy.String(100))
        Specialty= sqlalchemy.Column(sqlalchemy.String(100))
        status= sqlalchemy.Column(sqlalchemy.Integer)
        displaysuffix= sqlalchemy.Column(sqlalchemy.String(100))

        MT_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MT_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MT_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MT_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MT_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MT_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MT_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Staff(Connection.const.Connect.Base):
        __tablename__='M_Staff'
        MSID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Staff_MSID'),primary_key=True)
        code= sqlalchemy.Column(sqlalchemy.Integer)
        mobile= sqlalchemy.Column(sqlalchemy.String(100))
        CKid = sqlalchemy.Column(sqlalchemy.String(100))
        title= sqlalchemy.Column(sqlalchemy.Integer)
        fullname= sqlalchemy.Column(sqlalchemy.String(100))
        emailid= sqlalchemy.Column(sqlalchemy.String(100))
        Specialty= sqlalchemy.Column(sqlalchemy.String(100))
        status= sqlalchemy.Column(sqlalchemy.Integer)
        displaysuffix= sqlalchemy.Column(sqlalchemy.String(100))

        MT_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MT_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MT_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MT_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MT_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MT_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MT_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_DifferentMenu(Connection.const.Connect.Base):
        __tablename__='M_DifferentMenu'
        MDMID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_DifferentMenu_MDMID'),primary_key=True)
        MDM_FormName= sqlalchemy.Column(sqlalchemy.String(100))
        M_Control_MCID = sqlalchemy.Column(sqlalchemy.Integer)
        MDM_Label= sqlalchemy.Column(sqlalchemy.Integer)
        MDM_Id= sqlalchemy.Column(sqlalchemy.String(100))
        MDM_databstarget= sqlalchemy.Column(sqlalchemy.String(100))
        MDM_Path= sqlalchemy.Column(sqlalchemy.String(100))
        MDM_Preferences= sqlalchemy.Column(sqlalchemy.Integer)
        MDM_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MDM_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MDM_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MDM_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MDM_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MDM_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MDM_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ExpenseRegister(Connection.const.Connect.Base):
        __tablename__='M_ExpenseRegister'
        MEID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ExpenseRegister_MDMID'),primary_key=True)
        VendorName= sqlalchemy.Column(sqlalchemy.String(100))
        InvoiceNo = sqlalchemy.Column(sqlalchemy.String(100))
        Amount= sqlalchemy.Column(sqlalchemy.String(100))
        PaymentMode= sqlalchemy.Column(sqlalchemy.Integer)
        Status= sqlalchemy.Column(sqlalchemy.Integer)
        Comments= sqlalchemy.Column(sqlalchemy.String(100))
        InvoiceDate= sqlalchemy.Column(sqlalchemy.Date)
        DueDate= sqlalchemy.Column(sqlalchemy.Date)
        PaymentDate= sqlalchemy.Column(sqlalchemy.Date)

        ME_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        ME_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        ME_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        ME_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        ME_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        ME_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        ME_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_UserType(Connection.const.Connect.Base):
        __tablename__='M_UserType'
        MUID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_UserType_MUID'),primary_key=True)
        MU_UserType= sqlalchemy.Column(sqlalchemy.Integer)
        MU_UserName = sqlalchemy.Column(sqlalchemy.String(100))

        MU_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MU_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MU_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MU_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MU_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MU_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MU_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_UserCredentials(Connection.const.Connect.Base):
        __tablename__='M_UserCredentials'
        MUCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_UserCredentials_MUCID'),primary_key=True)
        MUC_UserType= sqlalchemy.Column(sqlalchemy.Integer)
        MUC_UserName = sqlalchemy.Column(sqlalchemy.String(100))
        MUC_Password = sqlalchemy.Column(sqlalchemy.String(100))

        MUC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MUC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MUC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MUC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MUC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MUC_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MUC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Rights(Connection.const.Connect.Base):
        __tablename__='M_Rights'
        MRID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Rights_MRID'),primary_key=True)
        MR_Name= sqlalchemy.Column(sqlalchemy.String(100))
        MR_InitialValue= sqlalchemy.Column(sqlalchemy.String(100))
        MR_Label= sqlalchemy.Column(sqlalchemy.String(100))
        MR_Type= sqlalchemy.Column(sqlalchemy.String(100))
        MR_required= sqlalchemy.Column(sqlalchemy.Boolean, unique=False, default=0)
        MR_RightPage= sqlalchemy.Column(sqlalchemy.String(100), default=0)

        MR_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MR_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MR_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MR_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MR_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MR_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MR_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Pages(Connection.const.Connect.Base):
        __tablename__='M_Pages'
        MPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Pages_MPID'),primary_key=True)
        MP_PageName= sqlalchemy.Column(sqlalchemy.String(100))
        MP_PageParent= sqlalchemy.Column(sqlalchemy.String(100))

        MP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MP_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Users(Connection.const.Connect.Base):
        __tablename__='M_Users'
        MUID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Users_MUID'),primary_key=True)
        MU_Name= sqlalchemy.Column(sqlalchemy.String(100))
        MU_Email= sqlalchemy.Column(sqlalchemy.String(100))
        MU_PersonalEmail= sqlalchemy.Column(sqlalchemy.String(100))
        MU_Mobile= sqlalchemy.Column(sqlalchemy.String(100))
        MU_Username= sqlalchemy.Column(sqlalchemy.String(100))
        MU_UserType= sqlalchemy.Column(sqlalchemy.Integer)
        MU_Password= sqlalchemy.Column(sqlalchemy.String(100))
        MU_ConfirmPassword= sqlalchemy.Column(sqlalchemy.String(100))

        MU_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MU_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MU_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MU_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MU_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MU_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MU_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Service(Connection.const.Connect.Base):
        __tablename__='M_Service'
        MSID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Service_MSID'),primary_key=True)
        MS_FileName= sqlalchemy.Column(sqlalchemy.String(100))
        MS_FilePath= sqlalchemy.Column(sqlalchemy.String(100))
        MS_CategoryName= sqlalchemy.Column(sqlalchemy.String(100))
        MS_Description= sqlalchemy.Column(sqlalchemy.String(100))

        MS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MS_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MS_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Policy(Connection.const.Connect.Base):
        __tablename__='M_Policy'
        MPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Policy_MPID'),primary_key=True)
        MP_PolicyName= sqlalchemy.Column(sqlalchemy.String(100))
        MP_PolicyParent = sqlalchemy.Column(sqlalchemy.String(20))
        MP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MP_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_AssignRole(Connection.const.Connect.Base):
        __tablename__='M_AssignRole'
        MARID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_AssignRole_MARID'),primary_key=True)
        M_Users_MUID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Policy_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)


        MP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MP_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_PolicyRights(Connection.const.Connect.Base):
        __tablename__='M_PolicyRights'
        MPRID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_PolicyRights_MPRID'),primary_key=True)
        M_Policy_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Pages_MPID= sqlalchemy.Column(sqlalchemy.Integer)
        M_Rights_MRID= sqlalchemy.Column(sqlalchemy.Integer)
        MPR_IsAssign= sqlalchemy.Column(sqlalchemy.Boolean)



        MP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MP_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ServicePro(Connection.const.Connect.Base):
        __tablename__='M_ServicePro'
        MSPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ServicePro_MSPID'),primary_key=True)
        MSP_serviceId= sqlalchemy.Column(sqlalchemy.Integer)
        MSP_Fee= sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        MSP_Duration= sqlalchemy.Column(sqlalchemy.Integer)
        MSP_Bonus= sqlalchemy.Column(sqlalchemy.Integer)
        MSP_SuitedFor= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_categories= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_ServiceOptions= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_FileName= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_FilePath= sqlalchemy.Column(sqlalchemy.String(100))

        MSP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSP_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MSP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ServicePackage(Connection.const.Connect.Base):
        __tablename__='M_ServicePackage'
        MSPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ServicePackage_MSPID'),primary_key=True)
        MSP_PackageType= sqlalchemy.Column(sqlalchemy.Integer)
        MSP_PackageName= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_ServiceName= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_Options= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_Price= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_Sessions= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_TotalCost= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_Months= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_PackagePrice= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_Tax= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_Total= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_Description= sqlalchemy.Column(sqlalchemy.String(100))
        MSP_Status= sqlalchemy.Column(sqlalchemy.Integer)

        MSP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSP_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MSP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSP_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MSP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Promotions(Connection.const.Connect.Base):
        __tablename__='M_Promotions'
        MPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_Promotions_MPID'),primary_key=True)
        MP_PromoName= sqlalchemy.Column(sqlalchemy.String(100))
        MP_FilePath= sqlalchemy.Column(sqlalchemy.String(100))
        MP_fileName= sqlalchemy.Column(sqlalchemy.String(100))
        MP_PromoType= sqlalchemy.Column(sqlalchemy.Integer)
        MP_TagLine= sqlalchemy.Column(sqlalchemy.String(100))
        MP_Description= sqlalchemy.Column(sqlalchemy.String(100))
        MP_StartDate= sqlalchemy.Column(sqlalchemy.String(100))
        MP_EndDate= sqlalchemy.Column(sqlalchemy.String(100))
        MP_DiscountPercent= sqlalchemy.Column(sqlalchemy.String(100))

        MP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_AddDate = sqlalchemy.Column(
           sqlalchemy.DateTime, default=datetime.datetime.now)
        MP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MP_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ServicePreTreatement(Connection.const.Connect.Base):
        __tablename__='M_ServicePreTreatement'
        MSPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ServicePreTreatement_MSPID'),primary_key=True)
        MSP_PreTreatement= sqlalchemy.Column(sqlalchemy.String(400))
        MSP_PackageID= sqlalchemy.Column(sqlalchemy.Integer)


        MSP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSP_AddDate = sqlalchemy.Column(
           sqlalchemy.DateTime, default=datetime.datetime.now)
        MSP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSP_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MSP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ServicePostTreatement(Connection.const.Connect.Base):
        __tablename__='M_ServicePostTreatement'
        MSPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ServicePostTreatement_MSPID'),primary_key=True)
        MSP_PostTreatement= sqlalchemy.Column(sqlalchemy.String(400))
        MSP_PackageID= sqlalchemy.Column(sqlalchemy.Integer)

        MSP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSP_AddDate = sqlalchemy.Column(
           sqlalchemy.DateTime, default=datetime.datetime.now)
        MSP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSP_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MSP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()


    class M_ServiceVideoLink(Connection.const.Connect.Base):
        __tablename__='M_ServiceVideoLink'
        MSID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ServiceVideoLink_MSID'),primary_key=True)
        MS_video= sqlalchemy.Column(sqlalchemy.String(400))
        MS_PackageID= sqlalchemy.Column(sqlalchemy.Integer)

        MS_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MS_AddDate = sqlalchemy.Column(
           sqlalchemy.DateTime, default=datetime.datetime.now)
        MS_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MS_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MS_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MS_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MS_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ServicePackageImage(Connection.const.Connect.Base):
        __tablename__='M_ServicePackageImage'
        MSPID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'M_ServicePackageImage_MSPID'),primary_key=True)
        MSP_FilePath= sqlalchemy.Column(sqlalchemy.String(400))
        MSP_FileName= sqlalchemy.Column(sqlalchemy.String(400))
        MSP_PackageID= sqlalchemy.Column(sqlalchemy.Integer)

        MSP_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSP_AddDate = sqlalchemy.Column(
           sqlalchemy.DateTime, default=datetime.datetime.now)
        MSP_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MSP_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MSP_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MSP_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MSP_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Inventory(Connection.const.Connect.Base):
        __tablename__='M_Inventory'
        MIID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'm_inventory_MIID'),primary_key=True)
        MI_InventoryType= sqlalchemy.Column(sqlalchemy.Integer)
        MI_ItemName= sqlalchemy.Column(sqlalchemy.String(100))
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        MI_UnitType= sqlalchemy.Column(sqlalchemy.String(100))
        MI_Price= sqlalchemy.Column(sqlalchemy.String(100))
        MI_Tax= sqlalchemy.Column(sqlalchemy.String(100))
        MI_mrp= sqlalchemy.Column(sqlalchemy.String(100))
        MI_Quantity= sqlalchemy.Column(sqlalchemy.String(100))
        MI_Batch= sqlalchemy.Column(sqlalchemy.String(100))
        MI_Manufacturer= sqlalchemy.Column(sqlalchemy.String(100))
        MI_ExpiryMonth= sqlalchemy.Column(sqlalchemy.String(100))
        MI_ExpiryYear= sqlalchemy.Column(sqlalchemy.String(100))

        MI_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MI_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MI_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MI_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MI_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MI_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MI_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_Broadcast(Connection.const.Connect.Base):
        __tablename__='m_broadcast'
        MBID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'm_broadcast_MBID'),primary_key=True)
        MB_Title= sqlalchemy.Column(sqlalchemy.String(400))
        MB_Message = sqlalchemy.Column(sqlalchemy.String(1000))

        MB_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MB_AddDate = sqlalchemy.Column(
           sqlalchemy.DateTime, default=datetime.datetime.now)
        MB_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MB_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MB_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MB_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MB_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()



    class M_ProductCatalogCateg(Connection.const.Connect.Base):
        __tablename__='m_productcatalogcateg'
        MPCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'm_productcatalogcateg_MPCID'),primary_key=True)
        MPC_FileName= sqlalchemy.Column(sqlalchemy.String(100))
        MPC_FilePath= sqlalchemy.Column(sqlalchemy.String(100))
        MPC_CategoryName= sqlalchemy.Column(sqlalchemy.String(100))
        MPC_Description= sqlalchemy.Column(sqlalchemy.String(100))

        MPC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPC_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MPC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class productCatalog(Connection.const.Connect.Base):
        __tablename__='productcatalog'
        MPCID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'productcatalog_MPCID'),primary_key=True)
        MPC_ItemName= sqlalchemy.Column(sqlalchemy.String(100))
        MPC_ItemType= sqlalchemy.Column(sqlalchemy.Integer)
        M_Branch_MBID= sqlalchemy.Column(sqlalchemy.Integer)
        MPC_LoyalityPoint= sqlalchemy.Column(sqlalchemy.String(100))
        MPC_Description= sqlalchemy.Column(sqlalchemy.String(100))
        MPC_SuitedFor= sqlalchemy.Column(sqlalchemy.String(100))
        MPC_categories= sqlalchemy.Column(sqlalchemy.String(100))
        MPC_Menufacturer= sqlalchemy.Column(sqlalchemy.String(100))
        MPC_FileName= sqlalchemy.Column(sqlalchemy.String(100))
        MPC_FilePath= sqlalchemy.Column(sqlalchemy.String(100))
        MPC_Recommendation= sqlalchemy.Column(sqlalchemy.String(100))
        MPC_Ingredients= sqlalchemy.Column(sqlalchemy.String(100))

        MPC_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPC_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MPC_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MPC_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MPC_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MPC_IsActive = sqlalchemy.Column(
         sqlalchemy.Boolean, unique=False, default=1)
        MPC_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()

    class M_ReferredByDoctor(Connection.const.Connect.Base):
        __tablename__='m_referredbydoctor'
        MRDID=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.Sequence(
            'm_referredbydoctor_MRDID'),primary_key=True)
        MRD_FirstName = sqlalchemy.Column(sqlalchemy.String(250))
        MRD_LastName= sqlalchemy.Column(sqlalchemy.String(250))
        MRD_MobileNo= sqlalchemy.Column(sqlalchemy.String(20))
        MRD_EmailId= sqlalchemy.Column(sqlalchemy.String(250))
        
        MRD_Status= sqlalchemy.Column(sqlalchemy.Boolean, unique=False, default=1)
        MRD_AddUser = sqlalchemy.Column(sqlalchemy.Integer)
        MRD_AddDate = sqlalchemy.Column(
            sqlalchemy.DateTime, default=datetime.datetime.now)
        MRD_AddIP = sqlalchemy.Column(sqlalchemy.String(100))
        MRD_ModUser = sqlalchemy.Column(sqlalchemy.Integer)
        MRD_ModDate = sqlalchemy.Column(sqlalchemy.DateTime)
        MRD_IsActive = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=1)
        MRD_IsDeleted = sqlalchemy.Column(
            sqlalchemy.Boolean, unique=False, default=0)

    Connection.const.createTable()