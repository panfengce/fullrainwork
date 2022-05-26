import uuid

from peewee import *

database = MySQLDatabase('fastapi', **{'charset' : 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True,
                                       'host'    : '129.211.85.31', 'port': 3306, 'user': 'fastapi',
                                       'password': 'fastAPI666888'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Finance(BaseModel):
    id = CharField(primary_key=True, default=uuid.uuid4())
    account = CharField(null=True)
    account_date = DateField(null=True)
    actual_collection = FloatField(null=True)
    create_time = DateTimeField(null=True)
    doc_number = CharField(null=True)
    drawee = CharField(null=True)
    payee = CharField(null=True)
    remark = CharField(null=True)
    sequence = IntegerField(null=True)
    total_receivable = FloatField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'finance'


class FinanceDetail(BaseModel):
    id = CharField(primary_key=True, default=uuid.uuid4())
    abstract = CharField(null=True)
    subjects = CharField(null=True)
    money = FloatField(null=True)
    customer_id = IntegerField(null=True)
    project_id = CharField(null=True)
    period_fz_end = CharField(null=True)
    period_fz_start = CharField(null=True)
    create_time = DateTimeField(null=True)
    update_time = DateTimeField(null=True)
    f = ForeignKeyField(column_name='f_id', field='id', model=Finance, null=True)

    class Meta:
        table_name = 'finance_detail'


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
    housing_fund = CharField(null=True)
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
