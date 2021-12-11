:param dealer_broekhuis => "Broekhuis Groep";
CREATE (n:Dealer:TopLevel {name: $dealer_broekhuis});
:param dealer_broekhuis_ede => "Ede";
CREATE (n:Dealer:SubLevel {name: $dealer_broekhuis_ede});
MATCH
  (d1:Dealer:TopLevel),
  (d2:Dealer:SubLevel)
WHERE d1.name = $dealer_broekhuis AND d2.name = $dealer_broekhuis_ede
CREATE (d2) - [pc:WORKSFOR {}] -> (d1);
:param dealer_broekhuis_zwolle => "Zwolle";
CREATE (n:Dealer:SubLevel {name: $dealer_broekhuis_zwolle});
MATCH
  (d1:Dealer:TopLevel),
  (d2:Dealer:SubLevel)
WHERE d1.name = $dealer_broekhuis AND d2.name = $dealer_broekhuis_zwolle
CREATE (d2) - [pc:WORKSFOR {}] -> (d1);
:param dealer_broekhuis_alkmaar => "Alkmaar";
CREATE (n:Dealer:SubLevel {name: $dealer_broekhuis_alkmaar});
MATCH
  (d1:Dealer:TopLevel),
  (d2:Dealer:SubLevel)
WHERE d1.name = $dealer_broekhuis AND d2.name = $dealer_broekhuis_alkmaar
CREATE (d2) - [pc:WORKSFOR {}] -> (d1);



:param dealer_van_mossel => "Van Mossel Automotive Groep";
CREATE (n:Dealer:TopLevel {name: $dealer_van_mossel});
:param dealer_van_mossel_amsterdam => "Amsterdam";
CREATE (n:Dealer:SubLevel {name: $dealer_van_mossel_amsterdam});
MATCH
  (d1:Dealer:TopLevel),
  (d2:Dealer:SubLevel)
WHERE d1.name = $dealer_van_mossel AND d2.name = $dealer_van_mossel_amsterdam
CREATE (d2) - [pc:WORKSFOR {}] -> (d1);

:param dealer_van_mossel_rotterdam => "Rotterdam";
CREATE (n:Dealer:SubLevel {name: $dealer_van_mossel_rotterdam});
MATCH
  (d1:Dealer:TopLevel),
  (d2:Dealer:SubLevel)
WHERE d1.name = $dealer_van_mossel AND d2.name = $dealer_van_mossel_rotterdam
CREATE (d2) - [pc:WORKSFOR {}] -> (d1);

:param dealer_van_mossel_groningen => "Groningen";
CREATE (n:Dealer:SubLevel {name: $dealer_van_mossel_groningen});
MATCH
  (d1:Dealer:TopLevel),
  (d2:Dealer:SubLevel)
WHERE d1.name = $dealer_van_mossel AND d2.name = $dealer_van_mossel_groningen
CREATE (d2) - [pc:WORKSFOR {}] -> (d1);

:param dealer_stern_groep => "Stern Groep";
CREATE (n:Dealer:TopLevel {name: $dealer_stern_groep});

:param dealer_stern_groep_houten => "Houten";
CREATE (n:Dealer:SubLevel {name: $dealer_stern_groep_houten});
MATCH
  (d1:Dealer:TopLevel),
  (d2:Dealer:SubLevel)
WHERE d1.name = $dealer_stern_groep AND d2.name = $dealer_stern_groep_houten
CREATE (d2) - [pc:WORKSFOR {}] -> (d1);

:param dealer_stern_groep_eindhoven => "Eindhoven";
CREATE (n:Dealer:SubLevel {name: $dealer_stern_groep_eindhoven});
MATCH
  (d1:Dealer:TopLevel),
  (d2:Dealer:SubLevel)
WHERE d1.name = $dealer_stern_groep AND d2.name = $dealer_stern_groep_eindhoven
CREATE (d2) - [pc:WORKSFOR {}] -> (d1);

:param dealer_stern_groep_veenendaal => "Veenendaal";
CREATE (n:Dealer:SubLevel {name: $dealer_stern_groep_veenendaal});
MATCH
  (d1:Dealer:TopLevel),
  (d2:Dealer:SubLevel)
WHERE d1.name = $dealer_stern_groep AND d2.name = $dealer_stern_groep_veenendaal
CREATE (d2) - [pc:WORKSFOR {}] -> (d1);



