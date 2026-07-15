# 📊 Enterprise Data Model

## Overview

The WorkForceIQ AI solution is built using a **Star Schema** dimensional model optimized for enterprise reporting, interactive analytics, and high-performance DAX calculations.

The model separates transactional data from descriptive attributes, enabling scalable reporting and reusable business logic across multiple dashboards.

---

# Data Model Objectives

The data model was designed to:

- Improve report performance
- Simplify DAX calculations
- Support reusable KPIs
- Enable interactive filtering
- Reduce data redundancy
- Support future scalability

---

# Model Architecture

The solution follows a Star Schema consisting of:

- 1 Fact Table
- 4 Dimension Tables

![Star Schema](ArchitectureAssets/StarSchema.png)

---

# Fact Table

## tickets

The Fact_Tickets table stores all ticket-level transactional information.

### Grain

One row represents one customer support ticket.

### Primary Key

- TicketID

### Key Metrics

- Resolution Hours
- Ticket Cost
- SLA Status
- Escalation Status
- Forecast Tickets
- Forecast Cost
- Capacity Metrics

---

# Dimension Tables

## dim_Date

Supports time intelligence and trend analysis.

### Key

Date

### Attributes

- Year
- Quarter
- Month
- Month Name
- Day

---

## dim_Agent

Contains workforce information.

### Key

AgentID

### Attributes

- Agent Name
- Team
- Experience Level
- Capacity Hours
- Utilization Target

---

## dim_Queue

Contains operational queues.

### Key

QueueID

### Attributes

- Hosting
- Billing
- Customer Support
- Website Builder
- Technical Support
- Domain Management

---

## dim_Region

Contains customer geography.

### Key

RegionID

### Attributes

- Australia
- Canada
- Germany
- India
- UK
- USA

---

# Relationship Design

All dimension tables connect directly to the Fact_Tickets table using **one-to-many relationships**.

Relationship characteristics:

- Cardinality: One-to-Many
- Cross Filter Direction: Single
- Active Relationships: Yes

This design eliminates ambiguity while maximizing query performance.

---

# Filter Flow

dim_Date

↓

tickets

↑

dim_Agent

↑

dim_Queue

↑

dim_Region

---

# Why Star Schema?

The dimensional model offers several advantages:

- Faster query execution
- Optimized DAX performance
- Simpler report development
- Easier maintenance
- Better scalability
- Enterprise BI best practices

---

# Power BI Modeling Best Practices

The project follows Microsoft-recommended modeling standards:

- Separate Fact and Dimension tables
- Use surrogate keys
- Avoid many-to-many relationships
- Single-direction filtering
- Reusable DAX measures
- Optimized relationships

---

# Scalability

The current model supports:

- Executive Reporting
- Workforce Analytics
- SLA Monitoring
- Forecasting
- Capacity Planning
- AI Recommendation Engine

The architecture can easily be extended by adding new dimensions (e.g., Customer, Product, Channel) without redesigning the model.

---

# Future Enhancements

Planned improvements include:

- Azure SQL Database
- Incremental Refresh
- Microsoft Fabric Lakehouse
- Direct Lake Mode
- Real-Time Streaming
- Row-Level Security (RLS)

---

# Summary

The WorkForceIQ AI data model provides a scalable and efficient analytical foundation that enables interactive reporting, advanced DAX calculations, forecasting, and executive decision support.

---

**Project:** WorkForceIQ AI

**Version:** 1.0

**Author:** Sowmika Kammili
