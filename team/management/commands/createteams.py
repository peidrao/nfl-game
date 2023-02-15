from django.core.management.base import BaseCommand

from team.models import Conferency, Division, Team

CONFERENCES = [
    {'name': 'National Football Conference', 'abbreviation': 'NFC'},
    {'name': 'American Football Conference', 'abbreviation': 'AFC'}
    ]
DIVISIONS = ['North', 'South', 'East', 'West']

TEAMS = [
    {'name': 'Arizona Cardinals', 'stadium': 'State Farm Stadium', 'logo': 'arizona-cardinals.png', 'division': 'West', 'tag': 'NFC' },
    {'name': 'Kansas City Chiefs', 'stadium': 'Arrowhead Stadium', 'logo': 'kansas-city-chiefs.png', 'division': 'West', 'tag': 'AFC' },
    {'name': 'Las Vegas Raiders', 'stadium': 'Allegiant Stadium', 'logo': 'las-vegas-raiders.png', 'division': 'West', 'tag': 'AFC' },
    {'name': 'Seattle Seahawks', 'stadium': 'CenturyLink Field', 'logo': 'seattle-seahawks.png', 'division': 'West', 'tag': 'NFC' },
    {'name': 'San Francisco 49ers', 'stadium': "Levi's Stadium", 'logo': 'san-francisco-49ers.png', 'division': 'West', 'tag': 'NFC' },
    {'name': 'Los Angeles Rams', 'stadium': 'SoFi Stadium', 'logo': 'los-angeles-rams.png', 'division': 'West', 'tag': 'NFC' },
    {'name': 'Los Angeles Chargers', 'stadium': 'SoFi Stadium', 'logo': 'los-angeles-rhargers.png', 'division': 'West', 'tag': 'AFC' },
    {'name': 'Denver Broncos', 'stadium': 'Empower Field at Mile High', 'logo': 'denver-broncos.png', 'division': 'West', 'tag': 'AFC' },
    {'name': 'Indianapolis Colts', 'stadium': 'Lucas Oil Stadium', 'logo': 'indianapolis-colts.png', 'division': 'South', 'tag': 'AFC' },
    {'name': 'Jacksonville Jaguars', 'stadium': 'TIAA Bank Field', 'logo': 'jacksonville-jaguars.png', 'division': 'South', 'tag': 'AFC' },
    {'name': 'Houston Texans', 'stadium': 'NRG Stadium', 'logo': 'houston-texans.png', 'division': 'South', 'tag': 'AFC' },
    {'name': 'Tampa Bay Buccaneers', 'stadium': 'Raymond James Stadium', 'logo': 'tampa-bay-buccaneers.png', 'division': 'South', 'tag': 'NFC' },
    {'name': 'New Orleans Saints', 'stadium': 'Mercedes-Benz Superdome', 'logo': 'new-orleans-saints.png', 'division': 'South', 'tag': 'NFC' },
    {'name': 'Atlanta Falcons', 'stadium': 'Mercedes-Benz Stadium', 'logo': 'atlanta-falcons.png', 'division': 'South', 'tag': 'NFC' },
    {'name': 'Tennessee Titans', 'stadium': 'Nissan Stadium', 'logo': 'tennessee-titans.png', 'division': 'South', 'tag': 'AFC' },
    {'name': 'Carolina Panthers', 'stadium': 'Bank of America Stadium', 'logo': 'carolina-panthers.png', 'division': 'South', 'tag': 'NFC' },
    {'name': 'Chicago Bears', 'stadium': 'Soldier Field', 'logo': 'chicago-bears.png', 'division': 'North', 'tag': 'NFC' },
    {'name': 'Green Bay Packers', 'stadium': 'Lambeau Field', 'logo': '.png', 'division': 'North', 'tag': 'NFC' },
    {'name': 'Pittsburgh Steelers', 'stadium': 'Heinz Field', 'logo': 'pittsburgh-steelers.png', 'division': 'North', 'tag': 'AFC' },
    {'name': 'Cincinnati Bengals', 'stadium': 'Paul Brown Stadium', 'logo': 'cincinnati-bengals.png', 'division': 'North', 'tag': 'AFC' },
    {'name': 'Minnesota Vikings', 'stadium': 'U.S. Bank Stadium', 'logo': 'minnesota-vikings.png', 'division': 'North', 'tag': 'NFC' },
    {'name': 'Detroit Lions', 'stadium': 'Ford Field', 'logo': 'detroit-lions.png', 'division': 'North', 'tag': 'NFC' },
    {'name': 'Baltimore Ravens', 'stadium': 'M&T Bank Stadium', 'logo': 'baltimore-ravens.png', 'division': 'North', 'tag': 'AFC' },
    {'name': 'Cleveland Browns', 'stadium': 'First Energy Stadium', 'logo': 'cleveland-browns.png', 'division': 'North', 'tag': 'AFC'} ,
    {'name': 'Buffalo Bills', 'stadium': 'Bills Stadium', 'logo': 'buffalo-bills.png', 'division': 'East', 'tag': 'AFC' },
    {'name': 'Dallas Cowboys', 'stadium': 'At&T Stadium', 'logo': 'dallas-cowboys.png', 'division': 'East', 'tag': 'NFC' },
    {'name': 'Washington Redskins', 'stadium': 'FedExField', 'logo': 'washington-redskins.png', 'division': 'East', 'tag': 'NFC' },
    {'name': 'Miami Dolphins', 'stadium': 'Hard Rock Stadium', 'logo': 'miami-dolphins.png', 'division': 'East', 'tag': 'AFC' },
    {'name': 'New England Patriots', 'stadium': 'Gillette Stadium', 'logo': 'new-england-patriots.png', 'division': 'East', 'tag': 'AFC' },
    {'name': 'New York Giants', 'stadium': 'MetLife Stadium', 'logo': 'new-york-giants.png', 'division': 'East', 'tag': 'NFC' },
    {'name': 'New York Jets', 'stadium': 'MetLife Stadium', 'logo': 'new-york-jets.png', 'division': 'East', 'tag': 'AFC' },
    {'name': 'Philadelphia Eagles', 'stadium': 'Lincoln Financial Field', 'logo': 'philadelphia-eagles.png', 'division': 'East', 'tag': 'NFC' },
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        conferences = []

        if not Conferency.objects.all().count() == 2:
            for conf in CONFERENCES:
                c = Conferency.objects.create(name=conf['name'], abbreviation=conf['abbreviation'])
                conferences.append(c)
            self.stdout.write(self.style.SUCCESS('Conferences were created'))

        if not Division.objects.all().count() == 8:
            for divi in DIVISIONS:
                Division.objects.bulk_create(
                    [Division(name=divi, conferency=conferences[0]),
                    Division(name=divi, conferency=conferences[1])]
                )

            self.stdout.write(self.style.SUCCESS('Divisions were created'))

        for team in TEAMS:
            if not Team.objects.filter(name=team['name']).exists():
                division = Division.objects.get(name=team['division'], conferency__abbreviation=team['tag'])
                Team.objects.create(name=team['name'], stadium=team['stadium'], logo=team['logo'], division=division)
        self.stdout.write(self.style.SUCCESS('Teams were created'))
