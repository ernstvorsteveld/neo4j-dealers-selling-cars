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

