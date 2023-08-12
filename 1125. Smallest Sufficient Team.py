# num of people in the team
def solver(skills, people):
     skills_dict = dict() 
     for p_skills in people: 
          for skill in p_skills: 
               if skill not in skills_dict: 
                    skills_dict[skill] = 1 
               else: 
                    skills_dict[skill] += 1 



