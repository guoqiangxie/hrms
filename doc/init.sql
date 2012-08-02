/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2012-8-2 20:29:53                            */
/*==============================================================*/


drop table if exists applyrtrack;

drop table if exists employee;

drop table if exists employee_overtimeform_ref;

drop table if exists overtimeform;

/*==============================================================*/
/* Table: applyrtrack   申请流程                                        */
/*==============================================================*/
create table applyrtrack
(
   id                   integer(10) not null,
   overtimeform_id      integer(10),
   approval_id          integer(10),
   approval_note        varchar(255),
   apply_date           timestamp,
   type                 varchar(10),
   primary key (id)
);

/*==============================================================*/
/* Table: employee  员工表                                            */
/*==============================================================*/
create table employee
(
   id                   integer(10) not null,
   name                 varchar(20),
   email                varchar(40),
   telephone            varchar(20),
   level                varchar(10),
   bak                  varchar(30),
   primary key (id)
);

alter table employee comment '员工表';

/*==============================================================*/
/* Table: employee_overtimeform_ref  中间表                           */
/*==============================================================*/
create table employee_overtimeform_ref
(
   employee_id          integer(10) not null,
   overtimeform_id      integer(10) not null,
   primary key (employee_id, overtimeform_id)
);

/*==============================================================*/
/* Table: overtimeform                                          */
/*==============================================================*/
create table overtimeform
(
   id                   integer(10) not null,
   begintime            timestamp,
   endtime              timestamp,
   reason               varchar(255),
   comment              varchar(255),
   applyer_id           integer(10),
   status               varchar(5),
   primary key (id)
);

alter table overtimeform comment '申请表';

alter table applyrtrack add constraint FK_Reference_2 foreign key (approval_id)
      references employee (id) on delete restrict on update restrict;

alter table applyrtrack add constraint FK_apply_over_f foreign key (overtimeform_id)
      references overtimeform (id) on delete restrict on update restrict;

