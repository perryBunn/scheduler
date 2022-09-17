# Class: Floor

## Description

A `Floor` will describe the shift requirements for a certain unit. This will give the number of beds open, the nurses and techs allowed at one time, the number of IMC beds, and number of required charge nurses at one time.

## Attribute Table

| Name            | Type | Default | Choice | Description                                                  |
| --------------- | ---- | ------- | ------ | ------------------------------------------------------------ |
| name            | Str  | None    | None   | Name of the floor to be scheduled                            |
| required_nurses | Int  | None    | None   | Number of nurses needed on the floor. This includes charge.  |
| required_techs  | Int  | None    | None   | Number of techs needed on the floor                          |
| required_charge | Int  | 1       | None   | Number of charge nurses needed on the floor.                 |
| beds            | Int  | None    | None   | Number of beds on the unit. This includes IMC beds.          |
| imc_beds        | Int  | None    | None   | Number of IMC beds on the unit.                              |
| imc_ratio       | Int  | 3       | None   | Number of IMC patients that an IMC Nurse can have at the same time. |
| nurse_ratio     | Int  | 4       | None   | Number of patients that a Nurse can have at the same time.   |
| tech_ratio      | Int  | 8       | None   | Number of patients that a Tech can have a the same time.     |

## Attributes

### Names

### Required Nurses

### Required Techs

### Required Charge Nurses

### Beds

#### IMC Beds

### Ratios

#### Nurse Ratio

#### Tech Ratio

#### IMC Ratio



