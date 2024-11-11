## Structs

### Task

| key | type | etc |
| --- | --- | --- |
| id | uuid | PK and v4|
| title | string | |
| content | string | |
| status | int | ref Status(Enum) |
| cretaed_at | datetime| |
| updated_at | datetime| |

### Status(Enum)

{TODO: 0, DOING: 1, DONE: 2}