# ⭐ Star Schema Relationship Diagram

## Overview

The WorkForceIQ AI data model follows a **Star Schema** architecture to optimize query performance, simplify report development, and support scalable analytics.

The model consists of one central fact table surrounded by multiple dimension tables.

This design minimizes redundancy, improves filter propagation, and enables reusable DAX calculations across all dashboards.

---

# Star Schema Diagram

![Star Schema](ArchitectureAssets/StarSchema.png)

---

# Data Model

The analytical model consists of:

## Fact Table

**Fact_Tickets**

Stores transactional ticket-level information including:

- Ticket ID
- Agent ID
- Queue ID
- Region ID
- Created Date
- Closed Date
- Resolution Hours
- SLA Status
- Escalation Status
- Ticket Cost
- Forecast Metrics

---

## Dimension Tables

### Dim_Date

Provides calendar intelligence.

Columns include:

- Date
- Month
- Quarter
- Year
- Month Name

---

### Dim_Agent

Contains workforce information.

Columns include:

- Agent ID
- Agent Name
- Team
- Experience Level
- Capacity
- Utilization

---

### Dim_Queue

Contains support queue information.

Examples include:

- Hosting
- Billing
- Customer Support
- Website Builder
- Technical Support
- Domain Management

---

### Dim_Region

Stores customer geography.

Examples:

- Australia
- Canada
- Germany
- India
- UK
- USA

---

# Relationship Design

The model uses:

- One-to-Many Relationships
- Single Direction Cross Filtering
- Dimension-to-Fact Filtering

This design improves report performance while preventing ambiguous filter paths.

---

# Relationship Flow

Dim_Date

↓

Fact_Tickets

↑

Dim_Agent

↑

Dim_Queue

↑

Dim_Region

---

# Why Star Schema?

The Star Schema provides several advantages:

- Faster DAX calculations
- Simplified report development
- Better model scalability
- Improved Power BI performance
- Reduced model complexity
- Easier maintenance

---

# Business Benefits

Using a dimensional model enables:

- Executive Reporting
- Workforce Analytics
- Forecasting
- Capacity Planning
- AI Recommendation Engine
- KPI Monitoring
- Cross-filtering across dashboards

---

# Best Practices Followed

✅ One Fact Table

✅ Separate Dimension Tables

✅ Surrogate Keys

✅ Optimized Relationships

✅ Reusable Measures

✅ Enterprise BI Modeling Standards

---

**Project:** WorkForceIQ AI

**Version:** 1.0
