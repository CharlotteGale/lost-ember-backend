import json
from app.config.db_config import get_connection

def seed_races():
    with open('_legacy_races.json', 'r') as file:
        races = json.load(file)

    conn = get_connection()
    cur = conn.cursor()

    for race in races:
        cur.execute(
            """
            INSERT INTO races (name, description, bonuses, perks, flavor)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (name) DO NOTHING;    
            """,
            (
                race.get('name'),
                race.get('description'),
                json.dumps(race.get('bonuses', {})),
                race.get('perks', []),
                race.get('flavor', '')
            )
        )
    conn.commit()
    cur.close()
    conn.close()
    print('Races seeding complete.')

if __name__ == '__main__':
    seed_races()