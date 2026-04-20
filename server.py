# import flask
from flask import Flask, render_template, request, jsonify
import re
from markupsafe import Markup


# create an app instance
app = Flask(__name__)
data = [
  {
    "id": 1,
    "name": "Lewis Hamilton",
    "media_link": "https://upload.wikimedia.org/wikipedia/commons/1/18/Lewis_Hamilton_2016_Malaysia_2.jpg",
    "career_start_year": 2007,
    "career_end_year": 2025,
    "championships": 7,
    "wins": 103,
    "pole_positions": 104,
    "podiums": 197,
    "summary": "Lewis Hamilton is widely regarded as one of the greatest Formula 1 drivers of all time due to his dominance across multiple eras. He matched Michael Schumacher’s record of seven world championships and holds numerous all-time records, including most wins and pole positions. Hamilton built his legacy primarily with Mercedes during the hybrid era, where he demonstrated exceptional consistency and racecraft. Beyond statistics, he is also known for his influence on the sport’s global popularity and his ability to perform under pressure in crucial moments.",
    "teams": ["McLaren", "Mercedes", "Ferrari"],
    "notable_races": ["2008 British Grand Prix", "2018 German Grand Prix", "2020 Turkish Grand Prix"]
  },
  {
    "id": 2,
    "name": "Michael Schumacher",
    "media_link": "https://upload.wikimedia.org/wikipedia/commons/8/80/Michael_Schumacher_2010_Malaysia.jpg",
    "career_start_year": 1991,
    "career_end_year": 2012,
    "championships": 7,
    "wins": 91,
    "pole_positions": 68,
    "podiums": 155,
    "summary": "Michael Schumacher dominated Formula 1 in the late 1990s and early 2000s, particularly with Ferrari. He secured five consecutive championships from 2000 to 2004, establishing one of the most dominant periods in the sport’s history. Schumacher was known for his relentless work ethic, technical feedback, and ability to extract maximum performance from the car. His success helped transform Ferrari into a powerhouse team and set records that stood for over a decade.",
    "teams": ["Jordan", "Benetton", "Ferrari", "Mercedes"],
    "notable_races": ["1996 Spanish Grand Prix", "2000 Japanese Grand Prix", "2004 French Grand Prix"]
  },
  {
    "id": 3,
    "name": "Ayrton Senna",
    "media_link": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Ayrton_Senna_1991_United_States_GP.jpg",
    "career_start_year": 1984,
    "career_end_year": 1994,
    "championships": 3,
    "wins": 41,
    "pole_positions": 65,
    "podiums": 80,
    "summary": "Ayrton Senna is celebrated for his extraordinary speed, especially in qualifying and wet conditions. Driving for McLaren, he won three world championships and delivered many iconic performances. Senna’s rivalry with Alain Prost became one of the most famous in motorsport history. His career was tragically cut short in 1994, but his legacy continues to inspire drivers and fans worldwide.",
    "teams": ["Toleman", "Lotus", "McLaren", "Williams"],
    "notable_races": ["1984 Monaco Grand Prix", "1988 Japanese Grand Prix", "1993 European Grand Prix"]
  },
  {
    "id": 4,
    "name": "Juan Manuel Fangio",
    "media_link": "https://upload.wikimedia.org/wikipedia/commons/3/36/J.M._Fangio_1957.jpg",
    "career_start_year": 1950,
    "career_end_year": 1958,
    "championships": 5,
    "wins": 24,
    "pole_positions": 29,
    "podiums": 35,
    "summary": "Juan Manuel Fangio dominated Formula 1’s early years, winning five championships in the 1950s. His win percentage remains one of the highest in F1 history, highlighting his efficiency and skill. Fangio succeeded with multiple teams, demonstrating adaptability across different cars and conditions. He is often considered the benchmark for greatness in the sport’s formative era.",
    "teams": ["Alfa Romeo", "Maserati", "Mercedes", "Ferrari"],
    "notable_races": ["1951 British Grand Prix", "1956 Argentine Grand Prix", "1957 German Grand Prix"]
  },
  {
    "id": 5,
    "name": "Alain Prost",
    "media_link": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Alain_Prost_in_1985_%28cropped%29.jpg",
    "career_start_year": 1980,
    "career_end_year": 1993,
    "championships": 4,
    "wins": 51,
    "pole_positions": 33,
    "podiums": 106,
    "summary": "Alain Prost earned the nickname 'The Professor' for his intelligent and calculated driving style. Rather than relying solely on raw speed, he focused on consistency and strategy to win races and championships. Prost captured four world titles and was a dominant force during the 1980s. His rivalry with Ayrton Senna defined an era of Formula 1.",
    "teams": ["McLaren", "Renault", "Ferrari", "Williams"],
    "notable_races": ["1982 French Grand Prix", "1985 European Grand Prix", "1993 German Grand Prix"]
  },
  {
    "id": 6,
    "name": "Sebastian Vettel",
    "media_link": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Sebastian_Vettel_in_2015_Malaysia.JPG",
    "career_start_year": 2007,
    "career_end_year": 2022,
    "championships": 4,
    "wins": 53,
    "pole_positions": 57,
    "podiums": 122,
    "summary": "Sebastian Vettel dominated the early 2010s with Red Bull Racing, winning four consecutive championships. Known for his precision and qualifying speed, he set records as the youngest world champion at the time. Vettel later moved to Ferrari, where he continued to fight for titles but faced strong competition. He retired as one of the most successful drivers of his generation.",
    "teams": ["BMW Sauber", "Toro Rosso", "Red Bull", "Ferrari", "Aston Martin"],
    "notable_races": ["2008 Italian Grand Prix", "2011 Indian Grand Prix", "2013 Brazilian Grand Prix"]
  },
  {
    "id": 7,
    "name": "Fernando Alonso",
    "media_link": "https://upload.wikimedia.org/wikipedia/commons/5/59/Fernando_Alonso_2015_Malaysia.jpg",
    "career_start_year": 2001,
    "career_end_year": 2025,
    "championships": 2,
    "wins": 32,
    "pole_positions": 22,
    "podiums": 106,
    "summary": "Fernando Alonso is widely respected for his versatility and racecraft across different teams and eras. He ended Michael Schumacher’s dominance by winning back-to-back championships with Renault. Alonso has remained competitive even in less dominant machinery, showcasing exceptional defensive driving and strategy. His longevity in the sport highlights his enduring skill and determination.",
    "teams": ["Minardi", "Renault", "McLaren", "Ferrari", "Alpine", "Aston Martin"],
    "notable_races": ["2005 Japanese Grand Prix", "2006 Hungarian Grand Prix", "2012 European Grand Prix"]
  },
  {
    "id": 8,
    "name": "Niki Lauda",
    "media_link": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Niki_Lauda%2C_1975_British_Grand_Prix.jpg",
    "career_start_year": 1971,
    "career_end_year": 1985,
    "championships": 3,
    "wins": 25,
    "pole_positions": 24,
    "podiums": 54,
    "summary": "Niki Lauda is known not only for his driving ability but also for his remarkable comeback after a near-fatal crash in 1976. He returned to racing just weeks later and continued to compete at the highest level. Lauda won three world championships with Ferrari and McLaren. His determination and analytical approach made him one of the sport’s most respected figures.",
    "teams": ["March", "BRM", "Ferrari", "Brabham", "McLaren"],
    "notable_races": ["1975 Monaco Grand Prix", "1976 Italian Grand Prix", "1984 Portuguese Grand Prix"]
  },
  {
    "id": 9,
    "name": "Max Verstappen",
    "media_link": "https://upload.wikimedia.org/wikipedia/commons/6/66/FIA_F1_Austria_2023_Max_Verstappen.jpg",
    "career_start_year": 2015,
    "career_end_year": 2025,
    "championships": 4,
    "wins": 60,
    "pole_positions": 40,
    "podiums": 100,
    "summary": "Max Verstappen represents the modern generation of Formula 1 champions. Known for his aggressive racing style and exceptional car control, he became the youngest race winner in F1 history. Verstappen dominated the early 2020s with Red Bull, securing multiple championships. His performances have redefined expectations for young drivers entering the sport.",
    "teams": ["Toro Rosso", "Red Bull"],
    "notable_races": ["2016 Spanish Grand Prix", "2021 Abu Dhabi Grand Prix", "2023 Miami Grand Prix"]
  },
  {
    "id": 10,
    "name": "Jim Clark",
    "media_link": "https://upload.wikimedia.org/wikipedia/commons/0/02/Jim_Clark_1965.jpg",
    "career_start_year": 1960,
    "career_end_year": 1968,
    "championships": 2,
    "wins": 25,
    "pole_positions": 33,
    "podiums": 32,
    "summary": "Jim Clark was one of the most naturally talented drivers in Formula 1 history. Driving for Lotus, he won two world championships and dominated several seasons. Clark was known for his smooth driving style and ability to perform across different racing disciplines. His career ended prematurely in 1968, but his influence on the sport remains significant.",
    "teams": ["Lotus"],
    "notable_races": ["1963 Dutch Grand Prix", "1965 Indianapolis 500", "1967 British Grand Prix"]
  }
]


