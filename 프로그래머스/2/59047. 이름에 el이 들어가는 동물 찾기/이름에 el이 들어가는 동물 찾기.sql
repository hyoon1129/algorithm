select ANIMAL_ID, NAME
from ANIMAL_INS
where LOWER(NAME) LIKE '%el%' AND ANIMAL_TYPE = "Dog"
order by NAME