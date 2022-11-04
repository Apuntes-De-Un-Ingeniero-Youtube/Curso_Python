"""
Cree un script en python, en el cual genere un json con dos diferentes razas para un video juego, 
las razas son: HUMANOS y ORCOS.

Los HUMANOS tienen diferentes roles de batalla (Guerrero, Jinete, Mago, Recolector y Observador) y los 
ORCOS cuentan con (Guerrero, Chamán y Jinete); cada uno de estos cuenta con un nivel de vida, id, ataque, 
defensa y poder mágico
"""
raza = {
    "Humanos": [
        {
            "Guerrero": {
                "vida": 150,
                "id": 123,
                "ataque": 45,
                "defensa": 34,
                "poder mágico": 0
            }
        },
        {
            "Jinete": {
                "vida": 125,
                "id": 345,
                "ataque": 58,
                "defensa": 70,
                "poder mágico": 15
            }
        },
        {
            "Mago": {
                "vida": 100,
                "id": 234,
                "ataque": 67,
                "defensa": 23,
                "poder mágico": 100
            }
        },
        {
            "Observador": {
                "vida": 120,
                "id": 877,
                "ataque": 0,
                "defensa": 90,
                "poder mágico": 40
            }
        }
    ],
    "Orcos": [
        {
            "Guerrero": {
                "vida": 200,
                "id": 777,
                "ataque": 89,
                "defensa": 22,
                "poder mágico": 0
            }
        },
        {
            "Chamán": {
                "vida": 60,
                "id": 111,
                "ataque": 37,
                "defensa": 12,
                "poder mágico": 120
            }
        },
        {
            "Jinete": {
                "vida": 115,
                "id": 315,
                "ataque": 28,
                "defensa": 20,
                "poder mágico": 25
            }
        }
    ]
}

print(raza)
