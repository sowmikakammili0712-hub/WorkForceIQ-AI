# Dimension Tables

## Overview

Dimension tables provide descriptive attributes that add business context to transactional data stored in the fact table.

In WorkForceIQ AI, dimension tables enable users to filter, group, and analyze operational metrics across different business perspectives such as agents, dates, queues, and regions.

The solution follows a Star Schema design where each dimension table maintains a one-to-many relationship with the Fact_Tickets table.

---

# Dimension Overview

| Dimension | Business Purpose |
|-----------|------------------|
| Dim_Agent | Workforce and agent information |
| Dim_Date | Calendar and time intelligence |
| Dim_Queue | Operational queue categorization |
| Dim_Region | Geographic reporting and regional analysis |

---
> **Note**
>
> The relationship between the dimension tables and `Fact_Tickets` is illustrated in the **RelationshipDiagram.md** and **DataModel.md** documents. Together, these documents describe the logical and physical structure of the WorkForceIQ AI semantic model.

# Dim_Agent

## Purpose

Stores descriptive information about support agents.

### Primary Key

AgentID

### Key Attributes

| Column | Description |
|---------|-------------|
| AgentID | Unique identifier |
| AgentName | Support agent name |
| Team | Assigned operational team |
| ExperienceLevel | Junior, Mid, Senior |
| Department | Business unit |

### Business Use Cases

- Agent Performance Dashboard
- Workforce Utilization
- Capacity Planning
- Performance Comparison

---

# Dim_Date

## Purpose

Provides calendar intelligence for trend analysis and time-based reporting.

### Primary Key

DateID

### Key Attributes

| Column | Description |
|---------|-------------|
| DateID | Calendar date |
| Day | Day of month |
| Month | Month name |
| Quarter | Quarter |
| Year | Calendar year |
| Week | Week number |
| DayName | Weekday |

### Business Use Cases

- Daily Operations
- Monthly Reporting
- Quarterly Reviews
- Forecasting
- Trend Analysis

---

# Dim_Queue

## Purpose

Categorizes support tickets by operational queue.

### Primary Key

QueueID

### Key Attributes

| Column | Description |
|---------|-------------|
| QueueID | Queue identifier |
| QueueName | Queue name |
| Category | Queue classification |

### Business Use Cases

- Queue Performance
- Backlog Analysis
- Workload Distribution
- Staffing Allocation

---

# Dim_Region

## Purpose

Provides geographic context for operational reporting.

### Primary Key

RegionID

### Key Attributes

| Column | Description |
|---------|-------------|
| RegionID | Region identifier |
| RegionName | Geographic region |

### Business Use Cases

- Regional Performance
- SLA Comparison
- Executive Reporting
- Capacity Planning

---

# Relationship Summary

| Dimension | Relationship | Fact Table |
|-----------|--------------|------------|
| Dim_Agent | One-to-Many | Fact_Tickets |
| Dim_Date | One-to-Many | Fact_Tickets |
| Dim_Queue | One-to-Many | Fact_Tickets |
| Dim_Region | One-to-Many | Fact_Tickets |

All relationships use single-direction filtering from the dimension table to the fact table.

---

# Design Principles

The dimension tables follow enterprise data modeling best practices:

- Descriptive business attributes
- Stable primary keys
- One-to-many relationships
- Minimal redundancy
- Optimized filtering
- Reusable across dashboards

---

# Business Value

Dimension tables transform raw operational data into meaningful business insights by enabling users to analyze KPIs across multiple perspectives.

This design improves report usability, simplifies analytical queries, and supports scalable enterprise reporting.

---

# Data Lineage

The dimension tables are generated through the enterprise analytics pipeline shown below.

```text
Python Data Generator
        ↓
Synthetic CSV Dataset
        ↓
Power Query ETL
        ↓
Dimension Tables
        ↓
Star Schema
        ↓
Power BI Semantic Model
        ↓
Enterprise Dashboards
```

The dimensional model provides the business context required for KPI calculations, AI recommendations, and executive reporting.

---

# Key Takeaways

- Dimension tables provide descriptive business context.
- Each dimension maintains a one-to-many relationship with the Fact_Tickets table.
- The Star Schema design improves performance, scalability, and report usability.
- Well-structured dimensions simplify filtering, aggregation, and business analysis.
