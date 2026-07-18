# Relationship Diagram

## Overview

The WorkForceIQ AI semantic model is built using a Star Schema, where a central fact table is connected to multiple dimension tables through one-to-many relationships.

This design minimizes model complexity, improves query performance, and supports scalable analytical reporting in Power BI.

---

# Relationship Diagram

![Star Schema](ArchitectureAssets/StarSchema.png)

---

# Model Relationships

| Parent Table | Child Table | Relationship | Filter Direction |
|--------------|-------------|--------------|------------------|
| Dim_Agent | Fact_Tickets | One-to-Many | Single |
| Dim_Date | Fact_Tickets | One-to-Many | Single |
| Dim_Queue | Fact_Tickets | One-to-Many | Single |
| Dim_Region | Fact_Tickets | One-to-Many | Single |

---

# Relationship Structure

```text
                 Dim_Agent
                      │
                      │
Dim_Date ───── Fact_Tickets ───── Dim_Queue
                      │
                      │
                 Dim_Region
```

---

# Cardinality

All relationships follow a **One-to-Many** design.

**One**

One business entity exists in the dimension table.

Examples:

- One Agent
- One Region
- One Queue
- One Calendar Date

↓

**Many**

Multiple support tickets may reference the same business entity.

Examples:

- One Agent handles many tickets.
- One Queue contains many tickets.
- One Region generates many tickets.
- One Date contains many ticket transactions.

---

# Filter Direction

The model uses **Single Direction Filtering**.

Dimension

↓

Fact

This approach was selected because it:

- Prevents ambiguous relationships
- Improves report performance
- Simplifies DAX calculations
- Follows Microsoft Power BI best practices
- Reduces model complexity

---

# Why Star Schema?

A Star Schema was selected instead of a Snowflake Schema because it provides:

| Star Schema Benefit | Business Value |
|---------------------|----------------|
| Fewer table joins | Faster dashboard performance |
| Simpler relationships | Easier report development |
| Better DAX optimization | Improved calculation efficiency |
| Lower model complexity | Easier maintenance |
| Improved usability | Better experience for report developers |

The model is optimized for analytical workloads where query performance and usability are more important than storage normalization.

---

# Relationship Validation

The following validation rules are applied during model development:

- Every ticket must reference a valid agent.
- Every ticket must reference a valid queue.
- Every ticket must reference a valid region.
- Every ticket must reference a valid calendar date.
- Duplicate primary keys are not permitted in dimension tables.
- Foreign key integrity is maintained throughout the model.

---
# Relationship Design Decisions

| Design Decision | Rationale |
|-----------------|-----------|
| Star Schema | Optimized for analytical reporting and Power BI performance |
| Single Fact Table | Maintains a consistent transactional grain |
| Separate Dimension Tables | Reduces redundancy and improves maintainability |
| One-to-Many Relationships | Supports efficient filtering and aggregation |
| Single-Direction Filtering | Prevents ambiguity and improves query execution |
| Surrogate Keys | Simplifies joins and future model expansion |

# Business Impact

The relationship model enables:

- Executive KPI reporting
- Workforce performance analysis
- Queue-level reporting
- Regional comparisons
- Time intelligence
- Capacity planning
- Forecasting
- AI-assisted recommendations
- Trusted AI Governance

---

# Best Practices Followed

The semantic model follows enterprise Power BI modeling standards:

- Star Schema architecture
- One-to-Many relationships
- Single-direction filtering
- Descriptive dimensions
- Transactional fact table
- Reusable dimensions
- Optimized DAX model
- High-performance reporting

---

# Data Lineage

The relationship model forms the foundation of the enterprise analytics pipeline.

```text
Python Data Generator
        ↓
Synthetic CSV Dataset
        ↓
Power Query ETL
        ↓
Dimension Tables + Fact Table
        ↓
Relationship Model
        ↓
Power BI Semantic Model
        ↓
DAX Measures
        ↓
Enterprise Dashboards
        ↓
AI Recommendation Engine
        ↓
Trusted AI Governance Center
```

The semantic model ensures that every dashboard, KPI, and recommendation is built on a consistent, governed, and scalable data foundation.

---

# Key Takeaways

- The semantic model follows a Star Schema architecture.
- One-to-many relationships improve reporting performance and scalability.
- Single-direction filtering reduces ambiguity and simplifies DAX.
- The relationship model provides a robust foundation for analytics, AI recommendations, and governance.