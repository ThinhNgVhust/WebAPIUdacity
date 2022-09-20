DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

create table user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT unique not null,
    password TEXT unique not null
);

create table post(
    id integer primary key AUTOINCREMENT,
    author_id integer not null,
    created timestamp not null default CURRENT_TIMESTAMP,
    title text not null,
    body text not null,
    FOREIGN key (author_id) references user (id) 
);