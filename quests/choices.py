
F_RANK = 'F'
E_RANK = 'E'
D_RANK = 'D'
C_RANK = 'C'
B_RANK = 'B'
A_RANK = 'A'
S_RANK = 'S'
RANK_CHOICES = [
    (F_RANK, F_RANK),
    (E_RANK, E_RANK),
    (D_RANK, D_RANK),
    (C_RANK, C_RANK),
    (B_RANK, B_RANK),
    (A_RANK, A_RANK),
    (S_RANK, S_RANK),
]
ROLE_CHOICES = [
    ('Project Manager', 'Project Manager'),
    ('Client Partner', 'Client Partner'),
    ('Product Designer', 'Product Designer'),
    ('Content Strategist', 'Content Strategist'),
    ('Team Member', 'Team Member'),
    ('UXR', 'UXR'), ('IA', 'IA'),
    ('IXD', 'IXD'), ('UI', 'UI'),
]
TEAM_SZ_SOLO = '1'
TEAM_SZ_FIVE = '2 - 5'
TEAM_SZ_NINE = '6 - 9'
TEAM_SZ_FOURTEEN = '10 - 14'
TEAM_SZ_MAX = '15 - 20(max)'
TEAM_SZ_CHOICES = [
    (TEAM_SZ_SOLO, TEAM_SZ_SOLO),
    (TEAM_SZ_FIVE, TEAM_SZ_FIVE),
    (TEAM_SZ_NINE, TEAM_SZ_NINE),
    (TEAM_SZ_FOURTEEN, TEAM_SZ_FOURTEEN),
    (TEAM_SZ_MAX, TEAM_SZ_MAX),
]
DELIVERABLES_CHOICES = [
    ('Card Sorting', 'Card Sorting'),
    ('Executive Summary', 'Executive Summary'),
    ('Information Architecture', 'Information Architecture'),
    ('Interviews', 'Interviews'), ('Survey', 'Survey'),
    ('Personas', 'Personas'),
    ('Recommendations', 'Recommendations'),
    ('Research Summary', 'Research Summary'),
    ('UX Map', 'UX Map'),
]