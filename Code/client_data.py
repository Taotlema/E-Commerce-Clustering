'''
Methods Data Analytics Assignment
Ayemhenre Isikhuemhen
March 14, 2025
File Description:
'''

# CSV handling libraries
import os
import csv

# Fields
customer_id = int
churn_flag = int
tenure = int
prefered_device = str
city_tier = int
warehouse_to_home = int
preferred_payment_mode = str
gender = str
hour_spent = int
num_device_reg = int
prefered_order_cat = str
satisfaction_score = int
marital_status = str
num_of_address = int
complaints = int
order_amount_annual = int
coupon_used = int
order_count = int
day_since_last_order = int
cash_back_amt = int

# Class for client_data
class client_data: 
    def __init__(self, CustomerID, Churn, Tenure, PreferredLoginDevice, CityTier,
                 WarehouseToHome, PreferredPaymentMode, Gender, HourSpendOnApp,
                 NumberOfDeviceRegistered, PreferedOrderCat, SatisfactionScore,
                 MaritalStatus, NumberOfAddress, Complain, OrderAmountHikeFromlastYear,
                 CouponUsed, OrderCount, DaySinceLastOrder, CashbackAmount):
        self.customer_id = int(CustomerID)
        self.churn_flag = int(Churn)
        self.tenure = int(Tenure)
        self.prefered_device = PreferredLoginDevice
        self.city_tier = int(CityTier)
        self.warehous_to_home = int(WarehouseToHome)
        self.preferred_payment_mode = PreferredPaymentMode
        self.gender = Gender
        self.hour_spent = int(HourSpendOnApp)
        self.num_device_reg = int(NumberOfDeviceRegistered)
        self.prefered_order_cat = PreferedOrderCat
        self.satisfaction_score = int(SatisfactionScore)
        self.marital_status = MaritalStatus
        self.num_of_address = int(NumberOfAddress)
        self.complaints = int(Complain)
        self.order_amount_total = int(OrderAmountHikeFromlastYear)
        self.coupon_used = int(CouponUsed)
        self.order_count = int(OrderCount)
        self.day_since_last_order = int(DaySinceLastOrder)
        self.cash_basck_amt = int(CashbackAmount)

# FILE READING FUNCTIONS

# load_csv: reads through the csv file and loads fields into a client_data object
def load_csv(file_path):
    client_entries = []  # Array of client objects

    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    client = client_data(
                        CustomerID=row.get('CustomerID') or 0,
                        Churn=row.get('Churn') or 0,
                        Tenure=row.get('Tenure') or 0,
                        PreferredLoginDevice=row.get('PreferredLoginDevice') or "Unknown",
                        CityTier=row.get('CityTier') or 0,
                        WarehouseToHome=row.get('WarehouseToHome') or 0,
                        PreferredPaymentMode=row.get('PreferredPaymentMode') or "Unknown",
                        Gender=row.get('Gender') or "Unknown",
                        HourSpendOnApp=row.get('HourSpendOnApp') or 0,
                        NumberOfDeviceRegistered=row.get('NumberOfDeviceRegistered') or 0,
                        PreferedOrderCat=row.get('PreferedOrderCat') or "Unknown",
                        SatisfactionScore=row.get('SatisfactionScore') or 0,
                        MaritalStatus=row.get('MaritalStatus') or "Unknown",
                        NumberOfAddress=row.get('NumberOfAddress') or 0,
                        Complain=row.get('Complain') or 0,
                        OrderAmountHikeFromlastYear=row.get('OrderAmountHikeFromlastYear') or 0,
                        CouponUsed=row.get('CouponUsed') or 0,
                        OrderCount=row.get('OrderCount') or 0,
                        DaySinceLastOrder=row.get('DaySinceLastOrder') or 0,
                        CashbackAmount=row.get('CashbackAmount') or 0
                    )
                    client_entries.append(client)
                except Exception as e:
                    error_handle(e, row)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return client_entries