@app.route('/')
def home_page():
  return render_template('home.html', data=data)


@app.route('/search', methods=['GET'])
def search():
  query = request.args.get('q', '').strip()
  if not query:
    return render_template('search.html', query='', results=[], count=0, data=data)
  
  def highlight(text):
    result = re.sub(query, f'<mark>{query}</mark>', str(text), flags=re.IGNORECASE)
    return Markup(result)

  results = []
  for driver in data:
    teams_text = ', '.join(driver['teams'])
    if (query.lower() in driver['name'].lower() or
        query.lower() in driver['summary'].lower() or
        query.lower() in teams_text.lower()):
      d = driver.copy()
      d['name_hl']    = highlight(driver['name'])
      d['summary_hl'] = highlight(driver['summary'][:120])
      d['teams_hl']   = highlight(teams_text)
      results.append(d)
  
  return render_template('search.html', query=query, results=results, count=len(results), data=data)

@app.route('/view/<int:driver_id>')
def view_driver(driver_id):
  driver = None
  for d in data:
    if d['id'] == driver_id:
      driver = d
      break
  return render_template('view.html', driver=driver, data=data)


@app.route('/add')
def add_page():
  return render_template('add.html', data=data)

@app.route('/add-driver', methods=['POST'])
def add_driver():
  new_driver = request.get_json()

  errors = {}

  text_fields = ['name', 'summary', 'media_link', 'teams', 'notable_races']
  for field in text_fields:
    if not new_driver.get(field, '').strip():
      errors[field] = 'This field is required'

  number_fields = ['career_start_year', 'career_end_year', 'championships', 'wins', 'pole_positions', 'podiums']
  for field in number_fields:
    val = str(new_driver.get(field, '')).strip()
    if val == '':
      errors[field] = 'This field is required'
    elif not val.isdigit():
      errors[field] = 'Must be a number'

  if errors:
    return jsonify({'success': False, 'errors': errors}), 400
  new_id = max(d['id'] for d in data) + 1
  driver = {
    'id': new_id,
    'name': new_driver['name'].strip(),
    'media_link': new_driver['media_link'].strip(),
    'career_start_year': int(new_driver['career_start_year']),
    'career_end_year': int(new_driver['career_end_year']),
    'championships': int(new_driver['championships']),
    'wins': int(new_driver['wins']),
    'pole_positions': int(new_driver['pole_positions']),
    'podiums': int(new_driver['podiums']),
    'summary': new_driver['summary'].strip(),
    'teams': [t.strip() for t in new_driver['teams'].split(',')],
    'notable_races': [r.strip() for r in new_driver['notable_races'].split(',')]
  }
  data.append(driver)
  return jsonify({'success': True, 'id': new_id})

