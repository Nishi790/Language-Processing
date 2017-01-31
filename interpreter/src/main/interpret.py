import re,nltk

def learnFact(sent,info, facts):
    args=info.split(",")
    a=args[0]
    a=a.split(":")
    b=args[1]
    b=b.split(":")
    newFact=(sent.group(int(a[0])+1)+":"+a[1]+":"+sent.group(int(a[2])+1))
    facts.append(newFact)
    newFact=(sent.group(int(b[0])+1)+":"+b[1]+":"+sent.group(int(b[2])+1))
    facts.append(newFact)
    print("I understand.")
    return facts
 
def testQuestion(question,info, facts):
    factsUsed=[]
    a=list(info)
    factToMatch=[question.group(int(a[0])+1),a[2],question.group(int(a[4])+1)]
    for fact in facts:
        elements=fact.split(":")
        if factToMatch[0]==elements[0]:
            if factToMatch==elements:
                print("Yes")
                return True
            elif elements[1]=="s":
                print("thinking")
                factsUsed.append(fact)
                newfact=[elements[2],factToMatch[1],factToMatch[2]]
                #print(newfact)
                finished=matchFact(newfact, facts, factsUsed)
                if finished is True:
                    print("Yes")
                    return True
                else:
                    continue
        else:
            continue    
    return False
        
                
def matchFact(factToMatch, facts, factsused):
    for fact in facts:
        #print(factToMatch)
        matcher=fact.split(":")
        #print(matcher)
        if fact in factsused:
            #print("Already used")
            continue
        elif factToMatch[0]!= matcher[0]:
            #print("Not on same subject")
            continue
        elif factToMatch==matcher:
            #print("facts are the same")
            return True
        elif matcher[1]=="s":
            print("thinking")
            factsused.append(fact)
            fact=[matcher[2],factToMatch[1],factToMatch[2]]
            print(fact)
            finished=matchFact(fact,facts,factsused)
            if finished is True:
                return True
    
        
        
        
def main():
    matchTypes=(
    (r"(\w+)[\s]is[\s](\w+)$", "0:e:1,1:e:0"),
    (r"[A]?[\s]?(\w+) is (a|an) (\w+)$", "0:s:2,2:S:0"),
    (r"(Every|Each) (\w*) is (a|an) (\w*)$", "1:s:3,3:S:1"),
    
    )
    questionTypes=(
    (r"Is (\w*) (a|an) (\w*)\?", "0:s:2"),
    (r"Is (\w*) ([a-zA-Z])\?", "0:e:1"),
    (r"Is (every|each) (\w*) (a|an) (\w*)\?", "4:S:2")
    )
    facts=[]
    print ("Teach me facts and ask me questions")
    while True:
        fact=input()
        if fact.endswith("?"):
            for regex in questionTypes:
                matches=re.match(regex[0], fact)
                if matches is not None:
                    result=testQuestion(matches, regex[1], facts)
                    if result is False:
                        print("Not as far as I know")


        else:
            for regex in matchTypes:
                matches=re.match(regex[0], fact)
                if matches is not None:
                    facts=learnFact(matches,regex[1], facts)
                    break


if __name__=="__main__":
    main()
  