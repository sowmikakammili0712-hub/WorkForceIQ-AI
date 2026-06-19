# Fact_Tickets

## Description

The Fact_Tickets table stores every support ticket created within CloudNova's customer support ecosystem.

Each row represents one unique support ticket and is the central fact table used for operational reporting, workforce planning, SLA monitoring and executive analytics.

---

## Grain

One Row = One Support Ticket

---

## Business Purpose

Supports analysis of

- Ticket Volume
- SLA Performance
- Resolution Time
- Analyst Productivity
- Capacity Planning
- Workforce Forecasting

---

## Primary Key

TicketID

---

## Foreign Keys

CreatedDateKey

ResolvedDateKey

AgentID

RegionID

PriorityID

CategoryID

CustomerID

TeamID

---

## Columns

| Column | Data Type | Description |
|-------------------------|------------|-------------------------------|
| TicketID | VARCHAR | Unique Ticket Identifier |
| CreatedDateKey | INT | Ticket Creation Date |
| ResolvedDateKey | INT | Ticket Resolution Date |
| AgentID | VARCHAR | Assigned Agent |
| TeamID | VARCHAR | Support Team |
| RegionID | VARCHAR | Customer Region |
| CategoryID | VARCHAR | Ticket Category |
| PriorityID | VARCHAR | Ticket Priority |
| CustomerID | VARCHAR | Customer Type |
| ResolutionMinutes | INT | Resolution Time |
| SLA_Target | INT | SLA Target Minutes |
| SLA_Met | BOOLEAN | SLA Compliance |
| Queue | VARCHAR | Support Queue |
| Status | VARCHAR | Ticket Status |

---

## Business Rules

Critical Tickets

SLA = 30 Minutes

High Priority

SLA = 120 Minutes

Medium Priority

SLA = 480 Minutes

Low Priority

SLA = 1440 Minutes

---

## Expected Record Count

Prototype

1,000

Production

200,000+

