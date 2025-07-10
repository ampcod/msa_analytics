from flask import Flask, request, jsonify, render_template
import psycopg2

app = Flask(__name__, static_folder='static', template_folder='templates')

# PostgreSQL Connection Details
DB_NAME = "MSA1"
DB_USER = "postgres"
DB_PASSWORD = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"


# Function to get only MSA 2020 value for quick display
def get_msa_2020(latitude, longitude):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cursor = conn.cursor()

        query = """
            SELECT AVG(overall_msa) 
            FROM msa_2020
            WHERE ST_DWithin(
                geom,
                ST_SetSRID(ST_MakePoint(%s, %s), 4326),
                3000
            );
        """
        cursor.execute(query, (longitude, latitude))
        avg = cursor.fetchone()[0]
        result = {"msa_2020":avg  if avg is not None else "No data"}

        cursor.close()
        conn.close()

        return result

    except Exception as e:
        print("❌ Error querying database:", e)
        return {"error": str(e)}


# Function to get all historical MSA values
def get_all_msa_values(latitude, longitude):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cursor = conn.cursor()

        tables = ['msa_1995', 'msa_2010', 'msa_2015']
        result = {}

        for table in tables:
            query = f"""
                SELECT AVG(overall_msa) 
                FROM {table}
                WHERE ST_DWithin(
                    geom,
                    ST_SetSRID(ST_MakePoint(%s, %s), 4326),
                    3000
                );
            """
            cursor.execute(query, (longitude, latitude))
            avg = cursor.fetchone()[0]
            result[table] = avg if avg is not None else "No data"

        cursor.close()
        conn.close()

        return result

    except Exception as e:
        print("❌ Error querying database:", e)
        return {"error": str(e)}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/map')
def index():
    return render_template('index.html')

# Route for quick MSA 2020 query
@app.route('/get_msa_2020', methods=['GET'])
def api_get_msa_2020():
    lat = request.args.get("lat")
    lng = request.args.get("lng")

    if not lat or not lng:
        return jsonify({"error": "Missing latitude or longitude"}), 400

    msa_value = get_msa_2020(float(lat), float(lng))
    return jsonify(msa_value)

# Route for historical MSA values
@app.route('/get_historical_msa', methods=['GET'])
def api_get_historical_msa():
    lat = request.args.get("lat")
    lng = request.args.get("lng")

    if not lat or not lng:
        return jsonify({"error": "Missing latitude or longitude"}), 400

    historical_values = get_all_msa_values(float(lat), float(lng))
    return jsonify(historical_values)

# Original route kept for compatibility
@app.route('/get_avg_value', methods=['GET'])
def api_get_avg_value():
    lat = request.args.get("lat")
    lng = request.args.get("lng")

    if not lat or not lng:
        return jsonify({"error": "Missing latitude or longitude"}), 400
    
    # Get 2020 data first
    msa_2020 = get_msa_2020(float(lat), float(lng))
    # Then get historical data
    historical = get_all_msa_values(float(lat), float(lng))
    
    # Combine results
    result = {**msa_2020, **historical}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)