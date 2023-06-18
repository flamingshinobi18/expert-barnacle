
from sklearn import preprocessing 
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os
from dbfile import mycursor,save_data

#Edit Section

about_model = '''What Is Online Banking?
Online banking allows a user to conduct financial transactions via the Internet. Online banking is also known as Internet banking or web banking.
Online banking offers customers almost every service traditionally available through a local branch including deposits, transfers, and online bill payments.
 Virtually every banking institution has some form of online banking, available both on desktop versions and through mobile apps.'''

cluster1_table ={"SerialNum":[1,2,3,4],"Type of Loan":["Educational Loan","Agrriculture/farmer","Health insurance","Two wheeler loan"],"Description":[
'''1.The scheme envisages loans up to Rs.7.5 lakh for studies in India and up to Rs. 15 lakh for studies abroad.
2.For loans up to Rs. 4 lakh no collateral or margin is required and the interest rate is not to exceed the Prime Lending Rates (PLR).
 For loans above Rs. 4 lakh the interest rate will not exceed PLR plus 1 percent.
3.The loans are to be repaid over a period of 5 to 7 years with provision of grace period of one year after completion of studies''',
'''Provides access to institutional finance to unfunded micro / small business units by extending loans upto Rs.10 lakh for 
manufacturing, processing, trading, services and activities allied to agriculture
''','''The RSBY health insurance scheme is primarily aimed at the people Below the Poverty Line, especially those in the unorganised sector.
 The scheme covers the workers and their families with coverage of up to Rs. 30,000 per family per annum''',
 '''Scheme: SBI TWO-WHEELER LOAN SCHEME
Purpose: Finance for purchase of new Two-wheeler
viz. scooter/motorcycle/ moped/battery operated/electric vehicles of reputed make (Registration with RTO is mandatory)
Loan to Value of vehicle: 85% of On-Road Price of vehicle
Age Criteria: 21-57 years
Minimum Income Criteria: Net Monthly Income Rs. 12,500/- (i.e., Rs. 1,50,000/- Net Annual Income)
 '''
    ],"EMI":[1,2,3,4]}
    
cluster2_table = {"SerialNum":[1,2,3,4],"Type of Loan":['Educational Loan', 'Car Loan', 'Gold Loan', 'Personal Loan'],"Description":['HDFC Bank grants education loans to study in India and abroad. The maximum loan amount for studying in India is limited to Rs. 20 Lakhs.Whereas, all the cost of education is covered under the loan for foreign education, with no upper limit. But you need to provide collateral in the form of a fixed deposit or immovable property to the bank.', 
                    'Axis Bank offers Car Loans at an attractive rate of interest, low processing fee, a repayment tenure of upto 7 years, and higher loan-to-value ratio  to purchase a new car, The Car Loan is offered even to proprietorship firms, partnership firms, companies, trusts and societies.To make the loan repayment comfortable, you have EMI option available', 
                    'The HDFC Bank Gold Loan is your definitive solution to meet your imperative financial needs. Whatever your reason may be, education, buisness expansion, personal requirment, or any other special end-use, our Loan against Gold is all you need.',
                    'Personal loans from Bank of Baroda offer a quick and easy solution to all your urgent financial needs and have many advantages over other forms of credit, such as credit cards & informal loans from friends, family members or untrustworthy financiers.'],"EMI":['Loan amount 5L for 4 years on a given ROI, monthly EMI will be 12,616', 'Loan amount 10L on a tenure of 7 years with given ROI, monthly EMI will be 15,304', 'You will have to pay ₹18,661 as interest every month & a lump sum amount of ₹20,35,834 at the end of the tenure.', 'Loan amount 5L on given intrest rate on tenure of 48 months, monthly EMI will be 12,780'],
                    'ROI': ['Education Loan for Indian Education is 9.25% to 13.68% & Education Loan for Abroad Education is 9.25% to 13.68', '9.3%', '11%', '9.60%']}
    
