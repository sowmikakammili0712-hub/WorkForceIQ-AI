import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

print("===================================")
print("WorkForceIQ AI")
print("Enterprise Data Generator")
print("Version 0.1")
print("===================================")

fake = Faker()

random.seed(42)
np.random.seed(42)

print("Libraries Loaded Successfully!")

agents = []

teams = ["Tier1", "Tier2", "Tier3"]

regions = [
    "North America",
    "Europe",
    "APAC"
]

experience_levels = [
    "Junior",
    "Mid",
    "Senior"
]

categories = [
    "Login Issue",
    "Billing",
    "Domain Management",
    "Hosting",
    "Website Builder",
    "Email Support"
]

priorities = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

statuses = [
    "Resolved",
    "Resolved",
    "Resolved",
    "Resolved",
    "Open"
]
queues = [
    "Customer Support",
    "Billing Support",
    "Technical Support",
    "Domain Support",
    "Hosting Support"
]

tiers = [
    "Tier1",
    "Tier2",
    "Tier3"
]
for i in range(100):

    agent = {
        "AgentID": f"AG{str(i+1).zfill(3)}",
        "AgentName": fake.name(),
        "Team": random.choice(teams),
        "Region": random.choice(regions),
        "ExperienceLevel": random.choice(experience_levels),
        "HireDate": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    }

    agents.append(agent)

agents_df = pd.DataFrame(agents)
tickets=[]
for i in range(1000):
 
    created_date = fake.date_between(
     start_date="-180d",
     end_date="today"
)
    resolution_hours = round(
      random.uniform(1,48),
      2
)
    closed_date = (
     datetime.combine(
        created_date,
        datetime.min.time()
     )
     +
     timedelta(hours=resolution_hours)
)
    ticket = {

        "TicketID": f"TKT{str(i+1).zfill(5)}",

        "Category": random.choice(categories),

        "Priority": random.choice(priorities),

        "AssignedAgent":
            random.choice(
                agents_df["AgentID"].tolist()
            ),

        "ResolutionHours":resolution_hours,

        "SLAHours":
            random.choice(
                [4,8,12,24]
            ),
            

        "Status":
            random.choice(statuses),
    
     "CreatedDate":created_date,


    "ClosedDate": 
    closed_date.date(),

     "Queue":
    random.choice(queues),

    "Tier":
    random.choice(tiers),

"EscalatedFlag":
    random.choice(
        [True, False]
    ),   

    }
    ticket["BacklogAge"] = (
    datetime.today().date()
    -
    ticket["CreatedDate"]
).days    
    ticket["SLAMet"] = (
    ticket["ResolutionHours"]
        <=
    ticket["SLAHours"]
    )
    tickets.append(ticket)

tickets_df = pd.DataFrame(tickets)

print("\nSample Data:")
print(agents_df.head())

print("\nTotal Agents Created:")
print(len(agents_df))

agents_df.to_csv(
    "02_Dataset/Sample/agents.csv",
    index=False
)

print("\nCSV Export Successful!")

tickets_df.to_csv(
    "02_Dataset/Sample/tickets.csv",
    index=False
)

print("\nTickets Export Successful!")
print("\nTicket Sample:")
print(tickets_df.head())

print("\nTotal Tickets:")
print(len(tickets_df))