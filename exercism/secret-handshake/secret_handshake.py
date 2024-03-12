def commands(binary_str):
    actions = {4: "wink",
               3: "double blink",
               2: "close your eyes",
               1: "jump",
               0: "Reverse"}
    indexes = list(reversed([i for i, x in enumerate(binary_str) if x == "1"]))
    do_actions = [actions[x] for x in indexes if x != 0]
    if 0 in indexes:
        do_actions.reverse()
    return do_actions
