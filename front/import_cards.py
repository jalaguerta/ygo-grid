import json
import psycopg2

# Database connection details
DB_HOST = "localhost"
DB_NAME = "yugioh_cards"
DB_USER = "jamielaguerta"

# Path to your JSON file
JSON_FILE_PATH = "yugioh_cards.json"

def import_json_to_postgres():
    try:
        # Connect to the database
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
        )
        cursor = conn.cursor()
        print("Connected to the database.")

        # Open and read the JSON file
        with open(JSON_FILE_PATH, "r") as file:
            data = json.load(file)["data"]

        for card in data:
            # Extract data with defaults for missing fields
            card_id = card["id"]
            card_name = card["name"]
            card_type = card["type"]
            card_frame_type = card.get("frameType", None)
            card_desc = card.get("desc", None)
            card_atk = card.get("atk", None)
            card_def = card.get("def", None)
            card_level = card.get("level", None)
            card_race = card.get("race", None)
            card_attribute = card.get("attribute", None)
            card_archetype = card.get("archetype", None)

            # Insert data into the database
            cursor.execute("""
                INSERT INTO yugioh_cards (
                    id, name, type, frame_type, description, atk, def, level, race, attribute, archetype
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
            """, (card_id, card_name, card_type, card_frame_type, card_desc, card_atk, card_def, card_level, card_race, card_attribute, card_archetype))


        for card in data:
            # Extract data with defaults for missing fields
            card_id = card["id"]
            card_archetype = card.get("archetype", None)

            if card_archetype:  # Only update if archetype exists
                cursor.execute("""
                    UPDATE yugioh_cards
                    SET archetype = %s
                    WHERE id = %s
                """, (card_archetype, card_id))

        # Commit the transaction
        conn.commit()
        print("Data imported successfully.")

        

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Database connection closed.")

# Run the import function
if __name__ == "__main__":
    import_json_to_postgres()
