"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores: list):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    new_list = []

    for score in enumerate(student_scores):
        new_list.insert(0, round(score[1]))
    
    return new_list


def count_failed_students(student_scores: list):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    count = 0

    for scores in student_scores:
        if scores <= 40:
            count += 1
    return count


def above_threshold(student_scores: list, threshold: int):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    the_best = []
    for score in student_scores:
        if score >= threshold:
            the_best.append(score)
    return the_best


def letter_grades(highest: int):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    increment = (highest - 40) / 4
    list_of_grades = []
    value = 41
    while value < highest:
        list_of_grades.append(int(value))
        value += increment
    return list_of_grades


def student_ranking(student_scores: list, student_names: list):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    ranking_list = []
    for index in enumerate(student_names):
        ranking_list.append(f"{index[0]+1}. {index[1]}: {student_scores[index[0]]}")
    return ranking_list


def perfect_score(student_info: list):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    perfect_student = []
    for index in enumerate(student_info):
        if index[1][1] == 100:
            perfect_student.extend(index[1])
            break
    return perfect_student
