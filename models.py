from peewee import *

database = MySQLDatabase('fr_work', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True,
                                       'host': '129.211.85.31', 'port': 3306, 'user': 'fr_work',
                                       'password': 'Lr13366616376'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Finance(BaseModel):
    f_id = AutoField(column_name='F_ID')
    abstract = CharField(null=True)
    account = CharField(null=True)
    account_date = DateField(null=True)
    customer = CharField(null=True)
    detailed_subjects = CharField(null=True)
    doc_number = CharField(null=True)
    drawee = CharField(null=True)
    end_month = CharField(null=True)
    first_subjects = CharField(null=True)
    is_review = CharField(null=True)
    money = FloatField(null=True)
    payee = CharField(null=True)
    project = CharField(null=True)
    remark = CharField(null=True)
    second_subjects = CharField(null=True)
    start_month = CharField(null=True)

    class Meta:
        table_name = 'finance'


class SocialHouse(BaseModel):
    s_id = AutoField()
    cus_credit_code = CharField(null=True)
    gongshang_company = FloatField(null=True)
    house_fund_company = FloatField(null=True)
    house_fund_person = FloatField(null=True)
    id_number = CharField()
    pay_type = CharField(null=True)
    person = CharField()
    shengyu_company = FloatField(null=True)
    shiye_company = FloatField(null=True)
    shiye_person = FloatField(null=True)
    social_month = IntegerField()
    social_year = IntegerField()
    yanglao_company = FloatField(null=True)
    yanglao_person = FloatField(null=True)
    yiliao_company = FloatField(null=True)
    yiliao_person = FloatField(null=True)

    class Meta:
        table_name = 'social_house'


class User(BaseModel):
    id = AutoField(column_name='ID')
    p_id = CharField(column_name='P_ID')
    basic_salary = FloatField(null=True)
    confirmation_date = CharField(null=True)
    education = CharField(null=True)
    entry_date = DateField()
    is_admin = CharField(null=True)
    leave_date = DateField(null=True)
    name = CharField()
    native_place = CharField(null=True)
    password = CharField(null=True)
    pay_card = CharField(null=True)
    person_id_number = CharField()
    person_state = CharField()
    positional_titles = CharField(null=True)
    registry_type = CharField(null=True)
    remarks = CharField(null=True)
    sex = CharField(null=True)
    social_security_base_number = FloatField(null=True)
    telephone = FloatField(null=True)

    class Meta:
        table_name = 'user'


class Customer(BaseModel):
    id = AutoField(column_name='ID')
    bank_bill_card = CharField(null=True)
    business_scope = TextField(null=True)
    contacts = CharField(null=True)
    cus_credit_code = CharField(null=True, unique=True)
    cus_id = IntegerField(null=True)
    cus_level = CharField(null=True)
    cus_name = CharField(null=True)
    cus_remaks = CharField(null=True)
    cus_simple_name = CharField(null=True)
    cus_source = CharField(null=True)
    cus_state = CharField(null=True)
    cus_tax_type = CharField(null=True)
    cus_term = CharField(null=True)
    establish_date = DateField(null=True)
    finance_end = DateField(null=True)
    housing_fund = CharField(null=True)
    is_change_pay = IntegerField(null=True)
    legal_representative = CharField(null=True)
    month_pay = FloatField(null=True)
    registered_address = CharField(null=True)
    registered_capital = CharField(null=True)
    registration_type = CharField(null=True)
    salesperson = CharField(null=True)
    service_personnel = CharField(null=True)
    social_password = CharField(null=True)
    social_security = CharField(null=True)
    start_service_date = DateField(null=True)
    stop_service_date = DateField(null=True)
    street_township = CharField(null=True)
    tax_bigtype_regist_date = DateField(null=True)
    tax_machine = CharField(null=True)
    tax_office = CharField(null=True)
    tax_start_date = DateField(null=True)
    trusteeship = CharField(null=True)

    class Meta:
        table_name = 'customer'
