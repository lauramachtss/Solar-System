planets = [
    {"name": "Mercury", "size": 20, "color": "gray", "distance": "50px", "duration": "10s"},
    {"name": "Venus", "size": 25, "color": "orange", "distance": "80px", "duration": "18s"},
    {"name": "Earth", "size": 30, "color": "blue", "distance": "110px", "duration": "30s"},
    {"name": "Mars", "size": 22, "color": "red", "distance": "150px", "duration": "60s"},
    {"name": "Jupiter", "size": 50, "color": "brown", "distance": "220px", "duration": "150s"},
    {"name": "Saturn", "size": 45, "color": "yellow", "distance": "300px", "duration": "300s"},
    {"name": "Uranus", "size": 35, "color": "lightblue", "distance": "400px", "duration": "500s"},
    {"name": "Neptune", "size": 34, "color": "darkblue", "distance": "500px", "duration": "600s"},
]

# Gerando o HTML dos planetas
planet_html = ""
for planet in planets:
    planet_html += f'''
    <div class="planet" style="
        width: {planet['size']}px;
        height: {planet['size']}px;
        background-color: {planet['color']};
        --distance: {planet['distance']};
        animation-duration: {planet['duration']};
    ">
        <span class="planet-name">{planet['name']}</span>
    </div>
    '''

# Salvando o código HTML gerado
with open("planets.html", "w") as file:
    file.write(planet_html)

print("HTML dos planetas gerado com sucesso!")
