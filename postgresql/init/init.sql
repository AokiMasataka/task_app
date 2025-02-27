set client_encoding = 'UTF8';


CREATE TABLE projects (
    id UUID PRIMARY KEY,
    title varchar(128) NOT NULL,
    description TEXT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);


CREATE TABLE tasks (
    id UUID PRIMARY KEY,
    project_id UUID REFERENCES projects (id) ON DELETE CASCADE,
    title varchar(128) NOT NULL,
    content TEXT,
    status INT NOT NULL,
    priority INT NOT NULL DEFAULT 0,
    duedate DATE,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);


CREATE TABLE docs (
    id UUID PRIMARY KEY,
    project_id UUID REFERENCES projects (id) ON DELETE CASCADE,
    title varchar(128) NOT NULL,
    content TEXT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);