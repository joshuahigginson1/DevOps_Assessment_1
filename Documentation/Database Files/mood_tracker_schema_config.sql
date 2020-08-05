/* An SQL script to initialise the mood tracker's database schema. */

/* Create the mood_tracker database if it does not already exist. */

CREATE DATABASE IF NOT EXISTS mood_tracker;
USE mood_tracker;

/* Create the user_table if it does not already exist. The user_table stores
information regarding the patients and psychiatrists on the service. */

CREATE TABLE IF NOT EXISTS user_table (

  username char(30) UNIQUE NOT NULL,
  password char(30) NOT NULL,
  first_name char(40) NOT NULL,
  last_name varchar(80) NOT NULL,
  email char(50) NOT NULL,

  /* Not sure how to make this a switch case:
  patient_or_psychiatrist char(80) - INDEX, NOT NULL */

  local_gp varchar(2000) NOT NULL,
  mob_number char(20),
  medical_conditions varchar(2000) DEFAULT 'This user has no medical conditions.'

  PRIMARY KEY(username)
);

/* Create the feelings_table if it does not already exist. This stores each
user's feelings, as well as any referee comments. */


CREATE TABLE IF NOT EXISTS feelings_table (

  feeling_id int UNIQUE AUTO_INCREMENT NOT NULL,
  feelings_username char(30) UNIQUE NOT NULL,
  baseline_mood char(40) UNIQUE NOT NULL,
  referee_comment varchar (5000) DEFAULT 'Your referee has not left a comment today.',
  patient_comment varchar (200) DEFAULT 'The patient has not left a comment today.' NOT NULL,
  date_of_comment date,

  /* need to make the date have a DEFAULT value of today's date! */

  PRIMARY KEY(feeling_id),
  FOREIGN KEY(feelings_username) REFERENCES user_table(username),
  FOREIGN KEY(baseline_mood) REFERENCES mood_list(mood)
);

/* Create the therapy_table if it does not already exist. This stores the
automatic positive mindset patient_tasks set by a psychiatrist. */

CREATE TABLE IF NOT EXISTS therapy_table (

  therapy_id int UNIQUE AUTO_INCREMENT NOT NULL,
  referee_username char(30) UNIQUE NOT NULL,
  baseline_mood char(40) UNIQUE NOT NULL,
  therapy_title varchar(500) DEFAULT 'This is the therapy title.' NOT NULL
  therapy_contents varchar(10000) DEFAULT 'This is the body text for any therapy treatment' NOT NULL

  PRIMARY KEY(therapy_id),
  FOREIGN KEY(referee_username) REFERENCES user_table(username),
  FOREIGN KEY(baseline_mood) REFERENCES mood_list(mood)

);

/* Create a list of moods if it does not already exists. Stores every emotion
as a primary key, so it can be explicitly referenced by other tables & resolving
many to many conflict. */

CREATE TABLE IF NOT EXISTS mood_list (

  mood char(40) UNIQUE NOT NULL,
  mood_description varchar(500) NOT NULL,
  mood_image varchar(200) DEFAULT 'This mood does not have a corresponding image.',
  PRIMARY KEY(mood)
);