@app.route('/edit/<int:driver_id>')
def edit_page(driver_id):
  # find the driver by id
  driver = None
  for d in data:
    if d['id'] == driver_id:
      driver = d
      break
  return render_template('edit.html', driver=driver, data=data)

@app.route('/update-driver/<int:driver_id>', methods=['POST'])
def update_driver(driver_id):
  updated = request.get_json()

  errors = {}
  text_fields = ['name', 'summary', 'media_link', 'teams', 'notable_races']
  for field in text_fields:
    if not updated.get(field, '').strip():
      errors[field] = 'This field is required'

  number_fields = ['career_start_year', 'career_end_year', 'championships', 'wins', 'pole_positions', 'podiums']
  for field in number_fields:
    val = str(updated.get(field, '')).strip()
    if val == '':
      errors[field] = 'This field is required'
    elif not val.isdigit():
      errors[field] = 'Must be a number'

  if errors:
    return jsonify({'success': False, 'errors': errors}), 400

  for d in data:
    if d['id'] == driver_id:
      d['name']              = updated['name'].strip()
      d['media_link']        = updated['media_link'].strip()
      d['career_start_year'] = int(updated['career_start_year'])
      d['career_end_year']   = int(updated['career_end_year'])
      d['championships']     = int(updated['championships'])
      d['wins']              = int(updated['wins'])
      d['pole_positions']    = int(updated['pole_positions'])
      d['podiums']           = int(updated['podiums'])
      d['summary']           = updated['summary'].strip()
      d['teams']             = [t.strip() for t in updated['teams'].split(',')]
      d['notable_races']     = [r.strip() for r in updated['notable_races'].split(',')]
      break

  return jsonify({'success': True, 'id': driver_id})