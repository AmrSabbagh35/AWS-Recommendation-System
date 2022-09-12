from experta import *
    
class AWSExpert(KnowledgeEngine):
    
    @DefFacts()
    def needed_data(self):
        yield Fact(aws = 'true')
        print("Hello, This is a service to assist you with the best recommendation for using Amazon Web Services (AWS).\nThe System will guide you through the answers of different questions according to your budget and needs ..!")

# Main Question        
    @Rule(Fact(aws='true'), NOT (Fact(purpose = W())) , salience = 998)
    def whatpurpose(self):
        def answer(question):
            x = int(input(question))
            if x == 1 or x == 2 or x == 3 or x == 4 or x== 5 or x== 6:
                return x
            return answer(question)
        self.purpose = answer("\nWhat is your purpose?\nPlease Enter the number..\n1_VR\n2_Web/Application\n3_Migration\n4_Blockchain\n5_Games Development\n6_ Machine Learning\n")
        if self.purpose == 1:
            self.purpose = "vr"
        elif self.purpose == 2:
              self.purpose = "web_app"
        elif self.purpose == 3:
             self.purpose = "mig"
        elif self.purpose == 4:
              self.purpose = "blockchain"
        elif self.purpose == 5:
              self.purpose = "gamedev"                                    
        elif self.purpose == 6:
              self.purpose = "ml"
        
                                    
        self.declare(Fact(purpose = self.purpose.strip().lower()))

# VR Questions : 

# VR Budget         
    @Rule(Fact(aws='true'), Fact(purpose="vr"), NOT (Fact(budget = W())),salience = 995)
    def whatbudget(self):
        def answer(question):
            x = int(input(question))
            return x
        question = answer("\nWhat is your budget?\n")
        if question < 2000:
            self.budget = "Low"
        elif question > 10000 and question < 20000:
            self.budget = "Medium"
        else:
            self.budget = "High"
        self.declare(Fact(budget = self.budget.strip().lower()))
# VR DB Low Budget
    @Rule(Fact(aws='true'), Fact(purpose="vr"), NOT (Fact(db = W())), Fact(budget="low"), salience = 990)
    def whatdb(self):
        def answer(question):
            x = int(input(question))
            if x == 1 or x == 2 or x == 3:
                return x
            return answer(question)
        question = answer("\nWhat is your Database Type?\nPlease Enter the number..\n1_Relational DB\n2_NOSQL\n3_Not interested\n")
        if question == 1:
            self.db = "RDB"
        elif question == 2:
            self.db = "NOSQL"
        else:
            self.db = "NotI"
        self.declare(Fact(db = self.db.strip().lower()))
# VR DB Medium Budget       
    @Rule(Fact(aws='true'), Fact(purpose="vr"), NOT (Fact(db = W())), Fact(budget="medium"), salience = 990)
    def whatdba(self):
        def answer(question):
            x = int(input(question))
            if x == 1 or x == 2 or x == 3 or x == 4:
                return x
            return answer(question)
        question = answer("\nWhat is your Database Type?\nPlease Enter the number..\n1_Relational DB\n2_NOSQL\n3_High Performance RDS\n4_Not interested\n")
        if question == 1:
            self.db = "RDB"
        elif question == 2:
            self.db = "NOSQL"
        elif question == 3:
            self.db = "HRDS"
        else:
            self.db = "NotI"
        self.declare(Fact(db = self.db.strip().lower()))
# VR DB High Budget     
    @Rule(Fact(aws='true'), Fact(purpose="vr"),NOT (Fact(db = W())), Fact(budget="high"), salience = 990)
    def whatdbaHigh(self):
        def answer(question):
            x = int(input(question))
            if x == 1 or x == 2 or x == 3 or x == 4:
                return x
            return answer(question)
        question = answer("\nWhat is your Database Type?\nPlease Enter the number..\n1_Relational DB\n2_NOSQL\n3_High Performance RDS\n4_Not interested\n")
        if question == 1:
            self.db = "RDB"
        elif question == 2:
            self.db = "NOSQL"
        elif question == 3:
            self.db = "HRDS"
        else:
            self.db = "NotI"
        self.declare(Fact(db = self.db.strip().lower()))        
