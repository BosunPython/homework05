CREATE TABLE PC (
Code INT AUTO_INCREMENT NOT NULL,
model VARCHAR(50),
speed SMALLINT,
ram SMALLINT,
hd REAL,
cd VARCHAR(10),
price DECIMAL(8,2),
PRIMARY KEY (Code)
);
INSERT INTO pc (Code, model, speed, ram, hd, cd,  price)
VALUES
(75843, "BVK-1", 4.8, 16, 500, "12x", 700),
(75895, "BVK-2", 3.9, 8, 1000, "16x", 800),
(75654, "BVK-3", 2.2, 8, 250, "8x", 390),
(75891, "BVK-4", 3.2, 24, 1000, "16x", 740),
(74367, "BVK-5", 4.1, 32, 2000, "16x", 1000),
(583301, "BVK-6", 5.2, 32, 4000, "16x", 1300);

-- SELECT * FROM pc
-- WHERE price <= 390

-- SELECT model,speed, hd FROM pc
-- WHERE 8<= ram <= 16 

-- SELECT price FROM pc
-- WHERE hd < 1000

UPDATE pc SET price = price * 2 WHERE price > 400;
SELECT * FROM pc;