import configparser
import json
import os
from flask import Flask, jsonify

app = Flask(__name__)

CONFIG_FILE = "config.ini"
DB_FILE = "config_data.json"


def read_config(file_path):
    """Read and parse configuration file."""
    config = configparser.ConfigParser()
    data = {}

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file not found: {file_path}")

    try:
        config.read(file_path)

        for section in config.sections():
            data[section] = {}
            for key, value in config.items(section):
                data[section][key] = value

        return data

    except Exception as e:
        raise RuntimeError(f"Error reading configuration: {e}")


def save_to_db(data, db_file):
    """Simulate saving data as JSON in a database (local file)."""
    try:
        with open(db_file, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        raise RuntimeError(f"Failed to save data to database: {e}")


def load_from_db(db_file):
    """Load data from JSON 'database'."""
    if not os.path.exists(db_file):
        return {}
    with open(db_file, "r") as f:
        return json.load(f)


@app.route("/get_config", methods=["GET"])
def get_config():
    """API endpoint to fetch stored configuration."""
    data = load_from_db(DB_FILE)
    return jsonify(data)


if __name__ == "__main__":
    try:
        print("Reading configuration file...")
        config_data = read_config(CONFIG_FILE)

        print("\nConfiguration File Parser Results:\n")
        for section, values in config_data.items():
            print(f"{section}:")
            for key, val in values.items():
                print(f"- {key}: {val}")
            print()

        # Save to JSON (simulate database)
        save_to_db(config_data, DB_FILE)
        print(f" Configuration saved to database file: {DB_FILE}")

        # Start Flask API
        print("\n Starting API server at http://127.0.0.1:5000/get_config\n")
        app.run(debug=False)

    except FileNotFoundError as fnf:
        print(f" {fnf}")
    except Exception as e:
        print(f" Unexpected error: {e}")
