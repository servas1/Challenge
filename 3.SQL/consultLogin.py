import mysql.connector

# Configura la conexión a la base de datos MySQL
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

# Consulta para obtener el nombre completo de los clientes y su número de fallos
query = """
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer, COUNT(e.status) AS failures
FROM customers c
JOIN campaigns ca ON c.id = ca.customer_id
JOIN events e ON ca.id = e.campaign_id
WHERE e.status = 'failure'
GROUP BY customer
HAVING COUNT(e.status) > 3;
"""

# Ejecutar la consulta
cursor.execute(query)
results = cursor.fetchall()

# Mostrar resultados
print("customer, failures")
for row in results:
    print(f"{row[0]}, {row[1]}")

# Cerrar la conexión
cursor.close()
conn.close()
