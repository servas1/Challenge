import subprocess
import time

def run_docker_compose():
    print("Starting Docker containers...")
    subprocess.run(["docker-compose", "up", "-d"])
    print("Docker containers started.")
    time.sleep(10)  # Espera para asegurar que los contenedores estén completamente levantados

def run_python_script(script_name):
    print(f"Running {script_name}...")
    subprocess.run(["python", script_name])
    print(f"{script_name} completed.")

def main():
    # Ejecuta Docker Compose
    run_docker_compose()
    
    # Ejecuta los scripts de Python en orden
    run_python_script("createTables.py")
    time.sleep(1)
    run_python_script("createValues.py")
    time.sleep(1)
    run_python_script("consultLogin.py")

    print("All tasks completed.")

if __name__ == "__main__":
    main()