import json
import ast
from Fleet import Fleet
from Spaceship import Spaceship
from Operator import Operator
from Mentalist import Mentalist

def save_data(fleet, file_name="data.json"):
    """
    Sauvegarde la flotte en JSON.
    Utilise __dict__ pour capturer tous les attributs, y compris privés.
    """
    json_string = json.dumps(
        fleet.__dict__,
        default=lambda o: o.__dict__,
        sort_keys=True,
        indent=4
    )
    json_dict = ast.literal_eval(json_string)
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(json_dict, f, indent=4)
    print("✅ Flotte sauvegardée dans", file_name)


def _get(data, *keys, default=None):
    """Essaie plusieurs clés, retourne la première trouvée ou default."""
    for k in keys:
        if isinstance(data, dict) and k in data:
            return data[k]
    return default


def load_data(file_name="data.json"):
    """
    Recharge la flotte depuis un fichier JSON.
    Supporte deux schémas:
    - Clés privées (ex: "_Fleet__name", "_Spaceship__shipType")
    - Clés propres (ex: "name", "type")
    Fournit des valeurs par défaut si absent.
    """
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)

    # -- Fleet --
    fleet_name = _get(data, "_Fleet__name", "name", default="Flotte inconnue")
    fleet = Fleet(fleet_name)

    # -- Spaceships list --
    spaceships_list = _get(data, "_Fleet__spaceships", "spaceships", default=[]) or []
    for ship_data in spaceships_list:
        ship_name = _get(ship_data, "_Spaceship__name", "name", default="Inconnu")
        ship_type = _get(ship_data, "_Spaceship__shipType", "type", default="transport")
        ship_condition = _get(ship_data, "_Spaceship__condition", "condition", default=100)

        ship = Spaceship(ship_name, ship_type, ship_condition)

        # -- Crew list --
        crew_list = _get(ship_data, "_Spaceship__crew", "crew", default=[]) or []
        for member_data in crew_list:
            first = _get(member_data, "_Member__first_name", "first_name", default="Inconnu")
            last = _get(member_data, "_Member__last_name", "last_name", default="Inconnu")
            gender = _get(member_data, "_Member__gender", "gender", default="autre")
            age = _get(member_data, "_Member__age", "age", default=0)

            # Operator vs Mentalist detection
            if _get(member_data, "_Operator__role", "role") is not None:
                role = _get(member_data, "_Operator__role", "role", default="technicien")
                experience = _get(member_data, "_Operator__experience", "experience", default=0)
                member = Operator(first, last, gender, age, role)
                member.set_experience(experience)
            else:
                mana = _get(member_data, "_Mentalist__mana", "mana", default=0)
                member = Mentalist(first, last, gender, age)
                member.set_mana(mana)

            ship.append_member(member)

        fleet.append_spaceship(ship)

    print("✅ Flotte chargée depuis", file_name)
    return fleet
