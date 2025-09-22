import simpy
import numpy as np
import pandas as pd
from draw_table import draw


def generate_bearing_lifespan():
    lifespan_random_number = {
        1000: np.random.randint(1, 10),
        1100: np.random.randint(11, 23),
        1200: np.random.randint(24, 48),
        1300: np.random.randint(49, 61),
        1400: np.random.randint(62, 70),
        1500: np.random.randint(71, 82),
        1600: np.random.randint(83, 84),
        1700: np.random.randint(85, 90),
        1800: np.random.randint(91, 95),
        1900: np.random.randint(96, 100)
    }
    
    life_span_hour = [
        1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900
    ]
    probs = [
        0.1, 0.13, 0.25, 0.13, 0.09, 0.12, 0.02, 0.06, 0.05, 0.05
    ]

    life_span = np.random.choice(life_span_hour, p=probs)
    random_num = lifespan_random_number[life_span]

    return life_span, random_num

def generate_delay_time():
    
    delay_time_random_number = {
        5: np.random.randint(1, 6),
        10: np.random.randint(7, 9),
        15: 0
    }

    delay_time = [5, 10, 15]
    probs = [0.6, 0.3, 0.1]

    random_delay_time = np.random.choice(delay_time, p=probs)
    random_number = delay_time_random_number[random_delay_time]

    return random_delay_time, random_number
    
def bearing_system(env, simulation_duration, data):
    cumulative_time = 0

    while cumulative_time < simulation_duration:
        bearing_1, random_number_1 = generate_bearing_lifespan()
        data["Bearing 1 Lifespan (hours)"].append(int(bearing_1))
        data["Random number for first bearing"].append(int(random_number_1))
        bearing_2, random_number_2 = generate_bearing_lifespan()
        data["Bearing 2 Lifespan (hours)"].append(int(bearing_2))
        data["Random number for second bearing"].append(int(random_number_2))
        bearing_3, random_number_3 = generate_bearing_lifespan()
        data["Bearing 3 Lifespan (hours)"].append(int(bearing_3))
        data["Random number for third bearing"].append(int(random_number_3))

        first_expiration = min(int(bearing_1), int(bearing_2), int(bearing_3))
        data["First Expiration (hours)"].append(first_expiration)
        cumulative_time += first_expiration # Simulation clock moves to reinstallation event
        data["Cumulative Time (hours)"].append(cumulative_time)

        delay, delay_random_number = generate_delay_time()
        data["Random Numbers (Delay)"].append(int(delay_random_number))
        data["Delay Time (minutes)"].append(int(delay))

    yield env.timeout(int(delay) / 60) # Convert to hours

def main():
    simulation_duration = 20000 # (hours)
    
    env = simpy.Environment()
    data = {
        "Bearing 1 Lifespan (hours)": [],
        "Random number for first bearing": [],
        "Bearing 2 Lifespan (hours)": [],
        "Random number for second bearing": [],
        "Bearing 3 Lifespan (hours)": [],
        "Random number for third bearing": [],
        "First Expiration (hours)": [],
        "Cumulative Time (hours)": [],
        "Random Numbers (Delay)": [],
        "Delay Time (minutes)": [],
    }

    env.process(bearing_system(env, simulation_duration, data))
    env.run()
    
    columns = [
        "Bearing 1 Lifespan (hours)",
        "Bearing 2 Lifespan (hours)",
        "Bearing 3 Lifespan (hours)",
        "First Expiration (hours)",
        "Cumulative Time (hours)",
        "Random Number",
        "Delay Time (minutes)"
    ]

    result = draw(data, columns=None)

    return result


if __name__ == '__main__':
    df = main()
    df.to_html("results.html", index=False)