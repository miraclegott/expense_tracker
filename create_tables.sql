CREATE TABLE currencies (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) NOT NULL UNIQUE,
    default_currency_id INTEGER REFERENCES currencies(id) ON DELETE SET NULL
);

CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    amount FLOAT NOT NULL CHECK (amount > 0),
    currency_id INTEGER REFERENCES currencies(id) ON DELETE SET NULL
);
