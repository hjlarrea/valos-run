# Introduction

This repository contains a simple game built with PyGame Zero for one of my kids. The my objectives behind this project are, beyond building something for him and to get him interested in Computers, to:
- Learn about the dynamics of writing games in Python
- Learn how to leverage WebAssembly (WASM) to distribute Python projects over the web

# Requirements

This game has been built using pyenv and virtual environments for isolating the dependencies required for executing it. Check the local `.python-version` file, if not using pyenv to ensure your local environment is compatible with the project's set up.

# How to start the project

There are different alternatives on how to run this project.

## Local run

Run the following command standing in the project's directory:

```
pgzrun main.py
```

## Local WASM execution

Run the following command standing in the project's directory:

```
pygbag .
```

Then navigate to `https://127.0.0.1:8000`.

## Docker image

Having executed `pygbag`, run the following command standing in the project's directory:

```
docker build -t valosrun:latest .
docker run --rm -d -p 8000:80 valosrun:latest
```

Then navigate to `https://127.0.0.1:8000`.

# How to play

TODO

# Infrastructure

TODO

# Roadmap

- [ ] Fix the loading issues in browsers: the WASM component might not load always, depends on the browser (Chrome, Firefox or Safari) and the platform (PC or Mobile). Might need documentation instead of a proper technical issue to be solved.
- [ ] Fix performance issues: depending on the browser and platform where the WASM component is executed, the game might be accelerated rendering it unplayable.
- [ ] Users are able to input their name while playing on PC, but not on mobile as the keyboard won't pop up in the main screen. Might require to render a keyboard on the screen.
- [ ] Implement a leaderboard. Upon `gameMode == 2` condition (game over), save the combination of user and score in an external source. Then build a static website to render the results.
- [ ] Improve game dynamics: jumping based on time mouse button kept down, animated sprites, randomness in enemy spawn.