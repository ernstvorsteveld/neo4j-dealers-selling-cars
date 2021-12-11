:param brand_peugeot => "peugeot";
CREATE (n:Brand {name: $brand_peugeot});

:param brand_citroen => "citroen";
CREATE (n:Brand {name: $brand_citroen});

:param brand_ds => "ds";
CREATE (n:Brand {name: $brand_ds});

:param brand_stellantis => "Stellantis";
CREATE (n:Brand {name: $brand_stellantis});

MATCH
  (b1:Brand),
  (b2:Brand)
WHERE b1.name = $brand_stellantis AND b2.name = $brand_peugeot
CREATE (b1) - [pc:OWNS {}] -> (b2);

MATCH
  (b1:Brand),
  (b2:Brand)
WHERE b1.name = $brand_stellantis AND b2.name = $brand_citroen
CREATE (b1) - [pc:OWNS {}] -> (b2);

MATCH
  (b1:Brand),
  (b2:Brand)
WHERE b1.name = $brand_stellantis AND b2.name = $brand_ds
CREATE (b1) - [pc:OWNS {}] -> (b2);

:param car_name => "206";
CREATE (n:Car {name : $car_name});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $car_name AND b.name = $brand_peugeot
CREATE (b)-[ae:PRODUCES {}]->(c);

:param car_name => "207";
CREATE (n:Car {name : $car_name});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $car_name AND b.name = $brand_peugeot
CREATE (b)-[ae:PRODUCES {}]->(c);

:param car_name => "308";
CREATE (n:Car {name : $car_name});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $car_name AND b.name = $brand_peugeot
CREATE (b)-[ae:PRODUCES {}]->(c);

:param car_name => "408";
CREATE (n:Car {name : $car_name});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $car_name AND b.name = $brand_peugeot
CREATE (b)-[ae:PRODUCES {}]->(c);

:param car_name => "ds3";
CREATE (n:Car {name : $car_name});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $car_name AND b.name = $brand_ds
CREATE (b)-[ae:PRODUCES {}]->(c);

:param car_name => "ds4";
CREATE (n:Car {name : $car_name});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $car_name AND b.name = $brand_ds
CREATE (b)-[ae:PRODUCES {}]->(c);

:param car_name => "ds5";
CREATE (n:Car {name : $car_name});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $car_name AND b.name = $brand_ds
CREATE (b)-[ae:PRODUCES {}]->(c);

:param car_name => "c1";
CREATE (n:Car {name : $car_name});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $car_name AND b.name = $brand_citroen
CREATE (b)-[ae:PRODUCES {}]->(c);

:param car_name => "c2";
CREATE (n:Car {name : $car_name});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $car_name AND b.name = $brand_citroen
CREATE (b)-[ae:PRODUCES {}]->(c);

:param car_name => "c3";
CREATE (n:Car {name : $car_name});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $car_name AND b.name = $brand_citroen
CREATE (b)-[ae:PRODUCES {}]->(c);

:param car_name => "c4";
CREATE (n:Car {name : $car_name});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $car_name AND b.name = $brand_citroen
CREATE (b)-[ae:PRODUCES {}]->(c);

:param car_name => "c5";
CREATE (n:Car {name : $car_name});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $car_name AND b.name = $brand_citroen
CREATE (b)-[ae:PRODUCES {}]->(c);
