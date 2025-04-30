import json
from app.config.db_config import get_connection

def seed_classes():
    with open('classes.json', 'r') as file:
        classes = json.load(file)

    conn = get_connection()
    cur = conn.cursor()

    for cls in classes:
        cur.execute(
            """
            INSERT INTO classes (name, description, bonuses, perks, flavor)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (name) DO NOTHING;
            """,
            (
                cls.get('name'),
                cls.get('description'),
                json.dumps(cls.get('bonuses', {})),
                cls.get('perks', []),
                cls.get('flavor', '')
            )
        )
    conn.commit()
    cur.close()
    conn.close()
    print('Classes seeding complete.')

if __name__ == '__main__':
    seed_classes()