# VR Security         
    @Rule(Fact(aws='true'), Fact(purpose="vr"), NOT (Fact(security = W())),salience = 985)
    def vrsecurity(self):
        def answer(question):
            x = input(question)
            x=x.lower().strip()
            if x == "yes" or x == "no":
                return x
            return answer(question)
        self.security = answer("\nDo you care about security? Please answer Yes/No\n")
        self.declare(Fact(security = self.security))

# Web Questions : 
# Web Simple Code
    @Rule(Fact(aws='true'), Fact(purpose="web_app"), NOT (Fact(simplecode = W())),salience = 995)
    def simplecodecheck(self):
        def answer(question):
            x = input(question)
            x=x.lower().strip()
            if x == "yes" or x == "no":
                return x
            return answer(question)
        self.simplecode = answer("\nis it a simple code? Please answer Yes/No\n\n")
        self.declare(Fact(simplecode = self.simplecode))                    
# Web DB
    @Rule(Fact(aws='true'),Fact(purpose="web_app"), NOT (Fact(webdb = W())), salience = 990)
    def whatdbWeb(self):
        def answer(question):
            x = int(input(question))
            if x == 1 or x == 2:
                return x
            return answer(question)
        question = answer("\nWhat is your Database Type?\nPlease Enter the number..\n1_Relational DB\n2_NOSQL\n")
        if question == 1:
            self.webdb = "rdb"
        elif question == 2:
            self.webdb = "nosql"
        self.declare(Fact(webdb = self.webdb.strip().lower()))
# Web Location
    @Rule(Fact(aws='true'), Fact(purpose="web_app"), NOT (Fact(location = W())),salience = 985)
    def locationCheck(self):
        def answer(question):
            x = input(question)
            x=x.lower().strip()
            if x == "yes" or x == "no":
                return x
            return answer(question)
        self.location = answer("\nDo you care about location support ? Please answer Yes/No\n")
        self.declare(Fact(location = self.location))
# Web Traffic
    @Rule(Fact(aws='true'), Fact(purpose="web_app"), NOT (Fact(traffic = W())),salience = 980)
    def trafficCheck(self):
        def answer(question):
            x = input(question)
            x=x.lower().strip()
            if x == "yes" or x == "no":
                return x
            return answer(question)
        self.traffic = answer("\nDoes your app need high traffic support ? Please answer Yes/No\n")
        self.declare(Fact(traffic = self.traffic))
# Web Security         
    @Rule(Fact(aws='true'), Fact(purpose="web_app"), NOT (Fact(websecurity = W())),salience = 985)
    def websecurity(self):
        def answer(question):
            x = input(question)
            x=x.lower().strip()
            if x == "yes" or x == "no":
                return x
            return answer(question)
        self.websecurity = answer("\nDo you care about security? Please answer Yes/No\n")
        self.declare(Fact(websecurity = self.websecurity))



# Migration Questions : 
# Migration Purpose 
    @Rule(Fact(aws='true'),Fact(purpose="mig"), NOT (Fact(migpurpose = W())), salience = 990)
    def migpurpose(self):
        def answer(question):
            x = int(input(question))
            if x == 1 or x == 2 or x == 3:
                return x
            return answer(question)
        question = answer("\nWhat is the migration case ?\nPlease Enter the number..\n1_Archiving old data DB\n2_Migrating from on-prem to cloud\n3_Uploading large size data to the cloud\n")
        if question == 1:
            self.migpurpose = "archive"
        elif question == 2:
            self.migpurpose = "onprem"
        elif question == 3:
            self.migpurpose = "large"
        self.declare(Fact(migpurpose = self.migpurpose.strip().lower()))
# Migration File System
    @Rule(Fact(aws='true'), Fact(purpose="mig"),Fact(migpurpose="archive"), NOT (Fact(filesystem = W())),salience = 985)
    def filesystem(self):
        def answer(question):
            x = input(question)
            x=x.lower().strip()
            if x == "yes" or x == "no":
                return x
            return answer(question)
        self.filesystem = answer("\nDo you need a network file system ? Please answer Yes/No \n")
        self.declare(Fact(filesystem = self.filesystem))
