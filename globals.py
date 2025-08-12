# constants from the windows API
WM_NCHITTEST = 0x0084
HTCLIENT = 1
HTCAPTION = 2
HTLEFT = 10
HTRIGHT = 11
HTTOP = 12
HTTOPLEFT = 13
HTTOPRIGHT = 14
HTBOTTOM = 15
HTBOTTOMLEFT = 16
HTBOTTOMRIGHT = 17

# GLOBALS 
counter = 0
GLOBAL_STATE = False  # do not touch this
LOGGED_IN = False  # and do not touch this either

# change the value of this glob to toggle the custom title bar
CUSTOM_TITLE_BAR = False
# THE CURRENT INDEX CACHE 
STACKED_INDEX = 0
SIDE_BAR_VISIBLE = False

# FILTERS VISIBLE 
FILTERS_HIDDEN = False
FILTERS_DISABLED = False
KEY_RETURN = 16777220

user_selection_choice = 0

# GLOBALLY STORE ALL THE SEARCH RESULTS FROM THE ANIMAL RESULTS TABLE 
search_results_table = list()
search_results_table_animal = list()

# animal health view options
search_option = True  # when set to true the search option is health history otherwise its-
# vaccination history for False.
animal_health_detail_colums = list()
