drop table if exists purchases;
drop table if exists usernames;
create table purchases(
    username text,
    item text,
    price number,
    entrydate date
);

create table usernames(
    username text
);
