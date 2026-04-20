# F1 Driver Profiles

A full-stack web application for browsing, searching, and managing Formula 1 driver profiles. Built for Columbia's User Interface Design course.

## Features
- Browse profiles of 10 F1 legends with career stats, teams, and notable races
- Search across names, summaries, and team histories with case-insensitive regex matching and highlighted results
- Add new drivers via AJAX form with client- and server-side validation
- Edit existing profiles with confirmation on discard
- Responsive multi-page UI built with Bootstrap

## Tech Stack
- **Backend:** Python, Flask, Jinja2
- **Frontend:** HTML, CSS, JavaScript, jQuery, Bootstrap
- **Patterns:** REST-style routes, AJAX with JSON endpoints, Jinja2 layout inheritance

## Routes
- `/` — Home page with top drivers
- `/search?q=<query>` — Search with regex highlighting
- `/view/<id>` — Individual driver profile
- `/add` — Add new driver form
- `/edit/<id>` — Edit existing driver
- `/add-driver`, `/update-driver/<id>` — JSON API endpoints

## Running Locally
```bash
pip install flask
python server.py
```
Then open `http://localhost:5000` in your browser.

## Author
Ethan Yang — Columbia University, CS & Financial Economics