           spawning patterns
              if random.choice(
                    [True, False]
                ):  # Randomly choose between generating above or below the screen
                    random_x = random.randint(
                        -padding, 0
                    )  # Generate between -padding and 0
                else:
                    random_x = random.randint(
                        window_width, window_width + padding
                    )  # Generate between max value and max value + padding

                # Generate random y-coordinate
                if random.choice(
                    [True, False]
                ):  # Randomly choose between generating above or below the screen
                    random_y = random.randint(
                        -padding, 0
                    )  # Generate between -padding and 0
                else:
                    random_y = random.randint(window_height, window_height + padding)
