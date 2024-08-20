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

# Crear las tablas en la base de datos
create_customers_table = """
CREATE TABLE IF NOT EXISTS customers (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64) NOT NULL
);
"""

create_campaigns_table = """
CREATE TABLE IF NOT EXISTS campaigns (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    customer_id SMALLINT,
    name VARCHAR(64),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
"""

create_events_table = """
CREATE TABLE IF NOT EXISTS events (
    dt DATETIME,
    campaign_id SMALLINT,
    status VARCHAR(64),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
);
"""

# Ejecutar las consultas de creación de tablas
cursor.execute(create_customers_table)
cursor.execute(create_campaigns_table)
cursor.execute(create_events_table)

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Tablas creadas exitosamente.")