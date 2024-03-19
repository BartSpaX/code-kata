def proverb(*args, qualifier=None):
    output = []
    if len(args) > 0:
        for i in range(len(args) -1):
                output.append(f"For want of a {args[i]} the {args[i+1]} was lost.")
        
        if qualifier != None:
             output.append(f"And all for the want of a {qualifier} {args[0]}.")
        else:
             output.append(f"And all for the want of a {args[0]}.")

    return output