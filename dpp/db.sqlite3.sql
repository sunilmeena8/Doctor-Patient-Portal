
CREATE TABLE IF NOT EXISTS "django_session" (
	session_key	varchar(40) NOT NULL,
	session_data	text NOT NULL,
	expire_date	datetime NOT NULL,
	PRIMARY KEY(session_key)
);
CREATE TABLE IF NOT EXISTS "portal_doctor" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"username"	varchar(40) NOT NULL,
	"email"	varchar(40) NOT NULL,
	"specialization"	varchar(40),
	"name"	varchar(40),
	"phone_number"	varchar(20),
	"address"	varchar(100),
	"user_id"	integer NOT NULL UNIQUE,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "portal_patient" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"username"	varchar(20) NOT NULL,
	"email"	varchar(40) NOT NULL,
	"name"	varchar(40),
	"phone_number"	varchar(20),
	"address"	varchar(100),
	"user_id"	integer NOT NULL UNIQUE,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "portal_person" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"username"	varchar(40) NOT NULL,
	"occupation"	varchar(20) NOT NULL,
	"email"	varchar(40) NOT NULL,
	"user_id"	integer NOT NULL UNIQUE,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "portal_freetimings" (
	"id"	integer NOT NULL,
	"did"	integer NOT NULL,
	"t0_1"	bool NOT NULL,
	"t1_2"	bool NOT NULL,
	"t2_3"	bool NOT NULL,
	"t3_4"	bool NOT NULL,
	"t4_5"	bool NOT NULL,
	"t5_6"	bool NOT NULL,
	"t6_7"	bool NOT NULL,
	"t7_8"	bool NOT NULL,
	"t8_9"	bool NOT NULL,
	"t9_10"	bool NOT NULL,
	"t10_11"	bool NOT NULL,
	"t11_12"	bool NOT NULL,
	"t12_13"	bool NOT NULL,
	"t13_14"	bool NOT NULL,
	"t14_15"	bool NOT NULL,
	"t15_16"	bool NOT NULL,
	"t16_17"	bool NOT NULL,
	"t17_18"	bool NOT NULL,
	"t18_19"	bool NOT NULL,
	"t19_20"	bool NOT NULL,
	"t20_21"	bool NOT NULL,
	"t21_22"	bool NOT NULL,
	"t22_23"	bool NOT NULL,
	"t23_24"	bool NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "portal_appointment" (
	"id"	integer NOT NULL,
	"did"	integer NOT NULL,
	"pid"	integer NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(150) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"first_name"	varchar(30) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"last_name"	varchar(150) NOT NULL
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag">=0),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL
);
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,1,'view_logentry','Can view log entry'),
 (5,2,'add_permission','Can add permission'),
 (6,2,'change_permission','Can change permission'),
 (7,2,'delete_permission','Can delete permission'),
 (8,2,'view_permission','Can view permission'),
 (9,3,'add_group','Can add group'),
 (10,3,'change_group','Can change group'),
 (11,3,'delete_group','Can delete group'),
 (12,3,'view_group','Can view group'),
 (13,4,'add_user','Can add user'),
 (14,4,'change_user','Can change user'),
 (15,4,'delete_user','Can delete user'),
 (16,4,'view_user','Can view user'),
 (17,5,'add_contenttype','Can add content type'),
 (18,5,'change_contenttype','Can change content type'),
 (19,5,'delete_contenttype','Can delete content type'),
 (20,5,'view_contenttype','Can view content type'),
 (21,6,'add_session','Can add session'),
 (22,6,'change_session','Can change session'),
 (23,6,'delete_session','Can delete session'),
 (24,6,'view_session','Can view session'),
 (25,7,'add_appointment','Can add appointment'),
 (26,7,'change_appointment','Can change appointment'),
 (27,7,'delete_appointment','Can delete appointment'),
 (28,7,'view_appointment','Can view appointment'),
 (29,8,'add_freetimings','Can add free timings'),
 (30,8,'change_freetimings','Can change free timings'),
 (31,8,'delete_freetimings','Can delete free timings'),
 (32,8,'view_freetimings','Can view free timings'),
 (33,9,'add_person','Can add person'),
 (34,9,'change_person','Can change person'),
 (35,9,'delete_person','Can delete person'),
 (36,9,'view_person','Can view person'),
 (37,10,'add_patient','Can add patient'),
 (38,10,'change_patient','Can change patient'),
 (39,10,'delete_patient','Can delete patient'),
 (40,10,'view_patient','Can view patient'),
 (41,11,'add_doctor','Can add doctor'),
 (42,11,'change_doctor','Can change doctor'),
 (43,11,'delete_doctor','Can delete doctor'),
 (44,11,'view_doctor','Can view doctor');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'auth','user'),
 (5,'contenttypes','contenttype'),
 (6,'sessions','session'),
 (7,'portal','appointment'),
 (8,'portal','freetimings'),
 (9,'portal','person'),
 (10,'portal','patient'),
 (11,'portal','doctor');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (1,'contenttypes','0001_initial','2019-11-12 17:01:11.573952'),
 (2,'auth','0001_initial','2019-11-12 17:01:11.689263'),
 (3,'admin','0001_initial','2019-11-12 17:01:11.828354'),
 (4,'admin','0002_logentry_remove_auto_add','2019-11-12 17:01:11.974279'),
 (5,'admin','0003_logentry_add_action_flag_choices','2019-11-12 17:01:12.105962'),
 (6,'contenttypes','0002_remove_content_type_name','2019-11-12 17:01:12.232754'),
 (7,'auth','0002_alter_permission_name_max_length','2019-11-12 17:01:12.407597'),
 (8,'auth','0003_alter_user_email_max_length','2019-11-12 17:01:12.548152'),
 (9,'auth','0004_alter_user_username_opts','2019-11-12 17:01:12.655973'),
 (10,'auth','0005_alter_user_last_login_null','2019-11-12 17:01:12.866161'),
 (11,'auth','0006_require_contenttypes_0002','2019-11-12 17:01:13.004437'),
 (12,'auth','0007_alter_validators_add_error_messages','2019-11-12 17:01:13.107194'),
 (13,'auth','0008_alter_user_username_max_length','2019-11-12 17:01:13.231863'),
 (14,'auth','0009_alter_user_last_name_max_length','2019-11-12 17:01:13.374783'),
 (15,'auth','0010_alter_group_name_max_length','2019-11-12 17:01:13.504874'),
 (16,'auth','0011_update_proxy_permissions','2019-11-12 17:01:13.643691'),
 (17,'portal','0001_initial','2019-11-12 17:01:13.795751'),
 (18,'sessions','0001_initial','2019-11-12 17:01:13.923345');
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
COMMIT;
