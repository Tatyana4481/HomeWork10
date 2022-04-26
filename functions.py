import json


def load_candidates():
    """
    загружает список кандитов из файла
    :return:
    """
    with open("candidates.json", "r", encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def main_line_candidates(candidates):
    temp_line = '<pre>'
    for candidate in candidates:
        temp_line += (
            f'  Имя кандидата - {candidate["name"]}\n'
            f'  Позиция кандидата - {candidate["position"]}\n'
            f'  Навыки через запятую - {candidate["skills"]}\n'
        )
    temp_line += '<pre>'
    return temp_line


def id_img_candidates(candidates, id):
    temp_line = '<pre>'
    for candidate in candidates:
        if candidate['id'] == id:
            temp_line += f'<img src="{candidate["picture"]}">\n ' \
                         f'{main_line_candidates(candidate)}'
    temp_line += '<pre>'
    return temp_line


def candidates_skill(candidates, candidate_skill):
    temp_line = []

    for candidate in candidates:
        candidate_skills = candidate['skills'].lower().split(', ')

        if candidate_skill.lower() in candidate_skills:
            temp_line.append(candidate)

    return temp_line
