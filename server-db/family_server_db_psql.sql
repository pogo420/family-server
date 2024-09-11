/*
    Schema for event manager table
*/
CREATE TABLE IF NOT EXISTS annual_events (
  event_id SERIAL PRIMARY KEY,
  event_name VARCHAR(40),
  event_type CHAR(1),
  event_date DATE,
  event_comments VARCHAR(50)
);
