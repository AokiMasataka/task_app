# usege

```sh
python -m venv env
./env/bin/pip install -r ./requierments.txt
./env/bin/python -m task_app
```

# API 仕様

## POST: /task

Task 作成

### Request

- *title: String
- *content: String
- *status: Int

### Response

- task_id: String[Uuid]

## GET: /task?status=<Int>

Task 一覧の取得

### Request

### Response

- tasks: [
    {
        title: String,
        content: String,
        id: Uuid,
        status: Int,
        created_at: Datetime,
        updated_at: Datetime
    }
]

## GET: /task/{task_id}

Task の取得

### Request

### Response

- title: String
- content: String
- id: Uuid
- status: Int
- created_at: Datetime
- updated_at: Datetime

## DELETE: /task/{task_id}

### Request

### Response