# Migration Budget
    @Rule(Fact(aws='true'), Fact(purpose="mig"),Fact(migpurpose="onprem"), NOT (Fact(migBudget = W())),salience = 985)
    def migBudget(self):
        def answer(question):
            x = int(input(question))
            if x == 1 or x == 2:
                return x
            return answer(question)
        question = answer("\nHow much do you estimate your budget ?\n1_Low\n2_High\n")
        if question == 1:
            self.migBudget = "low"
        elif question == 2:
            self.migBudget = "high" 
        self.migBudget = self.migBudget.lower()
        self.declare(Fact(migBudget = self.migBudget.strip().lower()))                 
# Migration Size
    @Rule(Fact(aws='true'), Fact(purpose="mig"),Fact(migpurpose="large"), NOT (Fact(sizecheck = W())),salience = 985)
    def sizecheck(self):
        def answer(question):
            x = input(question)
            x=x.lower().strip()
            if x == "yes" or x == "no":
                return x
            return answer(question)
        self.sizecheck = answer("\nis the size over 80 TB ? ? Please answer Yes/No \n")
        self.declare(Fact(sizecheck = self.sizecheck))



# Blockchain Questions: 
# Blockchain network : 
    @Rule(Fact(aws='true'), Fact(purpose="blockchain"),NOT (Fact(network= W())),salience = 990)
    def network(self):
        def answer(question):
            x = int(input(question))
            if x == 1 or x == 2:
                return x
            return answer(question)        
        self.network = answer("\nType of network ?\n1_Centralized\n2_Decentralized\n")
        if self.network == 1:
            self.network = "cent"
        elif self.network == 2:
            self.network = "decent" 
        self.network = self.network.lower()
        self.declare(Fact(network = self.network.strip().lower()))  


# Game Dev Questions : 
# Game Dev Type 
    @Rule(Fact(aws='true'), Fact(purpose="gamedev"),NOT (Fact(devtype= W())),salience = 990)
    def devtype(self):
        def answer(question):
            x = int(input(question))
            if x == 1 or x == 2:
                return x
            return answer(question)        
        self.devtype = answer("\nType of Development ?\n1_Real-Time Online Gaming Hosting\n2_3D Game-Engine\n")
        if self.devtype == 1:
            self.devtype = "host"
        elif self.devtype == 2:
            self.devtype = "3d" 
        self.devtype = self.devtype.lower()
        self.declare(Fact(devtype = self.devtype.strip().lower()))  
# Game Dev DB 
    @Rule(Fact(aws='true'), Fact(purpose="gamedev"),(Fact(devtype= "host")), NOT (Fact(gamedb = W())),salience = 985)
    def whatgamedb(self):
        def answer(question):
            x = int(input(question))
            if x == 1 or x == 2 or x==3:
                return x
            return answer(question)        
        self.gamedb = answer("\nWhat is your Database Type?\nPlease Enter the number..\n1_Relational DB\n2_NOSQL\n3_Not Interested\n")
        if self.gamedb == 1:
            self.gamedb = "rdb"
        elif self.gamedb == 2:
            self.gamedb = "nosql"
        elif self.gamedb == 3:
            self.gamedb = "nosql"            
        self.declare(Fact(gamedb = self.gamedb.strip().lower()))
# Game Dev Compiling 
    @Rule(Fact(aws='true'), Fact(purpose="gamedev"),(Fact(devtype= "3d")), NOT (Fact(comp = W())),salience = 985)
    def comp(self):
        def answer(question):
            x = input(question)
            x=x.lower().strip()
            if x == "yes" or x == "no":
                return x        
        self.comp = answer("\nDo you need online compiling ? Please answer Yes/No \n")
        self.comp = self.comp.lower()
        self.declare(Fact(comp = self.comp.strip().lower()))


#ML Questions : 
# ML Purpose 
    @Rule(Fact(aws='true'),Fact(purpose="ml"), NOT (Fact(mlpurpose = W())), salience = 990)
    def mlpurpose(self):
        def answer(question):
            x = int(input(question))
            if x == 1 or x == 2:
                return x
            return answer(question)        
        self.mlpurpose = answer("\nWhat is the purpose of ML?\nPlease Enter the number..\n1_NLP (Natural Language Processing)\n2_Image & Video Processing\n")
        if self.mlpurpose == 1:
            self.mlpurpose = "nlp"
        elif self.mlpurpose == 2:
            self.mlpurpose = "img"
        self.declare(Fact(mlpurpose = self.mlpurpose.strip().lower()))
