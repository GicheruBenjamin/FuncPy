
from app import change_state_thru_list, filter_even, sort_ascending, sort_descending

def main():
    football_teams = ['Liverpool', 'Manchester United', 'Chelsea', 'Arsenal', 'Tottenham Hotspur']
    print(football_teams)
    print(change_state_thru_list(football_teams, lambda x: x.upper()))
    print(filter_even(football_teams, lambda x: x.startswith('A')))
    print(sort_ascending(football_teams, lambda x: len(x)))
    print(sort_descending(football_teams, lambda x: len(x)))

if __name__ == '__main__':
    main()

