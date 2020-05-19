from helper.classes import Team
from helper import utils
from helper import elo

def processYear(year):
    matches = utils.loadMatches(year)
    teams = {}

    try: teams_1yr = utils.loadTeams(year-1)
    except Exception as e: teams_1yr = None

    try: teams_2yr = utils.loadTeams(year-2)
    except Exception as e: teams_2yr = None

    for match in matches:
        for alliance in [match.red, match.blue]:
            for team in alliance:
                if team not in teams:
                    if teams_1yr!=None and team in teams_1yr: team_1yr = teams_1yr[team].get_rating_max()
                    else: team_1yr = elo.new_rating()

                    if teams_2yr!=None and team in teams_2yr: team_2yr = teams_2yr[team].get_rating_max()
                    else: team_2yr = elo.new_rating()

                    teams[team] = Team(team, elo.existing_rating(team_1yr, team_2yr))

    for match in matches: elo.update_rating(year, teams, match)
    utils.saveProcessedMatches(year, matches)
    utils.saveTeams(year, teams)

def main():
    for year in range(2002,2021):
        print(year)
        processYear(year)

if __name__ == "__main__":
    main()
