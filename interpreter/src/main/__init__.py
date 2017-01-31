import re,nltk

def learnFact(sent,info, facts):
    args=info.split(",")
    a=list(args[0])
    b=list(args[1])
    newFact=(sent.group(int(a[0])+1)+a[1]+sent.group(int(a[2])+1))
    facts.append(newFact)
    newFact=(sent.group(int(b[0])+1)+b[1]+sent.group(int(b[2])+1))
    facts.append(newFact)
    print("I understand.")
    return facts
 
def testQuestion(question,info, facts):
    a=list(info)
    
    factToMatch=(question.group(int(a[0])+1)+a[1]+question.group(int(a[2])+1))
    for fact in facts:
        if fact==factToMatch:
            print("Yes")
            return
    print("I don't know")

def main():
    matchTypes=(
    ("(.*) is (.*)", "0e1,1e0"),
    
    )
    questionTypes=(
    ("Is (.*) (.*[^/?])?", "0e1"),
    )
    facts=[]
    while True:
        print ("Teach me facts and ask me questions")
        fact=input()
        if fact.endswith("?"):
            for regex in questionTypes:
                matches=re.match(regex[0], fact)
                if matches is not None:
                    testQuestion(matches, regex[1], facts)
        else:
            for regex in matchTypes:
                matches=re.match(regex[0], fact)
                if matches is not None:
                    facts=learnFact(matches,regex[1], facts)


if __name__=="__main__":
    main()
  