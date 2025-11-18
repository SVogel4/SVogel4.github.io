CREATE EXTENSION IF NOT EXISTS postgis;
DROP TABLE IF EXISTS places;
CREATE TABLE places (
  id SERIAL PRIMARY KEY,
  name TEXT,
  geom GEOMETRY(Point, 4326)
);

INSERT INTO places (name, geom) VALUES
 ('Mainz', ST_SetSRID(ST_MakePoint(8.2473, 49.9929),4326)),
 ('Frankfurt am Main', ST_SetSRID(ST_MakePoint(8.6821, 50.1109),4326)),
 ('Wiesbaden', ST_SetSRID(ST_MakePoint(8.2401, 50.0826),4326));
