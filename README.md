## Connecticut infraction codes, descriptions, and costs

This project was motivated by Civic Hack Night, June 6th, 2015. All data was
scraped from <https://www.jud.ct.gov/Publications/Infractions/infractions.pdf>.
<http://www.cometdocs.com/> was used to export pdf data into text.

## JSON schema

Format of costs.json:

    {
        "10a-139": {"variable": true},
        "14-219(a(1*SZ": {"cost": 449.0, "breakdown": [150.0, 19.0, 150.0, 15.0, 20.0, 75.0, 5.0, 15.0, 0.0]}
    }

Format of descriptions.json:

    [
        {
            "category": "MOTOR VEHICLES",
            "name": "14-219(a(1*SZ",
            "description": "Violation of 14-219(a)(1)* in a school zone (Also, see Appx D)"
        },
        {
            "category": "MISCELLANEOUS",
            "name": "10a-139",
            "description": "Violation of traffic regulations on grounds of University of Connecticut (Note:Amt = to fine assessed by trustees of UConn in accord w/regs not to exceed $90 + $1 for each $8 or fraction thereof of amnt + $20 in costs under C.G.S. 54-143a if fine is less than $35 or $35 in costs if fine is $35 or more)"
        }
    ]

## Cost column order

https://www.jud.ct.gov/Publications/Infractions/Chart_B.pdf

TOTAL AMT DUE - A sum of all the other columns
FINE
FEE - C.G.S. § 51-56a(c)
Z FEE - CONSTRUCTION, UTILITY, TRAFFIC OR FIRE STATION ZONE (Z) FEE (C.G.S. § 14-212a)
COST - C.G.S. § 54-143(a)
SURCHARGE - C.G.S. § 54-143a
STF - SPECIAL TRANSPORTATION FUND SURCHARGE (C.G.S. § 13b-70)
BIPSA - Unknown
MF - MUNICIPAL FEE (MF) (C.G.S. § 51-56a(d))
PLUS - Unknown
