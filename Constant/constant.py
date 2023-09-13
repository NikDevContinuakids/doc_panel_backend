class constant:
    rules = ['MCR_ID', 'MCR_Value', 'MCR_Type']

    jsonData = ['jsonData']

    OrgDtl = ['MOID', 'MO_Name']

    OrgDtls =['MOID', 'MO_Name','MO_Email']

    GetCountry = ['TDID', 'TD_Name']

    GetState = ['TDID', 'TD_Name']

    GetCity = ['TDID', 'TD_Name']

    GetGender = ['TDID', 'TD_Name']

    getPeriod = ['TDID', 'TD_Name']

    OrgAllDtl = ['ID','Name','Email','Mobile','About']

    getClinicAllDtls=['Organisation','Name','Email','Mobile','City','State','Country','PinCode','Address','OpenTime','CloseTime']

    AddReportform= ['type','name','formControlName','label','align','value']

    AddCollectionForm= ['type','name','formControlName','label','align','value']

    getClinic=['MBID','MB_Name']

    getAllMenu=['ID','state','name','type','icon']

    getAllControl=['ID','name','type']

    FloorAllDtls=['ID','Name','Alias']

    RoomAllDtls=['ID','Organisation','Clinic','Floor','Room Name','Room Number']

    getProcedure = ['TDID', 'TD_Name']

    getcorrectMenu = ['ID','state','name','type','icon','level','parent']

    getDoctor = ['ID','Name','Online Consult Fee (INR)','Online Consult Fee (USD $)','Clinic Visit Fee (INR)','Clinic Visit Fee (USD $)','Location','Type']

    getVaccination = ['ID','Patient','Date','Time','Age','Vaccine Type','Total Dose','Consumed dose']

    getbloodgrp = ['TDID', 'TD_Name']

    getPrescriptionDtl = ['visitId','visitType','Procedure','DOB','AppointDate','Name','UHID','DoctorName','Branch']
    
    Prescrip = ['MP_medication','MP_type','MP_route','MP_times','MP_duration','MP_dosage','MP_comments','MP_Prescription']

    getpackagedetailedview = ['ID','Package Name','Service','Total Payable','Start Date','End Date','Usage']
    
    getDepartment = ['TDID', 'TD_Name']

    dueBalanceDetails = ['InvoiceNo','Date','InvoiceTotal','Balance','Description','TotalPayable','AmountPaid','Comments','CardNo','CardType','Name','UHID','Procedure','DOB']
    
    getInvoicePdf = ['InvoiceNo','Date','InvoiceTotal','Balance','Description','TotalPayable','discountPercent',
                     'CGST','SGST','AmountPaid','Name','UHID','DOB','Procedure','Comments','CardNo','CardType']
    
    getAppointment = ['ID','Branch','Patient','Procedure','Date']

    getDetailedViewInvoice = ['InvoiceNo','Date','bankName','Card','CardType','Cash','CGST','SGST','doctorName','Discount','discountPercent',
                              'DiscountReason','Cheque','Comments','DueBalance','InvoiceTotal','invoiceType','lastDigits',
                              'Online','Prepaid','TotalPayable','Upi','AmountPaid','ServiceId','SettleInvoice','MainInvoiceNo',
                              'TotalAmount','PaidByPartner','PaidByPatient','TotalSessions','UsedSession','PaymentMode','InvoiceType',
                              'MedicineDetails','PartnerOrgId','ServiceName','AppointmentId','M_Branch_MBID','M_Patient_MPID',
                              'UHID','Name','DOB','PartnerOrgName','MPP_PackageId','MPP_PackagePrice','MPP_PackageName','Branch']
    
    
    getDetailedCreditReceipt = ['ReceiptNo','Date','PaymentMode','Amount','BankName','CardType','CardNumber','CreditType','Comment','Name','UHID','DOB','Branch']

    PartnerinvoiceDetails = ['InvoiceNo','Date','InvoiceTotal','Balance','Description','TotalPayable','discountPercent',
                     'CGST','SGST','AmountPaid','Name','UHID','DOB','Procedure','Comments','CardNo','CardType','PaidByPartner','PaidByPatient']
    
    CreateInvoiceFromPackage= ['MAID','M_Patient_MPID','MSP_PackageName','MPPID','MP_Procedure','MSP_Fee','MSP_Duration','MS_CategoryName','MPP_TotalSessions','MPP_UsedSessions','MPP_AvailSessions']

    getDetailedPackageReceipt = ['ReceiptNo','Date','PaymentMode','InvoiceTotal','ServiceName','TotalSessions','UsedSession','PackageName','Name','UHID','DOB','Branch']

    patientSessionNotes = ['Started','AppointmentId','todayfeel','dotoday','Notes','Date']
    
    patientProvisionalDiagnosis = ['ProvisionalDiagnosis','AppointmentId','ICDCode','ICDDescription','Date']
    
    getpackageAlldetailedview = ['ServiceName','sessionNo','AppointmentNo','DoctorName','ConsultTime','PackageId']
    
    CreateInvoiceForPartnerOrg= ['MAID','M_Patient_MPID','MP_Procedure','MS_CategoryName']
    
    checkPartnerOrg = ['OrgName','MPPID','MPP_OrgId']

    getPartnerOrg = ['ID','Name','Address','Email','Mobile','Amount']

    getPatientCreditnew = ['ID','Description','Total Amount','Type','Date','Receipt No']

    dueBalanceInvoice = ['Invoice','Amount','Service','InvDate']

    EditPartnerOrgForm = ['type','name','formControlName','label','align','value','className','controlType','multiline']

    getPatientPartnerOrg = ['Id','Patient Name','Partner Organisation','Add Date']

    getAppointments=['ID','Branch','Procedure','UHID','Patient','Date','Mobile','Time','Duration','Age','Status','PID','Invoiceno']
    
    getAppointmentss=['ID','Organisation','Branch','Room','Patient','Procedure','Date','Mobile','Time','Duration','Age','Status']

    getPatient=['ID','UHID','Name','Email','Mobile','Address','Referred By']

    getPatientDtl=['ID','UHID','Name','Email','Mobile','Address','Referred By']

    getVaccineType = ['ID', 'Vaccine_Name']

    getMenuItems= ['ID','state','name','type','icon','level','parent', 'children']

    getDynamicForm = ['type','name','formControlName','label','align','value','required','multiline']

    Designation= ['key', 'label']

    GetCityid=['key', 'label']

    GetCountryid=['key', 'label']
    
    getServiceDtls=['key', 'label']
    
    getServiceDtlss=['key', 'label']

    GetStateid=['key', 'label']

    getRoomForms = ['type','name','formControlName','label','align','value','className']
    
    getRoomForm = ['type','name','formControlName','label','align','value','className']

    getClinics = ['key', 'label']

    getReportType = ['key', 'label']
    
    getServiceDtl = ['key', 'label']
    
    getOrg = ['key', 'label']

    getFloor = ['key', 'label']

    getAddOrgForm = ['type','name','formControlName','label','align','value','className','controlType','multiline']

    getSearchOrgForm = ['type','name','formControlName','label','align','value']

    getSearchClinicForm = ['type','name','formControlName','label','align','value']

    getCliniclist = ['key', 'label']

    getOrglist = ['key', 'label']
    
    packageInvDetails = ['PackageNo','Date','PackageTotal','Balance','Description','TotalPayable','discountPercent','Tax','cgst','sgst','AmountPaid','Name','UHID','Procedure','DOB','Sessions','PackagePrice','CardType','Comments','Card']
    
    adminReport = ['doctorId', 'patientName', 'appointmentId',
                    'patientId', 'patientProcedure', 'appointmentDate', 'appointmentTime',
                      'patientDuration', 'patientAppointmentType', 'doctorDetailsId', 'organisationId',
                      'branchId', 'roomId', 'patientStatus', 'patientNotes', 'Duration']

    getAddClinicForm = ['type','name','formControlName','label','align','value','className','controlType','multiline']

    getSearchAdminReport = ['type','name','formControlName','label','align','value','className']
    
    getReportType = ['key', 'label']
    
    getReportBranch = ['key', 'label']
    
    getTiming = ['type','name','formControlName','label','align','value','className','controlType','multiline','style']

    getAddress = ['type','name','formControlName','label','align','value','className','controlType','multiline']

    AddPatientForm = ['type','name','formControlName','label','align','value']

    getProcedures = ['key', 'label']

    nameValidation = ['name','pattern','message']

    Validation = ['name','pattern','message']

    mobileValidation = ['name','pattern','message']

    emailValidation = ['name','pattern','message']

    numberValidation = ['name','pattern','message']

    GetGenders= ['key', 'label']

    getIdentityType = ['key', 'label']

    getRelation = ['key', 'label']

    EditPatientForm =['type','name','formControlName','label','align','value']

    searchPatientForm = ['type','name','formControlName','label','align','value']

    getDoctorProfile=['ID','Name','Phone','Email','Degree','Registration','PracticingSince','Languages','MedicalExpertise','AwardRecognitions','speciality','OutDate','HospitalAffiliation','MemberId','ProfilePic']

    getAppointmentForm = ['type','name','formControlName','label','align','value','filterDate','className']
    
    blankCellAppointment = ['type','name','formControlName','label','align','value','className','filterDate']
    
    getUploadForm = ['type','name','formControlName','label','align','value','filterDate']

    getDoctors = ['key', 'label']

    getRoom = ['key', 'label']
    
    getTherapists = ['Id','Full Name','Mobile','Specialty','Branch']
    
    getStaffs = ['Id','Continua Id','Full Name','Mobile','Designation','Branch']

    getStatus = ['key', 'label']

    getPatients= ['key', 'label']
    
    getPhoneCode = ['key', 'label']
    
    getPatientddllist = ['key', 'label']
    
    getDoctorDdlList = ['key', 'label']
    
    getTherapistDdlList = ['key', 'label']

    getSearchAppointmentForm =['type','name','formControlName','label','align','value']

    getEditAppointmentForm =['type','name','formControlName','label','align','value','filterDate']

    getClinicDtls=['ID','Clinic Name','Organisation','Mobile','Address','Open Time','Close Time']

    getClinicPracticeDtls=['ID','Doctor Name','Address','Mobile 1','Mobile 2']

    getinvoiceDetails =  ['Invoice','Visit Date','Invoice Date','Invoice No','Service Name','Description','AMT','AMT Paid','Due','Balance','AddDate']

    showParticularPatientDueInvoice =  ['Invoice','Date','Invoice No','Description','AMT','Balance']

    getPayType= ['key', 'label']

    getCredit= ['key', 'label']

    getCardType= ['key', 'label']

    getCardType2= ['key', 'label']

    getService= ['key', 'label']

    getInventory= ['key', 'label']

    getServiceforDDL= ['key', 'label']

    getUploadedFile = ['ID','Path','Patient Name','File Name','Add Date','DocName']


    getPatientCredit = ['ID','Service','Date','Total Amount']

    searchCreditForm = ['type','name','formControlName','label','align','value','className']

    getCreditEditForm=  ['type','name','formControlName','label','align','value']

    getConcentForm=  ['type','name','formControlName','label','align','value']

    getUploadedConsentForm = ['ID','Path','Patient Name','File Name','Add Date']

    getPackagetype = ['key', 'label']

    getDiscountType = ['key', 'label']

    EditPackageForm= ['type','name','formControlName','label','align','value']

    AddPackageForm= ['type','name','formControlName','label','align','value']

    getPaymentMode= ['key', 'label']

    searchPackageForm= ['type','name','formControlName','label','align','value']

    getPackage= ['key', 'label']
    
    getReferredDoctor = ['Id', 'Name','Mobile','Email']

    AddDoctorForm= ['type','name','formControlName','label','align','value']
    
    AddReferredDoctorForm= ['type','name','formControlName','label','align','value']

    nameform= ['type','name','formControlName','label','align','value','className','multiline']
    
    AddReferredDoctorFormRow= ['type','name','formControlName','label','align','value','className','multiline']

    AddDoctorPracticeForm= ['type','name','formControlName','label','align','value','className']

    getDoctorDtls= ['ID','Full Name','Online Fee (INR)','Online Fee (USD)','Visit Fee (INR)','Visit Fee (USD)','Clinic']

    getHistoryPage= ['type','name','formControlName','label','align','value','className','path']

    getVisitReasonForm= ['type','name','formControlName','label','align','value','className','path']

    getPastHistoryForm= ['type','name','formControlName','label','align','value','className','path']

    getPrenatalHistoryForm= ['type','name','formControlName','label','align','value','className','path']

    getPatientBirthHistoryForm= ['type','name','formControlName','label','align','value','className','path']

    yesno= ['key', 'label']

    Delivery= ['key', 'label']

    DeliveryLocation= ['key', 'label']

    Pregnancies= ['key', 'label']

    ChildBirth= ['key', 'label']

    BirthCry= ['key', 'label']

    getDevelopmentalHistoryForm= ['type','name','formControlName','label','align','value','className','path']

    getSpeechDevelopmentHistoryForm= ['type','name','formControlName','label','align','value','className','path']

    getsocialhistoryForm= ['type','name','formControlName','label','align','value','className','path']

    getmedicalhistoryForm= ['type','name','formControlName','label','align','value','className','path']

    geteducationhistoryForm= ['type','name','formControlName','label','align','value','className','path']

    getstutteringhistoryForm= ['type','name','formControlName','label','align','value','className','path']

    getfamilyhistoryForm= ['type','name','formControlName','label','align','value','className','path']

    AddStrutteringForm= ['type','name','formControlName','label','align','value','className','path']

    education= ['key', 'label']

    familyType= ['key', 'label']

    AddDoctorPracticeMobileForm = ['type','name','formControlName','label','align','value','className','multiline']

    AddDoctorPracticeAddressForm= ['type','name','formControlName','label','align','value','className','multiline']

    AddDoctorPracticeSlotTime= ['type','Day','Slot']

    togglebutton= ['type','name','formControlName','label','align','className','value']

    togglebutton2= ['type','name','formControlName','label','align','className','value']

    AddPatientForm2= ['type','name','formControlName','label','align','value']

    checked= ['name']

    AddPatientFormAfterCheck = ['type','name','formControlName','label','align','value']

    getEditOrgForm= ['type','name','formControlName','label','align','value','className','controlType','multiline']

    getSearchedClinic=['ID','Clinic Name','Organisation','Mobile','Address','Open Time','Close Time']

    getExaminationPage = ['type','name','formControlName','label','align','value','className','path']

    getAssessmentForm= ['type','name','formControlName','label','align','value','className','path']

    getGeneralExamForm = ['type','name','formControlName','label','align','value','className']

    AddVitalsExamForm= ['type','name','formControlName','label','align','value','className']

    AddSystemicExamForm= ['type','name','formControlName','label','align','value','className']

    AddPragmaticSkillsForm= ['type','name','formControlName','label','align','value','className']

    AddSTArticulationSpeechIntelligibilityForm= ['type','name','formControlName','label','align','value','className']

    AddSTArticulationVoice= ['type','name','formControlName','label','align','value','className']

    Loudness= ['key', 'label']

    EditDoctorForm= ['type','name','formControlName','label','align','value','className','multiline']

    getEditDoctor = ['ID','FirstName','LastName','Name','OnlineConsultINR','OnlineConsultUSD','ClinicVisitINR','ClinicVisitUSD']

    SearchDoctorForm= ['type','name','formControlName','label','align','value']

    getSearchedDoctor = ['ID','Name','Online Consult Fee (INR)','Online Consult Fee (USD $)','Clinic Visit Fee (INR)','Clinic Visit Fee (USD $)']

    CognitivePrerequitesform= ['type','name','formControlName','label','align','value','className']

    STVerbalCommunicationForm= ['type','name','formControlName','label','align','value','className']

    OTHandFunctionsform= ['type','name','formControlName','label','align','value','className']

    STNonVerbalCommunicationForm= ['type','name','formControlName','label','align','value','className']

    OTNonEquilibriumCoordinationForm= ['type','name','formControlName','label','align','value','className']

    OTEquilibriumCoOrdinationForm= ['type','name','formControlName','label','align','value','className']

    OTCognitionAndPerceptionSkillsForm= ['type','name','formControlName','label','align','value','className']

    OTSensoryExamForm= ['type','name','formControlName','label','align','value','className']

    OTSensoryProfileForm= ['type','name','formControlName','label','align','value','className']

    getAddtionalinfoForm= ['type','name','formControlName','label','align','value','className']

    PTFunctionalAbilitiesform= ['type','name','formControlName','label','align','value','className']

    PTFunctionalLimitationsform= ['type','name','formControlName','label','align','value','className']

    PTPosturalSystemAlignmentForm= ['type','name','formControlName','label','align','value','className']

    PTPosturalSystemBOSForm= ['type','name','formControlName','label','align','value','className']

    PTPosturalSystemCOMForm= ['type','name','formControlName','label','align','value','className']

    PTAnticipatoryControlFrom= ['type','name','formControlName','label','align','value','className']

    PTPosturalCounterbalance= ['type','name','formControlName','label','align','value','className']

    PTPosturalImpairments= ['type','name','formControlName','label','align','value','className']

    PTMovementSystem= ['type','name','formControlName','label','align','value','className']

    PTMovementStrategies= ['type','name','formControlName','label','align','value','className']

    PTRangeSpeedofMovement= ['type','name','formControlName','label','align','value','className']

    PTStabilityMobility= ['type','name','formControlName','label','align','value','className']

    PTMovementSystemImpairment= ['type','name','formControlName','label','align','value','className']

    PTRegulatorySystemForm= ['type','name','formControlName','label','align','value','className']

    PTNeurometerSystemForm= ['type','name','formControlName','label','align','value','className']

    PTMusculoskeletalSystem= ['type','name','formControlName','label','align','value','className']

    PTSensorySystem= ['type','name','formControlName','label','align','value','className']

    PTCognitiveSystem= ['type','name','formControlName','label','align','value','className']

    NICHQVanderbiltADHDParentForm= ['type','name','formControlName','label','align','value','className']

    SequinFormBoardTest= ['type','name','formControlName','label','align','value','className']

    ChildhoodAutismRatingScale= ['type','name','formControlName','label','align','value','className']

    VinelandSocialMaturityScale= ['type','name','formControlName','label','align','value','className']

    GeselsDrawingTestofintelligence= ['type','name','formControlName','label','align','value','className']

    MalinIntelligenceScaleforIndianChildren= ['type','name','formControlName','label','align','value','className']

    DevelopmentalProfile= ['type','name','formControlName','label','align','value','className']

    ChildBehaviorChecklist= ['type','name','formControlName','label','align','value','className']

    ConnersParentRatingScale= ['type','name','formControlName','label','align','value','className']

    RavenStandardProgressiveMatrices= ['type','name','formControlName','label','align','value','className']

    ReceptiveLanguageAssessment= ['type','name','formControlName','label','align','value','className']

    ExpressiveLanguageAssessment= ['type','name','formControlName','label','align','value','className']

    StutteringAssessment= ['type','name','formControlName','label','align','value','className']

    SpecialEdassessmenttwoyears= ['type','name','formControlName','label','align','value','className']

    SpecialEdassessmentthreeyears= ['type','name','formControlName','label','align','value','className']

    SpecialEdassessmentthreefouryears= ['type','name','formControlName','label','align','value','className']

    SpecialEdassessmentfouryears= ['type','name','formControlName','label','align','value','className']

    SpecialEdassessmentsevenyears= ['type','name','formControlName','label','align','value','className']

    achievement= ['key', 'label']

    review= ['key', 'label']

    consistancy= ['key', 'label']

    Aroused= ['key', 'label']

    Attendance= ['key', 'label']

    verbalComm= ['key', 'label']

    Cognitive= ['key', 'label']

    Loudness= ['key', 'label']

    Quality= ['key', 'label']

    Observation= ['key', 'label']

    Articulation= ['key', 'label']

    STOroperipheralExamForm= ['type','name','formControlName','label','align','value','className']

    AddtionalinfoForm= ['type','name','formControlName','label','align','value','className']

    LipsMovements= ['key', 'label']

    TongueMovements= ['key', 'label']

    TeethAppearance= ['key', 'label']

    TeethMovements= ['key', 'label']

    HardPalateAppearance= ['key', 'label']

    SoftPalateAppearance= ['key', 'label']

    SoftPalateMovements= ['key', 'label']

    UvulaAppearance= ['key', 'label']

    UvulaMovements= ['key', 'label']

    MandibleAppearance= ['key', 'label']

    MandibleMovements= ['key', 'label']

    Drooling= ['key', 'label']

    TongueAppearance= ['key', 'label']

    Expression= ['key', 'label']

    Comprehension= ['key', 'label']

    ShoulderScapular= ['key', 'label']

    ShoulderandScapular= ['key', 'label']

    ShouldernScapular= ['key', 'label']

    RibcageandChest= ['key', 'label']

    Trunk= ['key', 'label']

    Trunks= ['key', 'label']

    PelvicComplexRight= ['key', 'label']

    PelvicComplexLeft= ['key', 'label']

    HipjointRotation= ['key', 'label']

    BaseofSupport= ['key', 'label']

    CenterofMass= ['key', 'label']

    Strategiesposture= ['key', 'label']

    MuscleArchitecture= ['key', 'label']

    Howdoesthe= ['key', 'label']

    Childgenerallyperformsactivitie= ['key', 'label']

    Rangespeedmovement= ['key', 'label']

    StabilityMobility= ['key', 'label']

    Initiation= ['key', 'label']

    Sustenance= ['key', 'label']

    Termination= ['key', 'label']

    ContractionConcentric= ['key', 'label']

    ContractionIsometric= ['key', 'label']

    ContractionEccentric= ['key', 'label']

    RightLeft= ['key', 'label']

    PoorGood= ['key', 'label']

    Skeletalcomments= ['key', 'label']

    Oromotorsystem= ['key', 'label']

    modulationissues= ['key', 'label']

    Visualsystem= ['key', 'label']

    Postivenegative= ['key', 'label']

    Couldnotresist= ['key', 'label']

    AddCKASAssessment= ['type','name','formControlName','label','align','value','className']

    AddHRDSAssessment= ['type','name','formControlName','label','align','value','className']

    AddHARSAssessment= ['type','name','formControlName','label','align','value','className']

    AddPHQAssessment = ['type','name','formControlName','label','align','value','className']

    HARS= ['key', 'label']

    PHQ= ['key', 'label']

    HRDSDepressedMood = ['type','name','formControlName','label','align','value','className']

    HRDSFeelingGuilt = ['key', 'label'] #['type','name','formControlName','label','align','value','className']

    HRDSSucide = ['key', 'label']  #= ['type','name','formControlName','label','align','value','className']

    HRDSInsomnia = ['type','name','formControlName','label','align','value','className']

    HRDSMidNight = ['type','name','formControlName','label','align','value','className']

    HRDSEarlyMorning = ['type','name','formControlName','label','align','value','className']

    HRDSWork = ['type','name','formControlName','label','align','value','className']

    HRDSRetardation = ['type','name','formControlName','label','align','value','className']

    HRDSAgitation = ['type','name','formControlName','label','align','value','className']

    HRDSPsychic = ['type','name','formControlName','label','align','value','className']

    HRDSAnxietySomatic = ['type','name','formControlName','label','align','value','className']

    HRDSSomatic = ['type','name','formControlName','label','align','value','className']

    HDRSGeneralSomatic = ['type','name','formControlName','label','align','value','className']

    HDRSLossOfLibido = ['type','name','formControlName','label','align','value','className']

    HDRSHypochondriasis = ['type','name','formControlName','label','align','value','className']

    HDRSLossofWeight = ['type','name','formControlName','label','align','value','className']

    SessionNoteForm  = ['type','name','formControlName','label','align','value','className','path']


    Started = ['key', 'label']

    todayfeeling = ['key', 'label']

    dotoday = ['key', 'label']

    AddSessionNotes = ['type','name','formControlName','label','align','value','className','multiline']

    AddPatientFilesform= ['type','name','formControlName','label','align','value','className','path']

    AddProvisionalDiagnosis = ['type','name','formControlName','label','align','value','className','path']

    AddPatientreviewForm = ['type','name','formControlName','label','align','value','className','path']

    FollowAfter = ['key', 'label']
    
    getRefferDoctor = ['key', 'label']
    
    getRefferDoctors = ['key', 'label']

    AddServicesbox = ['type','name','formControlName','label','align','value','className','path']

    AddServicesboxForm = ['type','name','formControlName','label','align','value','className']

    ServiceStatus= ['key', 'label']

    AddPrescriptionBox = ['type','name','formControlName','label','align','value','className','path']

    AddInstructions = ['type','name','formControlName','label','align','value','className','path']

    AddAllAppointmentScene= ['type','name','formControlName','label','align','value']

    getDoctorsname= ['key', 'label']

    HRDSDepressedMoods= ['key', 'label']

    AddNewCouponForm= ['type','name','formControlName','label','align','value','className']

    Coupons= ['key', 'label']

    getDoctorList= ['key', 'label']

    AddPatrnerOrganisationlist= ['key', 'label']

    AddPartnerOrganisation= ['type','name','formControlName','label','align','value','className']

    AddInspectionsForm= ['type','name','formControlName','label','align','value','className']

    SearchAllAppointment= ['type','name','formControlName','label','align','value','className']

    getBranch= ['key', 'label']


    AddAdminPage= ['type','name','formControlName','label','align','value','className','path']

    AddTherapistRow= ['type','name','formControlName','label','align','value','className']

    AddTherapistForm= ['type','name','formControlName','label','align','value','className']

    AddNewCouponRow= ['type','name','formControlName','label','align','value','className']

    Status= ['key', 'label']

    Title= ['key', 'label']

    AddStaffForm= ['type','name','formControlName','label','align','value','className']

    AddStaffRow= ['type','name','formControlName','label','align','value','className']

    Code= ['key', 'label']

    AddDoctorMenu= ['type','label','target','MenuID','path']

    AddExpenseRegisterRow= ['type','name','formControlName','label','align','value','className']
    AddExpenseRegisterForm= ['type','name','formControlName','label','align','value','className']

    ExpenseStatus= ['key', 'label']

    AddDoctorPatientProfileForm= ['type','name','formControlName','label','align','value','className','controlType','multiline','filterDate']

    AddDoctorPatientProfileRow= ['type','name','formControlName','label','align','value','className','controlType','multiline']

    Gender= ['key', 'label']

    BloodGroup= ['key', 'label']

    getDuration = ['key', 'label']

    getPatientAllHistory= ['patientId','patientName','reasonForVisit','status','consultId','doctorName','doctorId','visitTimeFrom','visitTimeTo','date','mode']

    getPatientAll= ['patientId','Name','UHID','DOB']
    
    getPatientSearchHistory= ['patientId','patientName','reasonForVisit','status','consultId','doctorName','doctorId','visitTimeFrom','visitTimeTo','date','mode']

    pastConsultData= ['patientId','patientName','reasonForVisit','status','consultId','doctorName','doctorId','visitTimeFrom','visitTimeTo','date','mode']

    Pages=['S. No','Page','Menu','PageId']

    AddNewUserRow =['type','name','formControlName','label','align','value','className']

    # AddDoctorForm = ['type','name','formControlName','label','align','value','className']

    getUsers= ['Id','Name','Email','Mobile','Username','Status']

    getUserss= ['Id','Name','Email','Mobile','Username','Type','Status']

    UserType= ['key', 'label']

    SearchAllUser = ['type','name','formControlName','label','align','value','className']

    AddServiceCategoryRow = ['type','name','formControlName','label','align','value','className']

    AddServiceCategoryForm = ['type','name','formControlName','label','align','value','className']

    AddServiceCategoryForms = ['type','name','formControlName','label','align','value','className']

    getServiceCategory = ['Id','Name','Description','Active']
    
    ServiceNames = ['key', 'label']
    
    ServiceNamess = ['key', 'label']
    
    CreateInvoiceFromApp= ['MAID','M_Patient_MPID','MP_Procedure','MSP_Fee','MSP_Duration','MS_CategoryName','Prepaid']

    showParticularPatientAppointment = ['ID','Service','Consult Id','Doctor','Status','Total','Invoice No','Date','Time']

    AddPostTreatmentForm = ['type','name','formControlName','label','align','value','className']

    AddPreTreatmentFormRow = ['type','name','formControlName','label','align','value','className']

    AddNewUserForm = ['type','name','formControlName','label','align','value','className']

    AddNewUserForms = ['type','name','formControlName','label','align','value','className']

    AddServicesFormRow = ['type','name','formControlName','label','align','value','className']

    AddServicesFormRow1 = ['type','name','formControlName','label','align','value','className']

    AddServicesFormRow2 = ['type','name','formControlName','label','align','value','className']

    AddServicesFormRow3 = ['type','name','formControlName','label','align','value','className']

    AddServicesFormRow4 = ['type','name','formControlName','label','align','value','className']

    AddServicesFormRow5 = ['type','name','formControlName','label','align','value','className']


    CreateRightJSON  = ['name']

    RightsCols  =['type','name','label','required']

    AddUserRightsFormRow = ['type','name','formControlName','label','align','value','className']

    AddUserRightsForm = ['type','name','formControlName','label','align','value','className']

    Users = ['key', 'label']

    getUserRightsForm = ['Page','Right','Assign']

    Policy = ['key', 'label']

    getPolicyDetails = ['PolicyId','Policy','User', 'Branch']

    AddServicePackageRow = ['type','name','formControlName','label','align','value','className']

    AddServicePackageForms1 = ['type','name','formControlName','label','align','value','className']

    AddServicePackageForms2 = ['type','name','formControlName','label','align','value','className']

    AddServicePackageForms3 = ['type','name','formControlName','label','align','value','className']

    AddServicePackageForms4 = ['type','name','formControlName','label','align','value','className']

    serviceStatus = ['key', 'label']

    servicePackageType = ['key', 'label']

    getServicePackage = ['Id', 'name','price','type']

    getServicePackages = ['Id', 'name','price','type','sessions','Validity']

    getServicePackagesss = ['Id', 'name','price','type','sessions','Validity']

    AddPromotionsPageFormRow = ['type','name','formControlName','label','align','value','className']

    AddPromotionsPageForm1 = ['type','name','formControlName','label','align','value','className']

    AddPromotionsPageForm2 = ['type','name','formControlName','label','align','value','className']

    AddPromotionsPageForm3 = ['type','name','formControlName','label','align','value','className']

    AddPromotionsPageForm4 = ['type','name','formControlName','label','align','value','className']

    PromotionType = ['key', 'label']

    AddProductMenu = ['type', 'label','target','MenuID','path']

    getPromotionsDtls = ['Id', 'Name','Type','From','Till']

    AddservicePreTreatmentForm = ['type','name','formControlName','label','align','value','className']

    AddservicePreTreatmentRow = ['type','name','formControlName','label','align','value','className']

    AddservicePostTreatmentRow = ['type','name','formControlName','label','align','value','className']

    AddservicePostTreatmentForm = ['type','name','formControlName','label','align','value','className']

    AddServicePackageVideoLink = ['type','name','formControlName','label','align','value','className','placeholder']

    getServicePro = ['Id','service','Branch','Duration','Total']

    ServiceCatType = ['key', 'label']

    Inventorytype = ['key', 'label']

    Months = ['key', 'label']

    Years = ['key', 'label']

    AddInventoryFormRow = ['type','name','formControlName','label','align','value','className']

    AddInventoryForm = ['type','name','formControlName','label','align','value','className']

    AddInventoryForm1 = ['type','name','formControlName','label','align','value','className']

    AddInventoryForm2 = ['type','name','formControlName','label','align','value','className']

    getInventoryMedicalDtls = ['Id','Medecine Name','Unit Type','Quantity','Manufacturer']

    getInventoryConsumableDtls = ['Id','Consumable Name','Unit Type','Quantity','Manufacturer']

    getInventoryEquipmentDtls = ['Id','Equipment Name','Unit Type','Quantity','Manufacturer']

    AddQntyFormRow = ['type','name','formControlName','label','align','value','className']

    AddQntyForm = ['type','name','formControlName','label','align','value','className']

    AddQntyForm1 = ['type','name','formControlName','label','align','value','className']

    dedutQntyFormRow = ['type','name','formControlName','label','align','value','className']

    DeductQntyForm = ['type','name','formControlName','label','align','value','className']

    getCRMMenu = ['type','label','target','MenuID','path']

    AddBrodcastForm = ['type','name','formControlName','label','align','value','className','controlType','multiline']

    CRMDashboard = ['type','name','formControlName','label','align','value','className','path','linkTitle']

    getBroadcastdtls = ['Id','Title','Message','Active']

    getBroadcastNotify = ['Id','Title','Message','Time']

    AddProductcatalogCategoryRow = ['type','name','formControlName','label','align','value','className']

    AddProductcatalogCategory = ['type','name','formControlName','label','align','value','className']

    AddProductcatalogCategory1 = ['type','name','formControlName','label','align','value','className']

    getproductCatalogCategory = ['Id','Name','Description','Active']

    getproductCatalogPro = ['Id','Item Name','Item Type','Suited For','Category']

    AddProductCatalogRow = ['type','name','formControlName','label','align','value','className']

    AddProductCatalogRow1 = ['type','name','formControlName','label','align','value','className']

    AddProductCatalogRow2 = ['type','name','formControlName','label','align','value','className']

    AddProductCatalogRow3 = ['type','name','formControlName','label','align','value','className']

    AddProductCatalogRow4 = ['type','name','formControlName','label','align','value','className']

    ProductCatalogType = ['key', 'label']

    CatelogItemtype = ['key', 'label']

    getServices = ['ID','Service Name','Quantity','Total Cost']

    getSessionProgress = ['Id','Started','TodayFeeling','dotoday','notes','Date']

    AddPrescriptionForm= ['type','name','formControlName','label','align','value']

    MedecineType = ['key', 'label']

    RoutesType = ['key', 'label']

    timesADayType = ['key', 'label']

    DurationType = ['key', 'label']

    AddCheckInForm= ['type','name','formControlName','label','align','className','value']

    AddCheckInFormRow= ['type','name','formControlName','label','align','value']

    getClinicRights = ['key', 'label']

    CreateInvoiceFromPackage2 = ['MAID','M_Patient_MPID','MP_Procedure','MS_CategoryName','MSP_Fee','MSP_Duration']

    packageDetail = ['MPP_PackageId','MPPID','MPP_TotalSessions','MPP_UsedSessions','MPP_AvailSessions','MPP_PackageName','MSP_Price']

    editPrescriptionDtl = ['MP_medication','MP_type','MP_route','MP_times','MP_duration','MP_dosage','MP_comments','MP_Prescription']

    AllAppointmentadminReport = ['DATE','TIME','DURATION','PATIENT ID','PATIENT NAME','SERVICE','VISIT TYPE','HCP NAME','PAYMENT MODE','FEES','DISCOUNT','DATE OF RECEIPT','INVOICE NO.','CGST','SGST','TOTAL AMOUNT','STATUS','LOCATION','VISIT ID','PACKAGE NAME','SESSIONS AVAILED','REMOTE SESSION']
    
    CompletedClinicVisit = ['DATE','TIME','DURATION','PATIENT ID','PATIENT NAME','SERVICE','VISIT TYPE','HCP NAME','PAYMENT MODE','FEES','DISCOUNT','DATE OF RECEIPT','INVOICE NO.','CGST','SGST','TOTAL AMOUNT','STATUS','LOCATION','VISIT ID','PACKAGE NAME','SESSIONS AVAILED','REMOTE SESSION']
    
    AllClinicVisit = ['DATE','TIME','DURATION','PATIENT ID','PATIENT NAME','SERVICE','VISIT TYPE','HCP NAME','PAYMENT MODE','FEES','DISCOUNT','DATE OF RECEIPT','INVOICE NO.','CGST','SGST','TOTAL AMOUNT','STATUS','LOCATION','VISIT ID','PACKAGE NAME','SESSIONS AVAILED','REMOTE SESSION']
    
    AllOnlineVisit = ['DATE','TIME','DURATION','PATIENT ID','PATIENT NAME','SERVICE','VISIT TYPE','HCP NAME','PAYMENT MODE','FEES','DISCOUNT','DATE OF RECEIPT','INVOICE NO.','CGST','SGST','TOTAL AMOUNT','STATUS','LOCATION','VISIT ID','PACKAGE NAME','SESSIONS AVAILED','REMOTE SESSION']
    
    # NonGstInvoices = ['LOCATION','DATE','INVOICE NO.','VISIT ID','PATIENT ID','PATIENT NAME','SERVICE NAME','SERVICE FEE','DISCOUNT','DISCOUNT REASON','AMOUNT PAYABLE','AMOUNT PAID','AMOUNT BALANCE','PAYMENT MODE','CO-PAY AMOUNT','CO-PAY ORG NAME','BANK NAME','CARD TYPE','CARD NUMBER','COMMENTS','STATUS','CASH AMOUNT','CARD AMOUNT','UPI AMOUNT','ONLINE AMOUNT','CHEQUE AMOUNT','PREPAID AMOUNT']    
    NonGstInvoices = ['LOCATION','DATE','INVOICE NO.','VISIT ID','PATIENT ID','PATIENT NAME','SERVICE NAME','SERVICE FEE','DISCOUNT','DISCOUNT REASON','AMOUNT PAYABLE','AMOUNT PAID','AMOUNT BALANCE','CO-PAY AMOUNT','CO-PAY ORG NAME','BANK NAME','CARD TYPE','CARD NUMBER','COMMENTS','CASH AMOUNT','CARD AMOUNT','UPI AMOUNT','ONLINE AMOUNT','CHEQUE AMOUNT','PREPAID AMOUNT']

    viewVisitReasonForm = ['ID','Informed By','Present Concerns','Appointment Id']

    viewPastHistoryForm = ['ID','Appointment Id','Past Medications']

    viewPrenatalHistoryForm = ['ID','Appointment Id','Mother Conception','Mother Pregnancy','History Abortions','Gestational Diabetes',
                               'Neurological Disorder', 'Physical Emotional','Inompatibility','Jaundice','Seizures','TraumaInjury',
                               'Bleeding pregnancy','Adequate Nutrition','Infections','Smoking','Observations']

    viewPatientBirthHistoryForm = ['ID','Appointment ID','Mother Health','Delivery Type','Type of Delivery','Delivery Location',
                                   'Multiple Pregnancies','Complication Pregnancy','Child Birth','Child Birth Week','Birth Weight',
                                   'Birth Cry','Neonatal Condition','Special CareAny','Any Medical Events','Congenital','Observations']

    viewDevelopmentalHistoryForm = ['ID','Appointment ID','HoldUp HeadAge','Rollover age','Sit Age','Stand Alone Age','Walk Age','Talk Age',
                                    'Toilet Train Age','Feed Age','Dresshim Age','Observations']
    
    viewSpeechDevelopmentHistoryForm = ['ID','Appointment ID','Vocalization','Babbling','First Word','Phrases','Simple Sentences','Observations']
    
    viewsocialhistoryForm = ['ID','Appointment ID','Social History']
    
    viewmedicalhistoryForm =['ID','Appointment ID','Medical History']

    viewfamilyhistoryForm =['ID','Appointment Id','Family type','Consanguinity','Family History']
    
    vieweducationhistoryForm =['ID','Appointment Id','Education History']

    viewGeneralExamForm =['ID','Appointment Id','Height','Weight','Head Circumference','Observations']

    viewVitalsExamForm =['ID','Appointment Id','Blood Pressure','Pulse Rate','Respiratory Rate','Temperature']

    viewSystemicExamForm =['ID','Appointment ID','Observations']

    viewSTOroperipheralExamForm =['ID','Appointment Id','Lips Appearance','Lips Movements','Tongue Appearance','Tongue Movements','Teeth Appearance','Teeth Movements',
                                  'Hard Palate Appearance','Soft Palate Appearance','Soft Palate Movements','Uvula Appearance','Uvula Movements','Mandible Appearance','Mandible Movements','Drooling','Blowing','Biting','Sucking','Swallowing','Observations']

    viewSTArticulationSpeechIntelligibilityForm =['ID','Appointment Id','Noonecan','memberscan','Strangerscan','Observations']

    viewSTArticulationVoiceForm =['ID','Appointment Id','Pitch','Loudness','Quality','Observations']

    viewCognitivePrerequitesForm =['ID','Appointment Id','Imitation','Objectpermanence','Timeconcept','Colourconcept','Moneyconcept','Sequencing','Matching','Meanendrelationship','Observations']

    viewSTVerbalCommunicationForm =['ID','Appointment Id','Expression','Comprehension','Observations']

    viewSTNonVerbalCommunicationForm =['ID','Appointment Id','Expression','Comprehension','Observations']

    viewOTHandFunctionsForm =['ID','Appointment Id','Hand Dominance','Hand Preference','Reach Forward','Reach Backward','Reach Lateral','Reach Downward','Grasp UlnarPalmar','Grasp Palmar',
                              'Grasp RadialPalmar','Grasp RadialDigital','Grasp InferiorPincer','Reach Upward','Grasp NeatPincer','Grasp Palmarsupinate','Grasp Digitalpronate','Grasp Statictripod','Grasp Dynamictripod','Prehension PadtoPad','Prehension TiptoTip','Prehension PadtoSide']

    viewOTNonEquilibriumCoordinationForm =['ID','Appointment Id','Fingertonose','Fingertotherapistfinger','Fingertofinger','Alternatnosefinger','Fingeropposition','Massgrasp',
                                           'Pronationsupination','Reboundtest','Tappinghand','Tappingfeet','Pointingandpastpointing','Alternateheeltokneeheeltoe','Toetoexaminersfinger','Heeltoshin','Drawingacircle','Fixationorpositionholding']

    viewOTEquilibriumCoordinationForm =['ID','Appointment Id','Standingwithnormalbaseofsupport','Standingwithnarrowbaseofsupport','Standingintandemposition','Standingononefeet','Perturbation','Standinginfunctionalreach','Standinglateralflexionofthetrunktoeachside','Tandemwalking','WalkingInastraightline','Walksidewaysbackwards','Walkinhorizontalvertical','Marchinplace','Startstopabruptly',
                                        'Walkandpivotincommand','Walkincircle','Walkonheelsandtoes','Turnsoncommand','Stepoveraroundobstacles','Stairclimbingwithhandrails','Jumpingjacks','Sittingontherapybal']

    viewOTCognitionAndPerceptionForm =['ID','Appointment Id','Praxis','Rightleftdiscrimination','Fingerindentification','Orientationtoperson','Orientationtoplace',
                                       'Conceputalseriescompletion','Selectiveattention','Focusedattention','Spatialperception','Visualmemory','Verbalmemory','Identificationofobjects','Proverbinterpretation','Randomlettertest','Overlappingfigures']

    viewOTSensoryExamForm =['ID','Appointment Id','Visual tracking','Choreiform movements','Tremor','Exaggerated associated','Graphesthesis','Stereognosis','Weight bearing hands','Prone extension pattern']

    viewOTSensoryProfileForm =['ID','Appointment Id','Observations']

    viewAddtionalinfoForm =['ID','Appointment Id','Observations']

    viewPTFunctionalAbilitiesForm =['ID','Appointment Id','Gross Motor','Fine Motor','Communication Speech','Feeding','Playskills','ADL']

    viewPTFunctionalLimitationsForm =['ID','Appointment Id','Gross Motor','Fine Motor','Communication Speech','Feeding','Playskills','ADL']

    viewPTPosturalSystemAlignmentForm =['ID','Appointment Id','Head Neck','Shoulder Scapular','Shoulder and Scapular','Shouldern Scapular','Ribcage and Chest','Trunk',
                                        'Trunks','Pelvic Complex Right','Pelvic Complex Left','Hipjoint Abduction','Hipjoint Adduction','Hipjoint Rotation','Symmetrical','Assymetrical','Observations']
    
    viewPTPosturalSystemBOSForm =['ID','Appointment Id','Base of Support']

    viewPTPosturalSystemCOMForm =['ID','Appointment Id','Center of Mass','Within support','Strategies posture']

    viewPTAnticipatoryControlForm =['ID','Appointment Id','Canchildanti','Observations']

    viewPTPosturalCounterbalanceForm =['ID','Appointment Id','Observations']

    viewPTPosturalSystemImpairments =['ID','Appointment Id','Muscle Architecture','Anycallosities','Anyother specific posture','Observations']

    viewPTMovementSystemForm =['ID','Appointment Id','Canthey overcome','How do','Strategies used']

    viewPTMovementStrategiesForm =['ID','Appointment Id','Childgenerallyperformsactivitie','CanperformLateralweightshifts','CanperformLateralweightshiftsleft',
                                   'CanperformDiagonalweightRight','CanperformDiagonalweightLeft','CanperformneckthoracicspineRight','CanperformneckthoracicspineLeft','HowarethedissociationsPelvicfemoral','HowaredissociationsInterlimb','HowthedissociationsScapulohumeral','HowthedissociationsUpperLowerbody']
    
    viewPTRangeSpeedofMovementForm =['ID','Appointment Id','Range Speed Movement','at Trunk','Extremities']

    viewPTStabilityMobilityForm =['ID','Appointment Id','Mobility Strategies']

    viewPTMovementSystemImpairmentForm =['ID','Appointment Id','Excessive movement','movement StaticPostures','Integration of PostureMovement','Balance Transitions','Accuracy of Movements','Observations']
    
    viewPTRegulatorySystemForm =['ID','Appointment Id','Affect','Arousal','Attention','Action','Observations']

    viewPTNeurometerSystemForm =['ID','Appointment Id','Initiation','Sustenance','Termination','Control and Gradation','Contraction Concentric',
                             'Contraction Isometric','Contraction Eccentric','Reciprocal Inhibition','Isolated work','Dynamic stiffness','Extraneous Movement','Observations']
    
    viewPTMusculoskeletalSystemForm =['ID','Appointment Id','Muscle Endurance','Skeletal Comments','Tardieu ScaleTR1','Tardieu ScaleTR2','Tardieu ScaleTR3',
                                      'Tardieu ScaleHamsR1','Tardieu ScaleHamsR2','Observations']
    
    viewPTSensorySystemForm =['ID','Appointment Id','Modulation Issues','Visual system','Auditory system','Auditory system Response','Vestibular system','Somatosensory system','Oromotor system','Olfactory system','Observations']
    
    viewPTCognitiveSystemForm =['ID','Appointment Id','Intelligence','Memory','Adaptability','Motor Planning','Observations']
   
    viewNICHQVanderbiltADHDParentForm =['ID','Appointment Id','Score','Interpretation']
    
    viewSequinFormBoardTestForm =['ID','Appointment Id','Mental Age','IQ','Observations']
    
    viewChildhoodAutismRatingScaleForm =['ID','Appointment Id','Relating to People','Imitation','Emotional Response','Body Use','Object Use','Daptation Change','Visual Response','Listening Response','Taste Smell Use','Fear or Nervousness','Verbal','Non Verbal','Activity Level','Consistency Response','General Impression','Concluding Remark']
    
    viewVinelandSocialMaturityScaleForm =['ID','Appointment Id','Social Age','IQ','Observations']
    
    viewGeselsDrawingTestofintelligenceForm =['ID','Appointment Id','Mental Age','IQ','Observations']
    
    viewMalinIntelligenceScaleforIndianChildrenForm =['ID','Appointment Id','Verbal Quotient','Performance Quotient','Observations']
    
    viewDevelopmentalProfileForm =['ID','Appointment Id','Physical Score','Physical Category','Physical Age Equivalent','Adaptive Behavior Score','Adaptive Behavior Category','Adaptive Behavior Age Equivalent','Social Score','Social Category','Social Equivalent','Cognitive Score','Cognitive Category','Cognitive Age Equivalent','Comm Standard Score','Comm Category','Comm Age Equivalent','General Dev Score','General Dev Category','General Age Equivalent']
    
    # viewChildBehaviorChecklistForm =['ID','Appointment Id','Scores','Tscores','Range','Observations']
    
    viewConnersParentRatingScaleForm =['ID','Appointment Id','Scores','Tscores','Range','Observations']
    
    viewRavenStandardProgressiveMatricesForm =['ID','Appointment Id','Raw Score','Percentile','Grade','Interpretation','Corresponds To']
    
    viewReceptiveLanguageAssessmentForm =['ID','Appointment Id','Comprehends sounds','Comprehends loud','Comprehends categorizesounds','Comprehends animalsounds',
                                          'Comprehends fruitsname','Comprehends colorsname','Comprehends animalname','Comprehends vegetablename','Comprehends shapesname',
                                          'Comprehends bodyparts','Comprehends vehiclenames','Understandingrhymes','Respondscorrectly','Identifiessounds','Actsoutcommands','Comprehends stepscommands','Understandinggreeting','Understanding']
    
    viewExpressiveLanguageAssessmentForm =['ID','Appointment Id','Imitates environmental sounds','Imitates loud and softsounds','Imitates lexical categories','Imitates colors name','Imitates body parts','Imitates singing and phrases',
                                           'Imitates alphabets AtoZ','articles','Watches','Imitates counting','Claps','Respondstosinglesigns','Imitates socialgreetings','Occassionallytrytoimitate','Imitates commonsyllables']
    
    viewStutteringAssessmentForm =['ID','Appointment Id','Behavioural assessment','Cognitive assessment','Impact educational participation',
                                   'Likely to Achieve','Prognosis Effect']
    
    viewSpecialEdassessmenttwoyearsFForm =['ID','Appointment Id','Respondstoname','Makeseyecontact','Respondstolightandsoundtoys','canmoveeyesupanddown','canmoveeyesleftandright','repeatswords',
                                           'knowsidentificationofnumber','canrollpoundandsqueezeclay','vocabularyMom','vocabularyDad','Vocabularydog','vocabularycat','vocabularytree','vocabularytable','vocabularychair','vocabularycow',
                                           'vocabularycrayons','vocabularybus','vocabularycar','vocabularybook','vocabularyapple','vocabularybanana','vocabularybottle','Candostacking','canmaketower','respondstobubbles','Identifieshappyandsad',
                                           'Knowsshapes','knowscolors','knowsanimals','knowsvehicles','knowsbodyparts','knowsidentificationofalphabets','knowsmoreorless','knowsbigandsmall','knowsnearandfar','canidentifhisorher','canidentifybag','canidentifyshoes','canidentifybottle']
    viewSpecialEdassessmentthreeyearsForm =['ID','Appointment Id','respondstoname','makeseyecontact','cansitformins','canmoveeyesupanddown','canmoveeyesleftandright','cananswerfullname','vocabularybodyparts','canfollowstepsinstruction','cananswerold','cananswerwhatsyourmothersname','cananswerwhichisyoufavoritecolour',
                                            'canfixpiecepuzzle','vocabularyshapescircle','vocabularycolors','vocabularywild','Vocabularyfruits','canfollowstepinstruction','cansingrhymes','cangiveanswerseeinsky','cangiveanswerswiminwater','cangiveanswerseeontree','knowsidentificationofalphabets','knowsidentificationofnumbers','Canholdapencilcrayon'
                                            ,'canscribble','cancoloringivenshape','cantearandpaste','canidentifyemotionshappy','canidentifyemotionssad','canidentifyemotionsangry','canidentifyemotionsupset']
    
    viewSpecialEdassessmentthreefouryearsForm =['ID','Appointment Id','doesrespondtonamecall','doesmakeseyecontact','initiatesinteractiontoward','cansitformins','understandinstructionslikestand','getthatputthere',
                                                'givemegetthis','runwalkjump','lookdownup','cananswerwhatis','cananswerfavoritecolour','canfixpiecepuzzle','vocabularyshapes','vocabularycolors','vocabularywild','vocabularyfruits','vocabularybodyparts',
                                                'Canunderstandpositions','cansingrhymes','canunderstandstories','canWhatquestions','canidentifybasicobjects','canholdacrayonpencil','canmaketower','canimitate','canplaydoughballs','canheshethrow','canrecognisealphabet','Canrecognisenumerals','cancolourgivenshape']
    
    viewSpecialEdassessmentfouryearsForm =['ID','Appointment Id','respondnamecall','makeseyecontact','interactiontowardothers','cansitformins','cananswerwhatname','answerfavoritecolour','canfixpiecepuzzle','vocabularyshapes','vocabularycolors',
                                           'vocabularywild','vocabularybody','Vocabularyfruits','canunderstandpositions','cansingrhymes','canunderstandstories','replyWhatquestions','identifybasicobjects','holdcrayonpencil','canimitate','doughmakeballs','canthrow','recognisealphabets','recognisenumerals','cancolourshape']
    
    viewSpecialEdassessmentsevenyearsForm =['ID','Appointment Id','putneedsminimalassistance','eathandsonly','fixasandwich','givefirstlastname','cangiveaddress','awareofemotions','canzipper',
                                            'independentlyassistanct','asksmeaningfulquestions','tellsstorieswords','Doestellage','canobeysimplecommands','readsimplewords','writesimplewords',
                                            'namethingsaround','alternatesfeetupdownstairs','pedaltricycle','catchandthrowball','towersmallblocks','doughmakeballs','tieshoes','holdpencilproperly','drawsanyshape','usescissorscutshape']
    
    # viewPHQAssessmentForm =['ID','Appointment Id','AnyPleasure','AnyDepression','AnyTrouble','Anytiredness','AnyOvereat','Anybadfeel','TroubledbyAnything','MovingAroundAlot','AnyHurtYourself']
    viewPHQAssessmentForm =['ID','Appointment Id','Date']
    
    # viewHARSAssessmentForm =['ID','Appointment Id','anyAnxiousMood','AnyTensionFeeling','AnyFearsfeeling','AnyInsomnia','AnyIntellectual','AnyDipressedMood','AnySomaticpains',
    #                        'AnySomaticWeekness','AnyCardiovascular','AnyRespiratory','AnyGastrontedtinal','AnyGenitourinarySymptoms','AnyAutonomicSymptoms','AnyBehaviouratInterview']
    viewHARSAssessmentForm =['ID','Appointment Id','Date']
    
    # viewHRDSAssessmentForm =['ID','Appointment Id','HRDSDepressedMood','HRDSFeelingGuilt','HRDSSuide','HRDSInsomnia','HRDSMidNight','HRDSEarlyMorning',
    #                          'HRDSWork','HRDSRetardation','HRDSAgitation','HRDSPsychic','HRDSAnxietySomatic','HRDSSomatic','HDRSGeneralSomatic','HDRSLossOfLibido','HDRSHypochondriasis','HDRSLossofWeight','HDRSInsight']
    # viewCKASAssessmentForm =['ID','Appointment ID','Date','Score']
    # viewCKASAssessmentForm =['ID','Appointment Id','CKASConsistentEyeContact','CKASPointsTowardsObject','CKASFollowSimpleCommand','CKASRespondWhencalled','CKASTryToCopy','CKASCallOutMama'
    #                          ,'CKASInterestInplaying','CKASLimitedUseofLanguage','CKASFrequentEyeBlinkt','CKASClimbWithoutScare','CKASSpeakNonContextly','CKASIndicateTowardsObject','CKASAnyRegression']
    viewCKASAssessmentForm =['ID','Appointment ID','Date','Score']
    # AllAppointmentadminReport = ['DATE','TIME','DURATION','PATIENT ID','PATIENT NAME','SERVICE','VISIT TYPE','HCP NAME','PAYMENT MODE','FEES','DISCOUNT','DATE OF RECEIPT','INVOICE NO.','CGST','SGST','TOTAL AMOUNT','STATUS','LOCATION','VISIT ID','PACKAGE NAME','SESSIONS AVAILED','REMOTE SESSION']
    
    patientPastConsults = ['MAID','Branch','Doctor','Date','Service']

    patientMedicalHistory = ['MPID','AppointmentId','medication','type','route','times','duration','dosage','comments','Prescription','Branch','Doctor','Service','AddDate']
    
    CollectionReport = ['LOCATION','DATE','INVOICE/RECEIPT NO.','VISIT ID','PATIENT ID','PATIENT NAME','SERVICE NAME','SERVICE FEE','DISCOUNT','Payment Type','CASH AMOUNT','CARD AMOUNT','UPI AMOUNT','ONLINE AMOUNT','CHEQUE AMOUNT','PREPAID AMOUNT','DISCOUNT PERCENTAGE','CGST','SGST','AMOUNT PAYABLE','AMOUNT PAID','AMOUNT BALANCE','PAYMENT MODE','CO-PAY AMOUNT','CO-PAY ORG NAME','DISCOUNT REASON','BANK NAME','CARD TYPE','CARD NUMBER','COMMENTS','PACKAGE NAME','SESSION AVAILED','BILLED BY']

    UnsettledDues = ['DATE','INVOICE NO.','VISIT ID','PATIENT ID','PATIENT NAME','SERVICE NAME','SERVICE FEE','DISCOUNT','AMOUNT PAYABLE','AMOUNT PAID','AMOUNT BALANCE','PaymentMode','COMMENTS'
                      ,'PATIENT MOBILE','LOCATION']

    getDetailedCreditReceipts = ['DATE','RECEIPT NO.','PATIENT ID','PATIENT NAME','AMOUNT','Description','PAYMENT MODE','TRANSACTION COMMENTS','BANK NAME','CARD NUMBER','CARD TYPE']

    # CompletedClinicVisit = ['DATE','TIME','DURATION','PATIENT ID','PATIENT NAME','SERVICE','VISIT TYPE','HCP NAME','PAYMENT MODE','FEES','DISCOUNT','DATE OF RECEIPT','INVOICE NO.','CGST','SGST','TOTAL AMOUNT','STATUS','LOCATION','VISIT ID','PACKAGE NAME','SESSIONS AVAILED','REMOTE SESSION']
    
    # AllClinicVisit = ['DATE','TIME','DURATION','PATIENT ID','PATIENT NAME','SERVICE','VISIT TYPE','HCP NAME','PAYMENT MODE','FEES','DISCOUNT','DATE OF RECEIPT','INVOICE NO.','CGST','SGST','TOTAL AMOUNT','STATUS','LOCATION','VISIT ID','PACKAGE NAME','SESSIONS AVAILED','REMOTE SESSION']
    
    # AllOnlineVisit = ['DATE','TIME','DURATION','PATIENT ID','PATIENT NAME','SERVICE','VISIT TYPE','HCP NAME','PAYMENT MODE','FEES','DISCOUNT','DATE OF RECEIPT','INVOICE NO.','CGST','SGST','TOTAL AMOUNT','STATUS','LOCATION','VISIT ID','PACKAGE NAME','SESSIONS AVAILED','REMOTE SESSION']
    
    # NonGstInvoices = ['LOCATION','DATE','INVOICE NO.','VISIT ID','PATIENT ID','PATIENT NAME','SERVICE NAME','SERVICE FEE','DISCOUNT','DISCOUNT REASON','AMOUNT PAYABLE','AMOUNT PAID','AMOUNT BALANCE','PAYMENT MODE','CO-PAY AMOUNT','CO-PAY ORG NAME','BANK NAME','CARD TYPE','CARD NUMBER','COMMENTS','STATUS','CASH AMOUNT','CARD AMOUNT','UPI AMOUNT','ONLINE AMOUNT','CHEQUE AMOUNT','PREPAID AMOUNT']    
    # NonGstInvoices = ['LOCATION','DATE','INVOICE NO.','VISIT ID','PATIENT ID','PATIENT NAME','SERVICE NAME','SERVICE FEE','DISCOUNT','DISCOUNT REASON','AMOUNT PAYABLE','AMOUNT PAID','AMOUNT BALANCE','CO-PAY AMOUNT','CO-PAY ORG NAME','BANK NAME','CARD TYPE','CARD NUMBER','COMMENTS','CASH AMOUNT','CARD AMOUNT','UPI AMOUNT','ONLINE AMOUNT','CHEQUE AMOUNT','PREPAID AMOUNT']    
    
    # getClinicRights = ['key', 'label']

    CopayInvoices = ['DATE','INVOICE NO.','VISIT ID','PATIENT ID','PATIENT NAME','SERVICE NAME','SERVICE FEE','DISCOUNT','AMOUNT PAYABLE','AMOUNT PAID','AMOUNT BALANCE','PAYMENT MODE','COMMENTS',
                     'CO-PAY ORG NAME','CO-PAY AMOUNT','BANK NAME','CARD TYPE','CARD NUMBER','DISCOUNT REASON','LOCATION']
    
    # getAllPolicy =['Id','Policy Name'] 
    
    PackageMembership = ['DATE','PATIENT ID','PATIENT NAME','PACKAGE NAME','TOTAL SESSIONS','SESSIONS AVAILED','SESSIONS AVAILABLE','Branch']

    getAllPolicy =['Id','Policy Name','Add Date']

    getPatientDetailFromAppointment = ['AppointId','Pid','date','Doctor Name','Branch','Gender','Email','UHID','DOB','Address','Mobile','Patient']
    
    viewIndianScaleAssessmentAutismReport = ['ID','Appointment Id','SOCIAL RECIPROCITY','EMOTIONAL RESPONSIVENESS','SPEECH COMMUNICATION','BEHAVIOUR PATTERNS','SENSORY ASPECTS','COGNITIVE COMPONENT','Final Comment']  
    
    viewSequinFormBoardTestReport =['ID','Appointment Id','Mental Age','IQ','Shortest Time','Total Time','Corresponds Mental Age','Suggesting Intellectual Functioning']
    
    viewGeselsDrawingTestofintelligenceReport =['ID','Appointment Id','Mental Age','IQ','Mental Age Months','Mental Age Years','IQ of','Depicting']
    
    viewRavenStandardProgressiveMatricesReport =['ID','Appointment Id','Raw Score','Percentile','Grade','Interpretation','Corresponds To']
    
    viewDevelopmentalProfileReport =['ID','Appointment Id','Physical Score','Physical Category','Physical Age Equivalent','Adaptive Behavior Score','Adaptive Behavior Category','Adaptive Behavior Age Equivalent','Social Score','Social Category','Social Equivalent','Cognitive Score','Cognitive Category','Cognitive Age Equivalent','Comm Standard Score','Comm Category','Comm Age Equivalent','General Dev Score','General Dev Category','General Age Equivalent']
    
    viewWechslerTestForm = ['Appointment Id','SubsetScore','ReadCompStandardScore','ReadCompConfidenceInterval','ReadCompPercentileRank','ReadCompGradeEquivalent','WordReadStandardScore',
                            'WordReadConfidence','WordReadPercentileRank','WordReadGradeEquivalent','EssayCompStandardScore','EssayCompConfidence','EssayCompPercentileRank'
                           ,'EssayCompGradeEquivalent','NumOperStandardScore','NumOperConfidence','NumOperPercentileRank','NumOperGradeEquivalent','SpelStandardScore'
                           ,'SpelConfidence','SpelPercentileRank','SpelGradeEquivalent','Comment','MathematicsComment','WrittenExpComment']
    
    viewPerceptualAndVisualMotorAbilityForm = ['Appointment Id','VisualDiscr','VisualDiscrComments','VisualMemoryTest','VisualMemoryTestComments','AuditoryMemory','AuditoryMemoryComments','Attention',
                           'AttentionComments','DoubleNumCancel','DoubleNumCancelComments','Language','LanguageComments','Reading','ReadingComments'
                           ,'Comprehension','ComprehensionComments','Spelling','SpellingComments','WritingAndCopy','WritingAndCopyComments','WritingSkills'
                           ,'WritingSkillsComments','ExpressiveWriting','ExpressiveWritingComments','Copying','CopyingComments','Arithmetic',
                        'ArithmeticComments']
    
    viewPerceptualAndVisualMotorAbilityReport = ['Appointment Id','VisualDiscr','VisualDiscrComments','VisualMemoryTest','VisualMemoryTestComments','AuditoryMemory','AuditoryMemoryComments','Attention',
                           'AttentionComments','DoubleNumCancel','DoubleNumCancelComments','Language','LanguageComments','Reading','ReadingComments'
                           ,'Comprehension','ComprehensionComments','Spelling','SpellingComments','WritingAndCopy','WritingAndCopyComments','WritingSkills'
                           ,'WritingSkillsComments','ExpressiveWriting','ExpressiveWritingComments','Copying','CopyingComments','Arithmetic',
                        'ArithmeticComments']
    
    viewWechslerTestReport = ['Appointment Id','SubsetScore','ReadCompStandardScore','ReadCompConfidenceInterval','ReadCompPercentileRank','ReadCompGradeEquivalent','WordReadStandardScore',
                            'WordReadConfidence','WordReadPercentileRank','WordReadGradeEquivalent','EssayCompStandardScore','EssayCompConfidence','EssayCompPercentileRank'
                           ,'EssayCompGradeEquivalent','NumOperStandardScore','NumOperConfidence','NumOperPercentileRank','NumOperGradeEquivalent','SpelStandardScore'
                           ,'SpelConfidence','SpelPercentileRank','SpelGradeEquivalent','Comment','MathematicsComment','WrittenExpComment']
    
    viewChildBehaviorChecklistForm = ['Appointment Id','AnxiousScores','AnxiousTscore','AnxiousRange','WithdrawnScores','WithdrawnTscore','WithdrawnRange',
                           'SomaticComplaintScores','SomaticComplaintTscore','SomaticComplaintRange','SocialProblemScores','SocialProblemTscore','SocialProblemRange'
                           ,'ThoughtProblemScore','ThoughtProblemTscore','ThoughtProblemRange','AttentionProblemScore','AttentionProblemTscore','AttentionProblemRange'
                             ,'RuleBreakingBehaviorScore','RuleBreakingBehaviorTscore','RuleBreakingBehaviorRange','AggressiveBehaviorScores'
                             ,'AggressiveBehaviorTscore','AggressiveBehaviorRange','Comment']
    
    viewChildBehaviorChecklistReport = ['Appointment Id','AnxiousScores','AnxiousTscore','AnxiousRange','WithdrawnScores','WithdrawnTscore','WithdrawnRange',
                           'SomaticComplaintScores','SomaticComplaintTscore','SomaticComplaintRange','SocialProblemScores','SocialProblemTscore','SocialProblemRange'
                           ,'ThoughtProblemScore','ThoughtProblemTscore','ThoughtProblemRange','AttentionProblemScore','AttentionProblemTscore','AttentionProblemRange'
                             ,'RuleBreakingBehaviorScore','RuleBreakingBehaviorTscore','RuleBreakingBehaviorRange','AggressiveBehaviorScores'
                             ,'AggressiveBehaviorTscore','AggressiveBehaviorRange','Comment']
    
    viewMalinIntelligenceScaleforIndianChildrenForm = ['ID','Appointment Id','InformationTestScores','PictureTestScores','GeneralTestScores','BlockDesignTestScores',
                                                     'ArithmeticTestScores','ObjectScores','VocabularyTestScores','MazeTestScores','AnalogiesScores',
                                                     'CodingScores','VQ','PQ','FullScaleIQ','Comment']
    
    viewMalinIntelligenceScaleforIndianChildrenReport = ['ID','Appointment Id','InformationTestScores','PictureTestScores','GeneralTestScores','BlockDesignTestScores',
                                                     'ArithmeticTestScores','ObjectScores','VocabularyTestScores','MazeTestScores','AnalogiesScores',
                                                     'CodingScores','VQ','PQ','FullScaleIQ','Comment']
    
    viewChildAnxietyRelatedDisordersForm =['ID','Appointment Id','PanicDisorderScore','GeneralizedAnxietyDisorderScore','SeparationAnxietyDisorderScore'
                                           ,'SocialAnxietyDisorderScore','SchoolAvoidanceScore','AnxietyDisorderScore','Comment']
    
    viewChildAnxietyRelatedDisordersReport =['ID','Appointment Id','PanicDisorderScore','GeneralizedAnxietyDisorderScore','SeparationAnxietyDisorderScore'
                                           ,'SocialAnxietyDisorderScore','SchoolAvoidanceScore','AnxietyDisorderScore','Comment']
    
    viewHumanFormDrawingtestForm = ['ID','Appointment Id','findings','indicators','comment']
    
    viewHumanTreePersonTestForm = ['ID','Appointment Id','findings','indicators','comment']
    
    viewHumanFormDrawingtestReport = ['ID','Appointment Id','findings','indicators','comment']
    
    viewHumanTreePersonTestReport = ['ID','Appointment Id','findings','indicators','comment']
    
    viewDSMVCriteriaForm =['ID','Appointment Id','ACriteria','ACriteriaComment','BCriteria','BCriteriaComment','CCriteria','CCriteriaComment'
                           ,'DCriteria','DCriteriaComment','Question5','Question5Comment','Question6','Question6Comment','Question7','Question7Comment']
    
    viewDSMVCriteriaReport =['ID','Appointment Id','ACriteria','ACriteriaComment','BCriteria','BCriteriaComment','CCriteria','CCriteriaComment'
                           ,'DCriteria','DCriteriaComment','Question5','Question5Comment','Question6','Question6Comment','Question7','Question7Comment']
    
    viewEpidemiologicalStudiesDepressionScaleForm =['ID','Appointment Id','NotAtAllScore','ALittleScore','SomeScore','ALotScore','TotalRawScore','Comment']
    
    viewEpidemiologicalStudiesDepressionScaleReport =['ID','Appointment Id','NotAtAllScore','ALittleScore','SomeScore','ALotScore','TotalRawScore','Comment']
    
    viewVinelandSocialMaturityScaleReport =['ID','Appointment Id','Social Age','Social Quotient','Observations']

    viewChildhoodAutismRatingScaleReport =['ID','Appointment Id','Relating to People','Imitation','Emotional Response','Body Use','Object Use','Daptation Change','Visual Response','Listening Response','Taste Smell Use','Fear or Nervousness','Verbal','Non Verbal','Activity Level','Consistency Response','General Impression','Concluding Remark']

    viewIndianScaleAssessmentAutismForm = ['ID','Appointment Id','SOCIAL RECIPROCITY','EMOTIONAL RESPONSIVENESS','SPEECH COMMUNICATION','BEHAVIOUR PATTERNS','SENSORY ASPECTS','COGNITIVE COMPONENT','Final Comment']

    viewNICHQVanderbiltADHDParentReport =['ID','Appointment Id','Inattention Score','Hyperactivity Score','Combined Score','Oppositional Score','Conduct Score','Anxiety Score']

    getdoctormenu = ['ID','Branch','Patient','Age','Procedure','Date','Gender']

    patientExamHistory = ['MAID','Branch','Doctor','Date','Service']

    ProvisionalDiagnosisReport = ['ProvisionalDiagnosis','AppointmentId','ICDCode','ICDDescription','Date']

    editProvisionalDi=['MPD_ProvisionalDiagnosis','MPD_ICDCode','MPD_ICDDescription','MPDID']
    
    # ProvisionalDiagnosisReport = ['ProvisionalDiagnosis','AppointmentId','ICDCode','ICDDescription','Date']
    
    SessionNotesReport = ['Started','AppointmentId','todayfeel','dotoday','Notes','Date']
    
    VisitReasonReport = ['ID','Informed By','Present Concerns','Appointment Id']
    
    PastHistoryReport = ['ID','Appointment Id','Past Medications']

    PrenatalHistoryReport = ['ID','Appointment Id','Mother Conception','Mother Pregnancy','History Abortions','Gestational Diabetes',
                               'Neurological Disorder', 'Physical Emotional','Inompatibility','Jaundice','Seizures','TraumaInjury',
                               'Bleeding pregnancy','Adequate Nutrition','Infections','Smoking','Observations']

    PatientBirthHistoryReport = ['ID','Appointment ID','Mother Health','Delivery Type','Type of Delivery','Delivery Location',
                                   'Multiple Pregnancies','Complication Pregnancy','Child Birth','Child Birth Week','Birth Weight',
                                   'Birth Cry','Neonatal Condition','Special CareAny','Any Medical Events','Congenital','Observations']

    DevelopmentalHistoryReport = ['ID','Appointment ID','HoldUp HeadAge','Rollover age','Sit Age','Stand Alone Age','Walk Age','Talk Age',
                                    'Toilet Train Age','Feed Age','Dresshim Age','Observations']
    
    SpeechDevelopmentHistoryReport = ['ID','Appointment ID','Vocalization','Babbling','First Word','Phrases','Simple Sentences','Observations']
    
    socialhistoryReport = ['ID','Appointment ID','Social History']
    
    medicalhistoryReport =['ID','Appointment ID','Medical History']

    familyhistoryReport =['ID','Appointment Id','Family type','Consanguinity','Family History']
    
    educationhistoryReport =['ID','Appointment Id','Education History']
    
    GeneralExamReport =['ID','Appointment Id','Height','Weight','Head Circumference','Observations']

    VitalsExamReport =['ID','Appointment Id','Blood Pressure','Pulse Rate','Respiratory Rate','Temperature']

    SystemicExamReport =['ID','Appointment Id','Observations']

    STOroperipheralExam =['ID','Appointment Id','Lips Appearance','Lips Movements','Tongue Appearance','Tongue Movements','Teeth Appearance','Teeth Movements',
                                  'Hard Palate Appearance','Soft Palate Appearance','Soft Palate Movements','Uvula Appearance','Uvula Movements','Mandible Appearance','Mandible Movements','Drooling','Blowing','Biting','Sucking','Swallowing','Observations']

    STArticulationSpeechIntelligibilityReport =['ID','Appointment Id','Noonecan','memberscan','Strangerscan','Observations']

    STArticulationVoiceReport =['ID','Appointment Id','Pitch','Loudness','Quality','Observations']

    CognitivePrerequitesReport =['ID','Appointment Id','Imitation','Objectpermanence','Timeconcept','Colourconcept','Moneyconcept','Sequencing','Matching','Meanendrelationship','Observations']

    STVerbalCommunication =['ID','Appointment Id','Expression','Comprehension','Observations']

    STNonVerbalCommunicationReport =['ID','Appointment Id','Expression','Comprehension','Observations']

    OTHandFunctionsReport =['ID','Appointment Id','Hand Dominance','Hand Preference','Reach Forward','Reach Backward','Reach Lateral','Reach Downward','Grasp UlnarPalmar','Grasp Palmar',
                              'Grasp RadialPalmar','Grasp RadialDigital','Grasp InferiorPincer','Reach Upward','Grasp NeatPincer','Grasp Palmarsupinate','Grasp Digitalpronate','Grasp Statictripod','Grasp Dynamictripod','Prehension PadtoPad','Prehension TiptoTip','Prehension PadtoSide']

    OTNonEquilibriumCoordinationReport =['ID','Appointment Id','Fingertonose','Fingertotherapistfinger','Fingertofinger','Alternatnosefinger','Fingeropposition','Massgrasp',
                                           'Pronationsupination','Reboundtest','Tappinghand','Tappingfeet','Pointingandpastpointing','Alternateheeltokneeheeltoe','Toetoexaminersfinger','Heeltoshin','Drawingacircle','Fixationorpositionholding']

    OTEquilibriumCoordinationReport =['ID','Appointment Id','Standingwithnormalbaseofsupport','Standingwithnarrowbaseofsupport','Standingintandemposition','Standingononefeet','Perturbation','Standinginfunctionalreach','Standinglateralflexionofthetrunktoeachside','Tandemwalking','WalkingInastraightline','Walksidewaysbackwards','Walkinhorizontalvertical','Marchinplace','Startstopabruptly',
                                        'Walkandpivotincommand','Walkincircle','Walkonheelsandtoes','Turnsoncommand','Stepoveraroundobstacles','Stairclimbingwithhandrails','Jumpingjacks','Sittingontherapybal']

    OTCognitionAndPerceptionReport =['ID','Appointment Id','Praxis','Rightleftdiscrimination','Fingerindentification','Orientationtoperson','Orientationtoplace',
                                       'Conceputalseriescompletion','Selectiveattention','Focusedattention','Spatialperception','Visualmemory','Verbalmemory','Identificationofobjects','Proverbinterpretation','Randomlettertest','Overlappingfigures']

    OTSensoryExamReport =['ID','Appointment Id','Visual tracking','Choreiform movements','Tremor','Exaggerated associated','Graphesthesis','Stereognosis','Weight bearing hands','Prone extension pattern']

    OTSensoryProfileReport =['ID','Appointment Id','Observations']

    AddtionalinfoReport =['ID','Appointment Id','Observations']

    PTFunctionalAbilitiesReport =['ID','Appointment Id','Gross Motor','Fine Motor','Communication Speech','Feeding','Playskills','ADL']

    PTFunctionalLimitationsReport =['ID','Appointment Id','Gross Motor','Fine Motor','Communication Speech','Feeding','Playskills','ADL']

    PTPosturalSystemAlignmentReport =['ID','Appointment Id','Head Neck','Shoulder Scapular','Shoulder and Scapular','Shouldern Scapular','Ribcage and Chest','Trunk',
                                        'Trunks','Pelvic Complex Right','Pelvic Complex Left','Hipjoint Abduction','Hipjoint Adduction','Hipjoint Rotation','Symmetrical','Assymetrical','Observations']
    
    PTPosturalSystemBOSReport =['ID','Appointment Id','Base of Support']

    PTPosturalSystemCOMReport =['ID','Appointment Id','Center of Mass','Within support','Strategies posture']

    PTAnticipatoryControlReport =['ID','Appointment Id','Canchildanti','Observations']

    PTPosturalCounterbalanceReport =['ID','Appointment Id','Observations']

    PTPosturalSystemImpairmentsReport =['ID','Appointment Id','Muscle Architecture','Anycallosities','Anyother specific posture','Observations']

    PTMovementSystemReport =['ID','Appointment Id','Canthey overcome','How do','Strategies used']

    PTMovementStrategiesReport =['ID','Appointment Id','Childgenerallyperformsactivitie','CanperformLateralweightshifts','CanperformLateralweightshiftsleft',
                                   'CanperformDiagonalweightRight','CanperformDiagonalweightLeft','CanperformneckthoracicspineRight','CanperformneckthoracicspineLeft','HowarethedissociationsPelvicfemoral','HowaredissociationsInterlimb','HowthedissociationsScapulohumeral','HowthedissociationsUpperLowerbody']
    
    PTRangeSpeedofMovementReport =['ID','Appointment Id','Range Speed Movement','at Trunk','Extremities']

    PTStabilityMobilityReport =['ID','Appointment Id','Mobility Strategies']

    PTMovementSystemImpairmentReport =['ID','Appointment Id','Excessive movement','movement StaticPostures','Integration of PostureMovement','Balance Transitions','Accuracy of Movements','Observations']
    
    PTRegulatorySystemReport =['ID','Appointment Id','Affect','Arousal','Attention','Action','Observations']

    PTNeurometerSystemReport =['ID','Appointment Id','Initiation','Sustenance','Termination','Control and Gradation','Contraction Concentric',
                             'Contraction Isometric','Contraction Eccentric','Reciprocal Inhibition','Isolated work','Dynamic stiffness','Extraneous Movement','Observations']
    
    PTMusculoskeletalSystemReport =['ID','Appointment Id','Muscle Endurance','Skeletal Comments','Tardieu ScaleTR1','Tardieu ScaleTR2','Tardieu ScaleTR3',
                                      'Tardieu ScaleHamsR1','Tardieu ScaleHamsR2','Observations']
    
    PTSensorySystemReport =['ID','Appointment Id','Modulation Issues','Visual system','Auditory system','Auditory system Response','Vestibular system','Somatosensory system','Oromotor system','Olfactory system','Observations']
    
    PTCognitiveSystemReport =['ID','Appointment Id','Intelligence','Memory','Adaptability','Motor Planning','Observations']

    ReceptiveLanguageAssessmentReport =['ID','Appointment Id','Comprehends sounds','Comprehends loud','Comprehends categorizesounds','Comprehends animalsounds',
                                          'Comprehends fruitsname','Comprehends colorsname','Comprehends animalname','Comprehends vegetablename','Comprehends shapesname',
                                          'Comprehends bodyparts','Comprehends vehiclenames','Understandingrhymes','Respondscorrectly','Identifiessounds','Actsoutcommands','Comprehends stepscommands','Understandinggreeting','Understanding']
    
    ExpressiveLanguageAssessmentReport =['ID','Appointment Id','Imitates environmental sounds','Imitates loud and softsounds','Imitates lexical categories','Imitates colors name','Imitates body parts','Imitates singing and phrases',
                                           'Imitates alphabets AtoZ','articles','Watches','Imitates counting','Claps','Respondstosinglesigns','Imitates socialgreetings','Occassionallytrytoimitate','Imitates commonsyllables']
    
    ConnersParentRatingScaleReport =['ID','Appointment Id','Scores','Tscores','Range','Observations']
    
    
    SpecialEdassessmenttwoyearsReport =['ID','Appointment Id','Respondstoname','Makeseyecontact','Respondstolightandsoundtoys','canmoveeyesupanddown','canmoveeyesleftandright','repeatswords',
                                           'knowsidentificationofnumber','canrollpoundandsqueezeclay','vocabularyMom','vocabularyDad','Vocabularydog','vocabularycat','vocabularytree','vocabularytable','vocabularychair','vocabularycow',
                                           'vocabularycrayons','vocabularybus','vocabularycar','vocabularybook','vocabularyapple','vocabularybanana','vocabularybottle','Candostacking','canmaketower','respondstobubbles','Identifieshappyandsad',
                                           'Knowsshapes','knowscolors','knowsanimals','knowsvehicles','knowsbodyparts','knowsidentificationofalphabets','knowsmoreorless','knowsbigandsmall','knowsnearandfar','canidentifhisorher','canidentifybag','canidentifyshoes','canidentifybottle']
    SpecialEdassessmentthreeyearsReport =['ID','Appointment Id','respondstoname','makeseyecontact','cansitformins','canmoveeyesupanddown','canmoveeyesleftandright','cananswerfullname','vocabularybodyparts','canfollowstepsinstruction','cananswerold','cananswerwhatsyourmothersname','cananswerwhichisyoufavoritecolour',
                                            'canfixpiecepuzzle','vocabularyshapescircle','vocabularycolors','vocabularywild','Vocabularyfruits','canfollowstepinstruction','cansingrhymes','cangiveanswerseeinsky','cangiveanswerswiminwater','cangiveanswerseeontree','knowsidentificationofalphabets','knowsidentificationofnumbers','Canholdapencilcrayon'
                                            ,'canscribble','cancoloringivenshape','cantearandpaste','canidentifyemotionshappy','canidentifyemotionssad','canidentifyemotionsangry','canidentifyemotionsupset']
    
    SpecialEdassessmentthreefouryearsReport =['ID','Appointment Id','doesrespondtonamecall','doesmakeseyecontact','initiatesinteractiontoward','cansitformins','understandinstructionslikestand','getthatputthere',
                                                'givemegetthis','runwalkjump','lookdownup','cananswerwhatis','cananswerfavoritecolour','canfixpiecepuzzle','vocabularyshapes','vocabularycolors','vocabularywild','vocabularyfruits','vocabularybodyparts',
                                                'Canunderstandpositions','cansingrhymes','canunderstandstories','canWhatquestions','canidentifybasicobjects','canholdacrayonpencil','canmaketower','canimitate','canplaydoughballs','canheshethrow','canrecognisealphabet','Canrecognisenumerals','cancolourgivenshape']
    
    SpecialEdassessmentfouryearsReport =['ID','Appointment Id','respondnamecall','makeseyecontact','interactiontowardothers','cansitformins','cananswerwhatname','answerfavoritecolour','canfixpiecepuzzle','vocabularyshapes','vocabularycolors',
                                           'vocabularywild','vocabularybody','Vocabularyfruits','canunderstandpositions','cansingrhymes','canunderstandstories','replyWhatquestions','identifybasicobjects','holdcrayonpencil','canimitate','doughmakeballs','canthrow','recognisealphabets','recognisenumerals','cancolourshape']
    
    SpecialEdassessmentsevenyearsReport =['ID','Appointment Id','putneedsminimalassistance','eathandsonly','fixasandwich','givefirstlastname','cangiveaddress','awareofemotions','canzipper',
                                            'independentlyassistanct','asksmeaningfulquestions','tellsstorieswords','Doestellage','canobeysimplecommands','readsimplewords','writesimplewords',
                                            'namethingsaround','alternatesfeetupdownstairs','pedaltricycle','catchandthrowball','towersmallblocks','doughmakeballs','tieshoes','holdpencilproperly','drawsanyshape','usescissorscutshape']

    getSpecialedPage = ['type','name','formControlName','label','align','value','className','path']
    
    getAssessmentPhycologyPage = ['type','name','formControlName','label','align','value','className','path']


    editDSMVASDCriteria= ['Id','persistentDeficit','persistentDeficitComment','restrictedRepetitive','restrictedRepetitiveComment','symptomsMust','symptomsMustComment','symptomsCause','symptomsCauseComment','theseDisturbances','theseDisturbancesComment','question7','question7Comment']
    
    viewDSMVASDCriteria= ['Id','persistentDeficit','persistentDeficitComment','restrictedRepetitive','restrictedRepetitiveComment','symptomsMust','symptomsMustComment','symptomsCause','symptomsCauseComment','theseDisturbances','theseDisturbancesComment','question7','question7Comment']
    
    DSMVASDCriteriaReport= ['Id','persistentDeficit','persistentDeficitComment','restrictedRepetitive','restrictedRepetitiveComment','symptomsMust','symptomsMustComment','symptomsCause','symptomsCauseComment','theseDisturbances','theseDisturbancesComment','question7','question7Comment']

    IndianScaleAssessmentAutism = ['type','name','formControlName','label','align','value','className']

    getAllArticles = ['Id','articleTitle','articleThumbnail','articleDesc']

    getConditions = ['Id','Heading','Description']

    viewCKADHDScreening = ['ID','A19','B1018','C1921']
    
    languageExposureReport = ['ID','Appointment Id','SpokenAtHome','FamilyModel','CommunicationMode']
    
    getlanguageExposure = ['ID','Appointment Id','SpokenAtHome','FamilyModel','CommunicationMode']
    
    ParentConcernReport = ['ID','Appointment Id','Comment']
    
    getParentConcern = ['ID','Appointment Id','Comment']
    
    ProvisionalDiagnosisFormReport = ['ID','Appointment Id','Comment']
    
    getProvisionalDiagnosis = ['ID','Appointment Id','Comment']
    
    DiagnosticFormulationsReport = ['ID','Appointment Id','Comment','Type']
    
    getDiagnosticFormulations = ['ID','Appointment Id','Comment','Type']


    viewCKDevelopScreening=['ID','grossmotoryes','grossmotorno','finemotoryes','finemotorno','selfhelpyes','selfhelpno','problemsolvingyes','problemsolvingno','emotionalyes','emotionalno',
                            'receptiveyes','receptiveno','expressiveyes','expressiveno','socialyes','socialno']

    stutteringhistoryReport=['persistent','recovered','startedstuttering','phraserepititions','wordrepitions','Syllablerepitions',
        'Blockslike','Interjections','demonstrated','phsyicaltension','frustrationabout','Complaints','childeverbeenteased','childeverdiscussed',
        'childseemstostutter','stutterinyoursecondary','childstartedlearning','remarkableduringpregnancy','remarkableconditionatbirth',
        'currenthealthmedicalconcerns','takinganymedications','allergies','developmentalconcerns','hearingtested','behavioursoccur',
        'Inattentiveness','Hyperactivity','Nervousness','sensitivity','perfectionism','excitability','frustration','strongfears',
        'excessiveneatness','excessiveshyness','lackofconfidence','competitiveness','speakfluentlyathome','speakfluentlyatschool',
        'speakfluentlyinnewsituation','speakwithoutstutteringathome','speakwithoutstutteringatschool','speakwithoutstutteringinanycondition','stutteringaffectacademicperformance',
        'participationinschool','interactionwithother','interactionwithfamily','willingnesstotalk','selfesteemorattitude','teachernoticedyourchild']
    
    viewStutteringAssessmentReport =['ID','Appointment Id','Behavioural assessment','Cognitive assessment','Impact educational participation',
                                   'Likely to Achieve','Prognosis Effect']

    viewPragmaticSkillsReport = ['Id','InitiationSkills','RespondingSkills','MaintenanceSkills','TerminationSkills','Observations']
    
    VitalExamReport = ['ID','Appointment Id','Observations']
    
    DSMVADHDCriteriaReport = ['ID','Appointment Id','APersistent','BSeveral','CSeveral','Combinedpresentation','DThere','Ethesymptoms','Predominantly']
    
    SocialResponsivenessScaleReport = ['ID','Appointment Id','SCIRawScore','SCITscore','BehaviorsRawScore','BehaviorsTscore','socialAwarenessRawScore','socialAwarenessTscore','socialCognitionRawScore',
        'socialCognitionTscore','socialCommunicationRawScore','socialCommunicationTscore','socialMotivationRawScore','socialMotivationTscore']
    
    editCKADHDScreening = ['ID','mistakesinschoolwork','playactivities','spokentodirectly','failstofinishschool',
                           'difficulttoorganize','reluctantlyengages','losethings','distractedbyextraneous','dailyactivities','maintainalertness',
                           'squirmsinseat','seatinclassroom','climbsexcessively','leisureactivities','drivenbyamotor','Talksexcessively','answersbefore',
                           'difficulttosit','symptomspresent','symptomsleading','symptomsaffecting']
    
    editCKAutismScreening = ['ID','CKASConsistentEyeContact','CKASPointsTowardsObject','CKASFollowSimpleCommand','CKASRespondWhencalled',
                              'CKASTryToCopy','CKASCallOutMama','CKASInterestInplaying','CKASLimitedUseofLanguage','CKASFrequentEyeBlinkt',
                              'CKASClimbWithoutScare','CKASSpeakNonContextly','CKASIndicateTowardsObject','CKASAnyRegression']

    viewGrossMotorForm = ['ID','Appointment ID','0-3 Months','grossmotor03no','3-6 Months','grossmotor36no'
                          ,'6-9 Months','grossmotor69no','9-12 Months','grossmotor12no','12-18 Months',
                          'grossmotor1218no','18-24 Months','grossmotor1824no','24-30 Months','grossmotor2430no',
                          '30-36 Months','grossmotor3036no','36-42 Months','grossmotor3642no','42-48 Months',
                          'grossmotor4248no','48-54 Months','grossmotor4854no','54-60 Months','grossmotor5460no']
    
    viewFineMotorForm = ['ID','Appointment ID','0-3 Months','finemotor03no','3-6 Months','finemotor36no'
                          ,'6-9 Months','finemotor69no','9-12 Months','finemotor12no','12-18 Months',
                          'finemotor1218no','18-24 Months','finemotor1824no','24-30 Months','finemotor2430no',
                          '30-36 Months','finemotor3036no','36-42 Months','finemotor3642no','42-48 Months',
                          'finemotor4248no','48-54 Months','finemotor4854no','54-60 Months','finemotor5460no']
    
    viewSelfHelpForm = ['ID','Appointment ID','0-3 Months','selfhelp03no','3-6 Months','selfhelp36no'
                          ,'6-9 Months','selfhelp69no','9-12 Months','selfhelp12no','12-18 Months',
                          'selfhelp1218no','18-24 Months','selfhelp1824no','24-30 Months','selfhelp2430no',
                          '30-36 Months','selfhelp3036no','36-42 Months','selfhelp3642no','42-48 Months',
                          'selfhelp4248no','48-54 Months','selfhelp4854no','54-60 Months','selfhelp5460no']
    
    viewProblemSolvingForm = ['ID','Appointment ID','0-3 Months','finemotor03no','3-6 Months','finemotor36no'
                          ,'6-9 Months','finemotor69no','9-12 Months','finemotor12no','12-18 Months',
                          'finemotor1218no','18-24 Months','finemotor1824no','24-30 Months','finemotor2430no',
                          '30-36 Months','finemotor3036no','36-42 Months','finemotor3642no','42-48 Months',
                          'finemotor4248no','48-54 Months','finemotor4854no','54-60 Months','finemotor5460no']
    
    viewEmotionalForm = ['ID','Appointment ID','0-3 Months','finemotor03no','3-6 Months','finemotor36no'
                          ,'6-9 Months','finemotor69no','9-12 Months','finemotor12no','12-18 Months',
                          'finemotor1218no','18-24 Months','finemotor1824no','24-30 Months','finemotor2430no',
                          '30-36 Months','finemotor3036no','36-42 Months','finemotor3642no','42-48 Months',
                          'finemotor4248no','48-54 Months','finemotor4854no','54-60 Months','finemotor5460no']
    
    viewReceptiveForm = ['ID','Appointment ID','0-3 Months','finemotor03no','3-6 Months','finemotor36no'
                          ,'6-9 Months','finemotor69no','9-12 Months','finemotor12no','12-18 Months',
                          'finemotor1218no','18-24 Months','finemotor1824no','24-30 Months','finemotor2430no',
                          '30-36 Months','finemotor3036no','36-42 Months','finemotor3642no','42-48 Months',
                          'finemotor4248no','48-54 Months','finemotor4854no','54-60 Months','finemotor5460no']
    
    viewExpressiveLanguageForm = ['ID','Appointment ID','0-3 Months','finemotor03no','3-6 Months','finemotor36no'
                          ,'6-9 Months','finemotor69no','9-12 Months','finemotor12no','12-18 Months',
                          'finemotor1218no','18-24 Months','finemotor1824no','24-30 Months','finemotor2430no',
                          '30-36 Months','finemotor3036no','36-42 Months','finemotor3642no','42-48 Months',
                          'finemotor4248no','48-54 Months','finemotor4854no','54-60 Months','finemotor5460no']
    
    viewSocialSkillsForm = ['ID','Appointment ID','0-3 Months','finemotor03no','3-6 Months','finemotor36no'
                          ,'6-9 Months','finemotor69no','9-12 Months','finemotor12no','12-18 Months',
                          'finemotor1218no','18-24 Months','finemotor1824no','24-30 Months','finemotor2430no',
                          '30-36 Months','finemotor3036no','36-42 Months','finemotor3642no','42-48 Months',
                          'finemotor4248no','48-54 Months','finemotor4854no','54-60 Months','finemotor5460no']
    


