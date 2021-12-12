:param name_206 => "206";
:param type_gti => "gti"
CREATE (n:Car {name: $name_206, type: $type_gti, price: 1000});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $name_206 AND b.name = $brand_peugeot
CREATE (b)-[ae:PRODUCES {}]->(c);

:param name_207 => "207";
CREATE (n:Car {name: $name_207, type: $type_gti, price: 1000});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $name_207 AND b.name = $brand_peugeot
CREATE (b)-[ae:PRODUCES {}]->(c);

:param name_308 => "308";
CREATE (n:Car {name: $name_308, type: $type_gti, price: 1000});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $name_308 AND b.name = $brand_peugeot
CREATE (b)-[ae:PRODUCES {}]->(c);

:param name_408 => "408";
CREATE (n:Car {name: $name_408, type: $type_gti, price: 1000});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $name_408 AND b.name = $brand_peugeot
CREATE (b)-[ae:PRODUCES {}]->(c);

:param name_ds3 => "ds3";
CREATE (n:Car {name: $name_ds3, type: $type_gti, price: 1000});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $name_ds3 AND b.name = $brand_ds
CREATE (b)-[ae:PRODUCES {}]->(c);

:param name_ds4 => "ds4";
CREATE (n:Car {name: $name_ds4, type: $type_gti, price: 1000});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $name_ds4 AND b.name = $brand_ds
CREATE (b)-[ae:PRODUCES {}]->(c);

:param name_ds5 => "ds5";
CREATE (n:Car {name: $name_ds5, type: $type_gti, price: 1000});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $name_ds5 AND b.name = $brand_ds
CREATE (b)-[ae:PRODUCES {}]->(c);

:param name_c1 => "c1";
CREATE (n:Car {name: $name_c1, type: $type_gti, price: 1000});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $name_c1 AND b.name = $brand_citroen
CREATE (b)-[ae:PRODUCES {}]->(c);

:param name_c2 => "c2";
CREATE (n:Car {name: $name_c2, type: $type_gti, price: 1000});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $name_c2 AND b.name = $brand_citroen
CREATE (b)-[ae:PRODUCES {}]->(c);

:param name_c3 => "c3";
CREATE (n:Car {name: $name_c3, type: $type_gti, price: 1000});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $name_c3 AND b.name = $brand_citroen
CREATE (b)-[ae:PRODUCES {}]->(c);

:param name_c4 => "c4";
CREATE (n:Car {name: $name_c4, type: $type_gti, price: 1000});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $name_c4 AND b.name = $brand_citroen
CREATE (b)-[ae:PRODUCES {}]->(c);

:param name_c5 => "c5";
CREATE (n:Car {name: $name_c5, type: $type_gti, price: 1000});
MATCH
  (c:Car),
  (b:Brand)
WHERE c.name = $name_c5 AND b.name = $brand_citroen
CREATE (b)-[ae:PRODUCES {}]->(c);
