USE world;

SELECT country_name,language,percentage FROM languages
JOIN countries ON country_id =languages.country_id
WHERE language = 'Slovene'
ORDER BY percentage DESC;

SELECT country_name,COUNT(city_name) FROM cities
JOIN countries ON country_id=cities.country_id
GROUP BY countries.country_name
ORDER BY count(city_name) DESC;

SELECT countries.country_name,cities.city_name,cities.population,country_id FROM cities
JOIN countries ON country_id=cities.country_id
WHERE population > 500000 AND countries.country_name = 'Mexico';

SELECT country_name,language,percentage FROM languages
JOIN countries ON country_id = languages.country_id
WHERE percentage > 89
ORDER BY percentage DESC;

SELECT country_name,surface_area,population FROM countries
WHERE surface_area < 501 AND population > 100000;

SELECT country_name,government_form,capital,life_expectancy FROM countries
WHERE government_form= 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;

ALTER TABLE countries CHANGE name country_name VARCHAR(255);
ALTER TABLE cities CHANGE name city_name VARCHAR(255);
select countries.country_name,cities.city_name, district,cities.population FROM cities
JOIN countries ON country_id=cities.country_id
WHERE countries.country_name='Argentina' AND district = 'Buenos Aires' AND cities.population > 500000;

SELECT region, COUNT(countries.id) FROM countries
GROUP BY region
ORDER BY COUNT(countries.id) desc;