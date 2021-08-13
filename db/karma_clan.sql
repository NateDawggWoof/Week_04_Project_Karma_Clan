DROP TABLE deeds;
DROP TABLE actions;
DROP TABLE users;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    goal_daily INT,
    total_daily INT,
    total_overall INT
);

CREATE TABLE  actions (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    description TEXT,
    type VARCHAR(255)
);

CREATE TABLE deeds (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    action_id INT REFERENCES actions(id),
    date VARCHAR (255)
);
