from experta import *

class destinationRecommendation(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="Q")
    @Rule(Fact(action='Q'), NOT(Fact(Passport=W())))
    def passport(self):
        self.declare(Fact(Passport=input("Do you have a passport? (y/n) ")))
    
    ################################################################ NO PASSPORT
    @Rule(Fact(Passport='n'), NOT(Fact(Budget1=W())))
    def passport_n(self):
        self.declare(Fact(Budget1=input("What is your budget in usd? ")))
        
    @Rule(Fact(Budget1='value' << W()), NOT(Fact(SMC=W())))
    def budget1(self, value):
        if int(value) < 0:
            print('/nWrong value! ')
        elif int(value) < 1000:
            self.declare(Fact(SMC=input("Sea, mountain or city? (s/m/c) ")))
        else:
            print('\nYou should travel to Lebanon! ')
    
    @Rule(Fact(SMC='s'))
    def smc_s(self):
        print('\nYou should visit Lattakia or Tartus! ')
    
    @Rule(Fact(SMC='m'))
    def smc_m(self):
        print('\nYou should visit Homs! ')
        
    @Rule(Fact(SMC='c'))
    def smc_c(self):
        print('\nYou should visit Damascus or Aleppo! ')
    
    ################################################################ YES PASSPORT
    @Rule(Fact(Passport='y'), NOT(Fact(Purpose=W())))
    def passport_y(self):
        self.declare(Fact(Purpose=input("What is the purpose of your travle? (i-immigration / e-education / l-leisure) ")))
    
    ################################################################ IMMIGRATION
    @Rule(Fact(Purpose='i'), NOT(Fact(LifeWork=W())))
    def purpose_i(self):
        self.declare(Fact(LifeWork=input("Do you want a better life or better work? (l/w) ")))
        
    ################################################################ LIFE
    @Rule(Fact(LifeWork='l'), NOT(Fact(Married=W())))
    def lifeWork_l(self):
        self.declare(Fact(Married=input("Are you married? (y/n) ")))
    
    @Rule(Fact(Married='n'), NOT(Fact(Adapt=W())))
    def married_n(self):
        self.declare(Fact(Adapt=input("Can you adapt to different cultures? (y/n) ")))

    @Rule(Fact(Married='y'), NOT(Fact(Children=W())))
    def married_y(self):
        self.declare(Fact(Children=input("How many children do you have? ")))
    
    @Rule(Fact(Children='value' << W()), NOT(Fact(Adapt=W())), NOT(Fact(Medical=W())))
    def children(self, value):
        if int(value) < 0:
            print('\nWrong value!')
        elif int(value) == 0:
            self.declare(Fact(Adapt=input("Can you adapt to different cultures? (y/n) ")))
        else:
            self.declare(Fact(Medical=(input("Does anyone have a medical case that requires special attention? (y/n) "))))
    
    @Rule(Fact(Medical='y'))
    def medical_y(self):
        print('\nYou should move to Canada! ')
        
    @Rule(Fact(Medical='n'), NOT(Fact(Edu=W())))
    def medical_n(self):
        self.declare(Fact(Edu=input("Do you want a high level of education? (y/n) ")))
    
    @Rule(Fact(Edu='y'))
    def edy_y(self):
        print('\nYou should move to the United States! ')
        
    @Rule(Fact(Edu='n'))
    def edy_n(self):
        print('\nYou should move to Australia! ')
        
    @Rule(Fact(Adapt='y'), NOT(Fact(Climate1=W())))
    def adapt_y(self):
        self.declare(Fact(Climate1=input("What climate do you prefer? (h-hot / c-cold / t-temperate) ")))
    
    @Rule(Fact(Climate1='h'))
    def climate1_h(self):
        print('\nYou should move to Costa Rica! ')
        
    @Rule(Fact(Climate1='t'))
    def climate1_t(self):
        print('\nYou should move to New Zealand! ')
    
    @Rule(Fact(Climate1='c'))
    def climate1_c(self):
        print('\nYou should move to Sweeden! ')
    
    @Rule(Fact(Adapt='n'))
    def adapt_n(self):
        print('\nYou should move to Qatar! ')
    
    ################################################################ WORK
    @Rule(Fact(LifeWork='w'), NOT(Fact(Degree=W())))
    def lifeWork_w(self):
        self.declare(Fact(Degree=input("Do you have a degree? (y/n) ")))
    
    @Rule(Fact(Degree='n'), NOT(Fact(Skilled=W())))
    def degree_n(self):
        self.declare(Fact(Skilled=input("Are you a skilled worker? (y/n) ")))
    
    @Rule(Fact(Skilled='n'))
    def skilled_n(self):
        print('\nMigration is hard in your situation! ')
    
    @Rule(Fact(Skilled='y'), NOT(Fact(Age=W())))
    def skilled_y(self):
        self.declare(Fact(Age=input("How old are you? ")))
        
    @Rule(Fact(Age='value' << W()), NOT(Fact(Health=W())))
    def age(self, value):
        if int(value) < 0  or int(value) > 100: 
            print('\nWrong value!')
        elif int(value) > 45:
            print('\nMigration is hard in your situation! ')
        else:
            self.declare(Fact(Health=input("Do you have health problems? (y/n) ")))
    
    @Rule(Fact(Health='y'))
    def health_y(self):
        print('\nMigration is hard in your situation! ')
        
    @Rule(Fact(Health='n'))
    def health_n(self):
        print('\nYou should move to Germany! ')
    
    @Rule(Fact(Degree='y'), NOT(Fact(WorkExp=W())))
    def degree_y(self):
        self.declare(Fact(WorkExp=input("Do you have work experiance? (y/n) ")))
        
    @Rule(Fact(WorkExp='y'), NOT(Fact(Job=W())))
    def workExp_y(self):
        self.declare(Fact(Job=input("What is your job? (e-engineering / m-medicin / l-law / o-other) ")))
        
    @Rule(Fact(Job='o'), NOT(Fact(Eng1=W())))
    def job_o(self):
        self.declare(Fact(Eng1=input("Are you proficient in English? (y/n) ")))
        
    @Rule(Fact(Eng1='y'))
    def eng1_y(self):
        print('\nYou should move to Singapore! ')
        
    @Rule(Fact(Eng1='n'))
    def eng1_n(self):
        print('\nMigration is hard in your situation! ')
        
    @Rule(Fact(Job='e'))
    def job_e(self):
        print('\nYou should move to the United States! ')
        
    @Rule(Fact(Job='m'))
    def job_m(self):
        print('\nYou should move to the United States! ')
        
    @Rule(Fact(Job='l'))
    def job_l(self):
        print('\nYou should move to the United States! ')
        
    @Rule(Fact(WorkExp='n'))
    def workExp_n(self):
        print('\nMigration is hard in your situation! ')
    
    ################################################################ EDUCATION
    @Rule(Fact(Purpose='e'), NOT(Fact(Eng2=W())))
    def purpose_e(self):
        self.declare(Fact(Eng2=input("Are you proficient in English? (y/n) ")))
        
    @Rule(Fact(Eng2='y'), NOT(Fact(LvlOfEdu=W())))
    def eng2_y(self):
        self.declare(Fact(LvlOfEdu=input("What level of education do you want? (b-bachelor's / m-master's / d-doctorate) ")))
    
    @Rule(Fact(LvlOfEdu='b'), NOT(Fact(Budget2=W())))
    def lvlOfEdu_b(self):
        self.declare(Fact(Budget2=input("What is your yearly budget in usd? ")))
    
    @Rule(Fact(Budget2='value' << W()))
    def age(self, value):
        if int(value) < 10000: 
            print('\nNot possible to study abroad with this amount!')
        elif int(value) < 15000:
            print('\nYou should travel to Germany! ')
        elif int(value) > 15000 and int(value) < 30000:
            print('\nYou should travel to the Netherlands! ')
        else:
            print('\nYou should travel to the United States! ')
    
    @Rule(Fact(LvlOfEdu='m'), NOT(Fact(GPA=W())))
    def lvlOfEdu_m(self):
        self.declare(Fact(GPA=input("What is your Bachelor's GPA? (percentage) ")))
    
    @Rule(Fact(GPA='value' << W()), NOT(Fact(Field=W())))
    def age(self, value):
        if int(value) < 75: 
            print('\nYou should study in the United Kingdom! ')
        else:
            self.declare(Fact(Field=input("What field do you study? (b-business / e-engineering / s-science / t-technology) ")))
    
    @Rule(Fact(Field='b'))
    def field_b(self):
        print('\nYou should study in France! ')
    
    @Rule(Fact(Field='e'))
    def field_e(self):
        print('\nYou should study in Germany! ')
    
    @Rule(Fact(Field='s'))
    def field_s(self):
        print('\nYou should study in the United Kingdom! ')
        
    @Rule(Fact(Field='t'))
    def field_t(self):
        print('\nYou should study in the United States! ')
    
    @Rule(Fact(LvlOfEdu='d'), NOT(Fact(Research=W())))
    def lvlOfEdu_d(self):
        self.declare(Fact(Research=input("Do you have research experiance? (y/n) ")))
    
    @Rule(Fact(Research='n'))
    def research_n(self):
        print('\nYou should study in the United Kingdom! ')
    
    @Rule(Fact(Research='y'), NOT(Fact(Funding=W())))
    def research_y(self):
        self.declare(Fact(Funding=input("How much funding would you need in usd? ")))
    
    @Rule(Fact(Funding='value' << W()))
    def funding(self, value):
        if int(value) < 30000: 
            print('\nYou should study in Singapore! ')
        else:
            print('\nYou should study in the United States! ')
    
    @Rule(Fact(Eng2='n'), NOT(Fact(WorkAfterGrad=W())))
    def eng2_n(self):
        self.declare(Fact(WorkAfterGrad=input("Do you want to work after graduation? (y/n) ")))
    
    @Rule(Fact(WorkAfterGrad='y'))
    def workAfterGrad_y(self):
        print('\nYou should study in the United Arab Emirates! ')
        
    @Rule(Fact(WorkAfterGrad='n'))
    def workAfterGrad_n(self):
        print('\nYou should study in Jordan! ')
    
    ################################################################ LEISURE
    @Rule(Fact(Purpose='l'), NOT(Fact(Experiance=W())))
    def purpose_l(self):
        self.declare(Fact(Experiance=input("What is the experiance you want? (f-family / h-honeymoon) ")))
        
    ################################################################ FAMILY
    @Rule(Fact(Experiance='f'), NOT(Fact(Entertainment=W())))
    def experiance_f(self):
        self.declare(Fact(Entertainment=input("Do you like entertainment parks? (y/n) ")))
        
    @Rule(Fact(Entertainment='y'), NOT(Fact(ThemeAmuse=W())))
    def entertainment_y(self):
        self.declare(Fact(ThemeAmuse=input("Do you like theme parks or amusement parks? (t/a) ")))
    
    @Rule(Fact(ThemeAmuse='t'), NOT(Fact(MovSci=W())))
    def themeAmuse_t(self):
        self.declare(Fact(MovSci=input("Do you like movies and entertainment or science and technology? (m/s) ")))
        
    @Rule(Fact(MovSci='m'), NOT(Fact(EuAiAm=W())))
    def movSci_m(self):
        self.declare(Fact(EuAiAm=input("Do you prefer Europe, Asia or America? (e/a/m) ")))
        
    @Rule(Fact(EuAiAm='e'))
    def euAiAm_e(self):
        print('\nYou should visit France (Disneyland)! ')
        
    @Rule(Fact(EuAiAm='a'))
    def euAiAm_a(self):
        print('\nYou should visit Japan (Disneyland)! ')
        
    @Rule(Fact(EuAiAm='m'))
    def euAiAm_m(self):
        print('\nYou should visit the United States (Disneyland)! ')
    
    @Rule(Fact(MovSci='s'))
    def movSci_s(self):
        print('\nYou should visit Belgium (Technopolis Park)! ')
        
    @Rule(Fact(ThemeAmuse='a'))
    def themeAmuse_a(self):
        print('\nYou should visit Germany (Europa-Park)! ')
    
    @Rule(Fact(Entertainment='n'), NOT(Fact(Museums=W())))
    def entertainment_n(self):
        self.declare(Fact(Museums=input("Do you like museums? (y/n) ")))
        
    @Rule(Fact(Museums='y'), NOT(Fact(ArtHis=W())))
    def museums_y(self):
        self.declare(Fact(ArtHis=input("Do you prefer art museums or history museums? (a/h) ")))
        
    @Rule(Fact(ArtHis='a'))
    def artHis_a(self):
        print('\nYou should visit France (The Louvre)! ')
        
    @Rule(Fact(ArtHis='h'))
    def artHis_h(self):
        print('\nYou should visit the United Kingdom (British museum)! ')
        
    @Rule(Fact(Museums='n'), NOT(Fact(Water=W())))
    def museums_n(self):
        self.declare(Fact(Water=input("Do you like water parks? (y/n) ")))
        
    @Rule(Fact(Water='y'))
    def water_y(self):
        print('\nYou should visit the United Arab Emirates (Aquaventure)! ')
        
    @Rule(Fact(Water='n'), NOT(Fact(Aquarium=W())))
    def water_n(self):
        self.declare(Fact(Aquarium=input("Do you like aquariums? (y/n) ")))
        
    @Rule(Fact(Aquarium='y'))
    def aquarium_y(self):
        print('\nYou should visit Australia (Melbourne)! ')
        
    @Rule(Fact(Aquarium='n'))
    def aquarium_n(self):
        print('\nYou should visit Malaysia! ')
    
    ################################################################ HONEYMOON
    @Rule(Fact(Experiance='h'), NOT(Fact(ResPP=W())))
    def experiance_h(self):
        self.declare(Fact(ResPP=input("Do you prefer a resort or a private property? (r/p)) ")))
        
    @Rule(Fact(ResPP='r'), NOT(Fact(Stay=W())))
    def resPP_r(self):
        self.declare(Fact(Stay=input("Do you prefer to stay in the resort or do other activities? (s/a)) ")))
        
    @Rule(Fact(Stay='s'))
    def stay_s(self):
        print('\nYou should visit Mexico! ')
        
    @Rule(Fact(Stay='a'), NOT(Fact(Shopping=W())))
    def stay_a(self):
        self.declare(Fact(Shopping=input("Do you like shopping? (y/n)) ")))
    
    @Rule(Fact(Shopping='y'))
    def shopping_y(self):
        print('\nYou should visit Turkey! ')
    
    @Rule(Fact(Shopping='n'), NOT(Fact(Site=W())))
    def shopping_n(self):
        self.declare(Fact(Site=input("Do you like site viewing? (y/n)) ")))
    
    @Rule(Fact(Site='y'))
    def site_y(self):
        print('\nYou should visit Greece! ')
    
    @Rule(Fact(Site='n'))
    def site_n(self):
        print('\nYou should visit Hawaii! ')
        
    @Rule(Fact(ResPP='p'), NOT(Fact(Cities=W())))
    def resPP_p(self):
        self.declare(Fact(Cities=input("Do you like cities? (y/n)) ")))
   
    @Rule(Fact(Cities='y'))
    def cities_y(self):
        print('\nYou should visit Spain! ')
        
    @Rule(Fact(Cities='n'), NOT(Fact(Beaches=W())))
    def cities_n(self):
        self.declare(Fact(Beaches=input("Do you like beaches? (y/n)) ")))
        
    @Rule(Fact(Beaches='y'))
    def beaches_y(self):
        print('\nYou should visit the Maldives! ')
    
    @Rule(Fact(Beaches='n'), NOT(Fact(Mount=W())))
    def beaches_n(self):
        self.declare(Fact(Mount=input("Do you like mountaines? (y/n)) ")))
    
    @Rule(Fact(Mount='y'))
    def mount_y(self):
        print('\nYou should visit Switzerland! ')
        
    @Rule(Fact(Mount='n'))
    def mount_n(self):
        print('\nYou should visit Indonesia! ')
   

recommendedDestination = destinationRecommendation()
recommendedDestination.reset()
recommendedDestination.run()
