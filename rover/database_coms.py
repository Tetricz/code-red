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

    def updateRover(self, rover_id, battery):
        # id, status, online, state_entered, battery_level
        self.cursor.execute("UPDATE rover_state SET battery_level = " + str(battery) + " WHERE id = " + str(rover_id) + ";")
        self.cursor.execute("UPDATE rover_state SET battery_level = " + str(state_entered) + " WHERE id = " + str(rover_id) + ";")
        self.cursor.execute("UPDATE rover_state SET battery_level = " + str(online) + " WHERE id = " + str(rover_id) + ";")
        self.cursor.execute("UPDATE rover_state SET battery_level = " + str(status) + " WHERE id = " + str(rover_id) + ";")
        self.commit()

    def insertGeo(self, dataStr):
        self.cursor.execute("INSERT INTO geo_events (date, rover_id, geo_type, location) VALUES " + dataStr + ";")

    def insertWeather(self, dataStr):
        self.cursor.execute("INSERT INTO weather_events (date, rover_id, humidity, temp, atmosphere, wind_speed, visibilty) VALUES " + dataStr + ";")
    
    def insertVid(self, dataStr):
        self.cursor.execute("INSERT INTO vid_events (date, rover_id, vid_name, vid_path, size) VALUES " + dataStr + ";")

    def commit(self):
        self.conn.commit()
    
    def close(self):
        self.conn.close()

    def seedDatabase(self):
        cursor = self.cursor
        cursor.execute("DROP TABLE IF EXISTS test;")
        cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
        cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s);", (129, "abcdef"))
        cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s);", (149, "abcdef"))

        cursor.execute("DROP TABLE IF EXISTS rover_state;")
        cursor.execute("CREATE TABLE rover_state (id INT PRIMARY KEY, status INT, online BOOLEAN NOT NULL, state_entered TIMESTAMP, battery_level FLOAT);")
        cursor.execute("INSERT INTO rover_state (id, status, online, state_entered, battery_level) VALUES (%s, %s, %s, %s, %s);", (1, 0, True, "2020-01-01 00:00:00", 100.0))
        cursor.execute("INSERT INTO rover_state (id, status, online, state_entered, battery_level) VALUES (%s, %s, %s, %s, %s);", (2, 0, True, "2020-01-02 00:00:00", 100.0))
        cursor.execute("INSERT INTO rover_state (id, status, online, state_entered, battery_level) VALUES (%s, %s, %s, %s, %s);", (3, 0, True, "2020-01-03 00:00:00", 100.0))

        cursor.execute("DROP TABLE IF EXISTS rover_path;")
        cursor.execute("CREATE TABLE rover_path (key serial PRIMARY KEY, date TIMESTAMP, rover_id INT, lat FLOAT, long FLOAT, altitude FLOAT);")
        cursor.execute("INSERT INTO rover_path (date, rover_id, lat, long, altitude) VALUES (%s, %s, %s, %s, %s);", ("2020-01-01 00:00:00", 1, 0.0, 0.0, 0.0))
        cursor.execute("INSERT INTO rover_path (date, rover_id, lat, long, altitude) VALUES (%s, %s, %s, %s, %s);", ("2020-01-02 00:00:00", 1, 0.0, 0.0, 0.0))
        cursor.execute("INSERT INTO rover_path (date, rover_id, lat, long, altitude) VALUES (%s, %s, %s, %s, %s);", ("2020-01-03 00:00:00", 3, 0.0, 0.0, 0.0))
        cursor.execute("INSERT INTO rover_path (date, rover_id, lat, long, altitude) VALUES (%s, %s, %s, %s, %s);", ("2020-01-01 00:01:00", 1, 1.0, 2.0, 0.0))
        cursor.execute("INSERT INTO rover_path (date, rover_id, lat, long, altitude) VALUES (%s, %s, %s, %s, %s);", ("2020-01-02 00:01:00", 2, 2.0, 1.0, 0.0))
        cursor.execute("INSERT INTO rover_path (date, rover_id, lat, long, altitude) VALUES (%s, %s, %s, %s, %s);", ("2020-01-03 00:01:00", 3, 2.0, 2.0, 0.0))

        cursor.execute("DROP TABLE IF EXISTS weather_events;")
        cursor.execute("CREATE TABLE weather_events (key serial PRIMARY KEY, \
            date TIMESTAMP, rover_id INT, \
            humidity FLOAT, temp FLOAT, atmosphere FLOAT, wind_speed INT, visibilty INT);")
        cursor.execute("INSERT INTO weather_events (date, rover_id, humidity, temp, atmosphere, wind_speed, visibilty) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("2020-01-01 00:00:00", 1, 0.0, 0.0, 0.0, 0, 0))
        cursor.execute("INSERT INTO weather_events (date, rover_id, humidity, temp, atmosphere, wind_speed, visibilty) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("2020-01-02 00:00:00", 1, 0.0, 0.0, 0.0, 0, 0))
        cursor.execute("INSERT INTO weather_events (date, rover_id, humidity, temp, atmosphere, wind_speed, visibilty) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("2020-01-03 00:00:00", 3, 0.0, 0.0, 0.0, 0, 0))
        cursor.execute("INSERT INTO weather_events (date, rover_id, humidity, temp, atmosphere, wind_speed, visibilty) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("2020-01-01 00:01:00", 1, 1.0, 2.0, 0.0, 0, 0))
        cursor.execute("INSERT INTO weather_events (date, rover_id, humidity, temp, atmosphere, wind_speed, visibilty) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("2020-01-02 00:01:00", 2, 2.0, 1.0, 0.0, 0, 0))
        cursor.execute("INSERT INTO weather_events (date, rover_id, humidity, temp, atmosphere, wind_speed, visibilty) VALUES (%s, %s, %s, %s, %s, %s, %s);", ("2020-01-03 00:01:00", 3, 2.0, 2.0, 0.0, 0, 0))

        cursor.execute("DROP TABLE IF EXISTS geo_events;")
        cursor.execute("CREATE TABLE geo_events (key serial PRIMARY KEY, \
            date TIMESTAMP, rover_id INT, \
            geo_type VARCHAR, location VARCHAR);")
        cursor.execute("INSERT INTO geo_events (date, rover_id, geo_type, location) VALUES (%s, %s, %s, %s);", ("2020-01-01 00:00:00", 1, "type1", "location1"))
        
        cursor.execute("DROP TABLE IF EXISTS vid_events;")
        cursor.execute("CREATE TABLE vid_events (key serial PRIMARY KEY, \
            date TIMESTAMP, rover_id INT, \
            vid_name VARCHAR, vid_path VARCHAR, size FLOAT);")
        cursor.execute("INSERT INTO vid_events (date, rover_id, vid_name, vid_path, size) VALUES (%s, %s, %s, %s, %s);", ("2020-01-01 00:00:00", 1, "vid1", "path1", 20.0))

        print("Database seeded :D")

    def printData(self):
        cursor = self.cursor
        cursor.execute("SELECT * FROM test;")
        print("===Table test===")
        print(cursor.fetchall())

        cursor.execute("SELECT * FROM rover_state;")
        print("===Table rover_state===")
        print(cursor.fetchall())

        cursor.execute("SELECT * FROM rover_path;")
        print("===Table rover_path===")
        print(cursor.fetchall())

        cursor.execute("SELECT * FROM weather_events;")
        print("===Table weather_events===")
        print(cursor.fetchall())

        cursor.execute("SELECT * FROM geo_events;")
        print("===Table geo_events===")
        print(cursor.fetchall())

if __name__ == "__main__":
    database = DatabaseComs()
    database.seedDatabase()
    database.printData()
    database.commit()
    database.close()
