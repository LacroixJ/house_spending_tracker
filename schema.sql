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
insert into usernames values('James');
insert into usernames values('Taryn');
insert into usernames values('Connor');

insert into purchases values('James', 'Toilet Paper', 8.99, '2022-09-24');
insert into purchases values('Taryn', 'Toilet Paper', 8.99, '2022-09-24');
insert into purchases values('Connor', 'Toilet Paper', 8.99, '2022-09-24');
insert into purchases values('James', 'Toilet Paper', 3.99, '2022-09-23');
insert into purchases values('James', 'Toilet Paper', 1.99, '2019-09-23');
insert into purchases values('James', 'Toilet Paper', 8.99, '2029-01-01');
insert into purchases values('James', 'Toilet Paper', 8.99, '2010-11-01');
