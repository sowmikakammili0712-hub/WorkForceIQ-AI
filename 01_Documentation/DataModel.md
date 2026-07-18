# Enterprise Data Model

## Overview

WorkForceIQ AI follows a Star Schema data model optimized for analytical reporting, dashboard performance, and simplified DAX calculations.

The model separates transactional data from descriptive attributes, enabling efficient filtering, aggregation, and business intelligence reporting.

---

# Star Schema

![Star Schema](ArchitectureAssets/StarSchema.png)
---

# Why Star Schema?

A Star Schema was selected over a Snowflake Schema for the following reasons:

| Star Schema | Benefit |
|-------------|----------|
| Fewer joins | Faster dashboard performance |
| Simpler relationships | Easier report development |
| Better DAX performance | Optimized calculations |
| User-friendly model | Easier for analysts to understand |

Given the analytical nature of WorkForceIQ AI, the Star Schema provides the best balance between performance, maintainability, and scalability.

---

# Model Overview

The data model consists of:

- 1 Fact Table
- 4 Dimension Tables
- One-to-Many Relationships
- Single Direction Filtering

This design follows Microsoft Power BI best practices for enterprise reporting.

---

# Fact Table

## Fact_Tickets

The Fact_Tickets table stores transactional operational data generated from enterprise support activities.

Each row represents a single customer support ticket.

### Key Attributes

- Ticket ID
- Agent ID
- Queue ID
- Region ID
- Date ID
- Priority
- Status
- Resolution Hours
- SLA Hours
- Escalation Flag
- Cost Per Ticket

The fact table is used for:

- SLA reporting
- Resolution analytics
- Cost analysis
- Capacity planning
- Forecasting
- AI recommendations

---

# Dimension Tables

## Dim_Agent

Stores workforce information.

Attributes include:

- Agent ID
- Agent Name
- Team
- Experience Level
- Department

Used for:

- Agent Performance
- Utilization Analysis
- Workforce Planning

---

## Dim_Date

Provides calendar intelligence.

Includes:

- Date
- Month
- Quarter
- Year
- Week
- Day Name

Used for:

- Trend Analysis
- Time Intelligence
- Forecasting

---

## Dim_Queue

Stores operational queue information.

Examples:

- Technical Support
- Billing
- Customer Success
- Escalations

Used for:

- Queue Performance
- Backlog Monitoring
- Capacity Analysis

---

## Dim_Region

Stores geographical information.

Examples:

- North America
- Europe
- Asia-Pacific

Used for:

- Regional Reporting
- Operational Comparison
- Executive Insights

---

# Relationship Design

All relationships follow:

Dimension

↓

Fact

One-to-Many

↓

Single Direction Filter

This minimizes ambiguity and improves query performance.

---

# Cardinality

| Relationship | Cardinality |
|--------------|-------------|
| Agent → Tickets | One-to-Many |
| Date → Tickets | One-to-Many |
| Queue → Tickets | One-to-Many |
| Region → Tickets | One-to-Many |

---

# Data Grain

The grain of the fact table is:

> **One record represents one customer support ticket.**

Maintaining a consistent grain simplifies DAX calculations and prevents double counting.

---

# Benefits of Star Schema

The selected model provides several advantages:

- Faster report performance
- Simplified DAX measures
- Reduced model complexity
- Better scalability
- Easier maintenance
- Improved filter propagation

---

# Business Use Cases

The model supports enterprise analytics scenarios including:

- Executive reporting
- Workforce utilization
- SLA monitoring
- Backlog management
- Capacity forecasting
- AI-assisted recommendations
- Governance analytics

---

# Best Practices Followed

- Star Schema modeling
- One-to-Many relationships
- Single Direction filtering
- Separate Dimension and Fact tables
- Surrogate Keys
- Optimized DAX calculations
- Enterprise naming conventions

---

# Future Enhancements

Future versions of the model may include:

- Fact Workforce Capacity
- Fact Forecast
- Fact Staffing Plan
- Dim Customer
- Dim Product
- Slowly Changing Dimensions (SCD)
- Incremental Refresh
- Microsoft Fabric Lakehouse integration