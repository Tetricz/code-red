# downloads and uploads data to database
import psycopg2 as pg

class DatabaseComs:
    def __init__(self):
        conn = pg.connect(
            host="db-postgresql-nyc1-68733-do-user-6866201-0.b.db.ondigitalocean.com",
            port="25060",
            database="rovers",
            user="doadmin",
            password="AVNS_oV-wAZfj1Ve5UVwm4lf")
        self.conn = conn
        self.cursor = self.conn.cursor()
        
    def commit(self):
        self.conn.commit()
    
    def close(self):
        self.conn.close()

    def printTable(self, table):
        self.cursor.execute("SELECT * FROM " + table + ";")
        self.cursor.fetchall()

    def getRover(self, rover):
        self.cursor.execute("SELECT lat, long, rover_state.battery_level FROM rover_state, rover_path WHERE rover_state.id = " + rover + "AND rover_path.id = " + rover + ";")
        return self.cursor.fetchall()

    def getWeather(self):
        self.cursor.execute("SELECT * FROM weather_events;")
        return self.cursor.fetchall()

if __name__ == "__main__":
    database = DatabaseComs()
    s = database.getRover("3")
    print(s)
    database.close()
