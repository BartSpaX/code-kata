def answer(question: str):
    question = question.replace("What is ", "") \
                .replace("plus", "+") \
                .replace("minus", "-") \
                .replace("divided by", "/") \
                .replace("multiplied by", "*") \
                .replace("?" ,"") \
                .split()
    
    question.insert(0, "(")
    question.insert(4, ")")

    q = [x.isalpha() for x in question if x not in ("What", "is")]
    if any(q):
        raise ValueError("unknown operation")

    try:
        return eval(" ".join(question))
    except:
        raise ValueError("syntax error")