set client_encoding = 'UTF8';


CREATE TABLE tasks (
    id UUID PRIMARY KEY,
    title varchar(128) NOT NULL,
    content TEXT,
    status INT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);