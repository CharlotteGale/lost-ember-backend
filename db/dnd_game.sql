CREATE DATABASE dnd_game;

CREATE TABLE races (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,
  description TEXT,
  bonuses JSONB,    -- e.g. { "PER": 2 }
  perks TEXT[],     -- e.g. ["Beast Speech", "Nature Affinity"]
  flavor TEXT       -- Optional for back-of-card
);

CREATE TABLE classes (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,
  description TEXT,
  bonuses JSONB,             -- e.g. { "Stealth": 2, "Sleight of Hand": 2 }
  perks TEXT[],              -- e.g. ["Stealth Attack", "Shadow Step"]
  flavor TEXT
);

CREATE TABLE characters (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  race TEXT REFERENCES races(name),
  class TEXT REFERENCES classes(name),
  stats JSONB,
  gear JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
