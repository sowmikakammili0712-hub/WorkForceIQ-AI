# Fact Tables

## Overview

Fact tables store measurable business events that can be aggregated and analyzed.

In WorkForceIQ AI, the primary fact table captures customer support ticket transactions. It serves as the foundation for reporting, forecasting, AI recommendations, and executive dashboards.

---

# Fact Table

## Fact_Tickets

### Purpose

The Fact_Tickets table stores one record for every customer support ticket processed by the organization.

Each record represents a transactional event and contains the operational metrics required for workforce analytics.

---

# Table Grain

The grain of the table is:

> **One row represents one customer support ticket.**

Maintaining a single, consistent grain ensures accurate aggregation and prevents double counting during reporting.

---

# Primary Key

| Column | Description |
|---------|-------------|
| TicketID | Unique identifier for each support ticket |

---

# Foreign Keys

| Column | References |
|---------|------------|
| AgentID | Dim_Agent |
| QueueID | Dim_Queue |
| RegionID | Dim_Region |
| DateID | Dim_Date |

---

# Fact Table Attributes

| Column | Data Type | Description |
|---------|-----------|-------------|
| TicketID | Integer | Unique ticket identifier |
| AgentID | Integer | Assigned support agent |
| QueueID | Integer | Operational queue |
| RegionID | Integer | Customer region |
| DateID | Date | Ticket creation date |
| Priority | Text | Ticket priority |
| Status | Text | Current ticket status |
| ResolutionHours | Decimal | Resolution duration |
| SLAHours | Decimal | SLA target duration |
| EscalationFlag | Boolean | Indicates escalation |
| TicketCost | Decimal | Estimated operational cost |

---

# Measures Derived

The Fact_Tickets table supports the calculation of:

- Total Tickets
- SLA Compliance
- Resolution Time
- Escalation Rate
- Average Resolution Hours
- Operational Cost
- Backlog
- Forecast Capacity
- Executive Health Score

---

# Relationships

Fact_Tickets is connected to the following dimensions:

```
Dim_Agent
        │
Dim_Queue
        │
Dim_Date
        │
Dim_Region
        │
        ▼
   Fact_Tickets
```

---

# Business Scenarios

The table supports:

- Executive reporting
- Workforce analytics
- Queue performance
- Capacity planning
- Forecasting
- Cost analysis
- AI recommendation engine
- Trusted AI Governance

---

# Design Principles

The Fact_Tickets table follows enterprise data warehouse best practices:

- Atomic transaction storage
- Single business grain
- Foreign key relationships
- Minimal redundancy
- Optimized for aggregation
- Scalable design

---

# Data Quality Rules

The following validations are applied before data enters the analytical model:

- TicketID must be unique.
- AgentID must exist in Dim_Agent.
- QueueID must exist in Dim_Queue.
- RegionID must exist in Dim_Region.
- ResolutionHours cannot be negative.
- SLAHours must be greater than zero.
- EscalationFlag must contain valid Boolean values.

---

# Business Value

Fact_Tickets serves as the central analytical dataset powering all dashboards, KPIs, forecasts, and AI-assisted recommendations within WorkForceIQ AI.

---
---

# Data Lineage

The `Fact_Tickets` table is populated through the enterprise analytics pipeline shown below.

```text
Python Data Generator
        ↓
Synthetic CSV Dataset
        ↓
Power Query ETL
        ↓
Fact_Tickets
        ↓
DAX Measures
        ↓
Power BI Dashboards
        ↓
AI Recommendation Engine
        ↓
Trusted AI Governance Center
        ↓
Executive Decision Support
```

This end-to-end lineage ensures every KPI and AI-assisted recommendation can be traced back to its originating transaction, supporting transparency, auditability, and governance.

# Key Takeaways

- Fact_Tickets is the central transactional table in the solution.
- The table follows a single-ticket grain for accurate reporting.
- Foreign key relationships support a scalable Star Schema.
- Enterprise data quality checks ensure reliable analytics.
