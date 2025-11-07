'''''
Methods Data Analytics Assignment
Ayemhenre Isikhuemhen
March 14, 2025
File Descirption: visuals.py contains the functions and scirpts relevant to the creation and
output of graph figures used in data analysis.
'''''

# Data visualization libraries
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Package Libraries
from client_data import load_csv

# Fields
file_path = r"C:\Users\ayemi\Documents\GitHub\Dothem_Analyst\Data\dohtem_ecommerce_customers.csv"
output_folder = r"C:\Users\ayemi\Documents\GitHub\Dothem_Analyst\output"

# UTILITY FUNCTIONS

# Load Data
data = load_csv(file_path)

# Format Data
def format_data(data):
    return [{
        'Gender': client.gender,
        'Coupon_Usage': client.coupon_used,
        'Customer_Satisfaction': client.satisfaction_score,
        'Order_Amount_Hike': client.order_amount_total,
        'Complaints': client.complaints,
        'Days_Since_Last_Order': client.day_since_last_order,
        'PreferredLoginDevice': client.prefered_device,
        'PreferredPaymentMode': client.preferred_payment_mode,
        'PreferredOrderCat': client.prefered_order_cat,
        'Time_Spent': client.hour_spent,
        'MultipleDevices': client.num_device_reg,
        'ChurnFlags': client.churn_flag
    } for client in data]

# Setup the data so it can go into Plotly: client_data -> data -> df
df = pd.DataFrame(format_data(data))

'''
GENERAL PLOTS

Key: 
PreferedPaymentMode: 
1) "Debit Card"           3) "Cash on Delivery" & "COD"     5) "UPI"
2) "Credit Card" & "CC"     4) "E wallet"                     6) "Other"

PreferedLoginDevice Catagories:
1) "Computer"     2) "Mobile Phone" & "Phone" 
3) "Other"

PreferedOrderCat: 
1) "Laptop & Accessory"     2) "Mobile" & "Mobile Phone"
3) "Fashion"                4) "Groceries"
5) "Others"
'''

# pie_gender: Creates a pie chart of gender distribution amoung users
def pie_gender():
    fig = px.pie(df, names='Gender', title='Gender Distribution')
    fig.write_html(output_folder)
    fig.show()
    return 0

# coup_satis: Identifies correlation between coupon usage and customer satisfaction using linear regression
def coup_satis():
    fig = px.scatter(df, x='Coupon_Usage', y='Customer_Satisfaction', trendline='ols',
                     title='Coupon Usage vs Customer Satisfaction')
    fig.write_html(output_folder)
    fig.show()
    return 0

# cash_b_satis: Identifies the correlation between cashbacks and customer satisfaction using linear regression
def cash_b_satis():
    fig = px.scatter(df, x='Cashback_Received', y='Customer_Satisfaction', trendline='ols',
                     title='Cashback vs Customer Satisfaction')
    fig.write_html(output_folder)
    fig.show()
    return 0

# order_hike_satis: Identifies the correlation between customer satisfaction and order amount hike using linear regression
def order_hike_Satis():
    fig = px.scatter(df, x='Order_Amount_Hike', y='Customer_Satisfaction', trendline='ols',
                     title='Order Amount Hike vs Customer Satisfaction')
    fig.write_html(output_folder)
    fig.show()
    return 0

# cust_satis_complaints: Identifies th correlation between customer satisfaction and complaintes using linear regression
def cust_satis_complaints():
    fig = px.scatter(df, x='Complaints', y='Customer_Satisfaction', trendline='ols',
                     title='Complaints vs Customer Satisfaction')
    fig.write_html(output_folder)
    fig.show()
    return 0

# last_order_satis: Identifies the days since last order and customer satisfaction using linear regression
def last_order_satis():
    fig = px.scatter(df, x='Days_Since_Last_Order', y='Customer_Satisfaction', trendline='ols',
                     title='Days Since Last Order vs Customer Satisfaction')
    fig.write_html(output_folder)
    fig.show()
    return 0

'''
INVESTIGATION POINT ONE: DEVICE USAGE AND IMPACT ON CUSTOMER EXPERIENCE
'''