# ML recommend NLP 
    @Rule(Fact(aws='true'),Fact(purpose="ml"),Fact(mlpurpose="nlp"), NOT (Fact(rcmnd = W())), salience = 985)
    def rcmnd(self):
        def answer(question):
            x = input(question)
            x=x.lower().strip()
            if x == "yes" or x == "no":
                return x        
        self.rcmnd = answer("\nDo you need a recommendation system ? Please answer Yes/No \n")
        self.rcmnd = self.rcmnd.lower()
        self.declare(Fact(rcmnd = self.rcmnd.strip().lower()))
# ML recommend img
    @Rule(Fact(aws='true'),Fact(purpose="ml"),Fact(mlpurpose="img"), NOT (Fact(rcmndimg = W())), salience = 985)
    def rcmndimg(self):
        def answer(question):
            x = input(question)
            x=x.lower().strip()
            if x == "yes" or x == "no":
                return x        
        self.rcmndimg = answer("\nDo you need a recommendation system ? Please answer Yes/No \n")
        self.rcmndimg = self.rcmndimg.lower()
        self.declare(Fact(rcmndimg = self.rcmndimg.strip().lower()))
# ML Health 
    @Rule(Fact(aws='true'),Fact(purpose="ml"),Fact(mlpurpose="nlp"),Fact(rcmnd = "yes"), NOT (Fact(health = W())), salience = 980)
    def health(self):
        def answer(question):
            x = input(question)
            x=x.lower().strip()
            if x == "yes" or x == "no":
                return x        
        self.health = answer("\nIs your project Health Related ? Please answer Yes/No \n")
        self.health = self.health.lower()
        self.declare(Fact(health = self.health.strip().lower()))

    @Rule(Fact(aws='true'),Fact(purpose="ml"),Fact(mlpurpose="nlp"),Fact(rcmnd = "no"), NOT (Fact(health = W())), salience = 980)
    def health1(self):
        def answer(question):
            x = input(question)
            x=x.lower().strip()
            if x == "yes" or x == "no":
                return x        
        self.health = answer("\nIs your project Health Related ? Please answer Yes/No \n")
        self.health = self.health.lower()
        self.declare(Fact(health = self.health.strip().lower()))        

###################################################


# VR Solutions : -----------------------------

