# Practical 6 - COCOMO Cost Estimation

## Problem Statement

### Silent Emergency Network

Silent Emergency Network is an emergency response system that allows a user to discreetly send an emergency alert to predefined emergency contacts or authorities along with relevant information such as location, time, and emergency type.

## Objective

To estimate the software development effort and development time for the Silent Emergency Network using the Basic COCOMO model.

## COCOMO Model

The Basic COCOMO model is used for cost estimation.

### Effort

Effort = a × (KLOC)^b

### Development Time

Development Time = c × (Effort)^d

### Average Staff

Average Staff = Effort / Development Time

## Project Modes

The program supports:

1. Organic
2. Semi-Detached
3. Embedded

## Programming Language

Python

## File

`cocomo.py` - Contains the COCOMO cost estimation program.

## Output

The program calculates:

- KLOC
- Effort in Person-Months
- Development Time in Months
- Average Staff Required