# cluster3_table = {"SerialNum":[1,2,3,4],"Type of Loan":[],"Description":[],"EMI":[]}
cluster3_table = {"SerialNum":[1,2,3,4],"Type of Loan":["Debt consolidation","Line of credit","Credit-builder loans","Umbrella Insurance"],"Description":[
        '''
        Debt consolidation is when you take out a new loan to repay multiple loans, simplifying your repayment and potentially reducing the 
        overall cost of your loan. While it's a helpful tool for some, only two types of debt can be consolidated: credit card, and 
        high-interest personal loan debt.
        ''',
        '''
        You can get a line of credit from your bank or credit union. You can even get secured credit, such as a home equity line of credit.
        ''',
        r'''
        Credit-builder loans are small, short-term loans that are taken out to help you build credit. Instead of receiving the loan funds up 
front as you would on a traditional loan, you make fixed monthly payments and receive the money back at the end of the loan term. 
Credit-builder loans typically range between $300 to $3,000 and charge annual percentage rates (APRs) between 6% and 16%.
        ''',
        '''
        Umbrella insurance is an extra type of insurance policy that people can buy on top of other protection, such as auto insurance and 
homeowners insurance. Specifically, it provides added liability insurance protection that goes above and beyond the limits on existing 
coverage. For example, say a driver had a car insurance policy that included $100,000 of liability coverage. If the driver got into an 
accident and caused $200,000 in damage, the auto insurance would pay the first $100,000 in losses to victims and umbrella insurance 
would cover the difference.
        '''
    ],"EMI":[]}

##############

filename = 'final_model.sav'
loaded_model = pickle.load(open('C:\\MarketSegmentation\\pages\\'+ filename, 'rb'))
df = pd.read_csv('C:\\MarketSegmentation\\pages\\'+ "Clustered_Customer_Data.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)
header_style = '''
    <style>
        th{
            background-color: antiquewhite;
        }
    </style>

'''
st.markdown(header_style, unsafe_allow_html=True)
st.warning(about_model, icon=None)
st.title("Prediction")

with st.form("my_form"):
    name = st.text_input(label='Name')
    address = st.text_input(label = 'Address')
    contactnum = st.number_input(label ='Contact Number')	

    balance=st.number_input(label='Balance',step=0.001,format="%.6f")
    balance_frequency=st.number_input(label='Balance Frequency',step=0.001,format="%.6f")
    purchases=st.number_input(label='Purchases',step=0.01,format="%.2f")
    oneoff_purchases=st.number_input(label='OneOff_Purchases',step=0.01,format="%.2f")
    installments_purchases=st.number_input(label='Installments Purchases',step=0.01,format="%.2f")
    cash_advance=st.number_input(label='Cash Advance',step=0.01,format="%.6f")
    purchases_frequency=st.number_input(label='Purchases Frequency',step=0.01,format="%.6f")
    oneoff_purchases_frequency=st.number_input(label='OneOff Purchases Frequency',step=0.1,format="%.6f")
    purchases_installment_frequency=st.number_input(label='Purchases Installments Freqency',step=0.1,format="%.6f")
    cash_advance_frequency=st.number_input(label='Cash Advance Frequency',step=0.1,format="%.6f")
    cash_advance_trx=st.number_input(label='Cash Advance Trx',step=1)
    purchases_trx=st.number_input(label='Purchases TRX',step=1)
    credit_limit=st.number_input(label='Credit Limit',step=0.1,format="%.1f")
    payments=st.number_input(label='Payments',step=0.01,format="%.6f")
    minimum_payments=st.number_input(label='Minimum Payments',step=0.01,format="%.6f")
    prc_full_payment=st.number_input(label='PRC Full Payment',step=0.01,format="%.6f")
    tenure=st.number_input(label='Tenure',step=1)

    data=[[balance,balance_frequency,purchases,oneoff_purchases,installments_purchases,cash_advance,purchases_frequency,oneoff_purchases_frequency,purchases_installment_frequency,cash_advance_frequency,cash_advance_trx,purchases_trx,credit_limit,payments,minimum_payments,prc_full_payment,tenure]]
    submitted = st.form_submit_button("Submit")


if submitted:
    names = ['Emerging Wealth','Mass Affluent','High Net Worth','Ultra High Net Worth']
    clust=loaded_model.predict(data)[0]
    if name != "":
        save_data(str(name) ,str(address),int(contactnum),0,int(clust))
    print('Data Belongs to Cluster',names[clust])
    typ ={0:cluster1_table,1:cluster2_table,2:cluster3_table}    
    st.write('Data Belongs to Cluster',clust ,' Category : ',names[clust])
    if clust == 3:
        st.write('''Dear valued customer,
We hope this message finds you well. We would like to extend an invitation to schedule a meeting with our bank authorities. Our team would be honored to discuss our exclusive banking services that cater to high net worth individuals like yourself. Please let us know if you are interested in scheduling a meeting at your earliest convenience.
Best regards,
XYZ Bank''')
    else:
        st.table(typ[clust])
    cluster_df1=df[df['Cluster']==clust]
    plt.rcParams["figure.figsize"] = (20,3)
    for c in cluster_df1.drop(['Cluster'],axis=1):
        fig, ax = plt.subplots()
        grid= sns.FacetGrid(cluster_df1, col='Cluster')
        grid= grid.map(plt.hist, c)
        plt.show()
        st.pyplot()