# LOW : 
# VR LOW RDS 
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="low"), Fact(db="rdb"), Fact(security="yes"))
    def solution1(self):
        f = open('solution1.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()

        
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="low"), Fact(db="rdb"), Fact(security="no"))
    def solution2(self):
        f = open('solution2.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()

# VR LOW NO-SQL         
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="low"), Fact(db="nosql"), Fact(security="yes"))
    def solution3(self):
        f = open('solution3.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()
           
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="low"), Fact(db="nosql"), Fact(security="no"))
    def solution4(self):
        f = open('solution4.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()
# VR LOW NO DB         

    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="low"), Fact(db="noti"), Fact(security="yes"))
    def solution5(self):
        f = open('solution5.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 

    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="low"), Fact(db="noti"), Fact(security="no"))
    def solution6(self):
        f = open('solution6.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()
# Medium : 
# VR MEDIUM RDS            
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="medium"), Fact(db="rdb"), Fact(security="yes"))
    def solution7(self):
        f = open('solution7.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()   

    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="medium"), Fact(db="rdb"), Fact(security="no"))
    def solution8(self):
        f = open('solution8.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
# VR MEDIUM NO-SQL        
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="medium"), Fact(db="nosql"), Fact(security="yes"))
    def solution9(self):
        f = open('solution9.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()   

    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="medium"), Fact(db="nosql"), Fact(security="no"))
    def solution10(self):
        f = open('solution10.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()
# VR MEDIUM AROURA                
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="medium"), Fact(db="hrds"), Fact(security="yes"))
    def solution11(self):
        f = open('solution11.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()       

    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="medium"), Fact(db="hrds"), Fact(security="no"))
    def solution12(self):
        f = open('solution12.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
# VR MEDIUM NO DB                
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="medium"), Fact(db="noti"), Fact(security="yes"))
    def solution13(self):
        f = open('solution13.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()     
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="medium"), Fact(db="noti"), Fact(security="no"))
    def solution14(self):
        f = open('solution14.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()    

# High : 
# VR HIGH RDS                
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="high"), Fact(db="rdb"), Fact(security="yes"))
    def solution15(self):
        f = open('solution15.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()     
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="high"), Fact(db="rdb"), Fact(security="no"))
    def solution16(self):
        f = open('solution16.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()     
# VR HIGH NO-SQL          
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="high"), Fact(db="nosql"), Fact(security="yes"))
    def solution17(self):
        f = open('solution17.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()     
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="high"), Fact(db="nosql"), Fact(security="no")) 
    def solution18(self):
        f = open('solution18.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()     
# VR HIGH ARUORA               
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="high"), Fact(db="hrds"), Fact(security="yes")) 
    def solution19(self):
        f = open('solution19.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()     
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="high"), Fact(db="hrds"), Fact(security="no")) 
    def solution20(self):
        f = open('solution20.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()     
# VR HIGH NO DB               
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="high"), Fact(db="noti"), Fact(security="yes")) 
    def solution21(self):
        f = open('solution21.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()     
    @Rule(Fact(aws="true"), Fact(purpose="vr"), Fact(budget="high"), Fact(db="noti"), Fact(security="no")) 
    def solution22(self):
        f = open('solution22.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()     





# Web Solutions : -----------------------------

# Simple Code RDS : 

# Web SimpleCode RDS Location Traffic                   
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="rdb"), Fact(location="yes"),Fact(traffic="yes"),Fact(websecurity="yes"))
    def solution23(self):
        f = open('solution23.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="rdb"), Fact(location="yes"),Fact(traffic="yes"),Fact(websecurity="no"))
    def solution24(self):
        f = open('solution24.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
# Web SimpleCode RDS Location ===== NO Traffic =====               
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="rdb"), Fact(location="yes"),Fact(traffic="no"),Fact(websecurity="yes"))
    def solution25(self):
        f = open('solution25.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="rdb"), Fact(location="yes"),Fact(traffic="no"),Fact(websecurity="no"))
    def solution26(self):
        f = open('solution26.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
# Simple Code RDS === No Location === :     

# Web SimpleCode RDS Traffic                   
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="rdb"), Fact(location="no"),Fact(traffic="yes"),Fact(websecurity="yes"))
    def solution27(self):
        f = open('solution27.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="rdb"), Fact(location="no"),Fact(traffic="yes"),Fact(websecurity="no"))
    def solution28(self):
        f = open('solution28.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
# Web SimpleCode RDS ===== NO Traffic =====                   
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="rdb"), Fact(location="no"),Fact(traffic="no"),Fact(websecurity="yes"))
    def solution29(self):
        f = open('solution29.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="rdb"), Fact(location="no"),Fact(traffic="no"),Fact(websecurity="no"))
    def solution30(self):
        f = open('solution30.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
# =========================

# Simple Code NOSQL :   

# Web SimpleCode NOSQL Location Traffic                   
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="nosql"), Fact(location="yes"),Fact(traffic="yes"),Fact(websecurity="yes"))
    def solution31(self):
        f = open('solution31.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="nosql"), Fact(location="yes"),Fact(traffic="yes"),Fact(websecurity="no"))
    def solution32(self):
        f = open('solution32.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
# Web SimpleCode NOSQL Location ===== NO Traffic =====               
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="nosql"), Fact(location="yes"),Fact(traffic="no"),Fact(websecurity="yes"))
    def solution33(self):
        f = open('solution33.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="nosql"), Fact(location="yes"),Fact(traffic="no"),Fact(websecurity="no"))
    def solution34(self):
        f = open('solution34.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
# Simple Code NOSQL === No Location === :     
    
# Web SimpleCode NOSQL Traffic                   
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="nosql"), Fact(location="no"),Fact(traffic="yes"),Fact(websecurity="yes"))
    def solution35(self):
        f = open('solution35.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="nosql"), Fact(location="no"),Fact(traffic="yes"),Fact(websecurity="no"))
    def solution36(self):
        f = open('solution36.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  

# Web SimpleCode NOSQL ===== NO Traffic =====                   
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="nosql"), Fact(location="no"),Fact(traffic="no"),Fact(websecurity="yes"))
    def solution37(self):
        f = open('solution37.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="yes"), Fact(webdb="nosql"), Fact(location="no"),Fact(traffic="no"),Fact(websecurity="no"))
    def solution38(self):
        f = open('solution38.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()  
######################################

# NO SIMPLE CODE Solutions : 
      
# RDS : 

# Web RDS Location Traffic                   
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="rdb"), Fact(location="yes"),Fact(traffic="yes"),Fact(websecurity="yes"))
    def solution39(self):
        f = open('solution39.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="rdb"), Fact(location="yes"),Fact(traffic="yes"),Fact(websecurity="no"))
    def solution40(self):
        f = open('solution40.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
# Web RDS Location ===== NO Traffic =====               
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="rdb"), Fact(location="yes"),Fact(traffic="no"),Fact(websecurity="yes"))
    def solution41(self):
        f = open('solution41.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="rdb"), Fact(location="yes"),Fact(traffic="no"),Fact(websecurity="no"))
    def solution42(self):
        f = open('solution42.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
# RDS === No Location === :     

# Web RDS Traffic                   
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="rdb"), Fact(location="no"),Fact(traffic="yes"),Fact(websecurity="yes"))
    def solution43(self):
        f = open('solution43.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="rdb"), Fact(location="no"),Fact(traffic="yes"),Fact(websecurity="no"))
    def solution44(self):
        f = open('solution44.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
# Web RDS ===== NO Traffic =====                   
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="rdb"), Fact(location="no"),Fact(traffic="no"),Fact(websecurity="yes"))
    def solution45(self):
        f = open('solution45.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="rdb"), Fact(location="no"),Fact(traffic="no"),Fact(websecurity="no"))
    def solution46(self):
        f = open('solution46.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
# =========================

# NOSQL :   

# Web NOSQL Location Traffic                   
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="nosql"), Fact(location="yes"),Fact(traffic="yes"),Fact(websecurity="yes"))
    def solution47(self):
        f = open('solution47.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="nosql"), Fact(location="yes"),Fact(traffic="yes"),Fact(websecurity="no"))
    def solution48(self):
        f = open('solution48.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
# Web NOSQL Location ===== NO Traffic =====               
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="nosql"), Fact(location="yes"),Fact(traffic="no"),Fact(websecurity="yes"))
    def solution49(self):
        f = open('solution49.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="nosql"), Fact(location="yes"),Fact(traffic="no"),Fact(websecurity="no"))
    def solution50(self):
        f = open('solution50.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
# NOSQL === No Location === :     
    
# Web NOSQL Traffic                   
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="nosql"), Fact(location="no"),Fact(traffic="yes"),Fact(websecurity="yes"))
    def solution51(self):
        f = open('solution51.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="nosql"), Fact(location="no"),Fact(traffic="yes"),Fact(websecurity="no"))
    def solution52(self):
        f = open('solution52.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
# Web NOSQL ===== NO Traffic =====                   
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="nosql"), Fact(location="no"),Fact(traffic="no"),Fact(websecurity="yes"))
    def solution53(self):
        f = open('solution53.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
    @Rule(Fact(aws="true"), Fact(purpose="web_app"), Fact(simplecode="no"), Fact(webdb="nosql"), Fact(location="no"),Fact(traffic="no"),Fact(websecurity="no"))
    def solution54(self):
        f = open('solution54.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 





# Migration Solutions : -----------------------------

# Migration Archiving
    @Rule(Fact(aws="true"), Fact(purpose="mig"), Fact(migpurpose="archive"), Fact(filesystem="yes"))
    def solution55(self):
        f = open('solution55.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 

    @Rule(Fact(aws="true"), Fact(purpose="mig"), Fact(migpurpose="archive"), Fact(filesystem="no"))
    def solution56(self):
        f = open('solution56.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
# Migration on-premise to cloud
    @Rule(Fact(aws="true"), Fact(purpose="mig"), Fact(migpurpose="onprem"), Fact(migBudget="low"))
    def solution57(self):
        f = open('solution57.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 

    @Rule(Fact(aws="true"), Fact(purpose="mig"),Fact(migpurpose="onprem"), Fact(migBudget="high"))
    def solution58(self):
        f = open('solution58.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 
# Migration large files
    @Rule(Fact(aws="true"), Fact(purpose="mig"), Fact(migpurpose="large"), Fact(sizecheck="yes"))
    def solution59(self):
        f = open('solution59.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 

    @Rule(Fact(aws="true"), Fact(purpose="mig"),Fact(migpurpose="large"), Fact(sizecheck="no"))
    def solution60(self):
        f = open('solution60.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close() 





# Blockchain Solutions : -----------------------------

#Blockchain Network 
    @Rule(Fact(aws='true'), Fact(purpose="blockchain"), (Fact(network= "cent")),salience = 990)
    def solution61(self):
        self.declare(Fact(solution = 'Amazon Managed Blockchain - VPC - IAM- Cloudwatch/Logs'))

    @Rule(Fact(aws='true'), Fact(purpose="blockchain"), (Fact(network= "decent")),salience = 990)
    def solution62(self):
        self.declare(Fact(solution = 'QLDB - VPC - IAM- Cloudwatch/Logs'))




# Game Development Solutions : -----------------------------

# Game Dev Online
    @Rule(Fact(aws='true'), Fact(purpose="gamedev"),(Fact(devtype= "host")),(Fact(gamedb = "rdb")),salience = 990)
    def solution63(self):
        self.declare(Fact(solution = 'Game Lift - RDS- VPC- IAM- Load Balancer- Cloud Watch/Logs'))

    @Rule(Fact(aws='true'), Fact(purpose="gamedev"),(Fact(devtype= "host")),(Fact(gamedb = "nosql")),salience = 985)
    def solution64(self):
        self.declare(Fact(solution = 'Game Lift - Dynamo - VPC- IAM- Load Balancer- Cloud Watch/Logs'))

    @Rule(Fact(aws='true'), Fact(purpose="gamedev"),(Fact(devtype= "host")),(Fact(gamedb = "notint")),salience = 975)
    def solution65(self):
        self.declare(Fact(solution = 'Game Lift - VPC- IAM- Load Balancer- Cloud Watch/Logs'))
# Game Dev 3D
    @Rule(Fact(aws='true'), Fact(purpose="gamedev"),(Fact(devtype= "3d")),(Fact(comp = "yes")),salience = 990)
    def solution66(self):
        self.declare(Fact(solution = 'Lumberyard - Cloud9- VPC- IAM- Cloud Watch/Logs'))

    @Rule(Fact(aws='true'), Fact(purpose="gamedev"),(Fact(devtype= "3d")),(Fact(comp = "no")),salience = 990)
    def solution67(self):
        self.declare(Fact(solution = 'Lumberyard - VPC - IAM - Cloud Watch/Logs'))



# ML Solutions : -------------------------------

# ML NLP Recommendation 
    @Rule(Fact(aws='true'),Fact(purpose="ml"),Fact(mlpurpose = "nlp"), Fact(rcmnd = "yes"), Fact(health = "yes"), salience = 985)
    def solution68(self):
        self.declare(Fact(solution = 'Lex - SageMaker- Health Lake- Polly- Personalize- Transcribe'))
    @Rule(Fact(aws='true'),Fact(purpose="ml"),Fact(mlpurpose = "nlp"), Fact(rcmnd = "yes"), Fact(health = "no"), salience = 985)
    def solution69(self):
        self.declare(Fact(solution = 'Lex - SageMaker - Polly- Personalize- Transcribe'))

# ML NLP ==== NO Recommendation 
    @Rule(Fact(aws='true'),Fact(purpose="ml"),Fact(mlpurpose = "nlp"), Fact(rcmnd = "no"), Fact(health = "yes"), salience = 985)
    def solution70(self):
        self.declare(Fact(solution = 'Lex - SageMaker- Health Lake- Polly - Transcribe'))
    @Rule(Fact(aws='true'),Fact(purpose="ml"),Fact(mlpurpose = "nlp"), Fact(rcmnd = "no"), Fact(health = "no"), salience = 985)
    def solution71(self):
        self.declare(Fact(solution = 'Lex - SageMaker - Polly - Transcribe'))

# ML image  
    @Rule(Fact(aws='true'),Fact(purpose="ml"),Fact(mlpurpose = "img"), Fact(rcmndimg = "yes"), salience = 985)
    def solution72(self):
        self.declare(Fact(solution = 'Rekognition- SageMaker- Personalize'))
    @Rule(Fact(aws='true'),Fact(purpose="ml"),Fact(mlpurpose = "img"), Fact(rcmndimg = "no"), salience = 985)
    def solution73(self):
        self.declare(Fact(solution = 'Rekognition- SageMaker'))





if __name__ == "__main__":
    engine = AWSExpert()
    engine.reset() 
    engine.run()
    print('Printing engine facts after 1 run',engine.facts)