-- a script that displys the maximun temperatur of some states
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
