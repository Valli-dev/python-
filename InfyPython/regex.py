# from curses.ascii import isdigit
import re
# from sys import flags

# s="Good morning8"
# for i in range(len(s)):
#     if isdigit(s[0]):
#         print("Its a number")
#     else:
#         print("It is a string")
#         break
    
# print("I'm aditya")
# print(r'\ttab')

# search_text ='''
# PART I

# ITEM 1. BUSINESS

# Overview

#  ugh our website and retail locations. We also continue to grow our customer-facing infrastructure through a global network of vehicle service centers, Mobile Service technicians, body shops, Supercharger stations and Destination Chargers to accelerate the widespread adoption of our products. We emphasize performance, attractive styling and the safety of our users and er companies. 
# ITEM 2. We emphasize performance 
# Segment Information
# ITEM 3. overview  
# We operate as two reportable segments: (i) automotive and (ii) energy generation and storage.
# '''

# text= ''' the gross cost FY2021 Q1 was $4.85 billion
# fy2022 Q2 was $3 billion. 
# '''

# pattern1=' \(\d{3}\)\-(\d{3})\-(\d{4})|(\d{10})'
# pattern2='ITEM \d. ([^\n]*)'
# pattern3='FY(\d{4} Q[1-4])'
# pattern4='\$([0-9\.]+)'
# pattern5='FY(\d{4} Q[1-4])[^\$]+\$([0-9\.]+)'
# match= re.findall(pattern5,text, flags=re.IGNORECASE)
# matches=re.search(pattern5, text, flags=re.IGNORECASE)
# print(matches.groups())
# print(match)
# #print(matches)
text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern1 = 'https\:\/\/twitter\.com\/([a-zA-Z0-9_]+)' # todo: type your regex here

match=re.findall(pattern1, text)
print(match)
s="Go0od9morn_ing"
pattern3='([0-9]+)'
f=re.findall(pattern3,s)
print(f)

text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''
pattern6= 'Concentration of Risk\:([^\n]*)'

print(re.findall(pattern6, text))


text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''

pattern7 = 'FY(\d{4} (?:Q[1-4]|S[1-2]))'
matches = re.findall(pattern7, text)
print(matches)


