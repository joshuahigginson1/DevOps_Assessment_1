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

  feeling_id int UNIQUE NOT NULL,
  feelings_username char(30) UNIQUE NOT NULL,
  baseline_mood char(40) NOT NULL,

  /* Not sure if baseline_mood is a foreign key or not. The contents of this
  field will determine a returned course of therapy from therapy_table. */

  referee_comment varchar (5000) DEFAULT 'Your referee has not left a comment today.',
  patient_comment varchar (200) DEFAULT 'The patient has not left a comment today.' NOT NULL,
  date_of_comment date,

  /* need to make the date have a DEFAULT value of today's date! */

  PRIMARY KEY(feeling_id),
  FOREIGN KEY(feelings_username) REFERENCES user_table(username)
);

/* Create the therapy_table if it does not already exist. This stores the
automatic positive mindset tasks set by a psychiatrist. */

CREATE TABLE IF NOT EXISTS therapy_table (

  therapy_id int UNIQUE NOT NULL,
  referee_username char(30) UNIQUE NOT NULL,
  baseline_mood char(40) NOT NULL,

  /* Thinking of making another static table for different types of mood and their
  associated images/emojis. */

  therapy_title varchar(500) DEFAULT 'This is the therapy title.' NOT NULL
  therapy_contents varchar(10000) DEFAULT 'This is the body text for any therapy treatment' NOT NULL

  PRIMARY KEY(therapy_id),
  FOREIGN KEY(referee_username) REFERENCES user_table(username)
);
