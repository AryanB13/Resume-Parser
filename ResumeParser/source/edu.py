import re
from tkinter import END

def extract_education(lines):


    EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S','C.A.','c.a.','B.Com','B. Com','M. Com', 'M.Com','M. Com .',
            'ME', 'M.E', 'M.E.', 'MS', 'M.S', 'MBA'
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH', 'Master\'s', 'Bachelor\'s', 'Bachelor',
            'PHD', 'phd', 'ph.d', 'Ph.D.','MBA','mba','graduate', 'post-graduate','5 year integrated masters','masters',
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII', '10', '12', '%', 'CGPA', 'GPA', 'Degree', 'University', 'SSE', 'HSE', 'Board'
        ]


    education_pattern = re.compile(r'\b(?:' + '|'.join(re.escape(word) for word in EDUCATION) + r')\w*', re.IGNORECASE)

    


    for line in lines:
        # Split the line into words
        words = line.split()

        # Check if any word in the line is in the EDUCATION list
        if any(word.strip('.').strip(',').strip(':') in EDUCATION for word in words):
            print(line)
    return
