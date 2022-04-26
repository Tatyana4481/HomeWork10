from flask import Flask

import functions as func

app = Flask(__name__)

candidates = func.load_candidates()


@app.route('/')
def main_candidates():
    print(func.main_line_candidates(candidates))
    return func.main_line_candidates(candidates)


@app.route('/candidates/<int:id>')
def page_candidate(id):
    print(func.id_img_candidates)
    return func.id_img_candidates


@app.route('/skills/<skill>')
def skills(skill):
    return func.main_line_candidates(func.candidates_skill(candidates, skill))


app.run()
