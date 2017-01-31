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
            if (factToMatch[1]==elements[1] and factToMatch[2]==elements[2]):
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
    
def matchNouns(sentence, matchTypes, facts):
    temp=nltk.tokenize.word_tokenize(sentence)
    words=nltk.pos_tag(temp)
    nounList=[]
    adjList=[]
    for word in words:
        if word[1][0]=="N":
            nounList.append(word)
            continue
        elif "JJ" in word[1]:
            adjList.append(word)
    i=0
    for noun in nounList:
        if len(nounList)>1:
            temp=noun[0]+" is a "+nounList[i+1][0]
            print ("Did you mean "+temp+"?")
            response=input()
            if ("yes" or "Yes") in response:
                for regex in matchTypes:
                    matches=re.match(regex[0], temp)
                    if matches is not None:
                        learnFact(matches,regex[1], facts)
                        return
        else:
            for adj in adjList:
                temp=noun[0]+" is "+adj[0] 
                print ("Did you mean "+ temp+"?")
                response=input()
                if ("yes" or "Yes") in response:
                    for regex in matchTypes:
                        matches=re.match(regex[0], temp)
                        if matches is not None:
                            learnFact(matches,regex[1], facts)
                            return
                else:
                    i=i+1
    print("I don't understand")
               
        
        
def main():
    matchTypes=(
    (r"(\w+)[\s]is[\s](\w+)$", "0:e:1,1:e:0"),
    (r"[A]?[\s]?(\w+) is (a|an) (\w+)$", "0:s:2,2:S:0"),
    (r"(Every|Each) (\w*) is (a|an) (\w*)$", "1:s:3,3:S:1"),
    
    
    )
    questionTypes=(
    (r"Is (\w*) (a|an) (\w*)\?", "0:s:2"),
    (r"Is (\w*) (\w+)\?", "0:e:1"),
    (r"Is (every|each) (\w*) (a|an) (\w*)\?", "4:S:2")
    )
    facts=[]
    print ("Teach me facts and ask me questions")
    while True:
        fact=input()
        matchfound=False
        if fact.endswith("?"):
            for regex in questionTypes:
                matches=re.match(regex[0], fact)
                if matches is not None:
                    matchFound=True
                    result=testQuestion(matches, regex[1], facts)
                    if result is False:
                        print("Not as far as I know")


        else:
            for regex in matchTypes:
                matches=re.match(regex[0], fact)
                if matches is not None:
                    learnFact(matches,regex[1], facts)
                    matchFound=True
                    break
                else:
                    matchFound=False
        if matchFound is False:
            matchNouns(fact,matchTypes,facts)
                    


if __name__=="__main__":
    main()