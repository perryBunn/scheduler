# Class: Person

## Description

This class encapsulates the information necessary to describe the persons work time.  A Person is a `Nurse` or a `Tech`. 

## Attribute Table

| Attribute Name | Type | Default | Choices                   | Description                                                  |
| -------------- | ---- | ------- | ------------------------- | ------------------------------------------------------------ |
| Type           | Str  | None    | `Nurse`, `Tech`           | The type of person                                           |
| Name           | Str  | None    | None                      | Name of the person                                           |
| Shift          | Str  | Hybrid  | `Day`, `Night` , `Hybrid` | Shift type of the person                                     |
| Holidays       | Dict | None    | [Holidays](#holidays)     | Dictionary of which holidays that the person has off         |
| Hours          | Int  | 40      | None                      | Number of hours that the person will work in a week. This is a floor. Often the hours will not be met exactly unless the `hours` is dividable by 12. |
| shift_length   | Int  | None    | None                      | This attribute is Dependant on the type of person            |
|                |      |         |                           |                                                              |
|                |      |         |                           |                                                              |
|                |      |         |                           |                                                              |

###  Name

### Shift

### Holidays

### Hours

