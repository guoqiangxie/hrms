INSERT INTO auth_group VALUES (1,'info');
INSERT INTO auth_group VALUES (2,'manager');
INSERT INTO auth_group VALUES (3,'director');
INSERT INTO auth_group VALUES (4,'hr_audit');

INSERT INTO auth_group_permissions VALUES (1,2,22);
INSERT INTO auth_group_permissions VALUES (2,3,34);
INSERT INTO auth_group_permissions VALUES (3,3,22);
INSERT INTO auth_group_permissions VALUES (4,4,35);

INSERT INTO auth_user VALUES (1,'admin','','','admin@jinjiang.com','pbkdf2_sha256$10000$fuRYblDfRppO$5ob9PtuK/3K5VOFefeJxjRxCH3ZzejMhQnW5PkCp2Fw=',1,1,1,'2012-09-11 19:41:17','2012-09-11 19:40:49');
INSERT INTO auth_user VALUES (2,'xgq','','','','pbkdf2_sha256$10000$RhKXm9knvRFk$4iKvLUn8ai1gAE/0qMQ/tHOd9P+at8BLpuHjd7kaOjE=',0,1,0,'2012-09-11 19:52:59','2012-09-11 19:52:59');
INSERT INTO auth_user VALUES (3,'xhx','','','','pbkdf2_sha256$10000$vB0hVxrOWuAl$M4dGnrLg5ZmrTNtviM2IMX1uj8IIZ6q2dEFw/HMfwPE=',0,1,0,'2012-09-11 19:53:11','2012-09-11 19:53:11');
INSERT INTO auth_user VALUES (4,'wj','','','','pbkdf2_sha256$10000$2WpZRB4nCpRt$0E9bQhz4GpP4fDw7L3NHRoBbxECivrsmFCemfpZVvk0=',0,1,0,'2012-09-11 19:53:22','2012-09-11 19:53:22');
INSERT INTO auth_user VALUES (5,'cq','','','','pbkdf2_sha256$10000$iiDf261npUDk$ObXQJj4euz2CalEOJg6fFcIW68K3O2IW+26jK3n/8lk=',0,1,0,'2012-09-11 19:59:50','2012-09-11 19:59:50');

INSERT INTO auth_user_groups VALUES (1,5,4);
INSERT INTO auth_user_groups VALUES (2,4,3);
INSERT INTO auth_user_groups VALUES (3,2,1);
INSERT INTO auth_user_groups VALUES (4,3,2);