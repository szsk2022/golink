create table if not exists `goto`
(
    `ID` int not null auto_increment comment 'id' primary key,
    `url` varchar(256) not null,
    `user` varchar(256) not null,
    `status` int not null comment 'status'
) comment '`goto`';