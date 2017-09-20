def LoopTextArray(textArray, op):
    result = None
    for text in textArray:
        result = op(text)
        if result is not None:
            return result
    return None
