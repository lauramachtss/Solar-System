import random

planets = [
    {"name": "Mercury", "size": 20, "color": "gray", "distance": "80px", "duration": "10s"},
    {"name": "Venus", "size": 25, "color": "orange", "distance": "150px", "duration": "18s"},
    {"name": "Earth", "size": 30, "color": "blue", "distance": "230px", "duration": "30s"},
    {"name": "Mars", "size": 22, "color": "red", "distance": "320px", "duration": "60s"},
    {"name": "Jupiter", "size": 50, "color": "brown", "distance": "450px", "duration": "150s"},
    {"name": "Saturn", "size": 45, "color": "yellow", "distance": "580px", "duration": "300s"},
    {"name": "Uranus", "size": 35, "color": "lightblue", "distance": "700px", "duration": "500s"},
    {"name": "Neptune", "size": 34, "color": "darkblue", "distance": "820px", "duration": "600s"},
]

planet_html = ""
for planet in planets:
    initial_rotation = random.randint(0, 360)
    planet_html += f'''
    <div class="planet" style="
        width: {planet['size']}px;
        height: {planet['size']}px;
        background-color: {planet['color']};
        --distance: {planet['distance']};
        animation-duration: {planet['duration']};
        transform: rotate({initial_rotation}deg) translateX(var(--distance));
    ">
        <span class="planet-name">{planet['name']}</span>
    </div>
    '''

with open("planets.html", "w") as file:
    file.write(planet_html)
