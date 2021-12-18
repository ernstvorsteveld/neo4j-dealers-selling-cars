MATCH
  (c:Car),
  (d:Dealer)
WHERE c.name = $name_c5 AND d.name = $dealer_broekhuis_ede_citroen
CREATE (c)-[ae:MAYOFFER {commission: 100}]->(d);

MATCH
  (c:Car),
  (d:Dealer)
WHERE c.name = $name_c5 AND d.name = $dealer_broekhuis_ede_citroen
CREATE (d)-[ae:OFFERS {}]->(c);

MATCH
  (c:Car),
  (d:Dealer)
WHERE c.name = $name_c4 AND d.name = $dealer_broekhuis_ede_citroen
CREATE (c)-[ae:MAYOFFER {commission: 100}]->(d);

MATCH
  (c:Car),
  (d:Dealer)
WHERE c.name = $name_c3 AND d.name = $dealer_broekhuis_ede_citroen
CREATE (c)-[ae:MAYOFFER {commission: 100}]->(d);
