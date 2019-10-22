# EURITO "query" indicators

[EURITO](http://www.eurito.eu/) indicators have generally been generating following two broad approaches, either using "graph" database infrastructure or "search engine" database infrastructure. This repository contains code to generate EURITO indicators via [`clio-lite`](https://github.com/nestauk/clio-lite) to query the EURITO search engine database. The code for generating "graph" indicators can similarly be found in the [`graph_indicators`](https://github.com/EURITO/graph_indicators) repository.

# Indicator themes

EURITO has four indicator "themes":

* Theme 1: Emerging Technologies
* Theme 2: New research & funding analytics
* Theme 3: Predictive
* Theme 4: Inclusive and missions

In this repository, we explore themes 1 and 4. The code for generating these indicators are linked below.

## Theme 1: Emerging Technologies

1) Levels of AI activity in academic literature
    a) [National](theme_1/ai_activity/national_ai_activity.ipynb)
    b) [Regional](theme_1/ai_activity/regional_ai_activity.ipynb)
2) [Concentration of AI activity (subnational)](theme_1/ai_activity/subnational_concentration.ipynb)
3) Distribution of emergent technology in industry
4) Technological transformation

## Theme 4: Inclusive and missions

1) Activity by mission:
    a) [National](theme_4/activity/national_mission_activity.ipynb)
    b) [Regional](theme_4/activity/regional_mission_activity.ipynb)
2) Actors in mission fields.
3) Novelty of actors in mission fields.