# pie_devices: Creates a pie chart of primary devices that users use for Dothem's Website
def pie_devices():
    fig = px.pie(df, names='PreferredLoginDevice', title='Device Usage Distribution')
    fig.write_html(output_folder)
    fig.show()
    return 0

# bar_multDevices: Creates a bar graph showing amount of users with muiltiple devices per device group
def bar_multiDevices():
    device_counts = df.groupby('PreferredLoginDevice')['MultipleDevices'].sum().reset_index()
    fig = px.bar(device_counts, x='PreferredLoginDevice', y='MultipleDevices', title='Users with Multiple Devices')
    fig.write_html(output_folder)
    fig.show()
    return 0

# bar_catDevices: Creates a grouped bar graph showing the favourite shopping catagory per device group
def bar_catDevices():
    fig = px.bar(df, x='PreferredOrderCat', color='PreferredLoginDevice', barmode='group',
                 title='Favorite Shopping Category per Device Group')
    fig.write_html(output_folder)
    fig.show()
    return 0

# box_deviceTimes: Creates a box plot for timespent on app per device group
def bex_deviceTimes():
    fig = px.box(df, x='PreferredLoginDevice', y='Time_Spent', title='Time Spent on App per Device')
    fig.write_html(output_folder)
    fig.show()
    return 0

# box_deviceSatis: Creates a a bow plot for customer satisfaction per primary device catagory 
def box_deviceSatis():
    fig = px.box(df, x='PreferredLoginDevice', y='Customer_Satisfaction',
                 title='Customer Satisfaction per Device Category')
    fig.write_html(output_folder)
    fig.show()
    return 0

'''
INVESTIGATION POiNT TWO: PREFERED PAYMENT AND IMPACT ON CUSTOMER EXPERIENCE
'''

# pie_payment: Create a pie chart of preferd payment methods amoung customers
def pie_payment():
    fig = px.pie(df, names='PreferredPaymentMode', title='Preferred Payment Methods')
    fig.write_html(output_folder)
    fig.show()
    return 0

# box_payCoupon: Creates a boxplot for each prefered paynent method their coupon usage
def box_payCoupon():
    fig = px.box(df, x='PreferredPaymentMode', y='Coupon_Usage', title='Coupon Usage per Payment Method')
    fig.write_html(output_folder)
    fig.show()
    return 0

# bar_complainPay: Create a bar graph of complaints per each prefered payment method
def bar_payCoupon():
    fig = px.bar(df, x='PreferredPaymentMode', y='Complaints', title='Complaints per Payment Method')
    fig.write_html(output_folder)
    fig.show()
    return 0

# pie_payChurn: Creates pie charts per each Amount of Churn Flags per payment method
def pie_payChurn():
    fig = px.pie(df, names='PreferredPaymentMode', values='ChurnFlags',
                 title='Churn Flags per Payment Method')
    fig.write_html(output_folder)
    fig.show()
    return 0

# box_payOrder: Creates a box plot for each perfered card payment card to last order
def box_payOrder():
    fig = px.box(df, x='PreferredPaymentMode', y='Days_Since_Last_Order',
                 title='Last Order per Preferred Payment Method')
    fig.write_html(output_folder)
    fig.show()
    return 0

'''
INVESTIGATION POINT 3: SHOPPING CATAGORY IMPACT ON CUSTOMER
'''
# box_catTime: Creates a box plot for each prefered shopping catagory and the hours spent on the app
def box_catTime():
    fig = px.box(df, x='PreferredOrderCat', y='Time_Spent',
                 title='Time Spent on App per Shopping Category')
    fig.write_html(output_folder)
    fig.show()
    return 0

# bar_catCoupon(): Creates a bar graph for each shopping catagory and the amount of coupons customers have used
def bar_catCoupon():
    fig = px.bar(df, x='PreferredOrderCat', y='Coupon_Usage', title='Coupon Usage per Shopping Category')
    fig.write_html(output_folder)
    fig.show()
    return 0

# bar_catSatis(): Creates a bow plot for each shopping catagory and the customer satisfaction
def bar_catSatis():
    fig = px.box(df, x='PreferredOrderCat', y='Customer_Satisfaction',
                 title='Customer Satisfaction per Shopping Category')
    fig.write_html(output_folder)
    fig.show()
    return 0