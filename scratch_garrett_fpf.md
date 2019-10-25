#Thoughts

Data files needed:
1. QATM files (in a folder)
2. Inspection plans
    - material number
    - has In Process inspection (T/F)
    - has mutliple In Process Inpsections (#)
        - this is optional, I don't know how many this truly effects.  could be an improvement if needed

Logic.py
- this should contain all the functions you need and will keep the actual analysis page a lot cleaner.
- think of excel or PBI functions, I want to do X, but do not need to see to logic

Analysis.py
- where the magic happens

Purpose
quick and dirty look back on fpf using the 'new' standard
- level 2 loss analysis on FPF
    - which tests are failing the most
    - are we failing high or low
    - material breakdown
    - location breakdown
    - need in process data to rule out those samples
    - ? do we think the plants are logging resamples
        - if they are logging > we are screwed
- to consider level 2
    - Divisional owner
    - Registered type
    - tank analysis


Lauren's role
- how to pull in data and set up related DataFrames
- what are functions
    - what are they used for
    - how to create
    - benefits
- refresher on loops

Garrett's role
- make use of the functions and loops

