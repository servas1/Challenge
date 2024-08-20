import mysql.connector

# Configura la conexión a la base de datos MySQL en Docker
config = {
    'user': 'user',
    'password': 'user_password',
    'host': 'localhost',
    'port': '3306',
    'database': 'advertising_system'
}

# Conexión a la base de datos
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Inserta registros en la tabla customers
insert_customers = """
INSERT INTO customers (first_name, last_name)
VALUES 
    ('Whitney', 'Ferrero'),
    ('Dickie', 'Romera');
"""

# Inserta registros en la tabla campaigns
insert_campaigns = """
INSERT INTO campaigns (customer_id, name)
VALUES 
    (1, 'Upton Group'),
    (1, 'Roob, Hudson and Rippin'),
    (1, 'McCullough, Rempel and Larson'),
    (1, 'Lang and Sons'),
    (2, 'Ruecker, Hand and Haley');
"""

# Inserta registros en la tabla events incluyendo todos los casos de "success" y "failure"
insert_events = """
INSERT INTO events (dt, campaign_id, status)
VALUES 
    ('2021-12-02 13:52:00', 1, 'failure'),
    ('2021-12-02 08:17:48', 2, 'failure'),
    ('2021-12-02 08:18:17', 2, 'failure'),
    ('2021-12-01 11:55:32', 3, 'failure'),
    ('2021-12-01 06:53:16', 4, 'failure'),
    ('2021-12-02 04:51:09', 4, 'failure'),
    ('2021-12-01 06:34:04', 5, 'failure'),
    ('2021-12-02 03:21:18', 5, 'failure'),
    ('2021-12-01 03:18:24', 5, 'failure'),
    ('2021-12-02 15:32:37', 1, 'success'),
    ('2021-12-01 04:23:20', 1, 'success'),
    ('2021-12-02 06:53:24', 1, 'success'),
    ('2021-12-02 08:01:02', 2, 'success'),
    ('2021-12-01 15:57:19', 2, 'success'),
    ('2021-12-02 16:14:34', 3, 'success'),
    ('2021-12-02 21:56:38', 3, 'success'),
    ('2021-12-01 05:54:43', 4, 'success'),
    ('2021-12-02 17:56:45', 4, 'success'),
    ('2021-12-02 11:56:50', 4, 'success'),
    ('2021-12-02 06:08:20', 5, 'success');
"""

# Ejecuta las consultas de inserción
cursor.execute(insert_customers)
cursor.execute(insert_campaigns)
cursor.execute(insert_events)

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Registros insertados exitosamente con 'success' y 'failure'.")
